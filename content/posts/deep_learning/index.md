---
title: "DL 深度学习笔记"
subtitle: ""
date: 2026-05-20
draft: false
author: "Xiaopeng Xu"
description: "深度学习基础学习笔记：神经网络、反向传播与常见模型要点。"
tags: ["Deep Learning", "Basic"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

参考：https://www\.coursera\.org/specializations/deep\-learning?

## NN 基础

### 二分类问题

- 对 64x64x3 的图片，判断是否有猫（1/0）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2E1N2FjMWRiMzRlMDQ1OGEwOGYxMWZlZWM1NGFiNDhfMjQyNzcyNTM3OTI1MmUwNTNiNjg2ZjFkYjMyYjgwNWFfSUQ6NzM0MDc1OTc3NzYzNzQwMDU4MF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

#### 基本标记

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YTMxNTRjZGY2OWMxODk1MjlmNzg2NjAxNjIyMzlhOWRfMmExNzQ3MDA1ZjI4NzkzOTE3ZDhiZGVhM2U3ZjNmNzBfSUQ6NzM0MDc1OTg1NTQ4MjgxNDQ5Ml8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- X 的每一行对应的是一个样本，每一列对应的是一个特征。

### 逻辑回归 \(Logistics regression\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzZlOTBjMjY5NWU2MDcyNWE3NzNlN2JlMmE2ZjExZWZfMzFkNjk5ZDY1M2RlZTM3MzdiZWE2YzJhOTE0OTYzYTVfSUQ6NzM0MDc2MTg4MzI2NTI2OTc2M18xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2RhYmNjZGIyY2Y2ODRlZTMwZWRhMzA0OWRkMWUyOGVfYzU1MGIyZmRlMWM4OWMyMzkzMjNiNjM3NGE3YTczMzZfSUQ6NzM0MDc2MTkyNDU3MDc5MTkzOV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 二分类情况下，对应的 delta 函数是 sigmoid 函数。

#### Sigmoid 函数

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTYyZjIwNTg0OWI1NTAwYzk0YzdiODg1OTY4MWRhZjlfZmMxZjJiYWNhZmQ0NGMxMzNmNjY5MTY1YWZkMjVkMjFfSUQ6NzM0MDc2MTk5OTY3ODk4MDEwMF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWIxY2EzYzZlNTA2NWZkMjFmMDk4Y2QzNWY1ZDE1YzBfYjEzNmYyNTY3YTM0MGZiYmYyN2UyZTkxOWU3ZjJlNWJfSUQ6NzM0MDc2MjU5NDM1OTMyODc2OV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

#### 代价函数 \(cost function\)

- 目标：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzRkZDBlNTk5MzJmNzZiMDZiYmFiMWM2MWU0MTI4ZGZfMDdhZDAyOTU2ZmMwYTRjZjc4Zjc4ZGQ3ZGIwY2JmYmNfSUQ6NzM0MDc2MjY2MDA1NTM1MTI5OF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

##### 损失函数 \(loss/error function\)

- 损失函数 \(loss function\) 针对每一个样本计算的误差

- MSE 通常会受限于局部最小值 \(local minimum\) 而不能找到全局最小值 \(global minimum\) 因而实际中不常使用。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2FlZWY1NzFkM2IxMjU5MTcxOWFlYjc5OGI4YTEyN2JfNTI0NmVkOGEzYjIxNmZhMzhlYTExOTFmMDVkMDc3YTJfSUQ6NzM0MDc2MjczMzQwNTQzNzk1M18xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 实际中更常用的是下面这个：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzUwOTMzZmMzZjU4YzE5ODgyZmI2OTNkOWMyNjM2MjJfNTUwMWFiZDk5MGI2NTI1MzVhMjYxZDAxYmM5MzYxMzdfSUQ6NzM0MDc2Mjg0NzQzNTAzMDUyOV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

    - 举例分析：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGU2MDUwMDU2Y2JmZTY2Yzc0Zjc0Yjk0Y2UzZmYxZDhfZDU5ZGE5Zjc2NjZhZjkxZDhhYTAwMmM3MTVmYzNjOTJfSUQ6NzM0MDc2MzI3NzY3NDE2ODMyMl8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

##### 代价函数 \(cost function\)

- 代价函数是损失函数的平均值，在一个循环中只计算一次。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTlmN2RhMjMzNjUzZGI4Yjc2NmJmNDg2MzM5NWMwZDdfN2I5MGQyNjRiNjljNWE0OTZiYjk4N2Q4MGQxMjhhZmVfSUQ6NzM0MDc2MzMyMTUyNTYwMDI1OF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

### 梯度下降法 \(Gradient descent\)

- 目标：找到 w 和 b，以最小化损失函数 \(loss function\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWI0ZGI2YmFjMTRhODg2NjliOWJlN2JjMzY0YWQ5NzFfMDUyMjNkOWEzOGIxZmIxNGY0ZGNlY2FlMjk4NmUxMmJfSUQ6NzMzMzMzMzMyNjk4NTQ0NTQwNF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

#### 梯度 \(gradient\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzMzZmEwYTI3YzllNjE3MjM2NDdkNjBmZmNlZDUyZTBfZTBjZDgwYmI2MzNhOTZmN2YyMTc3ZGNjYmI2YmRmNDhfSUQ6NzMzMzMzMzMyOTk4ODU4MzQyNl8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 思想：在每次循环中，叠加导数值，这样可以逼近最优点 \(mimimum\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDg0MTBmODdiYTA0MGFhYmE2YTQ0ZGNkNmRkOWE5NjlfNjhlZTcxMDQzODc2NzA2MWQ5NWY1MTY4OWYwOWY1MmZfSUQ6NzMzMzMzMzMyOTI4MDU0ODg2OF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

- 通过偏导数，来计算导数函数。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTliNjAxNmMyOWY2MGFjYmNlZDdlMDdiNDgyOWQ0ZTNfOTY5N2UwOWY0MzliNDg4NWFhMDI1ZGU4MTFhZGEyZDRfSUQ6NzMzMzMzMzMyNzAyNzQwNDgyOF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

#### 导数 \(derivative\)

##### 线性函数的导数

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzJiYTc3MjQwYTQ5OTMwNGE3NTg2ZTgxMzc2MmI4NDJfZjAyNjQyODdkMWUyZTNhM2U1ZTg3YmZmMjUwZjYyNjJfSUQ6NzMzMzMzMzMyNjEyNTYxMzA4NF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

##### 二次方程的导数

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTExZDk1MTU0M2JkOGUyNDEyYjdmMWI0YWEzZmQzMTdfM2ZhZWEyM2JlZjAxMzUxNTIyYWNmYWViMDg1MGIxM2JfSUQ6NzMzMzMzMzMyNzA2OTMzMTQ4NF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

##### 更多导数

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjNkNWRiYTVhZDlkNGMwYWEwNDhkZjMyYzUxZTc4NTRfNmFiOGIzNjJkNGZmYTAxOGYyNWI0OTNmMDllYWFmMjhfSUQ6NzMzMzMzMzMyOTQ5ODY2OTA1N18xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

### 计算图

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTllODI1ZGM1YTJmOTZiY2M4YjRkNDkxMDBiYTc2OGNfOThhZDcxMDNhMGRjYmMyNmZkZjJiNzY2MWQxNzkyOWRfSUQ6NzMzMzMzMzMyODY5Njc1NDE3N18xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

#### 按计算图计算导数

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mzc3OGMxZjE5ZjQzOTBiYmJiMWEwOWJkYjAyMGQxZTJfYmRhY2I0ZDE0YTgzNDlmYzc1YmM2NDViYjNkMzRjYTFfSUQ6NzMzMzMzMzMyNDQ1NjI5NjQ3Nl8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzM3NzcxNWNhNGZhNDE5YWJjMzlkODhkZTg5NDA1MDBfMDRkODk2ZmM3NWVkZGUyZTQzZTEyY2JlY2ViMjJkMzNfSUQ6NzMzMzMzMzMzMTI4MTIxNTUxNl8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

### 深度神经网络

- 表示符号

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2NjY2EyYWM4NWM3N2U5NDc4M2Y1NzQ3NWUxMmI5ZWJfMTg0NmY0YTUyYzdmNjU4ODhiODQzMWZhM2NlOGFhNmJfSUQ6NzMzMzMzMzMyNzc3OTAyMDgwMV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- L 表示层数

- n\[1\], 表示 1 层中的节点数

- z\[1\], 表示 1 层中的 \(W\[1\]\*x\[0\] \+b\[1\]\)

- a\[1\], 表示 1 层中的激活值 g\(z\[1\]\)，g 常用 ReLU

## RNN

- 可以直观理解为相比传统的 NN 增加了时序记忆能力。但 Transformer 这种大网络中，也增加了类似 CNN 的抽象能力 \(即 Multi\-head attention\)。

### 应用

- 语音识别、音乐生成、情感分类、DNA 序列分析、机器翻译、视频行为识别、命名实体识别

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDIyYzRiNGY5Yzg5MGZiZjc5MmEyY2Q3YjE5YWI3MWJfYjhhNTJmZDdlMWFmN2I0OWVjMjRhYTMwNDBjNTRhNjFfSUQ6NzMzMzMzMzMzMTI4MTIzMTkwMF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

### 词表示 \(word representation\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODQzM2EzYjY0YWJlZTY3NDFkYzNiYWZkY2FjYzI0YTNfNTNjMzMxYzZkNGI0MzlhNDJhMmI1MDgxZDk0ZDYyNDVfSUQ6NzMzMzMzMzMyNTg4MzE2MjY1Ml8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

### 为什么不用标准的神经网络？

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjQwMmQ0MDEzNzcwOTRiMDdlN2ExOWRlZDZkOTM5NDFfMjk2YmQ2MTBhMGI1MWUwNTc5YzFhMzgxODQ4MzgyNzBfSUQ6NzMzMzMzMzMyNDQyMzU3NzYyOF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

### 简单的 RNN

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWM3MGQxNzRjOGFmNzQ1M2I5YTczNWZkYWZkYmMzYjVfMmU3OGM3MDJhZmM4ODUzYTI4NTZlY2U2ZTMzZmU4YTBfSUQ6NzMzMzMzMzMyOTA3ODQxOTQ1N18xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

##### 前向传播 \(Forward propagation\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODc3MGQ0MzZmMjBmM2Y5Y2NjNzQ1NzFhNmE5ZjFmN2ZfMTE3MjYxNjVkZDhlODM1NDJkYjAxZTEwZTU1ODJjNDdfSUQ6NzMzMzMzMzMyNzIyMDMyNjQyOF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

##### 简化的标记符

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTYwMzQ1YjUyOTIzNDNjMmQzYmM4MzRiZjI0N2EwMTZfZjQ4ZmZiNjQyYmRkYTUwYTY1ZGFmNGIwZjFiN2I4NTFfSUQ6NzMzMzMzMzMzMDAxMzc0OTI1Ml8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

##### 时间反向传播 \(backpropagation through time\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2U0NDVkNjE5ZTNjZjRjY2FlNGU3MjViYjQzNzU5NjlfNjM5YjY2YzFkNWI1MWUwNDRlZmU0NzRiYmZlMDZiODNfSUQ6NzMzMzMzMzMyOTI5MjMxMjU4MF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmY0MzI2ODU2NWY4MTVkYjk1ZWUzOWNjZjNlM2Y3OWNfOWEzNzNkODZhMjUwMTFiYjBkYjQ3YzM0NWZkYjIxMmNfSUQ6NzMzMzMzMzMzMDk3ODQwNjQyOF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

### RNN 类型

- 多对多，多对一，一对一，一对多

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NThhMjJmZDQzYjc4NzAwNzNiMDlmNjg2MTM3N2ZmYjBfMjkwMTMxYzRhYmM0ZTc1ZTg1OTQxMjU1MWYxZWUyNzNfSUQ6NzMzMzMzMzMzMDI0NDQzNTk5Nl8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

### GRU \(Gated Recurrent Unit\)

#### RNN unit

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODBhYTFiYzgyZDRiNDUxZGQ4NDA3NjIxM2M4Yzk2ODRfM2M2MTUzZGE3OTFmZDEyZWU0N2I0ZmI4MTNmNjRhYjNfSUQ6NzMzMzMzMzMyNzc3OTAwNDQxN18xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

#### GRU \(simplified\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWZkYjM2ZDA3YzM5YWNiZDAxYzQzMjQ1M2E4Zjg5YTZfMWUxOGU2NDcwZmIxZGEwN2NjNTI1YTZiMjUyZTRhZjNfSUQ6NzMzMzMzMzMyNzQ5NDYyNzMzMF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

#### 完整的 GRU

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2Q0YjU4OWJkOGE0M2ZlYzQ3M2Q3MmRhMTg0MmI5ZWZfNGVkNWU5ODkyZDVjMTZkNjBmYzRhY2E3MTAwNWZiMjlfSUQ6NzMzMzMzMzMyOTA0MDY4NzEwNl8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

u=update, r=remember

### \*LSTM \(long short term memory\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NmNjZDc1MzNkZDc1YTE5NGE4MTFiMDk4ODA5NTU5OTNfYmIyMDNiZmIxOTQwZTA0MWY3MmM4MTI1NzYzNmNkZmNfSUQ6NzMzMzMzMzMyNzU0MzI3MTQ1Ml8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

u=update, r=remember, 0=output, f=forget

GRU removed a in passing, removed forget gate, using "1 \- update" instead, and remember gate is similar to output gate\.

Significantly improve computing effenciency\.

#### 前向传播 Forward Illustration

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODVlNzkxNmQ1NTljMTVhZjFkMTA5NGYxZDYzYjQ3NGVfYjI1ZTg5N2QzZWQ0NDY1M2NiNjIxNGQ0MDc4MjcyZDJfSUQ6NzMzMzMzMzMyNDc5MTg0MDc5Nl8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzIyOWE0ZGZmYTQ2MTczZTg4MDYxNzE2ODJlMjIzNDNfMDhhNGYzNGMwMGQ2NTFiNDdhYTg1OWU5MjZmY2VmODFfSUQ6NzMzMzMzMzMyNzIwMzUzMjgwMV8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

A gate is a sigmoid function with w and b\. Softmax also contains a w and b\.

##### Forget gate

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGIzODZiMjg2ZTM5NGU4YmY3YTdhMDEwMTIwMGFiMmFfMDE0MGExNzE1OTc5Yjg2NGIzOWU4ZWJiYjdhNTgzZWZfSUQ6NzMzMzMzMzMzMTUxMTE4MTMxNF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- `Wf`: forget gate weight 𝐖𝑓

- `bf`: forget gate bias 𝐛𝑓

- `ft`: forget gate Γ⟨𝑡⟩

##### Candidate value

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2FiOGE0OWM0NjRiZjlkNzAzOWI1ODU0MDNkYzcyNjNfOTZhOTNjNGI5OTM5YmZhNDhhMWUxYzJmNDE2ZDVhMWJfSUQ6NzMzMzMzMzMyNjk5MzgzNDAxMl8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- `cct`: candidate value 𝐜̃⟨𝑡⟩

##### Update gate

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDQzMTY3NWFlZWU4YzIxYWQ5YjQ3MzFiMWE5NzhhMjNfYWVjMDE3OWU4NDdmNWVhOTAzY2JiOTYwYTEwZWVmMjlfSUQ6NzMzMzMzMzMyOTUxNDU5NDMwNV8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

- `Wi` is the update gate weight 𝐖𝑖

- `bi` is the update gate bias 𝐛𝑖

- `it` is the update gate 𝚪⟨𝑡⟩𝑖

##### Cell state

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MWYzZTk0MTQyN2U0ZTEyMjQ1MjQ0OWQ1MDVhNTM0MTZfZjE3NTI5Yjc4MTQzMzFmM2E4MGNlMDZjMjRhMzYzMDRfSUQ6NzMzMzMzMzMzMDg0ODM5OTM2M18xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- `c`: cell state, including all time steps, 𝐜 shape \(𝑛𝑎,𝑚,𝑇𝑥\)

- `c_next`: new \(next\) cell state, 𝐜⟨𝑡⟩ shape \(𝑛𝑎,𝑚\)

- `c_prev`: previous cell state, 𝐜⟨𝑡−1⟩, shape \(𝑛𝑎,𝑚\)

##### Output gate

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjI1ZmY0MWExYmQwMzgzZDc2M2U2ZmEzOWY1NTQ4MTdfNDIwYzFiNWQ4OTU3ZDA4MDQ1MzEwNGQzZjllODI3NjFfSUQ6NzMzMzMzMzMyNjk4NTQyOTAyMF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- `Wo`: output gate weight, 𝐖𝐨

- `bo`: output gate bias, 𝐛𝐨

- `ot`: output gate, 𝚪⟨𝑡⟩𝑜

- `a`: hidden state, including time steps\. 𝐚 has shape \(𝑛𝑎,𝑚,𝑇𝑥\)

- `a_prev`: hidden state from previous time step\. 𝐚⟨𝑡−1⟩ has shape \(𝑛𝑎,𝑚\)

- `a_next`: hidden state for next time step\. 𝐚⟨𝑡⟩ has shape \(𝑛𝑎,𝑚\)

- `y_pred`: prediction, including all time steps\. 𝐲𝑝𝑟𝑒𝑑 has shape \(𝑛𝑦,𝑚,𝑇𝑥\)

- `yt_pred`: prediction for the current time step 𝑡\. 𝐲⟨𝑡⟩𝑝𝑟𝑒𝑑 has shape \(𝑛𝑦,𝑚\)

##### 代码

```Python
def lstm_cell_forward(xt, a_prev, c_prev, parameters):
    # Retrieve parameters from "parameters"
    Wf = parameters["Wf"] # forget gate weight
    bf = parameters["bf"]
    Wi = parameters["Wi"] # update gate weight (notice the variable name)
    bi = parameters["bi"] # (notice the variable name)
    Wc = parameters["Wc"] # candidate value weight
    bc = parameters["bc"]
    Wo = parameters["Wo"] # output gate weight
    bo = parameters["bo"]
    Wy = parameters["Wy"] # prediction weight
    by = parameters["by"]
    
    # Retrieve dimensions from shapes of xt and Wy
    n_x, m = xt.shape
    n_y, n_a = Wy.shape

    # Concatenate a_prev and xt (≈1 line)
    print(a_prev.shape)
    print(xt.shape)
    concat = np.concatenate((a_prev, xt), axis=0)

    # Compute values for ft, it, cct, c_next, ot, a_next using the formulas given figure (4) (≈6 lines)
    ft = sigmoid(Wf.dot(concat) + bf)
    it = sigmoid(Wi.dot(concat) + bi)
    cct = np.tanh(Wc.dot(concat) + bc)
    c_next = ft * c_prev + it * cct
    ot = sigmoid(Wo.dot(concat) + bo)
    a_next = ot * np.tanh(c_next)
    
    # Compute prediction of the LSTM cell (≈1 line)
    yt_pred = softmax(Wy.dot(a_next) + by)

    # store values needed for backward propagation in cache
    cache = (a_next, c_next, a_prev, c_prev, ft, it, cct, ot, xt, parameters)

    return a_next, c_next, yt_pred, cache
```

#### 反向传播

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmZjNDIxNTA1M2VhMDdiODA1ZDQwODZmNjljMWM3MjVfNWI4ZTgwN2U4NWQwNmFmNDRmYzYyZDNlNGRmZGZiYTZfSUQ6NzMzMzMzMzMyNjIwNTMzNzYwMl8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MjBmMjI3NTM0MWQwY2UyNWJkMzc1YWRiNzBjODc5MThfM2ZlNjAzZWNlODhlOTUyYjEzM2Y4OTQ3ZjVjMjY0N2VfSUQ6NzMzMzMzMzMyODUxMjE4ODQ0NF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

##### 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzM2MWYwZDZlNTUzOGQyNWNiMzAyZmRmMDdlYTVhZjdfMTgxMDJjYzJhYTVkMGYzODQ2MDBlOGE0MmRjYjA4YTlfSUQ6NzMzMzMzMzMzMDQ5NjkxMzQxMF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTY4ZTRlMzBhMDViZGJiYzM3ZTcwYWUyZWJhZDA0YzFfM2IzOTUxNGU1NTNiMWJkYTcwZmUyNjNlZjI0N2U4ODFfSUQ6NzMzMzMzMzMyODc1MTI4MDEyOV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGM1ZDYzM2FlMzEyZWRlZmQ4YjExNjdiMjM1ZDc5ZjVfNzIzOTk5N2Q3ODg0ZDczNTJhZTkxZDU3MDNkNzkwYzlfSUQ6NzMzMzMzMzMyNjc1ODk1Mjk2NF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODU0NmFhNzgyMjkxZGRiNjBlNjY5MDAwZmU5MGM1ZGRfNmYwMGQ0YzExZmI5ZTA1Y2EwODUyMmFmNWUzMGE3NzVfSUQ6NzMzMzMzMzMyOTU0ODE4MTUzMl8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YWQ2ZjJkOWQxMDNkM2I5ZDg0MTI0MzRkYzQ4NmQ1NmZfMTFlNjNkMTkyODZhZTc5NzEzZTkxNmZlODY2MTg3OWNfSUQ6NzMzMzMzMzMzMDY0Mzc2MzIwMV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzNhYmI5OGU0MDcwYzMzMzJhMTQ3NDgxNzM0Nzg2Y2ZfOGRlMGVhZmQ0NjAwNjVjNTk3OWZiMDM2MjcxNGVkY2JfSUQ6NzMzMzMzMzMzMDUyOTYzMjI4NF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODlmODU1YTZkYjE4Yzk4YjQ2ZTk3MjY2NjNlMjUwMzhfZDcyZGU0NmVmNjIzMDRjZjNhNDEyNzIyMzdkOWJkZTlfSUQ6NzMzMzMzMzMzMTM2NTE2NzEwNV8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmNmY2JjZjNkN2RmYjRhYThhMzk0ZGE5YTZjYWE2NWRfMWM4NDlhODFhNjM5ZjQ3Y2M0ZGI0NjU4YTliMTU4Y2VfSUQ6NzMzMzMzMzMyNzI2NjQ0NzM4OF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 𝑑𝑥⟨𝑡⟩ is represented by dxt,

- 𝑑𝑊𝑎𝑥 is represented by dWax,

- 𝑑𝑎𝑝𝑟𝑒𝑣 is represented by da\_prev,

- 𝑑𝑊𝑎𝑎 is represented by dWaa,

- 𝑑𝑏𝑎 is represented by dba,

- `dz` is not derived above but can optionally be derived by students to simplify the repeated calculations\.

##### 代码

```Python
ef rnn_cell_backward(da_next, cache):
    # Retrieve values from cache
    (a_next, a_prev, xt, parameters) = cache
    
    # Retrieve values from parameters
    Wax = parameters["Wax"]
    Waa = parameters["Waa"]
    Wya = parameters["Wya"]
    ba = parameters["ba"]
    by = parameters["by"]

    # compute the gradient of dtanh term using a_next and da_next (≈1 line)
    dtanh = da_next * (1 - np.tanh(Wax.dot(xt) + Waa.dot(a_prev) + ba) ** 2)

    # compute the gradient of the loss with respect to Wax (≈2 lines)
    dxt = Wax.transpose().dot(dtanh)
    dWax = dtanh.dot(xt.transpose())

    # compute the gradient with respect to Waa (≈2 lines)
    da_prev = Waa.transpose().dot(dtanh)
    dWaa = dtanh.dot(a_prev.transpose())

    # compute the gradient with respect to b (≈1 line)
    dba = np.sum(dtanh, axis=1, keepdims = True)
    
    # Store the gradients in a python dictionary
    gradients = {"dxt": dxt, "da_prev": da_prev, "dWax": dWax, "dWaa": dWaa, "dba": dba}
    
    return gradients
```

#### 反向信息传递

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2UzZWZhNTk3OTA4ZjkzMTA4NTUzYjE1NDZmZTczYzZfMGM4OGEzYTIyNDcyNGZhYTY2OTI2ZDE5MjBmM2JjZDFfSUQ6NzMzMzMzMzMzMTI3NjIzNDc1NF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

##### 公式

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTAzNDM0OTk0NWQ5ZTg3NGViNDVmYmE4Y2FhNmY0OTRfMmY0ZWMyZjBmY2UyMjFjZTYwZDNiMzFkMzc4NTFjYWFfSUQ6NzMzMzMzMzMyNzY4MTc0ODk5NF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2UwYzliYThhYTVjZTJmNDJjZjMxMGY3YzcxNWNjMmRfOTJjMjQ0ZmIwZmQ5ZDNlZGJjMmVlZDMwNmY0NjAwM2JfSUQ6NzMzMzMzMzMyODc0NzA1MzA4NF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGEwZDhiMjRjMDZkZjhmZmMxMTc1MGM3MmY3ZGUxZTFfOWI2ZDliYmZmMGE2NzUyNWU2OWVlN2RlMDM0NmI3OTJfSUQ6NzMzMzMzMzMyODk2NTE4OTYzM18xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGRkYjBlNTAzNjA4OWM2ODRlYWE2NzgzY2ZiYWQ5ODBfMWIxMmRlMTJhOTM3YjI5NjJhOWM4YTIwNjY5MzJjZmRfSUQ6NzMzMzMzMzMyNDQ1NjI4MDA5Ml8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmU3MjA3ZGUxZGY5NGNhNjNiNjFhMDZlZDU5MmZmMmZfM2E2ZDljNDhhOWVkNjk2NWIzOTI1NTQ4NzE2MjlhYWRfSUQ6NzMzMzMzMzMzMjExOTI3MzQ3NF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

- 𝑑𝛾⟨𝑡⟩𝑜 is represented by `dot`,

- 𝑑𝑝𝑐˜⟨𝑡⟩ is represented by `dcct`,

- 𝑑𝛾⟨𝑡⟩𝑢 is represented by `dit`,

- 𝑑𝛾⟨𝑡⟩𝑓 is represented by `dft`

### 其他 RNN

#### 双向 RNN \(Bidirectional RNN\)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWQ5NzE0MzA4ODU2Yjk5ZjVhYTAwNjBhOGMyMmU2ZWRfOGJiZDE0YTgwNjMwN2YyZGZjMTdmMmU0ZWZhM2Y5MjRfSUQ6NzMzMzMzMzMyNDQ1NjI2MzcwOF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODljOWM4NmJkYWYwOGI4ZjUwMmI0YzIwNWMzMmM2MjZfYTZiYzgyOTg3YjA3ODcyMDVhOTg3ZTk3NGIyMmNhYjlfSUQ6NzMzMzMzMzMyOTU0ODE2NTE0OF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

#### Deep RNN

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjBkMTJhZjQyZTkxMGUwYmIzOWI0MTYwYmQ1MzUyMjNfNDRkOTNjZGY4ZWU5NDBjN2RhNGQyMzU4ZjE1MWJkZTNfSUQ6NzMzMzMzMzMyOTA3ODQzNTg0MV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

### \*Transformers / BERT

Vaswani et al\. 2017, Attention Is All You Need

#### 动机 \(Motivation\) 和直觉 \(Intuition\)

##### 动机 \(Motivation\)

- RNN \-\> GRU \-\> LSTM 是在时序上增加复杂度

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mzc5YmEyYzE2ZjQ5NGJiMzIyMDUyMTA3MWVlODM1YzZfMjY4MjVlOTczMzdiNDIyNWFjMzQxOTNmZGU2NDkyMThfSUQ6NzMzMzMzMzMyNTI1MzE4MTQ0MV8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

##### 直觉 \(Intuition\)

- 能否通过注意力机制 \(Attention\) 和 CNN 在平行层面增加抽象层次？

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Yjk5ZDZkM2RhZDc5ZmJmYzI1NDQ4MDA4NzUzMGQ1YjlfNTY5NWE2MGZiZTg2OTYzYmU3OWQ5N2E4MTc4NzQ2YmJfSUQ6NzMzMzMzMzMzMTg0MzI1MjIyNV8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWZmNWU0OGI5NDQ2OWEzNDUyYzIxNzllNjU0MTIzMWZfYmUwZmRjZjM1ZThiMDU2MWY4ZDI0MGYyYWQ0ZmZiNDdfSUQ6NzMzMzMzMzMzMTk3NjY1MDc4MF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

#### 自注意力机制 \(Self\-attention\)

##### 自注意力机制的直觉

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGU0ZGM1Nzc4ZjRkMTA4ZTZiYWI1MDJhMTEzNWQwMjFfZDg1ZjI5MDdjZjA4MWQwZjkzNTExODFmNDMzNDA4OTJfSUQ6NzMzMzMzMzMyOTQ5ODY4NTQ0MV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 整体上和 RNN 中的 attention 机制相似，都有 softmax 计算

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjQ1NTI4MTE4OWQ5ZDQ1NTMwZmFlNmM5MzkzYzg4YjhfMmRiZWYwMTA2YjdjYzdlZDU3ZTUzMjg5NDIzZDJlODBfSUQ6NzMzMzMzMzMyNjk5MzgxNzYyOF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

- 不同之处是，为每一个词增加了 K 和 V 向量表示，类似于数据库中的 k 和 v，如下

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGE0ZDI4NDFlMTE1NmIwYWZmZWE3M2EyNzAxMTcwNmZfYmZhY2YxNmU1MTUxMWJjZmU0ZGQ4ZDBjMzQyYWI0ZTJfSUQ6NzMzMzMzMzMyNzc3OTA1MzU2OV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

##### 计算过程

- 计算A\<3\> 时，会对附近词的 K 和 V 都纳入计算，K 作为 attention 权重输入， V 作为 attention 数值的输入

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2M3MmYwY2JiODQxZTJlYjk2YjEzMWMyNzZiMzMzM2VfMzllOGFkZDY1ZWU0OWMyMWE3OGZmOWQzNTdlZDY2MzBfSUQ6NzMzMzMzMzMyNzU5NzgxMzc4OF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 对应的向量公式：

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjhiNWI5ZDA3YmI1NjFkMTE4ZTg1NjJmNDc0N2FiMjhfMGZmMjExN2Q4OTgyMDc2ODgxMWJjOGY5ODI4MWNhOWVfSUQ6NzMzMzMzMzMyNjIwNTMyMTIxOF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- 
。dk 是一个 scale 项，对结果的影响可以忽略。

#### Multi\-Head Attention

- 每一个 head 就像是问了一个问题，不同问题对应的附近词的权重会不相同

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTBmMjViMGI5ZmQxYzNjYmUwYmE5MWE0ZTU4OTkyYTlfODNhM2QyNzViNWNlNTllZjhmYWNhYjM4MzgzMjEyNzhfSUQ6NzMzMzMzMzMyOTA3ODQwMzA3M18xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

- 在计算 Multi\-head attention 的时候，会把各个 head 的计算结果拼接在一起来计算出一个总体的权重。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTU3NzAwNmI2MWYwZmE5ZmI5Y2Y2NTJiNGZmNTgyZjFfNGE1MGMxNjg4YjI3MGZhY2EwZWQyYjc4YzRmOWVhZGFfSUQ6NzMzMzMzMzMyODkyNzQwODEyOV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

#### Transformer 详情

##### 核心框架 Encoder \& Decoder

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZjNhNDc1Yjg5ZWU0NTZkZWZiOWMxODczNWMzODhlMWNfMDEyMDUwMzRmN2Y5ZjQ3YjUyMzViNjQ2OWZjM2M2ODdfSUQ6NzMzMzMzMzMyODc1MTI2Mzc0NV8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

- Encoder 和 Decoder 都会计算 N 次， Decoder 上次的输出，会加入到下次的输入。

- 如何获得 K 和 V 向量？

##### 提升 transformer 性能的其他机制

1. 位置编码 \(Positional Encoding\) 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTA4YTUwZmYzNzkxYzgxMzdjNTZmYzk4YWY4OWQwZDlfNmFkYjY0MWIwMDRmMzkzM2UyM2Y0MjUwZmEzMTQ1MjhfSUQ6NzMzMzMzMzMyNjEyNTU5NjcwMF8xNzgxMjk0MjA2OjE3ODEzODA2MDZfVjM)

1. 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjY4NWMwMjU0ZTY0N2Q0Y2U2OGUxZWE5MjI1MWE3YjNfNjc1Nzk3OTNmNWE3YjU0YTE3NjA1YjQ5YzM0N2EwNjVfSUQ6NzMzMzMzMzMyOTU0ODE0ODc2NF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)

1. ResNet connections：将位置信息传递到整个架构中。

2. Add \& Norm： 可以加块训练速度。

3. Linear \& Softmax layer：来预测下一个词。

4. Masked mult\-head attention：在训练过程中模拟真实预测的场景，每次增加一个新词。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGMyM2FmMDAwODE2MjMwYTE1MmM4OWNmNGRhMTI2ZmNfNjM3Zjc4NTc4YzhhMTM2MzU1OGU3ZDk4MjgyYTM3YjNfSUQ6NzMzMzMzMzMzMTMyNjU2NjQyOF8xNzgxMjk0MjA1OjE3ODEzODA2MDVfVjM)
