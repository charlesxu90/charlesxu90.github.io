---
title: "驭缰工程（Harness Engineering）：AI 时代软件工程的新范式"
subtitle: ""
date: 2026-06-15
draft: false
author: "Xiaopeng Xu"
description: "梳理 Harness Engineering（驭缰工程）的核心概念：Agent = Model + Harness、五层架构与三个调节维度，及其与传统需求文档、Claude Code 的关系。"
tags: ["Harness Engineering", "Agentic AI", "Software Engineering"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

> "如果 Agent = Model + Harness，而你不是模型本身，那么你就是 Harness 的一部分。"
>
> —— Viv Trivedy，LangChain，2026

---

## 引言：一匹需要缰绳的马

2026 年初，HashiCorp 联合创始人 Mitchell Hashimoto 在记录自己 AI 使用历程的博客中，提出了一个简洁而深刻的工程原则：每当智能体（Agent）犯错时，工程师的职责不是"重试"，而是"构建一个让 Agent 永远不再犯同类错误的解决方案" [1]。这个原则，被后来的社区命名为 **Harness Engineering（驭缰工程）**。

随后，OpenAI 工程师 Ryan Lopopolo 发表了一篇里程碑式的文章，记录了他的团队如何用 5 个月时间、3 名工程师、0 行手写代码，通过 Codex 构建了一个拥有约 100 万行代码的内部产品 [2]。Martin Fowler 则从软件工程方法论的角度，对这一范式进行了系统性阐述 [3]。

"Harness" 的字面意思是马具（缰绳、鞍具）。这个比喻极为贴切：大语言模型（LLM）就像一匹蛮力十足但方向感不稳的马，Harness 的作用是把它的能量引导到正确的方向上。**Harness Engineering 并不优化模型本身，而是优化模型运行的环境。**

本文将系统梳理 Harness Engineering 的核心概念，并深入分析它与传统软件工程文档体系、Claude Code 架构，以及 AI 时代人类工程师不可替代价值之间的关系。

<!--more-->

---

## 一、什么是 Harness Engineering？

### 1.1 概念的演进脉络

理解 Harness Engineering，需要先看清它所处的历史坐标。它是一条演进链条上的第三个阶段：

**Prompt Engineering（2022–2024）** 关注的是单次交互的质量——如何写出一个好的提示词，让模型在一次对话中给出正确答案。这个阶段的核心问题是"如何表达意图"。

**Context Engineering（2024–2025）** 关注的是单次上下文窗口的质量——如何组装、压缩、排序输入给模型的信息，使其在有限的 Token 预算内做出最佳判断。这个阶段的核心问题是"如何喂养模型"。

**Harness Engineering（2026–）** 关注的是整个 Agent 系统的可靠性——如何设计约束、反馈回路和质量门控，使 Agent 在跨会话、长周期、多智能体协作的真实工程场景中，持续、可靠地产出符合预期的结果。这个阶段的核心问题是"如何驾驭 Agent"。

三个阶段的边界，可以用一个简单的时间维度来区分：Prompt Engineering 优化一次对话，Context Engineering 优化一个上下文窗口，而 Harness Engineering 优化整个任务生命周期。

### 1.2 核心公式

Harness Engineering 的核心公式极为简洁：

> **Agent = Model + Harness**

如果你不是模型本身，你就是 Harness 的一部分。这意味着 Harness 包含了围绕模型的一切非模型组件：系统提示、工具注册表、权限系统、上下文管理、反馈回路、会话持久化、编排逻辑……

### 1.3 Harness 的五层架构

一个成熟的 Harness 通常包含五个层次，每一层解决不同维度的可靠性问题：

| 层级 | 核心问题 | 主要制品与机制 |
|---|---|---|
| **Layer 1：记忆层（Memory）** | Agent 知道什么？ | `CLAUDE.md`、`AGENTS.md`、`architecture.md`、技能文件（Skills）|
| **Layer 2：工具层（Tools）** | Agent 能触达什么？ | 权限门控工具（Bash、Read、Write、Grep 等）、MCP 服务器 |
| **Layer 3：权限层（Permissions）** | Agent 被允许做什么？ | `settings.json`、deny-first 规则体系、权限模式 |
| **Layer 4：钩子层（Hooks）** | 运行时强制执行什么？ | `PreToolUse`/`PostToolUse` 钩子、自定义 Linter、结构测试 |
| **Layer 5：可观测层（Observability）** | 人类能看到什么？ | 会话日志、成本追踪、自我验证循环 |

这里有一个至关重要的区分，是许多工程师的认知盲区：

> **`CLAUDE.md` 中的规则只是建议（Advice），不是约束（Enforcement）。** 模型读取它、权衡它，大多数时候会遵守，但一次上下文截断、一次置信度过高的幻觉，都可以覆盖它。只有钩子层（`PreToolUse` 钩子退出码为 2）和权限层（`settings.json` 的 deny 规则）才是模型无法绕过的强制法则。

### 1.4 Harness 的三个调节维度

Martin Fowler 进一步将 Harness 的调节目标分为三个维度 [3]：

**可维护性 Harness（Maintainability Harness）**：调节代码内部质量，包括重复代码检测、圈复杂度、测试覆盖率、架构漂移、风格违规等。这是目前工具链最成熟的维度，计算型传感器（Linter、类型检查器）可以可靠地覆盖大部分问题。

**架构适应性 Harness（Architecture Fitness Harness）**：调节系统的非功能性特征，包括性能要求、可观测性规范、安全编码约定等。通常通过 Fitness Functions（适应度函数）来量化和监控。

**行为 Harness（Behaviour Harness）**：调节应用是否按预期功能运行。这是目前最难解决的维度——AI 生成的测试套件质量参差不齐，大量依赖 AI 生成测试的团队实际上是在用"AI 验证 AI"，信任链存在根本性缺陷。这一维度仍需要大量人工测试和监督。

---

## 二、与传统需求文档的关系：形态转化，而非替代

### 2.1 传统文档的根本局限

在讨论关系之前，需要理解传统文档体系的本质局限。BRD、PRD、TRD 等文档，其核心功能是**人类之间的对齐制品（Alignment Artifact）**——它们依赖人类的阅读理解、隐性知识和判断力来弥补文档的模糊性。

AI Agent 无法消费这种模糊性。GitHub 工程团队在 2025 年指出：

> "我们正在从'代码是事实之源'转变为'意图是事实之源'。有了 AI，规格说明成为事实之源，决定了什么被构建。"

传统 PRD 对 AI Agent 存在三个致命缺陷：其一，模糊性无法被推断——人类工程师可以凭经验理解"系统需要高性能"，但 Agent 需要明确的可测量指标；其二，整体性叙述无法被顺序执行——PRD 为人类理解整体愿景而优化，Agent 需要依赖顺序排列、每步有明确验收标准的分阶段任务；其三，文档与代码分离导致漂移——存在于 Confluence 或 Google Docs 中的文档，Agent 无法访问，对 Agent 而言等于不存在。

### 2.2 传统文档的"形态转化"路径

Harness Engineering 并非抛弃传统文档的内容，而是将其**重新编码（Re-encode）**为 Agent 可直接消费的制品：

**PRD 的转化**：产品愿景被保留在 SPEC.md 的高层描述中；功能列表和用户故事被转化为分阶段任务文件（Tasks），每个任务的工作量控制在 5–15 分钟，具有可测试的检查点；验收标准被转化为可执行的 BDD 场景或结构测试；非目标（Non-goals）被转化为显式的约束声明（如 `DO NOT CHANGE` 保护模式）。

**TRD 的转化**：技术设计文档被一分为二。架构规范部分被机械化为自定义 Linter 规则和结构测试——OpenAI 团队将依赖方向（Types → Config → Repo → Service → Runtime → UI）编码为自定义 Linter，违规时错误消息内嵌修复指令，让 Agent 能自我纠正 [2]。架构描述部分被转化为版本控制的活体文档（`architecture.md`），通过 CI 钩子检测文档与代码的漂移，解决了传统 TRD 最大的痛点：文档腐烂（Documentation Rot）。

**ADR 的地位提升**：在所有传统文档中，架构决策记录（ADR）是唯一被完整保留的形式。原因在于 ADR 记录的是"为什么"——决策背后的约束、权衡和理由——这是 Agent 永远无法从代码中自动推断的人类判断。ADR 被版本化存入仓库，成为 Agent 的"冷记忆知识库"的重要组成部分。

下表总结了这一转化关系：

| 传统文档 | Harness 中的对应制品 | 转化性质 |
|---|---|---|
| BRD 业务目标 | SPEC.md 的 Why/Vision 区块 | 浓缩保留 |
| PRD 功能列表 | 分阶段 Tasks 文件 | 结构化拆解 |
| PRD 验收标准 | 可测试检查点（Testable Checkpoints）| 可执行化 |
| PRD 非目标 | 显式约束声明（`DO NOT CHANGE`）| 显式化 |
| TRD 架构规范 | 自定义 Linter + 结构测试 | 机械化强制 |
| TRD 架构描述 | `architecture.md`（活体文档）| 持续同步 |
| 开发规范文档 | `AGENTS.md` 代码风格区块 | 示例化 |
| ADR 架构决策 | 版本化 ADR（仓库内）| 完整保留，地位提升 |

> **一言以蔽之**：传统文档是写给人看的，Harness Engineering 要求文档同时写给 Agent 看——这不是内容的消亡，而是形式的进化。

---

## 三、与 Claude Code 的关系：套娃式的嵌套结构

### 3.1 Claude Code 是一个 Harness

2026 年 3 月，Claude Code 2.1.88 版本因 npm source map 打包错误意外泄露了超过 50 万行 TypeScript 源代码。研究人员随即进行了逆向工程分析，得出了一个震撼性结论 [4]：

> **Claude Code 代码库中，约 98.4% 是操作基础设施（Harness），只有约 1.6% 是 AI 决策逻辑。**

其核心 Agent 循环极其简单——一个 `while(true)` 循环：组装上下文 → 调用 Claude 模型 → 解析 `tool_use` 请求 → 通过权限门控路由 → 执行工具并收集结果 → 重复，直到模型输出纯文本（停止信号）。

让 Claude Code 成为生产级工具的，是包裹这个循环的 98% 的基础设施：五层上下文压缩管线、deny-first 权限系统、会话持久化与分支管理、MCP 集成层、工具搜索机制……这些都是 Harness Engineering 的产物。

### 3.2 双层 Harness 结构

Martin Fowler 提出了一个关键区分 [3]：Claude Code 这类工具形成了一个**双层 Harness 结构**，两层之间的边界，正是 Harness Engineering 实践的分水岭。

**构建者 Harness（Builder Harness）**：由工具提供商（如 Anthropic）构建，即 Claude Code 本身。它包含 Agent 循环、工具分发、权限系统、上下文压缩等。这一层对用户而言是黑盒，但可以通过配置接口进行调整。

**用户 Harness（User Harness）**：由工程团队在 Claude Code 之上构建。这包括 `CLAUDE.md`、自定义 Linter 规则、架构约束、反馈回路、技能文件等。这一层是 Harness Engineering 实践的主战场。

```
三个同心圆（从内到外）：

① 模型（Model）
   └─ Claude 3.x / 4.x 系列模型本身

② 构建者 Harness（Builder Harness）= Claude Code 本身
   └─ Anthropic 构建的：Agent 循环、工具分发、权限系统、
      上下文压缩、会话持久化、MCP 集成……

③ 用户 Harness（User Harness）= 工程团队通过 Harness Engineering 构建的部分
   └─ 工程团队构建的：CLAUDE.md、自定义 Linter、架构约束、
      反馈回路、技能文件、执行计划……
```

这个结构解释了一个重要的数据点：Addy Osmani 的分析发现，同一个 Claude Opus 4.6 模型，在 Claude Code 内部运行的得分，远低于在定制用户 Harness 中运行的得分 [1]。LangChain 团队仅通过改进 Harness（不改动模型权重），在 Terminal Bench 2.0 上将同一模型从第 30 名提升至第 5 名。

**模型提供智能，Harness 提供可靠性。** 当多个团队使用同一个底层模型时，用户 Harness 的质量成为唯一的差异化变量。

---

## 四、软件工程实践的全景拆解：哪些是，哪些不是

### 4.1 坐标系：两个正交维度

要精确理解 Harness Engineering 的边界，需要建立两个正交的分类维度：

**维度一**：该工作是否属于 Harness Engineering？（是否在"设计 Agent 运行的约束环境"这个范畴内？）

**维度二**：AI 当前能否替代该工作？（可替代 / 可辅助 / 不可替代）

### 4.2 属于 Harness Engineering，且 AI 可以大量替代

这是当前 AI 能力最充分释放的区域。这些工作的共同特征是"形式明确、可验证"——要么是代码（可运行），要么是结构化文档（可检查）。

| 实践活动 | Harness 层次 | AI 替代程度 |
|---|---|---|
| 编写 AGENTS.md / CLAUDE.md 初稿 | 记忆层 | 高（需人类基于失败历史校正）|
| 编写自定义 Linter 规则 | 约束层 | 高（从架构约束描述生成规则）|
| 编写结构测试（ArchUnit 等）| 约束层 | 高（依赖方向测试、模块边界测试）|
| 编写 PreToolUse / PostToolUse 钩子 | 钩子层 | 高（本质是代码，AI 擅长）|
| 生成 architecture.md 初稿 | 记忆层 | 高（从代码库扫描生成模块地图）|
| 配置 MCP 服务器接入 | 工具层 | 高（配置文件编写）|
| 编写 CI 质量门控脚本 | 质量门控层 | 高（标准 CI 配置）|
| 文档"园丁"任务（检测过时文档）| 记忆层 | 高（OpenAI 团队已用 Agent 自动完成）|

### 4.3 属于 Harness Engineering，但 AI 目前无法替代

这是 Harness Engineering 中最具价值、也最难被替代的部分。这些工作的本质是**价值判断**，而非**形式转换**。

**决定哪些约束值得编码**：基于团队的失败历史和业务风险权衡，判断哪些错误需要转化为硬性约束。AI 没有这个上下文，无法做出这个判断。Mitchell Hashimoto 的 Ghostty 项目中，`AGENTS.md` 的每一行都可以追溯到一个真实的 Agent 失败案例——这个历史只存在于工程师的记忆中。

**设计反馈信号的语义**：一条说"违规检测"的 Linter 错误需要人类解读；一条说"请使用 `logger.info({event: 'name', ...data})` 替代 `console.log`"的错误消息则能让 Agent 自我纠正。设计这种"对 Agent 有意义"的错误消息，需要理解 Agent 的推理模式，这是一种元认知能力。

**制定验收标准（Acceptance Criteria）**：Martin Fowler 明确指出，如果人类没有清晰指定"什么是正确的"，任何传感器都无法检测正确性 [3]。验收标准是 Harness 的"根"，是整个约束系统的起点，必须由人类提供。

**架构决策（ADR）的制定**：涉及技术债、团队能力、业务约束的多维权衡，AI 只能提供选项矩阵，无法做出最终判断。

**判断 Harness 的边界与介入时机**："这个项目需要什么层次的 Harness？""Agent 何时需要人类审批？"这些问题本身就是判断问题，无法自动化。

### 4.4 不属于 Harness Engineering 的工作

这里有一个常见的认知混淆需要澄清：**编写业务逻辑代码不是 Harness Engineering，而是 Agent 执行的任务**。Harness Engineering 关心的是"如何让 Agent 可靠地完成这些任务"，而不是"完成这些任务本身"。

| 实践活动 | 与 Harness 的关系 |
|---|---|
| 编写业务逻辑代码、重构 | Agent 的输出物，不是 Harness |
| 编写单元测试 | Agent 的输出物（但测试质量是 Harness 监控的对象）|
| 编写 API 文档 | Agent 的输出物（但文档是 Harness 记忆层的原材料）|
| 产品战略决策、用户研究 | 超出 Harness Engineering 范畴，也无法被 AI 替代 |
| 系统级架构权衡、安全威胁建模 | 超出 Harness Engineering 范畴，也无法被 AI 替代 |

---

## 五、Harness Engineering 的三个核心误解

**误解一："写 AGENTS.md 就是 Harness Engineering 的全部"**

`AGENTS.md` 只是 Harness 的意图层（Layer 1），是建议而非约束。真正的 Harness 必须包含强制执行层——钩子（Hooks）、权限规则（Permissions）、CI 质量门控。一个只有 `AGENTS.md` 的 Harness，就像只有交通法规而没有红绿灯和摄像头的道路系统。

**误解二："Harness Engineering 是一次性工作"**

Harness 是一个**持续演化的系统**，每次 Agent 犯错都应该触发 Harness 的更新。Addy Osmani 将这个机制称为"棘轮（Ratchet）"——只加不减，直到某个约束因模型能力提升而变得冗余 [1]。好的 `AGENTS.md` 中的每一行，都应该可以追溯到一个具体的失败案例。

**误解三："更大的上下文窗口会让 Harness Engineering 变得不必要"**

上下文窗口的扩大解决的是"能看到多少信息"的问题，而 Harness Engineering 解决的是"如何确保输出符合约束"的问题。即使模型能看到整个代码库，它仍然需要明确的约束来防止架构漂移、安全漏洞和行为不一致。两者解决的是不同维度的问题。

---

## 六、OpenAI 百万行代码实验：Harness Engineering 的最佳实践案例

OpenAI 团队的实验是迄今为止 Harness Engineering 最具说服力的实证案例 [2]。5 个月、3 名工程师、约 100 万行代码、约 1,500 个 PR，人均日均 3.5 个 PR，效率约为传统方式的 10 倍。他们总结的核心 Harness 原则包括：

**设计环境，而非编写代码**：当 Agent 卡住时，诊断"缺少什么能力"并让 Agent 自己构建该能力。人类工程师的工作是识别能力缺口，而非填补它。

**机械化执行架构约束**：用自定义 Linter 强制执行依赖方向，且错误消息内嵌修复指令，让 Agent 能自我纠正。这将 TRD 中"应该遵守"的软性规范变成了"必须遵守"的硬性门控。

**仓库即唯一事实源**：Slack 讨论、Google Docs 中的知识对 Agent 等于不存在。所有对齐信息必须编码进仓库。

**将可观测性连接到 Agent**：通过 Chrome DevTools Protocol 让 Agent 能捕获 DOM 快照、查询日志和指标，使 Agent 能够自我验证。

**主动对抗熵**：用后台 Agent 任务定期清理低质量生成物（"AI Slop"），清理吞吐量与生成吞吐量同步扩展。

---

## 结语：工程师角色的本质转变

Harness Engineering 代表着软件工程师核心产出的一次根本性转变：**从"代码"到"约束系统"**。

在这个范式下，工程师的价值不再主要体现在敲击键盘的速度，而在于：

- 从失败历史中提炼规则的能力
- 将业务意图转化为可执行约束的能力
- 设计让 Agent 能够自我纠正的反馈回路的能力
- 判断何时介入、何时信任 Agent 的判断力

这些能力有一个共同的底层：**对"正确"的价值判断**。AI 可以执行，但无法定义"正确"。Harness Engineering 的本质，正是将人类对"正确"的判断，编码为 Agent 可以机械执行的约束系统。

模型提供智能，Harness 提供可靠性，而人类工程师提供方向。这三者的分工，构成了 AI 时代软件工程的新秩序。

---

## 参考文献

[1] Addy Osmani. (2026, April 19). *Agent Harness Engineering*. addyosmani.com. https://addyosmani.com/blog/agent-harness-engineering/

[2] Ryan Lopopolo / OpenAI. (2026, February 11). *Harness engineering: leveraging Codex in an agent-first world*. openai.com. https://openai.com/index/harness-engineering/

[3] Martin Fowler. (2026, April 2). *Harness engineering for coding agent users*. martinfowler.com. https://martinfowler.com/articles/harness-engineering.html

[4] Cobus Greyling. (2026, April 20). *98% of Claude Code Is Not AI*. cobusgreyling.substack.com. https://cobusgreyling.substack.com/p/98-of-claude-code-is-not-ai

[5] Augment Code. (2026, April 17). *Harness Engineering for AI Coding Agents: Constraints That Ship*. augmentcode.com. https://www.augmentcode.com/guides/harness-engineering-ai-coding-agents

[6] Wavespeed AI. (2026, April 6). *Claude Code Agent Harness: Architecture Breakdown*. wavespeed.ai. https://wavespeed.ai/blog/posts/claude-code-agent-harness-architecture/
