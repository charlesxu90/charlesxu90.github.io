---
title: "RL 强化学习笔记"
subtitle: ""
date: 2021-06-18
draft: true
author: "Xiaopeng Xu"
description: "强化学习学习笔记：从多臂赌博机到价值方法与策略梯度的核心概念。"
tags: ["Reinforcement Learning"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## RL 基础

### 2 多臂赌博机 \(K\-arm bandit\)

- 只有动作 \(action\) 和对应的收益 \(rewards\)。无状态 \(states\)。

- 动作价值函数

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260612234523209.webp)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260612234605437.webp)

- 增量式实现

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014131652.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014129256.png)

#### 多臂赌博机的$\varepsilon$\- 贪心算法 \(Espilon greedy\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014126591.png)

#### 探索 \(exploration\) vs 开发 \(eploitation\)

- **乐观初始值 Optimistic Initial Values**\-\- 鼓励在开始的时候多做探索

- **基于置信度上界 \(Upper\-Confidence\-Bound, UCB\) 的动作选择** \-\- 鼓励在探索时多选择低频的动作 \(action\)。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014123862.png)

- At is action, Nt\(a\) is number of action a\. t is time\-step\. c controls degree of exploration\.

- **Gradient Bandit Algorithms**\-\- Add action preference

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014121494.png)

- Where H\(a\) is preferences to action a\.

### 3 有限马尔可夫决策过程 \(Finite Markov Decision Processes\)

- 有状态 \(**states\)**、动作 \(\*\*actions\)\*\*和收益 \(**rewards\)**。相比多臂赌博机增加了状态。

- 定义：

    - In a **finite MDP**, the sets of **states**, **actions**, and **rewards** \(S, A, and R\) all have a finite number of elements\. In this case, the random variables **Rt** and **St** have well defined discrete probability distributions dependent only on the **preceding state** **St\-1**and **action At\-1**\.

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014119040.png)

#### “智能体\-环境”交互接口 The Agent–Environment Interface

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014116417.png)

#### 目标 \(Goals\)、收益 \(Rewards\)、回报 \(Returns\) 和分幕 \(Episodes\)

- 目标 Goals 和收益 Rewards

    - That all of what we mean by **goals** and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal \(called **reward**\)\.

- 回报 Returns、收益 Rewards、折扣率 \(discount rate\) 和分幕 \(episodes\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014113738.png)

- R is reward, G is return, r is discount rate\.

- This approach above makes sense in applications in which there is a natural notion of final time step, that is, when **the agent–environment interaction** **breaks naturally into subsequences**, which we call **episodes**

    - such as plays of a game, trips through a maze, or any sort of repeated interaction\. 

#### 策略 \(Policies\) 和价值函数 \(Value Functions\)

- **状态价值函数 \(State\-value function\)**：the value function of a state s under a policy pai：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014110802.png)

- **动作价值函数 \(Action\-value function\)**: the value function of taking action a in state s under a policy pai, \(\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014107826.png)

- **最优状态价值函数** \(Optimal state\-value function\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014104602.png)

- **最优动作价值函数**\(Optimal action\-value function\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014101554.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014058926.png)

#### 贝尔曼方程 \(Bellman function\)

- **状态价值函数**State\-value function

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014056054.png)

- **最优状态价值函数**Optimal state\-value function

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014053500.png)

- **最优动作价值函数**Optimal action\-value function

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014050903.png)

### 4 动态规划 \(Dynamic Programming\)

DP algorithms are obtained by turning **Bellman equations** \(such as optimal state\-value function and optimal action\-value function\) to update rules for improving approximations of the desired value functions in RL\.

#### 4\.1 策略评估 \(Policy Evaluation\) \(或 预测 \(Prediction\)\)

- 迭代策略评估公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014048475.png)

- 迭代策略评估算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014046322.png)

#### 4\.2 策略改进 \(Policy Improvement\)

- 迭代策略改进公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014043457.png)

#### 4\.3 策略迭代 \(Policy Iteration\)

- Sequence of monotonically improving policies and value functions:

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014040581.png)

- where 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014037888.png)

- 
denotes a policy evaluation and 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014035904.png)

- 
denotes a policy improvement

- 策略迭代算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014033511.png)

#### 4\.4 价值迭代 \(Value Iteration\) 80

- 价值迭代公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014031692.png)

- 价值迭代算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014029626.png)

#### 4\.6 广义策略迭代 \(Generalized Policy Iteration, GPI\) 84

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014027769.png)



![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014025671.png)

## 表格型方法 \(Tabular methods\)

### 5 蒙特卡洛方法 \(Monte Carlo Methods\)

- 能够使用历史经验或数据进行新策略的学习

#### 5\.1 蒙特卡洛预测 \(Monte Carlo Prediction\) 90

给定策略 pai，计算状态价值函数，即蒙特卡洛策略评估。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014023573.png)

5\.2 动作价值的蒙特卡洛估计 \(Monte Carlo Estimation of Action Values\) 的问题，某些状态\-动作二元组 \(s, a\) 可能永远也不会访问到\.

#### 5\.3 蒙特卡洛控制 Monte Carlo Control 95

##### 探索初始值蒙特卡洛算法 \( Monte Carlo Exploring Starts\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014021636.png)

#### 5\.4 没有试探性出发假设的蒙特卡洛控制 Monte Carlo Control without Exploring Starts 98

##### 同轨策略 \(on\-policy\) vs 离轨策略 \(off\-policy\)

- How can we avoid the unlikely assumption of exploring starts?

    - The only general way to ensure that all actions are selected infinitely often is for the agent to continue to select them\. There are two approaches to ensuring this, resulting in what we call on\-policy methods and off\-policy methods\.

- 同轨策略 \(On\-policy methods\): attempt to evaluate or improve the policy that is used to make decisions

- 离轨策略 \(off\-policy methods\): evaluate or improve a policy different from that used to generate the data\. 

##### 首次访问 MC 控制算法 （同轨策略）

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014019573.png)

#### 5\.5 基于重要度采样的离轨策略 \(Off\-policy Prediction via Importance Sampling\) 101

- How can they learn about the optimal policy while behaving according to an exploratory policy?

    - A more straightforward approach is to use two policies, one that is learned about and that becomes the optimal policy, and one that is more exploratory and is used to generate behavior\.

    - Target policy: the policy being learned about\.

    - Behavior policy: the policy used to generate behavior\.

- In this case we say that learning is from data “off” the target policy, and the overall process is termed **off\-policy learning**\.

- The relative probability of the trajectory under the target and behavior policiess \(**the importance\-sampling ratio**\) is

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014017599.png)

- 加权重要度采样 \(Weighted importance sampling\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014015565.png)

#### 5\.6 增量式实现 \(Incremental Implementation\) 107

加权重要度采样公式：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014013512.png)

##### MC 预测或策略评估（离轨策略）

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014011485.png)

#### 5\.7 离轨策略蒙特卡洛控制 \(Off\-policy Monte Carlo Control\) 108

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014009458.png)

### 6 时序差分学习 \(Temporal difference learning, TD\)

- 相比蒙特卡洛方法，每步都更新而不是等到分幕结束。计算速度更快，准确性通常也更高。

#### 6\.1 时序差分预测 TD Prediction 117

- A **simple every\-visit Monte Carlo method** suitable for nonstationary environments

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014007570.png)

- The **simplest TD method**

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014005646.png)

- Comparison：

    - **Monte Carlo methods**must **wait until the end of the episode** to determine the increment to V \(St\) \(only then is Gt known\), the **target** is Gt\.

    - **TD methods** need to **wait only until the next time step**\. At time t \+ 1 they immediately form a target and make a useful update using the observed reward Rt\+1 and the estimate V \(St\+1\)\. whereas the **target** is Rt\+1 \+ �V \(St\+1\)\.

##### 表格 TD \(0\) 来估计 Vpai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014002500.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014000444.png)

- MC 采用 6\.3 来故居，TD 用 6\.4 来故居。

- TD error

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013958449.png)

- MC error 可以写为 TD error 的和：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013956319.png)

##### 6\.2 时序差分预测方法的优势 \(Advantages of TD Prediction Methods\) 122

- 相比 DP 方法，TD 不需要一个收益和概率分布的模型。

- 相比 MC 方法，

    - TD 是一种在线 \(on line\) 算法，不需要等到幕 \(episode\) 结束再更新。

    - TD 通常能够更快的收敛。

        - 随机游走 \(Random Walk\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013954222.png)

        - 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013952175.png)

##### 6\.3 TD\(0\) 的最优性 \(Optimality of TD\(0\)\) 124

- 根据图所示的均方根误差度量，batch TD 方法能够比固定步长 MC 表现得更好

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013949904.png)

#### 6\.4 Sarsa：同轨策略下的时序差分控制 \(TD Control\) 127

- 情节 \(episode\) 由状态和状态\-动作对的交替序列组成：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013947864.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013945833.png)

- 对应的动作价值函数公式：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013943718.png)

##### Sarsa 算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013941686.png)

#### 6\.5 Q 学习 \(Q\-learning\)：离轨策略下的时序差分控制 129

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013939529.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013937429.png)

- 悬崖徒步 \(Cliff Walking\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013934900.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013933055.png)

##### 6\.6 期望 Sarsa \(Expected Sarsa\) 131

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013931210.png)

- 悬崖徒步问题中的性能比较

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013929309.png)

#### 6\.7 最大化偏差 \(Bias\) 与双学习 \(Double Learning\) 133

##### 双 Q 学习

- Q 学习有最大化偏差问题，因此引入双 Q 学习

    - 某个状态下的真实动作价值函数 q\(s, a\) 全为 0，但 Q 学习取最大值时对 q\(s, a\) 的估计会是有些大于 0，有些小于 0，从而产生最大化偏差。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013927300.png)

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013925012.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013922697.png)

### 7 n 步自举法

- TD 和 MC 通常不是最好的方法，走向了两个极端。n 步自举法是两种的折中，通常有更好的性能。

#### 7\.1 n 步时序差分 \(TD\) 预测 140

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013920553.png)

- 公式：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013918222.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013916145.png)

##### n 步 TD

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013913696.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013911636.png)

#### 7\.2 n 步 Sarsa 144

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013909584.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013907483.png)

- 其中 t\+n \>= T。

##### n 步 Sarsa

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013905400.png)

#### 7\.3 n 步离轨策略学习 146

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013903100.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013859187.png)

- 重要度采样

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013856671.png)

##### 离轨策略 n 步 Sarsa

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013854560.png)

#### 7\.5 不需要使用重要度采样的离轨策略学习方法 150

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013851905.png)

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013849624.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013847548.png)

- 
\(和 n 步 SARSA 一样\)

##### n步树回溯算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013845486.png)

### 8 基于表格型方法的规划和学习

- 增加了规划和学习，相比之前增加了从模型学习的反馈循环。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013843454.png)

#### 8\.1 模型（Models）和规划 \(Planning\) 157

- 模型：指智能体可以用来预测环境对其动作的反馈的任何事物。

- 分布模型 \(distribution model\)：生成对所有可能结果的描述及其对应的概率分布的模型。

- 样本模型 \(sample model\)：从所有可能行中生成一个确定性的结果，这个结果通过概率分布采样得到。

- 规划：此处代表任何以环境模型 \(model\) 为输入，并生成或改进与其进行交互的策略的计算过程

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013841180.png)

- 状态空间规划算法的通用结构

    - 1）所有的状态空间规划算法都会利用价值函数作为改善策略的关键中间步骤

    - 2）通过仿真经验的回溯操作来计算价值函数。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013838558.png)

##### 单步 Q 规划

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013836204.png)

#### 8\.2 Dyna：集成在一起的规划、动作和学习 159

- 通过模型的学习，增加新的反馈循环过程

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013834164.png)

- 通用 Dyna 架构 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013816154.png)

##### 表格型 Dyna\-Q 算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013813831.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013811546.png)

#### 8\.3 当模型错误的时候 164

- Dyna\-Q\+: 为鼓励测试长期未采取的动作，为期增加额外收益

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013809357.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013807304.png)

#### 8\.4 优先遍历 Prioritized Sweeping 166

- 优先级遍历的思想：

    - 1）通过从目标状态反向搜索，是的遍历的范围更为集中；

    - 2）为解决反响推演时，范围迅速扩大的问题，根据某种迫切性对更新进行优先级排序。

        - 例如：若某个“状态\-动作”而远足在更新之后的价值变化是不可忽略的，则将其放入优先队列维护。这个队列按照价值改变的大小来进行优先级排序。

##### 优先遍历算法

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013805185.png)

8\.5 期望更新与采样更新的对比 170

8\.6 轨迹采样 Trajectory Sampling 173

8\.7 实时动态规划 Real\-time Dynamic Programming 176

8\.8 决策时规划 Planning at Decision Time 179

8\.9 启发式搜索 Heuristic Search 180

8\.10 预演算法 Rollout Algorithms 182

8\.11 蒙特卡洛树搜索 Monte Carlo Tree Search 184

### 第一部分总结

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013802946.png)

## 近似求解方法 \(Approximate solution methods\)

### 9 基于函数近似 \(approximation\) 的同轨策略预测 195

- 增加函数近似。不再用表格来表示价值函数，而是用一个具有参数 \(如 W）的近似价值函数。近似价值函数如线性方法、人工神经网络。

- 因为线性方法不能表示所有的特征关系，因此引入特征构造的方法，如粗编码和瓦片编码。

#### 9\.2 预测目标 196

- 均方价值误差 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013800554.png)

#### 9\.3 随机梯度和半梯度方法 198

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013758137.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013756300.png)

##### 梯度 MC \(Gradient Monte Carlo\) \- 估计 v

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013753966.png)

##### 半梯度 TD\(0\) \- 估计 v

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013751898.png)

#### 9\.4 线性方法 202

- 是神经网络的基础，类似于逻辑回归 \(logistics regression\)

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013749939.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013747456.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013745623.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013743521.png)

##### n 步半梯度 TD \- 估计 v

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013741648.png)

#### 9\.5 线性方法的特征构造 207

##### 9\.5\.3 粗 \(Coarse\) 编码 212

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013739303.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013737123.png)

##### 9\.5\.4 瓦片 \(Tile\) 编码 214

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013734924.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013732820.png)

#### 9\.7 非线性函数逼近：人工神经网络 220

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013730527.png)

#### 9\.8 最小二乘时序差分 \(Least\-Squares\) TD 225

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013728749.png)

##### Least square TD \(LSTD\) \- 估计 v

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013726827.png)

### 10 基于函数逼近的同轨策略控制 239

- 通过近似的动作价值函数

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013724528.png)

- 
来解决控制问题。

#### 10\.1 分幕式半梯度控制 239

- 公式：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013722445.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013720570.png)

##### 分幕式半梯度 SARSA \- 估计 q

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013718534.png)

#### 10\.2 半梯度 n 步 Sarsa 242

- 公式：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013716542.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013714448.png)

##### 分幕式半梯度 n 步 SARSA \- 估计 q

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013712088.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013709757.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013707428.png)

#### 10\.3 平均收益 \(Average Reward\)：持续性任务中的新的问题设定 245

- 平均收益：一个策略 pai 的质量被定义为在遵循该策略时的收益率的平均值。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013705455.png)

- 差分价值方程：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013703162.png)

- 差分 TD error

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013701048.png)

- 差分半梯度 Sarsa 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013657187.png)

##### 差分半梯度 Sarsa \- 估计 q

- 增加平均收益 \(average reward\)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013655212.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013652832.png)

#### 10\.5 差分 \(Differential\) 半梯度 n 步 Sarsa 251

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013650423.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013648135.png)

##### 差分半梯度 n 步 Sarsa \- 估计 q

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013645662.png)

### 第13章 策略梯度方法 317

- 对策略本身进行函数化。

#### 13\.1 策略近似及其优势 318

- 增加策略近似，参数 theta

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013643299.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013640899.png)

#### 13\.2 策略梯度定理 320

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013638545.png)

- 定理：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013636600.png)

#### 13\.3 REINFORCE：蒙特卡洛策略梯度 322

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013634544.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013632493.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013630159.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013628026.png)

##### REINFORCE：蒙特卡洛策略梯度控制 \- pai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013625695.png)

#### 13\.4 带有基线 \(baseline\) 的 REINFORCE 325

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013623330.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013621145.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013619059.png)

- 其中 b\(s\) 是基线

##### 带有基线的 REINFORCE \(分幕问题\) \- 估计 pai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013616710.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013614425.png)

#### 13\.5 “行动器\-评判器”方法 \(Actor–Critic\) 327

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013612025.png)

##### 单步 Actor\-Critic \(分幕问题\) \- 估计 pai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013609709.png)

##### 带有资格迹的 Actor\-Critic \(分幕问题\) \- 估计 pai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013607563.png)

#### 13\.6 持续性问题的策略梯度 329

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013605259.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013603175.png)

##### Actor\-Critic \(连续问题\) \- 估计 pai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013601295.png)

##### 带有资格迹的 Actor\-Critic \(连续问题\) \- 估计 pai

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013558913.png)

#### 13\.7 针对连续动作的策略参数化方法 332

- 正态分布概率密度方程（PDF）

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013556475.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013553606.png)

- 公式

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013551502.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013548895.png)

## 强化学习 \(RL\) 实践

### 直升飞机螺旋控制

- 课本讲的学习模型来训练策略的方法，实际中工程师并不是这样做。原因是这样生成的策略并 不稳定。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013546208.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013543740.png)

- 

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013541103.png)

- 通常会用无悔算法和最优控制（控制相关的算法），可以在测试集上得到比较好的性能。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013538248.png)

- 在此过程中，会做多轮迭代，最终可以得到一个比较稳定的控制策略。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013535630.png)

#### 无悔算法 \(No\-regret algorithm\)

- 会使用无悔算法 \(No\-regret algorithm\)

    - 从先前数据中选取好的特征

    - 生成一个稳定的特征序列

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013533142.png)

#### 最优控制 \(Optimal Control\)

- 在此基础上，会增加一个最优控制 \(Optimal Control\) 生成的机制，来提升训练效果

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613013530526.png)
