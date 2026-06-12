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

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGJjZTNmOWI0NDBmYzIyNGJjMzhkMzQ3NDVhNTkyZDlfYTkzYjEzZjFmMTk0NTBjZWRkZmQ0ZjFjYzQzYzhkZDBfSUQ6NzMzMzMzMzQyOTI4NDUxOTkzN18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDAzYTRlMTkyNTQwOTg3NmNmNWY3YTdiMmUxOWI1YTJfNjg3NDlhOGIzMmNkOWNlOTczZDYzODEzYmE0YjM0NDdfSUQ6NzMzMzMzMzQyNjI3OTY5NDMzN18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 多臂赌博机的$\varepsilon$\- 贪心算法 \(Espilon greedy\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTgyYWIxNTMwMDhkOWQxNWMxYmY4MzY0NzNhMmEzYWNfZTg1MWMwMDFhNDg5MjE1MmVjOTBlNWI1MTJkNDZmMGZfSUQ6NzMzMzMzMzQyODI5OTY2MTMxNF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 探索 \(exploration\) vs 开发 \(eploitation\)

- **乐观初始值 Optimistic Initial Values**\-\- 鼓励在开始的时候多做探索

- **基于置信度上界 \(Upper\-Confidence\-Bound, UCB\) 的动作选择** \-\- 鼓励在探索时多选择低频的动作 \(action\)。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDY0OWMwMDQ5NTViMjU1MzQ2ZTBmY2FmM2ZkZWJjNmNfNjAwM2UwODE4NTI1Y2VmMTYxODMwYzg0MTZiYmRmMjFfSUQ6NzMzMzMzMzQyNzUwMjAyMjY1N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- At is action, Nt\(a\) is number of action a\. t is time\-step\. c controls degree of exploration\.

- **Gradient Bandit Algorithms**\-\- Add action preference

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWU3MTJjNzVlNzQyNDM0MGYxMDRhMDJiNWExOGI5OWZfYWE2ZDA0NWQ1ZmU4MWJiMWJlNzZjNjdhNDk1OWEyMDFfSUQ6NzMzMzMzMzQyMzAwMjI3MTc0Nl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- Where H\(a\) is preferences to action a\.

### 3 有限马尔可夫决策过程 \(Finite Markov Decision Processes\)

- 有状态 \(**states\)**、动作 \(\*\*actions\)\*\*和收益 \(**rewards\)**。相比多臂赌博机增加了状态。

- 定义：

    - In a **finite MDP**, the sets of **states**, **actions**, and **rewards** \(S, A, and R\) all have a finite number of elements\. In this case, the random variables **Rt** and **St** have well defined discrete probability distributions dependent only on the **preceding state** **St\-1**and **action At\-1**\.

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MWQ4Yjk1MDk4MjVkMjVmZTA3NTVjOGQ2YThiMTZhM2RfMjJkMzkyMGNkNGI5ZWFiZjRhMWQ5ZTk2OTM1MWU5M2JfSUQ6NzMzMzMzMzQyMzYyNjQ2OTM3N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### “智能体\-环境”交互接口 The Agent–Environment Interface

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Nzc4YTBjMzAxZjc4MzRkMjJhNzZlMWZjZjYwMWNhMzFfMWVhMjE3ZmFmM2RiMWM4NmZiNDIxZTlkMWUwZWUyMDNfSUQ6NzMzMzMzMzQyNTc2OTcyNTk1NF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 目标 \(Goals\)、收益 \(Rewards\)、回报 \(Returns\) 和分幕 \(Episodes\)

- 目标 Goals 和收益 Rewards

    - That all of what we mean by **goals** and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal \(called **reward**\)\.

- 回报 Returns、收益 Rewards、折扣率 \(discount rate\) 和分幕 \(episodes\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjMxM2ZiMmFiMWJlZjJiZDI1OTlmYzVhMDYyYTg1NDNfZTgyYTZlYmE2NzgzNGY2MDVmYzVhNGMzMWVhNjljZDFfSUQ6NzMzMzMzMzQzMjE2NjA1NTkzOF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- R is reward, G is return, r is discount rate\.

- This approach above makes sense in applications in which there is a natural notion of final time step, that is, when **the agent–environment interaction** **breaks naturally into subsequences**, which we call **episodes**

    - such as plays of a game, trips through a maze, or any sort of repeated interaction\. 

#### 策略 \(Policies\) 和价值函数 \(Value Functions\)

- **状态价值函数 \(State\-value function\)**：the value function of a state s under a policy pai：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjU0OTVlMmIzNWIwNjFjNDAzOTk5ZDQ0Y2QyMjRiMzNfYmZhNDQwMTYzOWQxOWJmZmUwMjI1MGY0NTcwOGY5MjhfSUQ6NzMzMzMzMzQzMzMyMzYxODMwNV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- **动作价值函数 \(Action\-value function\)**: the value function of taking action a in state s under a policy pai, \(\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjY2N2RlNDU2OTE1OTgyN2M1NWYxOWNmOTg4NTQ4N2JfMDE1ZDQ1YzlhMWE2MTk0NjUwMTYwZjg4MDExYmIzNDhfSUQ6NzMzMzMzMzQyMzk5OTc0NjA0OV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- **最优状态价值函数** \(Optimal state\-value function\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzMwZjIyNDE4MDUwMWRjMGMyYzljMzVlYzBiY2M1ZjFfNGU4MzBjN2I2NTc4NDE5ZjYzOGJjOGM3YWVhZTRmYzZfSUQ6NzMzMzMzMzQyNjA1MTUxNDM3MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- **最优动作价值函数**\(Optimal action\-value function\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWY5NTY2YmNjZjk1OTk2ZmE2YmFmZmVjMzg4OWIzYzNfYmE3Mjc4NTY2Y2ExM2EzNmRiMDE0YjkzMmFjMmE3YmRfSUQ6NzMzMzMzMzQzMTU5MTM3MDc4MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTRlNmFiN2E5ZGQwMTBiOGZkYzU2Y2YzN2I5OWQ2MjhfZTM4MTBkYTc3ZWE3MjljMWE4ZjQ0YjE3ZTM2MWQ2YTFfSUQ6NzMzMzMzMzQyMzUyOTkzNDg0OV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 贝尔曼方程 \(Bellman function\)

- **状态价值函数**State\-value function

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODM4NWE1NDMzNzRkMDUxZmNjOGMxMDYzM2Y4NDg4YjZfM2Y5YTJmMTliOGJlMzI3MmZmYWU4MTY4ZDRhZTVjMWNfSUQ6NzMzMzMzMzQyNDczOTUxNjQ0NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- **最优状态价值函数**Optimal state\-value function

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MWVlOWIwYjljNjBjZGMwNzMzOTE2MzkwZDUyYTU3ZmFfNTdhOWE5MTE3ZmNhMmFiYmYzM2UxNmQ3NjYzZTIwOTNfSUQ6NzMzMzMzMzQyNDk4NTM1ODMzOF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- **最优动作价值函数**Optimal action\-value function

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGIyNDMxMWYxNjlmOGI3YjljZGJkYTE0ZWQ4OTVhZDJfZGNkY2ViODc4ZmVjOTU4NDRkZmM1NmU2MzdkMmJjOThfSUQ6NzMzMzMzMzQzMzQyNDI5Nzk4N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

### 4 动态规划 \(Dynamic Programming\)

DP algorithms are obtained by turning **Bellman equations** \(such as optimal state\-value function and optimal action\-value function\) to update rules for improving approximations of the desired value functions in RL\.

#### 4\.1 策略评估 \(Policy Evaluation\) \(或 预测 \(Prediction\)\)

- 迭代策略评估公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGIwZjE0NDcyZjBhZTk0YTQxYTc2NzFlNTk2N2YyZWNfNmVhMTVhMDA4NGFhYjFkMzNjNGFkODZjYzU1ZTNiOTVfSUQ6NzMzMzMzMzQyMjMxMzYwMzEwMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 迭代策略评估算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzQ5NDA3ZmExMmUzOWMwNjhiNWJmZDUyMjI4ZmQ5OTVfZjBiYTk1ZDdiMTcyZWE1YmIyYmQ3NjUyMDU4ODIwMDlfSUQ6NzMzMzMzMzQyODc3MzY2NjgxOF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 4\.2 策略改进 \(Policy Improvement\)

- 迭代策略改进公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OThkMmIwNTkwNTZlNjM1NWRmMTQ5OTk4ZDc0YzY1MTFfNjIyNTZiNmQ3NDhiZDk0NzhhNTFhZTU4YjI2MjE5MTNfSUQ6NzMzMzMzMzQyODkzNjQwOTA5Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 4\.3 策略迭代 \(Policy Iteration\)

- Sequence of monotonically improving policies and value functions:

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTZiMGFjMzQyZmFkNTAwNmJmNjdiZThjMjkzZTIyNGFfOWZlMTRmNWE4NjYwMzNhYjczYWI4YmU5MTYyMWExN2JfSUQ6NzMzMzMzMzQzNDgwODUzMjk5NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- where 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGQwY2MxOTVjOGE5OTlkNTE2YmY5MWY0YTc2MDU4MzdfNzFjYmIwM2IzOGI1Y2Y4MGE3ZGQ5NjAyM2U0NzAzZjRfSUQ6NzMzMzMzMzQyOTQyNzE0MjY1OF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 
denotes a policy evaluation and 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmViYTlhZjkzOGQzNjQzNWNlOWQyN2FjMTQ2MTY1MDJfMjcyNjdjZjRkNzg1Yzc5MjZmNTIxZWI4OWM2ZjAxNzVfSUQ6NzMzMzMzMzQyODc3MzY1MDQzNF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 
denotes a policy improvement

- 策略迭代算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2VlODhiOGM1NzI0ODA2YzdiODI3MDE2Y2JlYTdjM2NfNTY0NDMzMmJkNjZlYmM3YzcxMmQxODJlYzZkN2ZlYzdfSUQ6NzMzMzMzMzQyMDgzNzE5MTY4MV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 4\.4 价值迭代 \(Value Iteration\) 80

- 价值迭代公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTliNGJlYmJjMTE5ZmZkM2I5MTA3MzU2YjQyNDY4MjVfMmJmY2MwYWJhZDY5MTg4MTdmZjY1MzgzMGQ2Mzg3MTBfSUQ6NzMzMzMzMzQyNTQ2NzcwMzI5OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 价值迭代算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGFkYzYwNTNmMDllN2ZhMDQ4NDVjNjk2MDUyMzY5OTJfODRjZGZkNzc2NDkyMzIyN2NlODgzZGQ3OWUzYjAwNWJfSUQ6NzMzMzMzMzQyODkzNzI5Mzg1Ml8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 4\.6 广义策略迭代 \(Generalized Policy Iteration, GPI\) 84

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGI5YzU0NDk0NWU3NjFlZmY4MzlhNDAyMmI2ZGNkNjhfOWRiYjRiM2FiYmNlZWIwZWMwZmRhNjM4OTVjMTcwZDZfSUQ6NzMzMzMzMzQzMDEwNjY4NTQ2OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)



![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjI2MWMyODYxZjI5ZjE2OTY0MjljMmM5NzI0MzU1NzhfOGM5YTVjNmIxMjBmNjg2ZGEwMDhlYWM2MWJmYjkxMTZfSUQ6NzMzMzMzMzQyMjMxMzYxOTQ4NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

## 表格型方法 \(Tabular methods\)

### 5 蒙特卡洛方法 \(Monte Carlo Methods\)

- 能够使用历史经验或数据进行新策略的学习

#### 5\.1 蒙特卡洛预测 \(Monte Carlo Prediction\) 90

给定策略 pai，计算状态价值函数，即蒙特卡洛策略评估。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTMzZDFkOWMxODdhMDg3OTY4N2VjYmM5ZjQxMThmYThfMWUzMWY2YTE2ZmU4NWI0MDdiYzBkNGIyNmM2YTA2M2JfSUQ6NzMzMzMzMzQzMDEwNjY2OTA4NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

5\.2 动作价值的蒙特卡洛估计 \(Monte Carlo Estimation of Action Values\) 的问题，某些状态\-动作二元组 \(s, a\) 可能永远也不会访问到\.

#### 5\.3 蒙特卡洛控制 Monte Carlo Control 95

##### 探索初始值蒙特卡洛算法 \( Monte Carlo Exploring Starts\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTEzY2VkZDMyOWI1NzcxM2YxZmU1NDljOTg5ZDA2M2FfODBlYzE5ZjNmZTI3ZGNkMTJhYWNkMDgwNDhlZWM1ZmFfSUQ6NzMzMzMzMzQyODg0NDExODAxOV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 5\.4 没有试探性出发假设的蒙特卡洛控制 Monte Carlo Control without Exploring Starts 98

##### 同轨策略 \(on\-policy\) vs 离轨策略 \(off\-policy\)

- How can we avoid the unlikely assumption of exploring starts?

    - The only general way to ensure that all actions are selected infinitely often is for the agent to continue to select them\. There are two approaches to ensuring this, resulting in what we call on\-policy methods and off\-policy methods\.

- 同轨策略 \(On\-policy methods\): attempt to evaluate or improve the policy that is used to make decisions

- 离轨策略 \(off\-policy methods\): evaluate or improve a policy different from that used to generate the data\. 

##### 首次访问 MC 控制算法 （同轨策略）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODg1MzIxM2I3YTdkYTJiN2JkMjI5OTljMmJkN2VkNzlfZjI2YWI1ZjM5NzNiOGI0OGExY2JjN2M5YzgzMTViY2ZfSUQ6NzMzMzMzMzQyODkzNzMyNjYyMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 5\.5 基于重要度采样的离轨策略 \(Off\-policy Prediction via Importance Sampling\) 101

- How can they learn about the optimal policy while behaving according to an exploratory policy?

    - A more straightforward approach is to use two policies, one that is learned about and that becomes the optimal policy, and one that is more exploratory and is used to generate behavior\.

    - Target policy: the policy being learned about\.

    - Behavior policy: the policy used to generate behavior\.

- In this case we say that learning is from data “off” the target policy, and the overall process is termed **off\-policy learning**\.

- The relative probability of the trajectory under the target and behavior policiess \(**the importance\-sampling ratio**\) is

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGY0ZDEzYmIwYWJhY2FhY2Y2NGM5NzZiYTQzNDMwMTdfN2IwNWY4NmRhY2Q5NTI0NmI4ZTQ5YjgwZDliODcxMTBfSUQ6NzMzMzMzMzQzMDMwMDM5MzQ3M18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 加权重要度采样 \(Weighted importance sampling\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjRhMWNkYzJhMDhjZTY5YjI4NTFlMDY2NTM5MTlmNDdfOGM3ZTVmZWMwNWZjMzUzZWNiYTJmYjA5MTc4MTJhOGJfSUQ6NzMzMzMzMzQzMDExNTAyNDg5OF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 5\.6 增量式实现 \(Incremental Implementation\) 107

加权重要度采样公式：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjJiZmM1YWZjZjYyMThjNDA1MTg5YmJkODY5MGRlZTRfMWRlZTE0OTEyMjkwOTYxOWU1NmIyMDczMzg4MGNlYTZfSUQ6NzMzMzMzMzQyNDE0NjUxMzkyM18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### MC 预测或策略评估（离轨策略）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjVkNmVhN2NlNjlmMDg1ZWY0OWMxYjM5ZGY5NTIyNzdfMjM3ZGIxNWE4NTkwZjlhZmMzYWM5YmYzZjk5NGQxOTBfSUQ6NzMzMzMzMzQyMzQxNjcwNTAyNV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 5\.7 离轨策略蒙特卡洛控制 \(Off\-policy Monte Carlo Control\) 108

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmMwYzBiNjJlMjU2MzA0NTViMWVhMThhMDBhMzgwZDlfZjc0M2I5ZjViYWE0NDJiMjk1MjY3M2Q0ODkzMzQ3MjVfSUQ6NzMzMzMzMzQyMjE3MTAxMzE0OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

### 6 时序差分学习 \(Temporal difference learning, TD\)

- 相比蒙特卡洛方法，每步都更新而不是等到分幕结束。计算速度更快，准确性通常也更高。

#### 6\.1 时序差分预测 TD Prediction 117

- A **simple every\-visit Monte Carlo method** suitable for nonstationary environments

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzkwNGM4YjI4Y2QzNDY2ODU5OGQyY2MyMDg5ZWY4ZjNfNTljZGNkODdmNmY1ODBjN2NmY2QyYmYzZTFhNzJhOGRfSUQ6NzMzMzMzMzQzMTc4NDMwODczOF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- The **simplest TD method**

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjcxYjhkMDc1NTA2YWU1Njg0MzFmM2QyZGRmY2Y4NTlfYzEyYzE4YmMyMzcyZTViMzU2OWYwOTQyZWUxYjc4Y2RfSUQ6NzMzMzMzMzQzMDI4Mjc4MDY3NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- Comparison：

    - **Monte Carlo methods**must **wait until the end of the episode** to determine the increment to V \(St\) \(only then is Gt known\), the **target** is Gt\.

    - **TD methods** need to **wait only until the next time step**\. At time t \+ 1 they immediately form a target and make a useful update using the observed reward Rt\+1 and the estimate V \(St\+1\)\. whereas the **target** is Rt\+1 \+ �V \(St\+1\)\.

##### 表格 TD \(0\) 来估计 Vpai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjNjZjA2N2Q2NzA5YzQ4ZDM0MDc0MTVhNDE4YTMyMmNfNzZjNjk4N2ViZmQ0NWNkNzdkOTA2Njc3MGM5YzY2MDFfSUQ6NzMzMzMzMzQzNDkxODI4OTQxMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzY5ZmZmN2I1ZmJlN2RmOWRlNjJiZDE4NzRlNDdiNjFfYjlmMmI1N2UwNDEzYjA3MTczZjE5ZjhlMDUyMmU1MTRfSUQ6NzMzMzMzMzQyMzAwMjI4ODEzMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- MC 采用 6\.3 来故居，TD 用 6\.4 来故居。

- TD error

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjliYTA1N2NjMjEzYTcxYmU1ZjYwMzcxMmU0M2NjNzBfMTM2NGQxNWQ1ZDMyY2Y5MGU0MGNiYmVkOTRmMDgxOWRfSUQ6NzMzMzMzMzQyNzgyOTEyOTIxN18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- MC error 可以写为 TD error 的和：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDIxNjBiYTc2MGYxOTIwNzlhYjc0MGRmN2ZhY2ViNTJfNzEzNmM4MDM2OGM5YTEyZGE3Mzc4NjVlNDQzNDgzZjJfSUQ6NzMzMzMzMzQzMjIyMDYzMTA2OF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 6\.2 时序差分预测方法的优势 \(Advantages of TD Prediction Methods\) 122

- 相比 DP 方法，TD 不需要一个收益和概率分布的模型。

- 相比 MC 方法，

    - TD 是一种在线 \(on line\) 算法，不需要等到幕 \(episode\) 结束再更新。

    - TD 通常能够更快的收敛。

        - 随机游走 \(Random Walk\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmNmZTUzOTUyMjUxZTc3N2NlNDg4OTMwNTk4NzE3ZTBfNjEzMzNhNDQ3M2E0MTVlY2FlOGRjYzA0ZTQ5MzYzY2JfSUQ6NzMzMzMzMzQzMDc2NTkyODQ1MF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

        - 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGZkYjM2NTZiOTY3NTQ1ZmUwMjc0YWM3MTA3NTgzYjdfMTQyYmM2ZmI2ZmQ0YTM1YzllODhlMWJjM2I3ZmI4NjFfSUQ6NzMzMzMzMzQzMTkyNjkzMTQ1N18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 6\.3 TD\(0\) 的最优性 \(Optimality of TD\(0\)\) 124

- 根据图所示的均方根误差度量，batch TD 方法能够比固定步长 MC 表现得更好

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjE0YTgyMzdmZWRlNjRjMmNiN2E3NmQ2YmUxZWU1ZTBfNTQwN2Q4YWExYTAyMzBjNzY1MTgxOWViMGU2ZTQ4ODZfSUQ6NzMzMzMzMzQyOTI1NjA0NDU0N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 6\.4 Sarsa：同轨策略下的时序差分控制 \(TD Control\) 127

- 情节 \(episode\) 由状态和状态\-动作对的交替序列组成：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjU0N2NhOTlhMWJhM2ZmNWUyMTNmZjhmMGMzZjJjYzJfYmQwZTRhZmNlMGZkZDk3NDJmYzIzMGFkOWVkNTI2YjdfSUQ6NzMzMzMzMzQyNzUzMjEwMzcwOF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2U0MzJiOTQ3NjgxYzBkMDU4YTZjNTI1YmUyOTEyNmVfZDE4OTM0MGJhNjg2ZmFkZTU1MWNiZjMwOGFmYzdlMWFfSUQ6NzMzMzMzMzQyMzU3Njg3NTAwOV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 对应的动作价值函数公式：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDk5YjUwMjk5ZTJmMTc5NWU3ODE1OGZmYzA5ODM5NWVfY2MxODNkZTk2ZmIxNjE2Nzg3MzEwYWMxODRjMWMzYmJfSUQ6NzMzMzMzMzQyODkzNzMxMDIzNl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### Sarsa 算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2M1NmFkMjAyNjg1ZDhhMGY2MDZmZmM2OTg3ODE3ZTlfODdmNTY2NjcxN2M1NzA3Mzg0NDg2YTY2MDRlZGY1MTJfSUQ6NzMzMzMzMzQzMjExOTg4NTg1Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 6\.5 Q 学习 \(Q\-learning\)：离轨策略下的时序差分控制 129

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmRjMWUyOWM0YjliMmFmNTc5ZjE4Y2ZjZjQ5YzQ2ZTlfNWJjMjdjZTkwNzc0YTdlMjg0N2VlMzg4YzE2OTIxZTJfSUQ6NzMzMzMzMzQzNDQwOTk3NTgxMF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MWY0MGI2NjQ2Y2Y1YTEwZTRmMmNmNmYwYmNmOGRlYWZfMWYwZTRiZWE4MWEwYmYyMzE0YmE4YzAwZTBlYjFlMTlfSUQ6NzMzMzMzMzQyMDgzNzE3NTI5N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 悬崖徒步 \(Cliff Walking\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGE0MDljNGE5NjgzZTZkMzUzYTgzMGM4NWFmNzc3ODRfNGQ3MTVmZWIxMzkwOWM4NDZiNGI5ZTkwYTRkM2FkODRfSUQ6NzMzMzMzMzQyNjIxODUxNjQ4MV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGVkZDgwMGYxMGYwNzQzOTE2ZTVhZWNkNTk5MjA3YzhfMGI5NTBhYmNhMjRhNzJmZGZhZGM2YzFlZThkNWM3ZDhfSUQ6NzMzMzMzMzQyMDcyNDE0MjA4MV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 6\.6 期望 Sarsa \(Expected Sarsa\) 131

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2FmYmY3ODI0MTliNDg1ZjYxZGNhZWM1YzA4MTBkNjBfMDkyZjFkZTNhMDM0NjdkNTU5NDBjMjc5YjMxMjVjZDRfSUQ6NzMzMzMzMzQzNDk3MTk3OTc3OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 悬崖徒步问题中的性能比较

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjZlYThmN2VlYTJjY2QxMmRiYTQ3ZjgwMzRlMjY5OTZfNDljNzY4NzZmNGQ3MGYzY2YyNjEwOGM3OTM0MzIxYjVfSUQ6NzMzMzMzMzQyMzUyOTkxODQ2NV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 6\.7 最大化偏差 \(Bias\) 与双学习 \(Double Learning\) 133

##### 双 Q 学习

- Q 学习有最大化偏差问题，因此引入双 Q 学习

    - 某个状态下的真实动作价值函数 q\(s, a\) 全为 0，但 Q 学习取最大值时对 q\(s, a\) 的估计会是有些大于 0，有些小于 0，从而产生最大化偏差。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2MzNzFkYjlmYThjYjcwOGI5ZTAxMTU4NDc0NThjZTVfMjY0ODBlYjhkY2FjYzZhOGUxY2YwYjE5NzE4ODA1YzdfSUQ6NzMzMzMzMzQyNTU2ODM1MDIxMl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2M1NTNiNjhkY2I5MzA5NTc4ZGU5NjhhZTNkMTQ3MmVfMTVkYzFjYWU0ZmNkYzkzYmM3NTFiODQwMDQwNjlkYzlfSUQ6NzMzMzMzMzQzMDM0Mzk1ODUzMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MWYwYTA2NjE5OWUwNWE3OGFiOGZmZGMwOTFhODg1YjVfOGRkODUwNzk2NjlhZmJhOTgwMzc5YWRjMDgxNDkwNzVfSUQ6NzMzMzMzMzQzMDExNTAwODUxNF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

### 7 n 步自举法

- TD 和 MC 通常不是最好的方法，走向了两个极端。n 步自举法是两种的折中，通常有更好的性能。

#### 7\.1 n 步时序差分 \(TD\) 预测 140

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODJjZDM4YWQwZjEyNWNlZWQ0MzVlOTZhMzMyM2FiMmVfMDJiNjU1Njc3MzBlN2Q0OWJhZjRmYTc2YmM3MDEyZGVfSUQ6NzMzMzMzMzQyODY4ODk0NTE1NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 公式：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTAwNzg3MGM4OGVjZTQzMTU4M2VmNDRiMWYwZTY0MzBfMGNkNjc0ZmY3MDI1YWEyNzdlY2VlYWY2MDhkNzUxZTJfSUQ6NzMzMzMzMzQyNzUzMjEyMDA5Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Nzc5ODNiMWU3NjBiMDEwNWJlYjBlZmU2MDQzZGNkZGZfYmMzMDQ1NGQ5ZTRiYjZkN2NkZDVlMTY5MmE1N2NhMGZfSUQ6NzMzMzMzMzQzMTgyNjI1MTgwNF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### n 步 TD

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDJmZjVjNDVlYTlmNWNjYTUxMjkyZWNkMTlmNTM4MjFfMGY0MjAxNTdkNDEwOTVmNjY2OTA4ZWY2YmNiZmFjY2ZfSUQ6NzMzMzMzMzQzNDYzNjQ2ODI1Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzY2YzBlMjVkZmI3YWFhNmVmM2U4NjIzNjA1ODUyNDZfN2IyZGQ2ZTdkOGVlMmNlNDU1ZWVkMmZiZTA3ZDAxZjFfSUQ6NzMzMzMzMzQzMjU3NzAzMjE5NF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 7\.2 n 步 Sarsa 144

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDE4M2I4MzhhZjczYTE5ZjFkMGU3ODJlMWI1ZmUzNDNfM2EzYmJmMzY1ZDU3ZmU3ZmQwODFhZDg0OTAxNWY5MThfSUQ6NzMzMzMzMzQzMTgyNjI2ODE4OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWQ1YzA5ODhjNTA1NDYzZDNkZWM4NTRhODgzZjIyNWJfNGNjOGQ3OTA2ZGZlOWQ1NzEzNjdkYmU1NzQ4M2E0NzFfSUQ6NzMzMzMzMzQyMzYyNjUwMjE0NV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 其中 t\+n \>= T。

##### n 步 Sarsa

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDA2NjRhM2U1NDE3OTlkYTlhYzdiNzQ2MWNlMzhjOGVfZGQ5N2QwYWQzMDI1N2Q1ODA4NTk4ZGI4ODQxOTZlYjlfSUQ6NzMzMzMzMzQzMDU3MjIwNDAzM18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 7\.3 n 步离轨策略学习 146

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWMyNDUxZDVkOWU0MzRhOGYxOGY1YmJkOWUyZDQyMjhfYzM3NjA2M2VjYTcyNjZkNTJmNDEwNjcwYjdlZjZlNWVfSUQ6NzMzMzMzMzQyNTgxNjAyNzEzN18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWFiNTBmMjllMmZiOTVkNGJkMDZmZjc5NDkzMGJiNTlfMDNiYjc3ZjQxYTUyOGZhM2Y3NzY5MDgzN2U4ZTA3NjNfSUQ6NzMzMzMzMzQzMDkyODcwMzUxNl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 重要度采样

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDY0NGMzODNhNzdlNWI3Y2VhNDUwODZiMjQ4NmU5MDRfNDU2YWEzNTcwMTUwYTU5MmYxNjQ5MWYwMDg2M2U2Y2FfSUQ6NzMzMzMzMzQzMTc5MjczMDE0MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 离轨策略 n 步 Sarsa

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTVkMzRhYmZlYzQxYTVjMzk0M2I4NjNmY2ZiZWMyZjRfYWIyNDJlNGRkOWVhZDdjYTJjZDIzMWUzNjE5MzEzZjZfSUQ6NzMzMzMzMzQyMDcyNDEyNTY5N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 7\.5 不需要使用重要度采样的离轨策略学习方法 150

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjViOWU2MTNmZGRjMmE0YWM3Y2JhZjJjZTQ3N2YxYTFfNTBjNGI0ZjY1NDE3OWVjYjUxNmZiNjc0OTg5YzMwZmZfSUQ6NzMzMzMzMzQyNjU1ODIyMjM2NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2VjZGFhMTFkZDNkMDgyNTIwNzIxN2M1OWM5ZjUzNzBfYjc5ZDc1NmY5M2Y4NGFlMTViYTVhMTg4NzM2ZjJhMGJfSUQ6NzMzMzMzMzQyOTMxNDY5OTI2Nl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDM5ZTBkMzkzZjViOGI3ZTU5NGIzOTFmMmZjMGNjM2ZfMzBjZjk1MmQ1YTcyODQxNzk0MGU3YjEzNDgwN2JkMDNfSUQ6NzMzMzMzMzQyNjA1MTUzMDc1NF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 
\(和 n 步 SARSA 一样\)

##### n步树回溯算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTc4MTIxYjEzZjc3NGEyYzBkMTUzYTlhNzE4OTZkMTdfODg3Y2M4ZWM3OTkwY2YxNDYxODNjYzg4ODUzZjYzY2ZfSUQ6NzMzMzMzMzQyMzQxNjc3MDU2MV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

### 8 基于表格型方法的规划和学习

- 增加了规划和学习，相比之前增加了从模型学习的反馈循环。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTQxYTMzN2I5MzE2MjUyOWM3NzlhY2Y4NjdiZWVhMTRfZGU4MDgzMTRhMmExNzllMjEzZGVmMTIxN2FhOTE4N2ZfSUQ6NzMzMzMzMzQyMzMzMjgzNTMzMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 8\.1 模型（Models）和规划 \(Planning\) 157

- 模型：指智能体可以用来预测环境对其动作的反馈的任何事物。

- 分布模型 \(distribution model\)：生成对所有可能结果的描述及其对应的概率分布的模型。

- 样本模型 \(sample model\)：从所有可能行中生成一个确定性的结果，这个结果通过概率分布采样得到。

- 规划：此处代表任何以环境模型 \(model\) 为输入，并生成或改进与其进行交互的策略的计算过程

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWFlNmFkYWE2ZGMxOTQ2Mjk5YTUxMDAzODU3Y2NmNDZfYjIyMjBmNjc3YzY3M2EzNTU3YWM2NmYyZDg3MDAyYTFfSUQ6NzMzMzMzMzQyMTc1MjM2OTE4MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 状态空间规划算法的通用结构

    - 1）所有的状态空间规划算法都会利用价值函数作为改善策略的关键中间步骤

    - 2）通过仿真经验的回溯操作来计算价值函数。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmIyZjMzOTRkZjQ0YTk2ZmE5NjdhNWJhMTJlYjkwNDZfMmQwYmM4MzIyZmNjMjljYTQ4OWY5MmRkMjUwOWQ4NGNfSUQ6NzMzMzMzMzQyMzQxNjczNzc5M18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 单步 Q 规划

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTA4MmMzYTVjZjhlZDAyNGY4MTVlNmM0NWJmZmUwZDBfMjA4MzFkOGJhZjZkMzAxODg4YmM4YTFhZGNkOTMxN2NfSUQ6NzMzMzMzMzQyMzU5Mjg0OTQxMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 8\.2 Dyna：集成在一起的规划、动作和学习 159

- 通过模型的学习，增加新的反馈循环过程

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTU2NzM3OTM0M2RhYTU5MGM3ZWY1NjdlMTBiMDA5NzhfNWFmYTJiYTEzZDg5ZWFiODFiOTc4NmZhMzE5NjA2MDZfSUQ6NzMzMzMzMzQyMDM0NjU0MDAzNF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 通用 Dyna 架构 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmY0NjA2MGRiZjJkYjZlNjE3YTNlYjQ5N2E5ZTI4YTdfNDEyNThlMGIyYWNiNjNiZGE5MmYyNWZiMTQ2ZDg0NmJfSUQ6NzMzMzMzMzQyMDQ0NDU0OTE0OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 表格型 Dyna\-Q 算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWE0ZmQ5YzBhZWM4OWU0NDVkZDk5ZmU2NDI4YmM1NWFfYjVkYzhiNzA3NjAyZDUyYTBhM2ZiN2ZhNGIxNTlmY2JfSUQ6NzMzMzMzMzQyNDY0MTQwOTAyNV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjQ4MmRiNmUxYjM0OWVlZTExZDgzNTExNWFmYmFlNDdfZDQ4ZDkwOTRmMzAyMWM0MDRhNTdiMzNmY2EwMjEwODJfSUQ6NzMzMzMzMzQyMTU1ODU5NTU4Nl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 8\.3 当模型错误的时候 164

- Dyna\-Q\+: 为鼓励测试长期未采取的动作，为期增加额外收益

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjFlMjU1MjU4ZTNlYzFiMDMyMDU1YWQ1MDNkYjljZGRfNTYwMTNlZDUyODFmZTliZTBjMjBiZTQzZDE4YTU1MGZfSUQ6NzMzMzMzMzQzMDUxNzY0NTMxM18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWFjNzQwM2RmZTNiYTk5Njc3YWY0Y2QwNzc1MmNlZWVfYTliMmJkMDI5NTllNDYwOThkODZmYmI2Y2ZjNmIzNGJfSUQ6NzMzMzMzMzQzMjE2NjA4ODcwNl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 8\.4 优先遍历 Prioritized Sweeping 166

- 优先级遍历的思想：

    - 1）通过从目标状态反向搜索，是的遍历的范围更为集中；

    - 2）为解决反响推演时，范围迅速扩大的问题，根据某种迫切性对更新进行优先级排序。

        - 例如：若某个“状态\-动作”而远足在更新之后的价值变化是不可忽略的，则将其放入优先队列维护。这个队列按照价值改变的大小来进行优先级排序。

##### 优先遍历算法

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTJlMjY2NGQ4OTE5NWI5YmQwMjFhMzNjYTI1ZjM0ZThfYWUyMDVjMjE3MDI3NWFjNjMzZmJhNDBhNTUxMTVjNzBfSUQ6NzMzMzMzMzQyNzgyOTExMjgzM18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

8\.5 期望更新与采样更新的对比 170

8\.6 轨迹采样 Trajectory Sampling 173

8\.7 实时动态规划 Real\-time Dynamic Programming 176

8\.8 决策时规划 Planning at Decision Time 179

8\.9 启发式搜索 Heuristic Search 180

8\.10 预演算法 Rollout Algorithms 182

8\.11 蒙特卡洛树搜索 Monte Carlo Tree Search 184

### 第一部分总结

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDRlM2RmZDljMjlmMjM3NzM1MzM1OGZmZjVkNDlhYmVfYTI2YWZjMjQ2YmMwZTkyYTBmMGUwODJmZjVhMjIzMzNfSUQ6NzMzMzMzMzQyNDU2MjU1MjgzNl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

## 近似求解方法 \(Approximate solution methods\)

### 9 基于函数近似 \(approximation\) 的同轨策略预测 195

- 增加函数近似。不再用表格来表示价值函数，而是用一个具有参数 \(如 W）的近似价值函数。近似价值函数如线性方法、人工神经网络。

- 因为线性方法不能表示所有的特征关系，因此引入特征构造的方法，如粗编码和瓦片编码。

#### 9\.2 预测目标 196

- 均方价值误差 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTdiNTM0ZjliNTZhOGYyNjEzYzY3ZjdjY2IxZWViMmZfNjYxYTdhMzlmMmRmZmYzNWI0YzMwYzcxNzdjOWFiODlfSUQ6NzMzMzMzMzQyODk1NzM4MDYzNl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 9\.3 随机梯度和半梯度方法 198

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWVjZjdmN2QxYTliNDMxYzg4OWNmZmViMTMyNTllMzhfYmU3NzkwM2Y0YWMxN2FkY2UyODY4YTNlZTIxNDJkZTBfSUQ6NzMzMzMzMzQzMTc4MDExNDQ2MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmJlZjhkYjkzNzJjMjgzZjE4YTE3MjAyNTA0OGY2YjZfYTJlMzVhYmQ0Y2RmOTljZmQzNWFmY2Y4M2YwOTlhZTNfSUQ6NzMzMzMzMzQzNDYzNjQzNTQ4NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 梯度 MC \(Gradient Monte Carlo\) \- 估计 v

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWVjODQ1Mjg2MTc4OGJlNzY1MmEyMmNmNDVlNGIzNmJfNmE1N2FkN2NlZWU2YTQ3N2I4OGE0OWMzYzVkNWJmNTZfSUQ6NzMzMzMzMzQzMDg1MzIwNjAxN18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 半梯度 TD\(0\) \- 估计 v

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjA1MzI2NWEzOGYwNjRlYjU2YzMwZjNjOTlkZDdlOGNfMTQzMGRmYzZiY2E2MmU1ODlhOGZhMjY2OTM1ZDkzNjFfSUQ6NzMzMzMzMzQyMzk4MjkxOTY4Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 9\.4 线性方法 202

- 是神经网络的基础，类似于逻辑回归 \(logistics regression\)

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDUyMDFkMzU2MjhkODZlOTE5YTk2YzBkYTJjN2Q1ZjdfYTE0YjE0ZDZiMGM5ZDgwZDkxMmVlMGE4YzcyNGNmZTdfSUQ6NzMzMzMzMzQzMDY3NzA2MTYzM18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjUyNGViZDlkZTY5Yjk5ZTkxMzVlODkwMjM0MDNhYWRfMjJkZGM0NDE1MWI0MzVlMTIzYjdmNjlkZDE3OGQxMmJfSUQ6NzMzMzMzMzQzMDM0Mzk0MjE0Nl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTExOTViODUwZDVjOTFiN2FiNmEzMDIxZjk5ZmExM2JfYmVkZTMzM2EzNzM2YTUxNTZiMDI1ZGJhYTBiYTZlMmZfSUQ6NzMzMzMzMzQyODc4NTM5Nzc2NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTcwMTFkZWJhOGNhODQxZDcwOTAxMjk1OTU0NmMwMTNfYWRiOTIwNTQzNzhhNGMyMTlmNjZjMjc1NDE3NWIzYzlfSUQ6NzMzMzMzMzQyODI3NzkwMzM4OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### n 步半梯度 TD \- 估计 v

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjRkOWZkZGRjYWQ3ZTliY2QyNzAwNWZlMGZhNGJiZmFfZDk4NjU0NWEyODY3MjgyYzcwNGVlZGU4MDllMWIwMmFfSUQ6NzMzMzMzMzQyOTMxNDcxNTY1MF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 9\.5 线性方法的特征构造 207

##### 9\.5\.3 粗 \(Coarse\) 编码 212

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTE3YTdlYzcyNzNjMWI0ZjM4MTJiZDI1YmY4NGJiZThfMTdiYzFkOGUxOGE4YjdiZGMzMTViYWE1ZWNiMWFlYWZfSUQ6NzMzMzMzMzQyODk1NzM2NDI1Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjI4ZTIwY2UwOWU1YzkwNGIyOWNhYjA4MjY1MjZjYzVfYzMxYzliNmJlODE5ZDFmYTA4NzMwM2Y5M2JmYzI1NjdfSUQ6NzMzMzMzMzQyOTMxNDY4Mjg4Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 9\.5\.4 瓦片 \(Tile\) 编码 214

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWZjNWZkNDVhYWM0ZTY2MmE0YjAzZjlhNTZkNjEwZmNfYjJhODFmZGRjOGM1YjhjODhlNzU1NGVjNjA1YmViZTRfSUQ6NzMzMzMzMzQzNDYzNjQ1MTg2OF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTIwOGRmZDUyNWFjODM1MTMyMzI0NDBlNjhjNmYxYjlfMmEzZWZhODFlNmE5ZTIxMWIyZmNjMmY2ZjNlMmZmNTBfSUQ6NzMzMzMzMzQyNTg1ODU5Mjc5Nl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 9\.7 非线性函数逼近：人工神经网络 220

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmNkOGY2ZDVhNWIxY2M2ZmQzZTRhZDRiNDM1ODFmZDNfMDFlMGY4OTM1ODkzOTIwYTk2YTMwMTI1Y2YyNTk3OTVfSUQ6NzMzMzMzMzQyMzk4MjkzNjA2Nl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 9\.8 最小二乘时序差分 \(Least\-Squares\) TD 225

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmJmNTA4ZDNhNjFlZjU1NTdhYzI2MTU0OTViNjVjNzdfYTIzNzg3YzNhM2VjOGU4ODdkOTZhYTkxYTQ0YmYwOGJfSUQ6NzMzMzMzMzQyNDM5Mzk5NDI0MV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### Least square TD \(LSTD\) \- 估计 v

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTU0YTFmNDVhZWQ4ZjJkNWViZGZmNjU2ZGMxMzZhNTJfNzYzNjRlYzZkZTJjMmVjNTY2NGJjZjRmMTE4YjAzZWJfSUQ6NzMzMzMzMzQyNTc2NTQ5ODkwOF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

### 10 基于函数逼近的同轨策略控制 239

- 通过近似的动作价值函数

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzMyOWNkZDE2MTcxOGEzY2EyOTlmNGEyZjhiYzk2YTlfYTQ2MzNlNjY1ZGYyYTA5M2M3ZWY3NGQ0ZGVlNDc5MjZfSUQ6NzMzMzMzMzQyNjU1ODIzODc0OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 
来解决控制问题。

#### 10\.1 分幕式半梯度控制 239

- 公式：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGRhNDYxMmU1NTQ0NTU2YTJhOGZhYThjNzRmZjU3ZTdfMGYwNDRiYWQ0OGZkYTI5YWM0ZGYxZTU3Njk0NjAwZmFfSUQ6NzMzMzMzMzQzMjYyNzM4MDIyNV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzgxOTNhMTA0ZTEwOWJiYzhhMThhYjYxMGFmZTE4NWNfMmRhMzgzYjhhMmNlNzQ0ZmRlZGZkYjg2YWVlMTVhNzRfSUQ6NzMzMzMzMzQyNzkyNTU5ODIzNl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 分幕式半梯度 SARSA \- 估计 q

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzRlNWYwZjI1ZWNlNTc2NGRlMTFjMzMyNTc5YjY0ZmRfYTM2YjljYzZjYTJiMGUyMTRkYmViYjZkNzcyODZhNzZfSUQ6NzMzMzMzMzQyMTUyMDg3OTY0NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 10\.2 半梯度 n 步 Sarsa 242

- 公式：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjU4ZWRlOTY0MzM4M2VkYjNjOGNiNDYxMWM5MmFjNjlfMzRjNzhkNTAxMDBjYmM0OTI0NGU3YzgxMzBhNGQ1NDFfSUQ6NzMzMzMzMzQzMjExOTkwMjIzNl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDRmNWE3ZDdiYjI3NzU5ZWIwOGUzZWJhNTQ5ODViYTJfOTY1OGYyOTUwYmE2NmY5YjY5ZDViMTk2MmQxM2ZkMmFfSUQ6NzMzMzMzMzQzMjA0NDQyMTE0OF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 分幕式半梯度 n 步 SARSA \- 估计 q

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGM4N2YzYTFhZjcxZTFlYTVjNmNlOTNhNmNiN2FiNGFfNDM0NzZkY2EzYmIzMWZkOGY2NzJiZjVhNGQyYzBiMTdfSUQ6NzMzMzMzMzQyODkzNzI3NzQ2OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDAwNTlmOTBmNjhiZGYwZWUxZmFkNDNlM2JjYjE5ODBfZjk5YWU4YjU0YTQwOTg0MDRkMTMxNjQ1ZTQ2ZDliMzNfSUQ6NzMzMzMzMzQyNzc1MzU4MjU5M18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODRiZWY4YTkxY2M4ZDU3MzRjZWQ4NDgzZjkxYmIwNDhfY2IzYWFkZTFkMWU0MGE0ODhiZDAxMGQ2ZmM3YWQzMDVfSUQ6NzMzMzMzMzQyNTg1ODU3NjQxMl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 10\.3 平均收益 \(Average Reward\)：持续性任务中的新的问题设定 245

- 平均收益：一个策略 pai 的质量被定义为在遵循该策略时的收益率的平均值。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2IyZGUxOTEwMTEwZjA1ZGQxODAzMDUzN2Q4YjRiZDZfOTYwOWQ1ZDMzNjYyODBiZWM3NzQ3MGE2YzQ3NjUxMTRfSUQ6NzMzMzMzMzQzMDI4Mjc0NzkwNl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 差分价值方程：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWY1NDA5NDg2MWI5ZTZlMmYzZmQ4MGE2ODE4Nzg5NDhfMDE4NTZhYjdhNDBmN2Y2MjkyNDZmZjYzNTI1MjQyNzlfSUQ6NzMzMzMzMzQzNTE0ODE1NjkyOV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 差分 TD error

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzhkN2Y3YmIxNjY4ZTBiYzViNmMzMGJkM2Y3YTY1ZmZfNzg4NDIwZmE2MGY2ZTEwYTE0MDE0NDk3NGFiOWFkMjBfSUQ6NzMzMzMzMzQzMDg1MzE4OTYzM18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 差分半梯度 Sarsa 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmEzMTVlNjU2ZTEwMzZlNjJiODM3M2NmMjUzNzhlNGFfZTQ4M2MyYzJmMGFkODc0ZTdhZjY2N2JlNmFmMThhYTdfSUQ6NzMzMzMzMzQyOTAzMjg0NTMxNF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 差分半梯度 Sarsa \- 估计 q

- 增加平均收益 \(average reward\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTAzN2U0ZTgwMWNhNTIxMTliZjQ4YTg3YTg1YzVmNTJfNzA4NzEyMmNkZmVlZDQ0ZTkxM2M3ZDU4NTMwZTY4ZDZfSUQ6NzMzMzMzMzQyNzcxMTY1NTkzOF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDQ1NjFkMjk4MmRhMTc4MDNiNTNjMTFhMDdiMjA2OTlfZTMzNmMwYWQzOWQ1MWU4MGEzYjBiZTE3YjdhMDFlYTZfSUQ6NzMzMzMzMzQyNTgyMDEwNjc4MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 10\.5 差分 \(Differential\) 半梯度 n 步 Sarsa 251

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDQ3ZDk4YTE4OTE5YzU4YjU3NDhkNGFkMDEzZWYxMDBfNzUxZjBiMDdlNDJhMTU5NWYwNTg0NjY1YWY0ZTEzYzZfSUQ6NzMzMzMzMzQyNTc2OTcwOTU3MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzFkMmZmODI5MTBhYzI4NmM1OGIwZjI0MzkwMjQyMTRfNWIzOTRiMzBmMTQwZjA0YmMyY2I0NGMzMDhiNTE2NzhfSUQ6NzMzMzMzMzQzMDkyODY4NzEzMl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### 差分半梯度 n 步 Sarsa \- 估计 q

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTRlNzUyNGI3ZDIxZmMxNjE3OTNlOTA5MmQ4NTZhZTNfNDA0YjJjNzMzZTk4ZmEwNzdjZmI0YmQ2YjMxN2E5YWRfSUQ6NzMzMzMzMzQzMjA0NDQwNDc2NF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

### 第13章 策略梯度方法 317

- 对策略本身进行函数化。

#### 13\.1 策略近似及其优势 318

- 增加策略近似，参数 theta

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGZiZGEzYzE5NjA2NzYyOWE4YjFlNGU4MmU0Y2Q1ODVfMGI4ZjIzMWU3ZGFlOGJhOGFmNDQ3YTg5ODYwZjJjNDVfSUQ6NzMzMzMzMzQyNTEzMjk2MTgyMF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjVmMWRhMWMwMGY1M2YwYWUzODNiZDk2YmJlNDM1NTJfOWJiMjQzYjVjMmJiZjRmNmVjYjM3Mjk5MzZiNDI1MjRfSUQ6NzMzMzMzMzQyNzI5MjI0MTkyMl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 13\.2 策略梯度定理 320

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDIwN2IxZDg0N2JjYWZhYzZjY2EwMzU0NDVlZjA1ZWVfYjViNWViOTM2ZDAyZTQ3MzQ5NGQxMTc4Yjk3N2U2OGZfSUQ6NzMzMzMzMzQyMzYyNjQ4NTc2MV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 定理：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2QwZjcwODJmNTIyZmM5NDkxYWNhYmI5ZmNkMGE1MDdfMGUzMzg5MGM3ZWE0MmIxYzg4ZDlhM2E3YzQ4MjdhMTdfSUQ6NzMzMzMzMzQyOTc2MjY4Njk3N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 13\.3 REINFORCE：蒙特卡洛策略梯度 322

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mjc2YzgyY2JjOGI5MWIwMTBkYjI3YTBkNTUzZDU2YWNfYzQ2ODc1ODBiMmY4OGNlOTlkMTJmNzFiMjMzYThjNGVfSUQ6NzMzMzMzMzQzMzA2Nzc5ODUzMF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTJhNzcxYjhlNDAzMmE4MDRiMTMyM2M5MjVmNDJkMThfMjE5ZTI1OTA4OGQzMjc5NWE1NjEwNmM0MDIwODI2MTJfSUQ6NzMzMzMzMzQyNDkwOTg2MDg2NV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjZiZjc0ZWZmZDE1Mjg5YjVjZmJjMjU5NmJkYmRhYjlfYjczMzA2OWFkYjk5NTE5OTAzNmVkYWM5MWNkNDE3OTZfSUQ6NzMzMzMzMzQyNTgxNTk5NDM2OV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTZhZjg0ZDFmOWExYjk0Mjg1ZDAwY2FlMjk0YjkyM2RfY2I3NzUwMmQzYjIwNzAzMTBiYjNhYWExZjcxMjNkZDZfSUQ6NzMzMzMzMzQyOTc2MjY3MDU5M18xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

##### REINFORCE：蒙特卡洛策略梯度控制 \- pai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODhmMmNmYTM0MjY0NjlhMDNmMDllZjhjZDA5NmM2MmZfNDg2MjQ4OGUzZmYwNGQ5MTljYzgzOGE3ODVkMTQ2MTlfSUQ6NzMzMzMzMzQyNzkyNTU2NTQ2OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 13\.4 带有基线 \(baseline\) 的 REINFORCE 325

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTQzZTgwNzhlMDFlMDRkZTg2N2ExYWNjOWEyYWU3ZWNfMjhlN2Y5N2I5ZTU3N2IxYTcxNjBlZWVkNzA3N2M1MGJfSUQ6NzMzMzMzMzQyMjE3MDk5Njc2NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDg4NjU2NWM4MWZkN2JlZGQ2ZDdiMTE1ZjQyZDA1OTdfYWE2MzIxMTBiNzVlYTg4MzU0YjZkNjcxNTFjYWM4OTZfSUQ6NzMzMzMzMzQyNzUzMjEzNjQ3Nl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDZhODhkYTMzZjU3ZmM2YzM5MGI3ZjVlNDU4MWI3MzJfMTkwYTA3ODlmYzNjOTI5MGY5NjAwY2U1MGFjZTk1NjBfSUQ6NzMzMzMzMzQyNjA0NjUwMDg2Nl8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 其中 b\(s\) 是基线

##### 带有基线的 REINFORCE \(分幕问题\) \- 估计 pai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTU3NDk4YjA1OGZiMTc0NDU5MmFiNDgyMWUxNDNmZjBfZjlkOGJiODY3ZWI2YWNhZWNmNmMzMDliZWE5MDYzYzNfSUQ6NzMzMzMzMzQzMDg5OTMyNjk3N18xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjhhNmE4ZWNjZmUwNzI3NjZhNDRlNmJhYzdjZmZkYTdfMDBkMTY3NTAxYjJmOGQ3NmRiYzEyNzMyNjAzM2QzYjVfSUQ6NzMzMzMzMzQyODI3Nzg4NzAwNF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 13\.5 “行动器\-评判器”方法 \(Actor–Critic\) 327

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzRhZWI4ZWM3MDMxMzljZDRhMDJlOGEzMTMzOWFmMWRfOTk2OGFhZjhkYWVmM2VmNDZiMGJkMjU2M2I3MWNmZjRfSUQ6NzMzMzMzMzQzNDkxODMwNTc5NF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 单步 Actor\-Critic \(分幕问题\) \- 估计 pai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTc1MDlhNzY5MGU3NjQ4ZjRhNTk5OThlNDAzODExMWVfZGY4ZGNkMzIzNWQ0MjZkNWQ1NjNjMTlmY2E0MTVkN2RfSUQ6NzMzMzMzMzQyMzE5NDU4NzEzOF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 带有资格迹的 Actor\-Critic \(分幕问题\) \- 估计 pai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGEwZmU0YWExMmZhMmVmNDg2Yzk5ZjAxOGI2ZGE4ZjVfOGM3ZTNjMGYwZTRkMDYzZWU5MDA4ZGNhMWNkZjMwMTBfSUQ6NzMzMzMzMzQzMTc5Mjc0NjUyNF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 13\.6 持续性问题的策略梯度 329

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGU1MjAwOGE0MWIxMjQ2MTVkN2U5YmVlZDI4YjcyODVfYjM0MWE4NWQ3ZjI4MTMyOTMzZGE3MDA3ZGYzNTE2MDJfSUQ6NzMzMzMzMzQyMjY0MDcyNjAxOV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDk2ZmFiNGFmYTIxMDc3NmRjNzg3YzExMjM2ODAxMzFfMDVlZTIxZmEyOThlN2EzZDkzYmMxNzJlM2E0OWI3MTNfSUQ6NzMzMzMzMzQzMjU3NzA2NDk2Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### Actor\-Critic \(连续问题\) \- 估计 pai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTBlZTk4NTkzMzAyZTFhYTk0MDhlY2QzMWVjZjY4OWVfZGJiZDAzNzZkODE0ZjcwZDA0MjM1YWZlZmZmMzJjOWNfSUQ6NzMzMzMzMzQzNDI0NjQ2MzQ5Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

##### 带有资格迹的 Actor\-Critic \(连续问题\) \- 估计 pai

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTE4ZGJiY2NkOTcxMTgzMzEzYTQzOTAwNTNjNWRhYTZfNDAxNjA0NjkwMzA5MWIwZmI1NjY0MzRiNWFlZDYzOTdfSUQ6NzMzMzMzMzQyNTgxNjA0MzUyMV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 13\.7 针对连续动作的策略参数化方法 332

- 正态分布概率密度方程（PDF）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmRmODFmYmZkOTcwNDFmYzQzOWMyOTBhNjU4ZDc4ODFfOWQ4NjVhOTU4MDk2ODk2ZjQ4OTQzYTZhNjE5ZjYwYjVfSUQ6NzMzMzMzMzQzMTgzMDQ0NjEwOF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGZkZTI5NDQzZDUwNzM4MWI1YTgwMmFkNjAxNjY0ZjVfZmNlZGQwYzE0YzIyNTMxNTZhOWEwMzY3NDJhMzYzNjVfSUQ6NzMzMzMzMzQyNTk4MzU4NjMwNl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDkwZDJlNDNkZTQzZjJkZDQ4YjUyNzlmNjdmYjk4NmJfNzE5N2I5MzJiZWMzOTU5MmJlYTI0MzMwYWRmZGRjY2FfSUQ6NzMzMzMzMzQzMjU3NzA0ODU3OF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTRiYjQxODViNGM1N2UwZWNkNDc2ZTA2MzVmNDYyYTRfZDM2ZTFlYWQ1YWI3YWU1ODZiMTQ3MjZjNDdiMjYxM2RfSUQ6NzMzMzMzMzQyNTc2NTUxNTI5Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

## 强化学习 \(RL\) 实践

### 直升飞机螺旋控制

- 课本讲的学习模型来训练策略的方法，实际中工程师并不是这样做。原因是这样生成的策略并 不稳定。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGE5NjdhZGQ0ZGYyMzkyZWI4MjRkMjM0ZTMyYjMwNGNfYzEyYTk1ZmNiZjI2YTRiOWRmNmZiNmFhZjE3Y2JiZmNfSUQ6NzMzMzMzMzQzNDg2Nzk0MTM3OF8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWQ5ZWRjYWU3YTVhY2RkNTg0OTRkYjU3N2Y1MzRhMThfMDk0YzBjODNmMjhmZGFiMDc5YjJmYjc3MjFiMGE4OWFfSUQ6NzMzMzMzMzQyODc3MzYzNDA1MF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OWFlYjMzYjYyNmFhYWY0ZWRmODFiYTA2YjBkZWI0MDdfN2M4YmNiNmRlYTJlNWViYjUxOTRiZmY4Yjk4NjRiNzhfSUQ6NzMzMzMzMzQzMjIyMDU4MTkxNl8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 通常会用无悔算法和最优控制（控制相关的算法），可以在测试集上得到比较好的性能。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2IzY2M2M2RjOWViNTIzNmMyY2M3NDkzYjcyMzczMTdfMmQzY2I0MTU2MTA0MTg4NGJiOGM2ZjQ1Mzc3YWYxMzlfSUQ6NzMzMzMzMzQyNTQ2NzY4NjkxNF8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

- 在此过程中，会做多轮迭代，最终可以得到一个比较稳定的控制策略。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTcyYTBhMThjNjhhNTJiZjYxZDY1ZDhmYWFmZDViZmVfNjcwNDZlOGI1ZjJjNTc2NjNmZGY4NzhlNDM4Nzg0OWNfSUQ6NzMzMzMzMzQzMDY3NzA0NTI0OV8xNzgxMjk0MTY2OjE3ODEzODA1NjZfVjM)

#### 无悔算法 \(No\-regret algorithm\)

- 会使用无悔算法 \(No\-regret algorithm\)

    - 从先前数据中选取好的特征

    - 生成一个稳定的特征序列

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2ZiMjE1MWMzYWQ4NTRjZjRhOWM3NGRiNTY2NTlhNmNfZjUxNjljMWIwYzUxZjljN2UyMGJjZGU5NmY0NTcwMTdfSUQ6NzMzMzMzMzQzMDU3MjE3MTI2NV8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)

#### 最优控制 \(Optimal Control\)

- 在此基础上，会增加一个最优控制 \(Optimal Control\) 生成的机制，来提升训练效果

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWYyOTgzOWQxNGY4YzdjZWZkMDIzYjY0ZmFiNTYxYzNfZjgxNWJkMmUxMGViYjNiNGI1MmZhNTUzOGQxNzQxYzZfSUQ6NzMzMzMzMzQyNzkyNTU4MTg1Ml8xNzgxMjk0MTY3OjE3ODEzODA1NjdfVjM)
