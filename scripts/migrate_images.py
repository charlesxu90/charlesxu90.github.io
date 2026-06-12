#!/usr/bin/env python3
"""One-off: migrate Feishu temp-image URLs (and staged TODO placeholders) to
Aliyun OSS via the running PicGo HTTP server, rewriting the markdown in place."""
import re, os, glob, json, tempfile, urllib.request, time

PICGO = "http://127.0.0.1:36677/upload"
LOG = "/tmp/migrate.log"
RESULT = "/tmp/migrate_result.json"

def log(msg):
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(msg + "\n")

def picgo_upload(path):
    req = urllib.request.Request(PICGO, data=json.dumps({"list": [path]}).encode(),
                                 headers={"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=120))
    if r.get("success") and r.get("result"):
        return r["result"][0]
    raise RuntimeError(r.get("message", "picgo failed"))

EXT = {"image/png": "png", "image/jpeg": "jpg", "image/jpg": "jpg",
       "image/webp": "webp", "image/gif": "gif", "image/svg+xml": "svg"}

def download(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        ct = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
        data = resp.read()
    if not ct.startswith("image/"):
        raise RuntimeError(f"not an image (ct={ct})")
    return data, EXT.get(ct, "png")

def migrate_url(url):
    data, ext = download(url)
    fd, tmp = tempfile.mkstemp(suffix="." + ext); os.close(fd)
    open(tmp, "wb").write(data)
    try:
        return picgo_upload(tmp)
    finally:
        os.remove(tmp)

open(LOG, "w").close()
summary = {}
feishu_re = re.compile(r'(!\[[^\]]*\]\()(https://internal-api-drive-stream\.feishu\.cn[^)]+)(\))')

# total for progress
files = sorted(glob.glob("content/posts/*/index.md"))
grand = sum(len(feishu_re.findall(open(f, encoding="utf-8").read())) for f in files)
done = 0
log(f"START feishu_total={grand}")

for f in files:
    s = open(f, encoding="utf-8").read()
    matches = list(feishu_re.finditer(s))
    if not matches:
        continue
    name = f.split("/")[2]
    ok = fail = 0
    # process right-to-left so spans stay valid
    for m in reversed(matches):
        url = m.group(2)
        try:
            oss = migrate_url(url)
            s = s[:m.start()] + m.group(1) + oss + m.group(3) + s[m.end():]
            ok += 1
        except Exception as e:
            fail += 1
            log(f"  FAIL {name}: {e} :: {url[:70]}")
        done += 1
        if done % 10 == 0 or done == grand:
            log(f"  progress {done}/{grand} (current {name})")
    open(f, "w", encoding="utf-8").write(s)
    summary[name] = {"ok": ok, "fail": fail}
    log(f"DONE {name}: ok={ok} fail={fail}")

# staged TODO placeholders (intelligent_systems etc.)
todo_re = re.compile(r'<!-- TODO image:[^>]*?Original saved at ([^\s]+)[^>]*?-->')
for f in files:
    s = open(f, encoding="utf-8").read()
    if "TODO image" not in s:
        continue
    name = f.split("/")[2]
    def repl(m):
        rel = m.group(1)
        path = os.path.join("/home/xux/Desktop/MyPage", rel)
        try:
            oss = picgo_upload(path)
            log(f"  TODO {name}: uploaded {rel}")
            return f"![{name}]({oss})"
        except Exception as e:
            log(f"  TODO FAIL {name}: {e}")
            return m.group(0)
    s2 = todo_re.sub(repl, s)
    if s2 != s:
        open(f, "w", encoding="utf-8").write(s2)
        summary.setdefault(name, {}).update({"todo_fixed": True})

json.dump(summary, open(RESULT, "w"), ensure_ascii=False, indent=2)
log("ALL DONE")
