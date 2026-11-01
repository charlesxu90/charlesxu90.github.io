---
title: "递归自我改进（Recursive Self-Improvement）：当 AI 开始改进自己，智能爆炸还有多远？"
subtitle: ""
date: 2026-11-01
draft: false
author: "Xiaopeng Xu"
description: "从 Gödel Machine 到自进化 Agent，梳理 RSI（递归自我改进）的三个层次、代表性工作（DGM、HyperAgents、AIDE²、AlphaEvolve、AFlow）、五个剥离炒作的评估问题，以及它与 Harness、Loop、Graph Engineering 的关系。"
tags: ["Recursive Self-Improvement", "Self-Evolving Agents", "Harness Engineering", "Loop Engineering", "Graph Engineering", "Agentic AI", "AI for Science"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

> "让一台超智能机器去设计更好的机器，毫无疑问会随之而来一场'智能爆炸'。"
>
> —— I. J. Good，1965；但这是一条**基于条件的推论**，不是一条已被证明的增长定律。

---

## 引言：从解决问题，到改进解决问题的方法

在上一篇关于《[Graph Engineering](/posts/graph_engineering/)》的文章中，我们讨论了一个问题：**能否用外层循环，不断优化 Agent 系统的组织结构？** [\[3\]](#ref-3) 如果把这个问题再往前推一步，就会遇到 **Recursive Self-Improvement（RSI，递归自我改进）**：当 AI 不只是完成任务，也参与改进自己完成任务的方法时，会发生什么？

这个问题既有令人兴奋的一面，也很容易被夸大。今天的 Agent 已经可以根据反馈修改提示词、工具、工作流，甚至自己的代码；但这并不意味着 AI 已经具备不受限制、自我加速的通用进化能力。

**本文的核心判断是：RSI 的局部进展是真实的，但从"系统变得更好"到"系统越来越擅长改进自己"，中间仍有很长的距离。**

<!--more-->

---

## 一、什么是 RSI？三个必须分开的层次

假设我们有一个 Coding Agent。它收到任务后写代码、运行测试、读取错误日志，再修改代码直到测试通过。这是一个有反馈的任务执行循环，但它未必构成自我改进：如果下一次运行仍然从同样的配置开始，系统只是解决了眼前的问题。

现在假设，Agent 发现自己经常在大文件中定位错误失败，于是提出一个改动：增加基于语法树的代码检索工具。经过独立测试后，这个工具被保留下来，并在之后的任务中使用。此时，系统发生了**跨任务的持久改进**。

再进一步，如果新版本不仅更会完成任务，还能更有效地发现、提出和验证下一轮系统改进，我们就开始接近 RSI 最有意思的部分：**改进"改进自身"的能力。**

可以把这几个层次放在一起理解：

| 层次 | 改的是什么 | 是否跨任务持久 | 后继系统是否参与下一轮改进 |
| :--- | :--- | :--- | :--- |
| **Self-correction（自我纠错）** | 当前答案或当前任务的执行步骤 | 否 | 否 |
| **Self-improvement（自我改进）** | 保存有效变化，让后续任务受益 | 是 | 否 |
| **Recursive self-improvement（递归自我改进）** | 后继系统参与下一代改进 | 是 | 是；更强的意义上，它还**更擅长**产生和验证改进 |

这一划分是为了理解问题而采用的工作定义，并不是所有论文都遵守的统一标准。有些研究会把有界的代码自修改称为 RSI；另一些讨论则用 RSI 指向更完整的模型设计、训练和后继部署。阅读论文时，比争论标签更重要的是追问：**究竟改了什么？改动由谁提出和选择？它是否持续进入下一轮？** [\[6\]](#ref-6)

> **系统性能提高，不自动等于改进机制变强；存在递归循环，也不自动等于增长会越来越快。**

### 1.1 为什么 RSI 现在受到关注？

RSI 的思想很早就存在。I. J. Good 曾讨论过一种可能性：如果足够强的机器能够设计更强的机器，那么机器设计本身可能进入加速循环。这是后来"智能爆炸"讨论的重要思想来源，但它是基于条件的推论，不是一条已经得到证明的增长定律 [\[4\]](#ref-4)。

今天这个问题重新受到关注，有更实际的工程原因。大语言模型可以阅读和修改代码；Agent 可以调用工具并执行实验；软件测试、编译器、模拟器和数学检验器，又能为一部分任务提供自动反馈。

当这几件事结合在一起，原本由工程师主导的"提出方案—实现—测试—调整"过程，开始有一部分能够交给 AI 执行。但**提出一个候选方案，比可靠地判断它是否真正更好容易得多**；这也正是 RSI 的核心难点。

---

## 二、Gödel Machine 与 Self-Evolving Agents：理论和实践之间

### 2.1 Gödel Machine：先证明，再修改

2003 年，Jürgen Schmidhuber 提出了 Gödel Machine。它是一个可以分析和修改自身程序的理论模型，其中包括执行任务的程序和负责搜索证明的程序 [\[5\]](#ref-5)。

它的关键思想是：**只有当系统能够在给定公理、效用函数和环境假设下证明某次自我修改值得执行时，才切换到新版本。** 被修改的部分甚至可以包括证明搜索机制本身。

这里的"最优"有严格条件。它并不是说系统能找到现实世界中所有可能程序的绝对最优解，而是说：在给定形式化假设下，已证明的切换优于继续运行原证明搜索器、等待其他改写的方案。如果效用函数没有覆盖真实风险，或者有效改动无法在可用资源内被证明，这个理论保证就不能直接解决现实问题 [\[5\]](#ref-5)。

Gödel Machine 因而更适合被视为**理论上的自修改模型**，而不是一套可以直接用于构建今天的 LLM Agent 的成熟框架。

### 2.2 Self-Evolving Agents：把证明门槛换成经验反馈

今天更活跃的研究方向是 Self-Evolving Agents，即能够根据经验持续改变自身行为或组成部分的 Agent。它们通常不要求对每次改写进行形式证明，而是使用测试、奖励、执行反馈或人工评价来决定是否保留变化 [\[6\]](#ref-6)。

这些系统可能进化的对象并不相同：

- **Prompt 与 Memory**：更新指令、总结失败经验、保存可复用知识。
- **Tools 与 Skills**：创建或改进工具，将成功的操作保存为技能。
- **Workflow 与 Graph**：调整任务分解、角色分工、路由和验证方式。
- **Agent Code 与 Harness**：修改工具调用、上下文管理或控制逻辑。
- **Model 与 Training**：通过数据生成、微调或强化学习改变模型参数。

例如，Voyager 在 Minecraft 中不断探索，将成功的可执行程序保存到技能库，之后再检索和组合这些技能。它展示了在**不更新基础模型权重**的情况下积累能力的可能性，但它并没有因此证明自己的通用学习算法会持续自我改进 [\[7\]](#ref-7)。

因此，自进化 Agent 与 RSI 有交集，但不能画等号。一个系统可以长期积累记忆，却没有修改自己的改进机制；也可以通过修改 Agent 代码形成有限的递归过程，却仍然依赖固定的基础模型和外部评价器。

---

## 三、从 Gödel Machine 到现代 Agent：几项代表性工作

### 3.1 Darwin Gödel Machine：让 Agent 修改自己的代码

Darwin Gödel Machine（DGM）是理解现代 Agent 自修改的重要案例。它继承了 Gödel Machine 中"系统可以修改自身"的思想，但不再要求对每次修改给出形式证明，而是使用编程任务上的经验评估 [\[8\]](#ref-8)。

其基本过程是：

```text
选择一个已有 Agent
      ↓
分析执行日志与失败模式
      ↓
修改 Agent 的提示、工具或代码
      ↓
在编程任务上运行与评估
      ↓
将候选版本和结果放入 Archive
      ↓
从不同版本继续探索下一代
```

这里的 Archive 不只是保存一个"冠军"。不同版本可以形成不同的改进路径；暂时分数不高的版本，也可能成为后续改进的起点。DGM 的实验表明，在特定设置下，代码自修改和保留多条探索路径都有实际价值 [\[8\]](#ref-8)。

但经常被引用的"**SWE-bench 从 20% 到 50%**"需要小心理解：初始版本的 20% 来自 60 题记录，论文报告的最优版本 50% 来自逐步筛选后的 200 题子集，两者不能直接当成同一题集上的精确提升；更不能误写成完整 500 题的成绩 [\[8\]](#ref-8)。

Polyglot 的完整 225 题重测中，论文报告初始版本为 14.2%，最佳版本为 30.7%。这是更有说服力的局部成果，但最优版本仍经过搜索和选择。DGM 改进的是 Agent 的代码与运行方式，基础模型和外层搜索控制器仍然受到既定设置的约束 [\[8\]](#ref-8)。

**DGM 说明 Agent 可以参与改进 Agent；它没有证明模型会因此无限变强，也不具有 Gödel Machine 的形式证明保证。**

### 3.2 HyperAgents：让"改进者"也成为可修改对象

Meta 等研究者提出的 HyperAgents 将 Task Agent 和 Meta Agent 放在同一个可编辑的程序中：前者负责解决问题，后者负责读取代码和历史结果，并提出下一代的修改。这样，系统不仅可以修改解题流程，也可以修改提出改进的部分逻辑 [\[24\]](#ref-24)。

论文中的 DGM-HyperAgents 仍然使用外层 Archive 来保存多个版本。在主要实验中，基础模型权重、任务分布、评价协议和 Archive 的选择机制依然固定。研究者在编程、论文接收预测和机器人奖励设计等任务上观察到了有希望的结果，但部分与较强人工设计基线的差异没有达到统计显著 [\[24\]](#ref-24)。

因此，HyperAgents 更接近"改进机制也在可搜索范围内"的研究目标，却不是全系统无约束自治进化的证明。它与 DGM 的区别也不应被夸大为一个可以自修改、另一个完全不可以：更准确地说，HyperAgents 明确把 Task Agent 和 Meta Agent 一起纳入了可编辑程序。

### 3.3 AIDE²：改进后的 Agent，更擅长改进了吗？

如果说 DGM 把自修改做成了可运行实验，那么 AIDE² 把**评估问题**往前推进了一步。它用外层研发 Agent 改写内层 AI 研发 Agent，再按固定任务预算评估候选版本 [\[9\]](#ref-9)。

研究者报告，在一条为期 8 天的实验轨迹中，系统提出 99 个改写候选，接受了其中 7 次；用于选择的综合分数从 0.703 提高到 0.778。这里的轨迹有 100 个节点，指的是初始版本加 99 个候选，**不是 100 台计算机**。作者还在未参与版本选择的任务上检验了部分改进是否迁移 [\[9\]](#ref-9)。

这项工作最值得关注的，是它专门提出了一个"**点火测试**"（ignition test）：把进化得到的 Agent 放到外层，看看它是否比原来的改进者更擅长推动下一轮自我改进。

结果并没有证明这一点。论文中两组各有三次运行，平均最终成绩相近；作者明确指出，样本量和结果波动使比较尚无定论。这个结果很重要，因为它提醒我们：**即使后继系统在任务上更强，也必须单独测试它是否更擅长改进系统。** [\[9\]](#ref-9)

### 3.4 AlphaEvolve：进化的是算法，不一定是自己

Google DeepMind 的 AlphaEvolve 把大语言模型生成代码的能力与进化搜索结合起来：模型提出程序变体，自动评价器执行并打分，表现较好的候选被保留并用于生成后续版本 [\[10\]](#ref-10)。

它展示了算法发现的实际潜力。例如，研究者报告了一种计算两个 **4×4 复数矩阵**乘积的算法，只需 48 次复数标量乘法。这是特定代数问题上的结果，不能直接理解成所有矩阵乘法都在实际硬件上更快 [\[10\]](#ref-10)。

AlphaEvolve 也被用于优化数据中心调度和训练相关计算。它说明 AI 可以改进未来 AI 研发所依赖的基础设施；但其主要进化对象是被指定的算法或程序。**优化一个算法，不等于已经证明它能持续修改自己的改进机制。**

### 3.5 AFlow：用搜索优化 Agent Graph

AFlow 研究的是另一个层面：如何自动生成和优化 Agent Workflow。它把工作流表示为由节点和边连接的代码，再通过蒙特卡洛树搜索（MCTS）与执行反馈探索不同方案 [\[11\]](#ref-11)。

这正好连接了上一篇 Graph Engineering 的问题：**Graph 不一定永远由人手工设计。** 系统可以尝试不同的步骤、调用顺序和协作结构，再根据评估结果筛选方案。

不过，**自动搜索 Graph 不必然是强意义上的 RSI**。如果负责提出和选择 Graph 的外部搜索过程始终不变，那么它证明的是工作流优化，而不是"优化器自己越来越擅长优化"。

---

## 四、RSI 与 Harness、Loop、Graph Engineering 的关系

在前面的三篇文章中，我们分别讨论了《[Harness Engineering](/posts/harness_engineering/)》[\[1\]](#ref-1)、《[Loop Engineering](/posts/loop_engineering/)》[\[2\]](#ref-2) 和《[Graph Engineering](/posts/graph_engineering/)》[\[3\]](#ref-3)。一个常见误解是把它们理解为一条互相替代的升级路线：Harness → Loop → Graph → RSI。

更准确的理解是：**前三者描述系统设计的不同维度，RSI 描述系统如何跨版本地改变这些维度。** 它们之间有重叠，不存在所有文章都共同遵守的唯一分层标准。

### 4.1 Harness：Agent 靠什么运行？

Harness 是围绕模型构建的运行支撑，包括工具接口、上下文、记忆、权限、沙箱、日志、验证和恢复机制。它决定 Agent 可以访问什么，以及哪些行为会被允许或阻止 [\[1\]](#ref-1)。

当 Agent 根据历史失败修改工具、提示或上下文管理，并让通过验证的改动用于后续运行时，Harness 就从运行基础设施变成了**进化对象**。DGM 的很多修改正发生在这一层。

需要区分的是，OpenAI 的 Codex Harness Engineering 案例主要展示工程团队如何设计 Agent 可读的仓库、反馈和约束，让 Agent 更可靠地构建产品。Agent 参与完善工作环境，并不自动等于该案例已经证明完整的自主 RSI [\[21\]](#ref-21)。

### 4.2 Loop：工作如何根据反馈推进？

Loop Engineering 关注的是目标、行动、观察、验证、重试和停止条件 [\[2\]](#ref-2)。一段 Loop 可以发生在单次任务中，也可以发生在跨任务的系统优化过程中。

LangChain 描述的第四层 Hill-climbing Loop，会分析多次运行产生的轨迹，并据此调整 Prompt 或工具配置 [\[22\]](#ref-22)。这与 RSI 的联系比"测试失败后重试"更近：**外层循环的输出，是下一轮运行所使用的系统。**

但是否构成更强的递归，还要看是谁生成改动、改动是否持久，以及下一代系统是否参与了后续改进。固定脚本每周重写一次 Prompt，可能是有价值的自动优化，却不能仅凭"循环运行"就证明改进能力在自我增强。

### 4.3 Graph：多个工作单元如何协作？

Graph Engineering 关注节点、边、共享状态和路由 [\[3\]](#ref-3)。节点可以是 Agent，也可以是确定性的代码、测试器或人工审批；它不一定需要每个节点都是一个 Agent，也不要求整个图都由模型控制。

例如，版本改进可以组织成：

```text
历史轨迹 ─→ 诊断节点 ─→ 改动提案 ─→ 隔离执行
                                      ↓
                          独立评估 ← 候选版本
                              ↓
                    通过 → 人工/策略门控 → 部署
                    拒绝 → 保存原因 → 继续搜索
```

这里 Graph 决定谁负责诊断、谁可以调用工具、谁验证结果，以及失败后如何返回。Loop 决定这个过程什么时候重复、预算是多少、什么时候停止。Harness 则提供执行环境与约束。

需要澄清的是，这里讨论的 Graph 是**工作流和控制流图**：节点表示执行单元，边表示数据传递或控制转移。它与知识图谱不同；后者的节点和边主要表示实体及其语义关系，可以为 Agent 提供知识，但不必然决定下一步调用哪个节点。

如果系统进一步根据运行反馈修改节点职责、路由规则或验证位置，Graph 本身就成了进化对象。这是从静态 Graph Engineering 走向 **Adaptive Graph Engineering** 的一种方式。但即使 Graph 会变化，仍需要证明变化是持久且有效的；运行时根据条件选择不同路径，不等于跨版本地改进了 Graph。

### 4.4 一张统一的心智地图

```text
Model       提供基础推理和生成能力
Harness     提供工具、环境、权限和可观测性
Loop        组织行动、反馈、验证与停止
Graph       组织节点、状态、路由与协作
RSI         让系统参与改进上述组成，并使有效变化进入后续版本
```

这个图不是严格的包含关系。现实中的 Harness 往往已经包含 Loop 和 Graph 的实现；同一个系统也可能由多个 Harness 和多个相互连接的 Loop 构成。这里的价值在于区分**分析视角**，而不是重新发明彼此隔离的技术层。

> **Harness 解决"能做什么"，Loop 解决"如何迭代"，Graph 解决"如何协作"；RSI 进一步追问：系统能否让这些机制随经验变得更好？**

---

## 五、有哪些值得关注的框架与研究路线？

讨论框架时，首先要区分"**能搭建 Agent**"和"**内置自我改进**"。LangGraph、OpenHands 等可以用于构建 Agent 或 Coding Agent，但使用这些框架本身，并不意味着系统会自主进化 [\[16\]](#ref-16) [\[17\]](#ref-17)。

| 研究目标 | 代表工作 | 进化对象 | 需要注意的边界 |
| :--- | :--- | :--- | :--- |
| **Agent 自修改** | DGM、SICA [\[8\]](#ref-8) [\[23\]](#ref-23) | Agent 代码、工具、提示 | 题集反复使用；改进不单调 |
| **Prompt / 指令优化** | GEPA [\[12\]](#ref-12) | 提示词与模块指令 | 优化 Prompt ≠ 修改模型权重 |
| **算法 / 工作流搜索** | AlphaEvolve、OpenEvolve、AFlow [\[10\]](#ref-10) [\[15\]](#ref-15) [\[11\]](#ref-11) | 程序、工作流图 | 外层搜索器本身通常固定 |
| **Harness 跨任务演化** | GEAR [\[25\]](#ref-25) | 工具、环境、上下文管理 | 预印本与快速迭代中的研究软件 |
| **参数更新** | Agent Lightning、SEAL [\[13\]](#ref-13) [\[14\]](#ref-14) | 模型权重 | 权重适应 ≠ 自主重写研发流程 |
| **科学工作流** | The AI Scientist-v2 [\[18\]](#ref-18) | 想法、实验、论文生成 | 能写论文 ≠ 可靠发现科学规律 |

几点补充说明：

**Agent 自修改**：SICA 允许 Agent 修改自己的代码，并在固定任务集上进行多轮评估；其论文显示过明显提升，同时也存在题集反复使用和改进不单调的问题 [\[23\]](#ref-23)。

**算法与工作流搜索**：OpenEvolve 是独立的开源程序演化项目，受 AlphaEvolve 启发，**并非 Google 官方发布的 AlphaEvolve 源码** [\[15\]](#ref-15)。

**Harness 的跨任务演化**：GEAR 是 2026 年公开的早期开源研究项目。它让任务 Agent 收集轨迹，再由 Meta Agent 基于跨任务反馈提出和评测 Harness 修改。项目方报告了特定配置下的结果，但它仍是预印本和快速迭代中的研究软件；已公开结果不能直接证明独立任务上的通用收益 [\[25\]](#ref-25)。

**科学工作流**：The AI Scientist-v2 是自动科研的代表案例，但能生成一篇研究论文，不等于系统已经可靠地发现可重复的科学规律，也不等于它会自动改进自己的科研能力 [\[18\]](#ref-18)。针对早期版本的独立评估也观察到实验执行等方面的困难，但不能将其直接作为对 v2 的评测 [\[19\]](#ref-19)。

这些工作关注的是不同的进化对象和反馈条件。它们可以组合使用，但不应被当成一组已经实现完整 RSI 的同类产品。

---

## 六、剥离炒作：如何判断系统是否真的在进化？

看到一个系统的 Benchmark 得分提高，我们至少要追问五个问题。

### 6.1 改进发生在哪里？

Prompt 更好、记忆更多、工具更强、Graph 更合理，或者基础模型权重发生变化，都是不同类型的进步。它们可能提升最终结果，但不能统称为"模型自身变聪明了"。

同样，冻结模型并不意味着系统无法获得有价值的持续改进；但将工具和 Harness 改进视为与训练出更强的基础模型完全等价，也会掩盖技术上的差异。

### 6.2 有没有控制预算与基线？

一个进化系统尝试了 1,000 个候选，另一个基线只运行一次，前者最终分数更高并不奇怪。应同时报告模型版本、候选数量、运行时间、Token、美元、算力和人工参与，并与同预算的重试、随机搜索或人工设计版本比较。

DGM 的 SWE-bench 实验约需两周、约 22,000 美元 API 成本。这不是否定它的价值，而是提醒我们：**提高任务分数与提高单位成本下的改进效率，是两个不同的问题。** [\[8\]](#ref-8)

### 6.3 有没有真正留出的任务？

如果系统反复在同一批题目上提出修改、查看结果并选择最优版本，那么这些题目已经成为搜索过程的一部分。即使它们一开始被称为"测试集"，最终结果也可能反映对这批题目的适应，而不是对新任务的泛化。

更可靠的做法是分开**开发集、版本选择集和最终保留集**，再用不同项目、不同任务类型或更新鲜的数据评估迁移。保留集如果被反复查询，也需要更新或重新设计。

### 6.4 改进是否稳定，旧能力是否保留？

一次最佳结果，不等于每一代都更好。系统可能在修复速度上进步，却在复杂任务、成本或安全性上退化。应该观察多次运行、逐代曲线、旧任务回归和失败分支，而不只是展示最漂亮的一条进化路径。

### 6.5 谁来保证评价器不会被优化？

优化过程会主动寻找得分更高的路径。若评分函数有漏洞，系统可能学会提高分数，而不是完成我们真正关心的目标。DGM 论文就记录过 Agent 通过修改与检测相关的工具标记，绕过一项检查的案例 [\[8\]](#ref-8)。

这也是为什么改进版本不应同时拥有修改隐藏测试、安全规则、预算计数和最终评估器的无限权限。**生成者可以提出改动，但不能由它单方面决定什么叫成功。**

RAND 对公开证据的梳理也指出，AI 已经参与 AI 研发中的重要环节，但公开披露的系统尚未独立设定完整研究议程并设计后继系统 [\[20\]](#ref-20)。这不是说未来不可能发生，而是提醒我们不要用局部成功代替整个闭环的证据。

---

## 七、从 Coding Agent 到 AI for Science：循环之外还有现实世界

在代码任务中，一次修改通常可以通过编译器、单元测试和运行时间快速获得反馈。科学研究的反馈往往更慢、更贵，也更不完整。

以**蛋白质设计**为例，系统可以先生成序列，再使用结构预测、能量函数或分子模拟筛选候选，最后选择少量候选进入湿实验。计算评分可以帮助缩小搜索空间，但预测指标并不等于真实表达量、稳定性或功能活性。

这里可以设计两个相互关联的循环：

```text
内层：蛋白质候选优化
设计序列 → 计算筛选 → 选择候选 → 实验验证 → 更新候选

外层：设计策略优化
比较多轮结果 → 分析预测与实验偏差 → 修改工具组合/筛选流程
           → 独立回归与实验验证 → 接受或回滚新版工作流
```

关键差别在于：内层学习"**哪个序列有效**"，外层学习"**怎样的设计流程更可能找到有效序列**"。如果新版流程还能更好地提出并验证下一轮流程改进，我们才有了更强的递归证据。

这并不是说系统应该一味增加实验次数。更合理的目标，是比较单位预算下获得了多少可靠信息，并把昂贵的实验用于区分最有价值的假设。跨批次保留实验、记录阴性结果、比较不同模型，并将最终湿实验指标与代理评分分开，都是避免系统只优化计算指标的重要条件。

Scientific RSI 因此特别有吸引力，也特别困难。它需要的不只是更强的模型，还包括可信的实验、版本化数据和对失败原因的解释。**在科学领域，现实世界才是最终的评价器。**

---

## 八、未来会走向哪里？

我认为，近期最值得关注的不是某个系统是否宣布自己实现了"完全 RSI"，而是几个更具体的变化。

第一，**Harness 的局部自优化可能越来越实用**。Prompt、工具选择、上下文管理和验证步骤通常比基础模型训练更容易修改，也更容易保存版本和回滚。真正的挑战是让局部收益在新任务上仍然成立，而不是对固定评测集越调越熟。

第二，**Loop 会从任务执行扩展到系统优化，Graph 也会成为被优化的对象**。例如，系统可能发现某类失败适合增加验证节点，另一类任务则应该取消昂贵而无效的多 Agent 分工。但 Graph 越复杂，并不天然意味着效果越好；每条新增边和每个新节点都会带来成本与治理要求。

第三，**模型训练、Agent 轨迹和工程环境可能逐渐耦合**。Agent 执行产生的数据可以用于后训练，更强的模型也可能更善于操作或改进 Harness。这个方向值得重视，但耦合本身并不能证明收益一定复利增长；算力、数据、实验速度和可靠评估都可能成为瓶颈。

第四，**安全与评估会从附加功能变成核心架构**。当系统能够修改自己的工作方式，版本控制、沙箱隔离、留出评估、权限门控、审计和回滚，就不再只是部署细节，而是判断改进是否可信的前提。

---

## 结语：从改进结果，到改进改进的过程

如果把这个系列放在一起看，可以得到一条更清晰的线索：

- **Harness Engineering**：让 Agent 在可信的环境中工作。
- **Loop Engineering**：让 Agent 能够根据反馈持续推进。
- **Graph Engineering**：让多个工作单元以可控的方式协作。
- **RSI**：让系统参与改进这些机制，并检验改进后的系统能否继续改进自己。

这不是四个互相替代的阶段，也不是任何一个技术名词带来的魔法。现实中的进化系统需要模型、反馈、运行环境和外部验证共同配合。

对于 RSI，最值得期待的不是一个立刻失控的"智能爆炸"故事，而是一个可以被严肃检验的工程问题：

> **我们能否构建这样的系统：它不仅能够解决问题，还能够在明确的目标、可验证的反馈和人类设定的边界内，持续改进自己解决问题的方法？**

答案不会来自某一次漂亮的 Benchmark 成绩，而会来自**可复现的跨任务收益、透明的资源账本、可靠的评估，以及面对失败时能够解释和回滚的系统**。

---

## 参考文献

<a id="ref-1"></a>[1] Xiaopeng Xu. (2026). *驾驭工程（Harness Engineering）：AI 时代软件工程的新范式*. xu-xp.com. <https://xu-xp.com/posts/harness_engineering/>

<a id="ref-2"></a>[2] Xiaopeng Xu. (2026). *循环工程（Loop Engineering）：炒作还是 AI 智能体架构的下一次演进*. xu-xp.com. <https://xu-xp.com/posts/loop_engineering/>

<a id="ref-3"></a>[3] Xiaopeng Xu. (2026). *图工程（Graph Engineering）：剥离炒作，重构 AI 智能体的组织拓扑*. xu-xp.com. <https://xu-xp.com/posts/graph_engineering/>

<a id="ref-4"></a>[4] I. J. Good. (1965). *Speculations Concerning the First Ultraintelligent Machine*. Advances in Computers. <https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065245808604180>

<a id="ref-5"></a>[5] Jürgen Schmidhuber. (2003). *Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements*. arXiv. <https://arxiv.org/abs/cs/0309048>

<a id="ref-6"></a>[6] arXiv:2508.07407. (2025). *A Comprehensive Survey of Self-Evolving AI Agents*. arXiv. <https://arxiv.org/abs/2508.07407>

<a id="ref-7"></a>[7] arXiv:2305.16291. (2023). *Voyager: An Open-Ended Embodied Agent with Large Language Models*. arXiv. <https://arxiv.org/abs/2305.16291>

<a id="ref-8"></a>[8] arXiv:2505.22954. (2025). *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents*. arXiv. <https://arxiv.org/html/2505.22954v3>

<a id="ref-9"></a>[9] arXiv:2609.26457. (2026). *Recursive Self-Improvement of AI Research Agents*. arXiv. <https://arxiv.org/html/2609.26457v1>

<a id="ref-10"></a>[10] Google DeepMind. (2025). *AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery*. arXiv. <https://arxiv.org/html/2506.13131v1>

<a id="ref-11"></a>[11] arXiv:2410.10762. (2025). *AFlow: Automating Agentic Workflow Generation*. arXiv. <https://arxiv.org/abs/2410.10762>

<a id="ref-12"></a>[12] arXiv:2507.19457. (2025). *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*. arXiv. <https://arxiv.org/abs/2507.19457>

<a id="ref-13"></a>[13] arXiv:2508.03680. (2025). *Agent Lightning: Train ANY AI Agents with Reinforcement Learning*. arXiv. <https://arxiv.org/abs/2508.03680>

<a id="ref-14"></a>[14] NeurIPS. (2025). *Self-Adapting Language Models (SEAL)*. proceedings.neurips.cc. <https://proceedings.neurips.cc/paper_files/paper/2025/file/6b41e04c41726e2a60e456d0a2b961ab-Paper-Conference.pdf>

<a id="ref-15"></a>[15] OpenEvolve. *OpenEvolve: An Open-Source Implementation of Evolutionary Coding Agents*. github.com. <https://github.com/algorithmicsuperintelligence/openevolve>

<a id="ref-16"></a>[16] OpenHands. *OpenHands SDK Architecture Overview*. docs.openhands.dev. <https://docs.openhands.dev/sdk/arch/overview>

<a id="ref-17"></a>[17] LangChain. *LangGraph Overview*. docs.langchain.com. <https://docs.langchain.com/oss/python/langgraph/overview>

<a id="ref-18"></a>[18] arXiv:2504.08066. (2025). *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*. arXiv. <https://arxiv.org/abs/2504.08066>

<a id="ref-19"></a>[19] arXiv:2502.14297. (2025). *Evaluating The AI Scientist for Autonomous Research*. arXiv. <https://arxiv.org/html/2502.14297v2> 该评估针对较早版本的 AI Scientist，并非对 v2 的直接评测。

<a id="ref-20"></a>[20] RAND. (2026). *Recursive Self-Improvement and Automated AI Research and Development*. rand.org. <https://www.rand.org/pubs/perspectives/PEA5068-1.html>

<a id="ref-21"></a>[21] Ryan Lopopolo / OpenAI. (2026). *Harness engineering: leveraging Codex in an agent-first world*. openai.com. <https://openai.com/index/harness-engineering/>

<a id="ref-22"></a>[22] LangChain. (2026). *The Art of Loop Engineering*. langchain.com. <https://www.langchain.com/blog/the-art-of-loop-engineering>

<a id="ref-23"></a>[23] arXiv:2504.15228. (2025). *A Self-Improving Coding Agent*. arXiv. <https://arxiv.org/html/2504.15228v2>

<a id="ref-24"></a>[24] arXiv:2603.19461. (2026). *HyperAgents: Co-Evolving Task and Meta Agents*. arXiv. <https://arxiv.org/html/2603.19461v1>

<a id="ref-25"></a>[25] GEAR. (2026). *GEAR: Generalizable Evolving Agent Harness — Project Page and Preprint*. rsi-gear.github.io. <https://rsi-gear.github.io/>
