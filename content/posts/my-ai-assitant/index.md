---
title: "AI 助理配置"
subtitle: ""
date: 2026-05-16
draft: false
author: "Xiaopeng Xu"
description: "AI 助理配置笔记：常用 AI 编程助手的配置与使用。"
tags: ["AI Assistant", "Agentic AI"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Claude code 使用

https://github\.com/anthropics/claude\-code

https://deepwiki\.com/anthropics/claude\-code

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTg4OGFhMjU2NTU4OWE4N2VlOTBkZDM2OTM1OGM3N2ZfMzM2MDI0MjhkNzY1N2YwM2JmMjlmNzBhMTRhMGExZDZfSUQ6NzYwNDIwOTk0ODEyOTU3NzkyM18xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

### 安装

```Python
# Install
curl -fsSL https://claude.ai/install.sh | bash

# Uninstall
npm uninstall -g @anthropic-ai/claude-code

# Regular usage
claude
claude --resume

# Use without frequent responds
claude  --dangerously-skip-permissions

# Use resume previous sessions
claude  --dangerously-skip-permissions --resume
```

### 常用命令

```Python
# !直接运行命令输入，结果直接进上下文，不用来回切终端
!git status 
!npm test

# 双击Esc后悔药        
# 代码改乱了?按两下Esc， 直接回到上一个检查点，后悔来得及

#Ctrl+R翻旧账        
# 昨天的提示词忘了?按Ctrl+R秒速搜索历史对话，比翻记事本快

# @召唤文件
# 想引用某个文件?打@就行，像微信@人一样，再也不用复制粘贴
@results/file.fasta

# Remote 随时随地接力
# 网页版开始写代码，回家接着写用 claude--teleport 把云端会话"拉"到本地，无缝切换设备

# /export留下证据
# 重要对话输 /export 导出自动生成Markdown文档.写文档，复盘都超方便

# claude RD steps
/plan implement rate limiting on the /api/upload endpoint   # plan first, confirm
# ... approve plan ...
/prp-implement                                              # build w/ validation loops
/code-review --fix                                          # review + auto-apply cleanups
/security-review                                            # since it's an endpoint
/verify                                                     # run it, confirm behavior
/pr                                                         # push + open PR
```

### Claude\.md 命令

Claude\.md 是一个很重要的 claude 功能，能够让 claude 对项目结构有比较好的记忆，减少每次反复开发。在开发过程中，很好的维护他，会让开发效率大大提升。

```Python
# 自动生成CLAUDE.md 项目说明书
/init  
# AI scans your folders and creates a new guide with build commands and style rules

# Saving current status/ **Adding New Rules** into claude.md
"Update CLAUDE.md to include our new deployment commands."
"Update CLAUDE.md to include our new testing workflow."
# AI modifies the existing file without deleting your old instructions.

**# Maintenance**
"Refactor CLAUDE.md based on the current project structure."
# AI cleans up outdated paths or commands while keeping the core logic.

# Memory Updates 智能记忆
"记住我用bun不用npm"
# AI 会自动记在 CLAUDE.md 里。下次自动用对命令，不打断心流
```

### 
配置 Zotero MCP

由于我们需要经常根据文献来开发具体的 MCP 和 skills，尤其是针对 Rosetta 系列的蛋白设计软件。这时候，就需要同时基于代码库和文献中的 methods 描述来做设计。Zotero mcp 是一个很方便的 MCP，可以直接让 claude code 来访问 Zotero 的 API，这样就能直接看文章中的内容。后面做 ModelEvolve 中，同样也可以使用起来。

```Python
# claude mcp add zotero -- zotero-mcp
claude mcp add zotero -- /home/xux/.local/bin/zotero-mcp
```

注意需要打开 zotero 的 API 才可以使用。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTE4M2YxOTIyYzllYTE5ZDE2NmU4YmEzYmI2M2VlZjBfZjhmOTkyOTA2ZDMyZmQyMjBlY2M0ZTJmMzE1NjdlZjRfSUQ6NzYwNDE4Mzk2NjM4MzQ0MzEyMl8xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

### 配置 Asana MCP

https://developers\.asana\.com/docs/connecting\-mcp\-clients\-to\-asanas\-v2\-server\#cursor

首先，必须要安装好 claude code。

接下来，在 Asana 页面中，创建 Asana PAT。https://app\.asana\.com/0/my\-apps。 参考

https://developers\.asana\.com/docs/personal\-access\-token



接下来，需要安装 asana mcp

```Python
# Start with read-only to test safely
claude mcp add --scope user asana \
  -e ASANA_ACCESS_TOKEN=<YOUR_TOKEN> \
  -e READ_ONLY_MODE=true \
  -- npx -y @roychri/mcp-server-asana
  
My token: <YOUR_ASANA_TOKEN> 
```

手动在 Asana 中创建项目

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODhjODRiMzZhZWU1YjUxYzQ4YjY5MDE1NjA3NTM5YWNfMzEyN2UzMGI5ZWRjNGY3MmRmYTg5ZDYyMzE5OTY2MjVfSUQ6NzYxMjIxMjEwMDIxNTYyMjg1M18xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

之后，就可以打开 claude code，让其操作 Asana 项目了。

注意：可以将项目对应关系存储到 claude．md文件中，方便后续找对应性项目。

## ~~Vibe\-kanban~~

https://github\.com/BloopAI/vibe\-kanban

https://deepwiki\.com/BloopAI/vibe\-kanban

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTFhMjZhYjk4Y2QxZTg0MTYwYWZhYWQwODA4Zjk2MjFfNGNiYWE1ZjM5MDgzZTcwYzNkMTBjMDgxMDhkZDMxOTNfSUQ6NzYwNDIxMzA2Mzk5NDA2ODE2OF8xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

### 安装并启动

```Python
npx vibe-kanban@latest

PORT=45090 nohup npx vibe-kanban@latest 2>&1 > vibe-kanban.log &
```

在 Settings 里面配置 Claude Code 为其后台 vibe coding 工具，然后添加项目即可创建任务来使用。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjUzOTk4ZjEwYTRkNmVmYmU2YTczODY1ZDU5ZmU2OGRfMTc1OTM3MWI0MmUyOWU0ZDgyMDM5NzA0MGM3ZjBmZjdfSUQ6NzYwMjU3MTMwMzYyNzc3MTA3NF8xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

项目页面：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWM0YWVkMzc4NmJlY2UyZDI0M2ZjYjg0ZDQ5ODc0ZDhfZTkxNDYwYTg2ZDExYTdlNDYxNzg0ZTZmNTU1Y2ZmNWJfSUQ6NzYwMjU3MTA0MTQ5OTc5NDYyMl8xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

## ~~OpenClaw 使用~~



https://github\.com/openclaw/openclaw

https://deepwiki\.com/openclaw/openclaw

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGQyYzM3NmE1NGIzZjA0ODlhMDk3OGY3ZGNmZmZiMWNfZmQ5MTY3NzYxNmY5Y2IzODhhMzMwMzJiMzQ2YzEwOGFfSUQ6NzYwNDIwNDY1NjU0NTI1NDM0M18xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

### 安装并启动 OpenClaw

```Python
# Install and run openclaw
npm install -g openclaw@latest
# or: pnpm add -g openclaw@latest

openclaw onboard --install-daemon


# Install Feishu plugin (best for dev use)
openclaw plugins install @m1heng-clawd/feishu

# Restart gateway after plugin installation
openclaw gateway restart

# Run openclaw in background
nohup openclaw gateway --port 18789 2>&1 > openclaw.log &
```

### 配置WhatsApp机器人

按照默认的配置，扫描 QR 码就可以添加。添加后，给自己本人发消息，OpenClaw 就会回复。

### 配置飞书机器人

需要有组织的管理员权限，就可以配置飞书机器人。注意：权限配置非常重要，需要增加比较高的权限才可以使用。

### 安装 OpenClaw skills

https://github\.com/openclaw/clawhub

https://github\.com/VoltAgent/awesome\-openclaw\-skills

OpenClaw必备三技能：1\.联网搜索\(tavily\-search\)，获取实时信息；2\.技能查询\(find\-skills\)，自动发现适配技能；3\.主动代理\(proactive\-agent\)，失败时自我迭代升级。装好这三项才能真正释放工具价值。

```Markdown
# 联网搜索(tavily-search)，获取实时信息, Enter BRAVE_API_KEY
openclaw configure --section web

# 技能查询(find-skills)
openclaw configure --section skills


# 主动代理(proactive-agent)，失败时自我迭代升级
openclaw configure --section skills
```

### Heartbeats

Edit `~/clawd/HEARTBEAT.md` with a checklist of things to monitor:

```Markdown
**# Heartbeat checklist**- Check email for urgent messages
- Review calendar for events in next 2 hours
- If idle for 8+ hours, send a brief check-in
```

Configure the interval in `~/.clawdbot/clawdbot.json`

```JSON
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "activeHours": {
          "start": "08:00",
          "end": "22:00"
        }
      }
    }
  }
}
```

### Cron jobs 

```Python
# Daily morning briefing at 7am
openclaw cron add --name "Morning brief" --cron "0 7 * * *" --message "Weather, calendar, top emails"
 
# One-shot reminder in 2 hours
openclaw cron add --name "Call back" --at "2h" --session main --system-event "Call the client"
 
# List active cron jobs
openclaw cron list
 
# Remove a job by ID (get the ID from the list output)
openclaw cron rm <job-id>
```

## ~~claw2kanban 使用，让 OpenClaw来管理任务看板~~

鉴于 OpenClaw 个人助理的便捷性和 Vibe－kanban 任务管理的直观性。我开发了 claw2kanban 插件，来让 OpenClaw 帮我做任务管理。这样就可以并行很多任务，自己也不用事必躬亲，只关注当下最重要的问题即可。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGIxOGU2Y2UyM2M1ZWVjN2M2ZWExMmZlNGI2YzVjY2ZfOTg0NjJiMzcyMzNkMzZmMDY0NTUyN2Y4MTM3MTA4MzdfSUQ6NzYwNDIyMDg2MDE0NDA3ODA0NV8xNzgxMjk5MDg4OjE3ODEzODU0ODhfVjM)

### 安装 OpenClaw claw2kanban 插件

```Markdown
# Option A — Link from local path (recommended for development)
openclaw plugins install --link /home/xux/Desktop/MyAssist/claw2kanban

# Option B — Install from the global npm link
openclaw plugins install @openclaw/vibe-kanban

openclaw gateway restart
```
