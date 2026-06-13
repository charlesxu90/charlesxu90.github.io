---
title: "DL 深度学习笔记"
subtitle: ""
date: 2021-06-14
draft: false
author: "Xiaopeng Xu"
description: "DL 深度学习笔记相关笔记。"
tags: ["Deep Learning", "Basic"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## NN 基础

### 二分类问题

* 对 64x64x3  的图片，判断是否有猫（1/0）![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030752833.png)

#### 基本标记

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030754968.png)

* X 的每一行对应的是一个样本，每一列对应的是一个特征。

### 逻辑回归 (Logistics regression)

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030757234.png)

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030758759.png)

* 二分类情况下，对应的 delta 函数是 sigmoid 函数。

#### Sigmoid 函数

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030800262.png)

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030801097.png)

#### 代价函数 (cost function)

* 目标：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030802859.png)

##### 损失函数 (loss/error function)

* 损失函数 (loss function) 针对每一个样本计算的误差

* MSE 通常会受限于局部最小值 (local minimum) 而不能找到全局最小值 (global minimum) 因而实际中不常使用。![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030804355.png)

* 实际中更常用的是下面这个： ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030805450.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030806591.png)

   * 举例分析：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030807779.png)

##### 代价函数 (cost function)

* 代价函数是损失函数的平均值，在一个循环中只计算一次。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030810003.png)
### 梯度下降法 (Gradient descent)

* 目标：找到 w 和 b，以最小化损失函数 (loss function)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030811749.png)

#### 梯度 (gradient)

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030813920.png)

* 思想：在每次循环中，叠加导数值，这样可以逼近最优点 (mimimum)

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030815477.png)

* 通过偏导数，来计算导数函数。![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030816931.png)

#### 导数 (derivative)

##### 线性函数的导数

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030818713.png)
##### 二次方程的导数

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030820596.png)
##### 更多导数

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030822739.png)
### 计算图

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030825151.png)
#### 按计算图计算导数

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030826611.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030828969.png)

### 深度神经网络

* 表示符号![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030831645.png)

   * L 表示层数

   * n[1], 表示 1 层中的节点数

   * z[1], 表示 1 层中的 (W[1]*x[0] +b[1])

   * a[1], 表示 1 层中的激活值 g(z[1])，g 常用 ReLU


## RNN

* 可以直观理解为相比传统的 NN 增加了时序记忆能力。但 Transformer 这种大网络中，也增加了类似 CNN 的抽象能力 (即 Multi-head attention)。

### 应用

* 语音识别、音乐生成、情感分类、DNA 序列分析、机器翻译、视频行为识别、命名实体识别

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030833883.png)
### 词表示 (word representation)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030836814.png)
### 为什么不用标准的神经网络？

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030839408.png)
### 简单的 RNN

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030842303.png)
##### 前向传播 (Forward propagation)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030844461.png)
##### 简化的标记符

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030846697.png)
##### 时间反向传播 (backpropagation through time)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030849778.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030851494.png)

### RNN 类型

* 多对多，多对一，一对一，一对多

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030853705.png)

### GRU (Gated Recurrent Unit)

#### RNN unit

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030855583.png)
#### GRU (simplified)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030857385.png)
#### 完整的 GRU

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030859566.png)
u=update, r=remember

### *LSTM (long short term memory)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030901553.png)
u=update, r=remember, 0=output, f=forget

GRU removed a<t> in passing, removed forget gate, using "1 - update" instead, and remember gate is similar to output gate.

Significantly improve computing effenciency.


#### 前向传播 Forward Illustration

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030903278.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030905093.png)
A gate is a sigmoid function with w and b. Softmax also contains a w and b.

##### Forget gate

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030907158.png)
* `Wf`: forget gate weight 𝐖𝑓

* `bf`: forget gate bias 𝐛𝑓

* `ft`: forget gate Γ⟨𝑡⟩

##### Candidate value

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030908357.png)
* `cct`: candidate value 𝐜̃⟨𝑡⟩

##### Update gate

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030909542.png)
* `Wi` is the update gate weight 𝐖𝑖

* `bi` is the update gate bias 𝐛𝑖

* `it` is the update gate 𝚪⟨𝑡⟩𝑖

##### Cell state

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030910771.png)

* `c`: cell state, including all time steps, 𝐜 shape (𝑛𝑎,𝑚,𝑇𝑥)

* `c_next`: new (next) cell state, 𝐜⟨𝑡⟩ shape (𝑛𝑎,𝑚)

* `c_prev`: previous cell state, 𝐜⟨𝑡−1⟩, shape (𝑛𝑎,𝑚)

##### Output gate

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030911989.png)

* `Wo`: output gate weight, 𝐖𝐨

* `bo`: output gate bias, 𝐛𝐨

* `ot`: output gate, 𝚪⟨𝑡⟩𝑜

* `a`: hidden state, including time steps. 𝐚 has shape (𝑛𝑎,𝑚,𝑇𝑥)

* `a_prev`: hidden state from previous time step. 𝐚⟨𝑡−1⟩ has shape (𝑛𝑎,𝑚)

* `a_next`: hidden state for next time step. 𝐚⟨𝑡⟩ has shape (𝑛𝑎,𝑚)

* `y_pred`: prediction, including all time steps. 𝐲𝑝𝑟𝑒𝑑 has shape (𝑛𝑦,𝑚,𝑇𝑥)

* `yt_pred`: prediction for the current time step 𝑡. 𝐲⟨𝑡⟩𝑝𝑟𝑒𝑑 has shape (𝑛𝑦,𝑚)

##### 代码

```python
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

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030913267.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030914840.png)

##### 公式

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030916840.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030918093.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030919320.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030920543.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030921754.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030922798.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030924222.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030925285.png)
* 𝑑𝑥⟨𝑡⟩ is represented by dxt,   

* 𝑑𝑊𝑎𝑥 is represented by dWax,   

* 𝑑𝑎𝑝𝑟𝑒𝑣 is represented by da_prev,    

* 𝑑𝑊𝑎𝑎 is represented by dWaa,   

* 𝑑𝑏𝑎 is represented by dba,   

* `dz` is not derived above but can optionally be derived by students to simplify the repeated calculations.

##### 代码

```python
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

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030926324.png)
##### 公式

#### ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030927822.png)

#### ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030929581.png)

#### ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030930817.png)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030932055.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030933265.png)
* 𝑑𝛾⟨𝑡⟩𝑜 is represented by `dot`,

* 𝑑𝑝𝑐˜⟨𝑡⟩ is represented by `dcct`,

* 𝑑𝛾⟨𝑡⟩𝑢 is represented by `dit`,

* 𝑑𝛾⟨𝑡⟩𝑓 is represented by `dft` 


### 其他 RNN

#### 双向 RNN (Bidirectional RNN)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030934431.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030936124.png)

#### Deep RNN

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030938257.png)

### *Transformers / BERT

Vaswani et al. 2017, Attention Is All You Need

#### 动机 (Motivation) 和直觉 (Intuition)

##### 动机 (Motivation) 

* RNN -> GRU -> LSTM 是在时序上增加复杂度

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030940142.png)
##### 直觉 (Intuition)

* 能否通过注意力机制 (Attention) 和 CNN 在平行层面增加抽象层次？

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030942307.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030943758.png)
#### 自注意力机制 (Self-attention)

##### 自注意力机制的直觉

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030945018.png)
* 整体上和 RNN 中的 attention 机制相似，都有 softmax 计算![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030946454.png)

* 不同之处是，为每一个词增加了 K 和 V 向量表示，类似于数据库中的 k 和 v，如下![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030948182.png)

##### 计算过程

* 计算A<3> 时，会对附近词的 K 和 V 都纳入计算，K 作为 attention 权重输入， V 作为 attention 数值的输入![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030950219.png)

* 对应的向量公式：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030952422.png)。dk 是一个 scale 项，对结果的影响可以忽略。


#### Multi-Head Attention

* 每一个 head 就像是问了一个问题，不同问题对应的附近词的权重会不相同![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030953646.png)

* 在计算 Multi-head attention 的时候，会把各个 head 的计算结果拼接在一起来计算出一个总体的权重。![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030955856.png)

#### Transformer 详情

##### 核心框架 Encoder & Decoder

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030957359.png)
* Encoder 和 Decoder 都会计算 N 次， Decoder 上次的输出，会加入到下次的输入。

* 如何获得 K 和 V 向量？

##### 提升 transformer 性能的其他机制

1. 位置编码 (Positional Encoding) ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031000066.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031001614.png)

2. ResNet connections：将位置信息传递到整个架构中。

3. Add & Norm： 可以加块训练速度。

4. Linear & Softmax layer：来预测下一个词。

5. Masked mult-head attention：在训练过程中模拟真实预测的场景，每次增加一个新词。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031003040.png)
