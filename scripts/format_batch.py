#!/usr/bin/env python3
"""Batch-format new notes: migrate base64+Feishu images to OSS via PicGo,
lift inline Date: lines, add front matter, demote headings. Excludes
digital_manufacturing (still being edited)."""
import re, os, glob, json, base64, tempfile, urllib.request

PICGO="http://127.0.0.1:36677/upload"; LOG="/tmp/fmt.log"; RES="/tmp/fmt_result.json"
open(LOG,"w").close()
def log(m):
    open(LOG,"a",encoding="utf-8").write(m+"\n")
def upload(p):
    req=urllib.request.Request(PICGO,data=json.dumps({"list":[p]}).encode(),headers={"Content-Type":"application/json"})
    r=json.load(urllib.request.urlopen(req,timeout=120))
    if r.get("success") and r.get("result"): return r["result"][0]
    raise RuntimeError(r.get("message","picgo fail"))
EXT={"image/png":"png","image/jpeg":"jpg","image/jpg":"jpg","image/webp":"webp","image/gif":"gif"}
def dl(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req,timeout=60) as r:
        ct=r.headers.get("Content-Type","").split(";")[0].strip().lower(); data=r.read()
    if not ct.startswith("image/"): raise RuntimeError("not image "+ct)
    return data, EXT.get(ct,"png")

MONS={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def parse_date(v):
    v=v.strip()
    m=re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})$',v)
    if m: return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    m=re.match(r'^([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2}),?\s+(\d{4})$',v)
    if m and m.group(1).title() in MONS: return f"{m.group(3)}-{MONS[m.group(1).title()]}-{int(m.group(2)):02d}"
    return None

META={
 '3d-struct-analysis':('三维结构分析',['RDKit','Structure','Bioinformatics'],'Technology'),
 'ab-gen-post':('AB-Gen 抗体设计',['AB-Gen','Antibody Design'],'Technology'),
 'ai_in_drugs':('AI 在药物研发中的应用',['AI for Drug Discovery'],'Technology'),
 'ai_in_drugs_lecture':('AI 在药物研发中的应用（讲座）',['AI for Drug Discovery','Lecture'],'Technology'),
 'bioinfo_conf_journal':('生物信息学会议与期刊',['Bioinformatics','Academia'],'Research'),
 'deep_learning':('DL 深度学习笔记',['Deep Learning','Basic'],'Technology'),
 'dft_organic_reaction':('DFT 有机反应建模',['DFT','Chemistry'],'Technology'),
 'dl_in_graph':('深度学习在图上的应用',['GNN','Deep Learning'],'Technology'),
 'drug_design_notes':('药物设计笔记',['Drug Design'],'Technology'),
 'google_site_dev':('Google Sites 网站开发',['Google Sites','Web'],'Technology'),
 'graduate_training':('研究生科研训练',['PhD','Mentoring'],'Research'),
 'graph_dl':('图深度学习：成果、挑战与未来',['GNN','Deep Learning'],'Technology'),
 'hat_acquisition':('杰青/优青项目申请',['Funding','Proposal Writing'],'Research'),
 'industrial_enzymes':('工业酶调研',['Enzyme','Industry'],'Technology'),
 'md_simulations_amber':('Amber 分子动力学模拟',['Amber','Molecular Dynamics'],'Technology'),
 'md_simulations_gromacs':('GROMACS 分子动力学模拟',['GROMACS','Molecular Dynamics'],'Technology'),
 'proposal_intent_writing':('基金申请意向书写作',['Proposal Writing'],'Research'),
 'proposal_writing':('基金申请技巧',['Proposal Writing'],'Research'),
 'reinvent_study':('REINVENT 系列介绍',['REINVENT','Molecular Generation'],'Technology'),
 'rl':('RL 强化学习笔记',['Reinforcement Learning'],'Technology'),
 'translational_funds':('转化基金申请写作',['Funding','Proposal Writing'],'Research'),
 'tts':('TTS 语音合成',['TTS','Speech'],'Technology'),
 'vaccine_dev':('疫苗设计',['Vaccine Design'],'Technology'),
 'visual_tools':('可视化工具',['Visualization','Tools'],'Technology'),
}
fence=re.compile(r'^\s*(```|~~~)'); head=re.compile(r'^(#{1,6})(\s)'); lh=re.compile(r'^(\s*[-*+]\s+)(#{1,6})(\s)')
b64_re=re.compile(r'!\[(?P<alt>[^\]]*)\]\(data:image/(?P<ext>[a-zA-Z]+);base64,(?P<b64>[^)]+)\)')
feishu_re=re.compile(r'(!\[[^\]]*\]\()(https://internal-api-drive-stream\.feishu\.cn[^)]+)(\))')
norm=lambda t: re.sub(r'[\s*#＃:：（）()&\-/]','',t)

summary={}
for name,(title,tags,cat) in META.items():
    d=f'content/posts/{name}'
    srcs=glob.glob(d+'/*.md'); idx=d+'/index.md'
    src=idx if os.path.exists(idx) else srcs[0]
    raw=open(src,encoding='utf-8').read().replace('\r\n','\n')
    okimg=failimg=0

    # base64 -> OSS
    parts=[]; last=0
    for m in b64_re.finditer(raw):
        parts.append(raw[last:m.start()]); last=m.end()
        try:
            ext=m.group('ext').lower(); ext='jpg' if ext=='jpeg' else ext
            fd,tmp=tempfile.mkstemp(suffix='.'+ext); os.close(fd)
            open(tmp,'wb').write(base64.b64decode(m.group('b64'))); url=upload(tmp); os.remove(tmp)
            parts.append(f"![{m.group('alt') or title}]({url})"); okimg+=1
        except Exception as e:
            parts.append(m.group(0)); failimg+=1; log(f"  B64 FAIL {name}: {e}")
    parts.append(raw[last:]); raw=''.join(parts)
    # feishu -> OSS
    for m in list(feishu_re.finditer(raw))[::-1]:
        try:
            data,ext=dl(m.group(2)); fd,tmp=tempfile.mkstemp(suffix='.'+ext); os.close(fd)
            open(tmp,'wb').write(data); url=upload(tmp); os.remove(tmp)
            raw=raw[:m.start()]+m.group(1)+url+m.group(3)+raw[m.end():]; okimg+=1
        except Exception as e:
            failimg+=1; log(f"  FEISHU FAIL {name}: {e}")
    log(f"{name}: images ok={okimg} fail={failimg}")

    # lift Date: line
    date=None
    dm=re.search(r'(?im)^[ \t]*date[ \t]*[:：][ \t]*(.+?)[ \t]*$', raw)
    if dm:
        date=parse_date(dm.group(1))
        if date: raw=raw[:dm.start()]+raw[dm.end():]
    if not date: date='2024-01-01'; log(f"  {name}: NO DATE -> placeholder")

    lines=raw.split('\n')
    # remove first heading if it duplicates the title
    i=0
    while i<len(lines) and lines[i].strip()=='': i+=1
    if i<len(lines):
        m=re.match(r'^#{1,6}\s+(.*)$', lines[i])
        if m and (norm(m.group(1)) and (norm(m.group(1)) in norm(title) or norm(title) in norm(m.group(1)))):
            del lines[i]

    # demote if any H1 outside fences
    has_h1=False; inf=False
    for ln in lines:
        if fence.match(ln): inf=not inf; continue
        if not inf and (re.match(r'^# ',ln) or re.match(r'^\s*[-*+]\s+# ',ln)): has_h1=True; break
    out=[]; inf=False
    for ln in lines:
        if fence.match(ln): inf=not inf; out.append(ln); continue
        if not inf and has_h1:
            m=head.match(ln)
            if m and len(m.group(1))<6: ln='#'+ln
            else:
                m2=lh.match(ln)
                if m2 and len(m2.group(2))<6: ln=m2.group(1)+'#'+m2.group(2)+m2.group(3)+ln[m2.end():]
        out.append(ln)
    body='\n'.join(out).lstrip('\n').rstrip('\n')

    FM=('---\n'+f'title: "{title}"\nsubtitle: ""\ndate: {date}\ndraft: false\n'
        f'author: "Xiaopeng Xu"\ndescription: "{title}相关笔记。"\n'
        f'tags: [{", ".join(chr(34)+t+chr(34) for t in tags)}]\ncategories: ["{cat}"]\n'
        'lightgallery: true\ntoc:\n  enable: true\n---\n')
    open(idx,'w',encoding='utf-8').write(FM+'\n'+body+'\n')
    if src!=idx and os.path.exists(src): os.remove(src)
    summary[name]={'date':date,'images_ok':okimg,'images_fail':failimg,'size_kb':os.path.getsize(idx)//1024}
    log(f"DONE {name} date={date}")

json.dump(summary,open(RES,'w'),ensure_ascii=False,indent=2)
log("ALL DONE")
