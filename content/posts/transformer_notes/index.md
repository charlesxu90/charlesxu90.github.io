---
title: "Transformer 学习笔记"
subtitle: ""
date: 2022-06-13
draft: false
author: "Xiaopeng Xu"
description: "Transformer 学习笔记相关学习笔记。"
tags: ["Transformer", "Deep Learning"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 基础介绍

参考：

1. [https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/](https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/)

2. [https://zhuanlan.zhihu.com/p/351558402](https://zhuanlan.zhihu.com/p/351558402)


### 注意力机制 attention

Attention 是神经网络中的一种机制：模型可以通过选择性地关注给定的数据集来学习做出预测。Attention的个数是通过学习权重来量化的，输出则通常是一个加权平均值。


常见的Transformer是依赖于scaled-dot-product的形式，也就是：给定query矩阵Q, key矩阵K以及value矩阵V，那么我们的输出就是值向量的加权和，其中，分配给每个值槽的权重由Quey与相应 Key 的点积确定。 

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015001293.png)
对于单个query以及单个key向量, ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015002699.png) ,我们可以计算得到下面的标量值：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015003965.png)

其中， Si 是keys的集合。

#### 自注意力 self attention

* 是一种注意机制，模型利用对同一样本观测到的其他部分来对数据样本的剩下部分进行预测。从概念上讲，它感觉非常类似于non-local的方式。还要注意的是，Self-attention是置换不变的；换句话说，它是对集合的一种操作。


而关于 attention 和 self-attention 存在非常多的形式。这个后面会讨论到。

#### 多头自注意力 Multi-Head Self-Attention

multi-head self-attention 是 Transformer 的核心组成部分，和简单的 attention 不同之处在于，Multihead 机制将输入拆分为许多小的 chunks，然后并行计算每个子空间的scaled dot product，最后我们将所有的 attention 输出进行拼接。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015005228.png)
其中，![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015006759.png)，![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015008485.png) 是 concate 操作，![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015009721.png) 是权重矩阵，它将我们的输出 embeddings(L*d) 的映射到 query, key, value 矩阵，而且 ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015011159.png) 是输出的线性转化，这些权重都是在训练的时候进行训练的。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015012573.png)

### Transformer

Transformer，很多时候我们也称之为"vanilla Transformer", 它有一个 encoder-decoder 的结构。开始是为文本翻译任务，基于 Seq2Seq 而开发的模型。单独的 Transformer decoder 可以在语言建模的时候获得非常好的效果，如 GPT。单独的 encoder 在 embedding 学习中有非常好的效果，如 BERT。

#### 编码器解码器结构 Encoder-Decoder

Encoder 生成一个基于 attention 的表示，能够从一个大的上下文中定位一个特定的信息片段。它由6个身份识别模块组成，每个模块包含两个子模块、一个 multihead self-attention 和一个 point-wise 全连接前馈网络。

按 point-wise 来说，这意味着它对序列中的每个元素应用相同的线性变换（具有相同的权重）。这也可以看作是滤波器大小为1的卷积层。每个子模块都有一个剩余连接和layer normalization。所有子模块输出相同维度的数据。

Transformer 的 decoder 功能是从 encoder 的表示中抽取信息。该结构与 encoder 非常相似，只是 decoder 包含两个多头注意子模块，而不是在每个相同的重复模块中包含一个。第一个多头注意子模块被屏蔽，以防止位置穿越，即 attend 到还没生成的位置上。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015014916.png)
#### 位置编码 Positional Encoding

因为 self-attention 操作是与不考虑顺序的 (permutation invariant)，所以使用正确的位置编码在数值上对输入加以区分是非常重要的。

下面是两种常见的位置编码。通过位置编码来学习到 order 信息。

1. Sinusoidal positional encoding，给定 token 的位置![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015017541.png) ,维度![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015018946.png),![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015020170.png) ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015021933.png)

1. Learned positional encoding, 对每个学习得到的列向量，对每个绝对位置进行编码。


#### 辅助 Loss auxiliary loss？

为了取得更好的效果，我们一般会加入辅助 loss，

* 除了在序列末尾只生成一个预测之外，每个中间步骤也要做出正确的预测，这就迫使模型在给定的较小上下文作出准确预测（例如，上下文窗口开头的前几个 tokens）。

* 每个 Transformer 中间层也要用于进行预测。随着训练的进行，较低层的权重对总损失的贡献越来越小。

* 序列中的每个位置可以预测多个目标。即，对未来的两个或多个 token 进行预测。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015023923.png)
## 问题

1. Attention 是如何和之前时间点的位置作关注的，而不是时间点以后的位置，即 Causal？通过 Attention 中的 Mask，Attention 是个 t-t 的结果，做一个三角形的 mask，可以实现 causal 关系。

2. Inference 时候的复杂度是如何计算得到的？

## 典型工作

### Reformer 

做了如下的改进，是的模型的复杂度从 O(L^2) 变为了 O(L log(L))

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015026269.png)
#### 主要解决的痛点

* Transformer模型的空间复杂度高，所以sequence length必须不能很长，batch size也不能很大。在attention机制中，由于 attention 机制在计算时需要计算两两的attention score，这需要的时间和空间复杂度是 O(L^2) ，所以即使序列的长度很短，也会使用大量的资源。

* 以BERT为例，transfer的encoder的层数越多，需要储存的参数量越大，因为我们需要储存层与层之间的连接参数（activations），用于反向传播时的计算。因为我们知道，我们encoder中，分为self-attention以及feed forward neural network（FFN），其中FFN是两层的神经网络，其中的中间层的hidden size ( d_ff ) 比self attention的hidden size ( d_model )更大，所以 占据了更多的内存空间。例如：bert—base的中文模型的( d_model ) `"hidden_size": 768`, 而 FFN ( d_ff )的 `"intermediate_size": 3072` 。


#### 采用的方式

* 降低 attention 内存消耗－Locality Sensitive Hashing。Attention 使用了LSH的方式，将attention score 相近（即Key相似的）的分到同一个bucket中。因为我们经过softmax之后，一个 query 和其他的所有的token的计算 attention score主要是取决于高相似度的几个tokens，所以采用这种方式将近似算得最终的attention score。

* 降低 ResNet 导致的 activation 存储内存 －－Reversible layers。[RevNet](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/1707.04585) 的提出是为了解决ResNet层数加深后，我们需要储存每一层的activations（即每一层的输入），导致 memory 消耗过大的问题。同样我们在transformer中也遇到了同种问题，我们采用这种方式的话，不需要我们记录中间层的activations，而只需要我们储存最后一层的输出，从而通过模型的特定结构，反推出中间层的结果。

* 降低 FFN 内存消耗－Chunking FFN layers 将FFN分段处理，因为FFN中的输入之间互相独立，进行分段的处理可以降低空间消耗。

##### Locality Sensitive Hashing Attention

背景：通常在一个 attention 中，与某一位置关联性比较大的只有几个。因此可以考虑通过 LSH 来找关联点。

* LSH 局部敏感哈希的设计初衷：两个相近的输入比相远的输入更容易获得相同的hash 值。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015028560.png)
* 好处：并行性，可以并行处理，每个值都有特定的区域

* 可能的坏处：近似性，如果两个值很近，但是刚好在临界地区，那么这两个可能会被分的很远。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015031112.png)
测试了下，在序列长度 400 以内，实现 LSH attention，并不会提升内存使用效率。而且学习的精度比较差（可能与使用的参数也有关系）。

##### Reversible layers

##### Chunking


#### 取得的成果

该改进版的reformer能够是的sequence length 长度达到64k，相比于之前的常见的512 长了不少。得到的效果和之前的transformer 差不多，但是速度却快了不少。





## 热点主题

### 长序列学习 Improved Attention Span

提高 Attention Span 的目的是使可用于 self-attention 的上下文更长、更有效、更灵活。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015033867.png)
### 更小的计算成本 Less Time and Memory Cost

一般 Transformer 的计算和存储开销随序列长度呈二次增长，因此很难应用于很长的序列。因此有很多方法在研究如何减少计算和内存的消耗。

#### 采用 sparse attention：Sparse Transformer

Sparse Transformers 中提出用 Sparse Attention Matrix Factorization 来减小内存使用。在 GPT-3 训练中得到了使用。

Sparse Transformer 引入分解的 self-attention，通过稀疏矩阵分解，我们可以训练上百层的 dense 的 attention 网络，序列长度可以达到 16384。


给定attention链接的模式集合  ,其中  记录key位置的集合，第  个query向量可以扩展为： 

尽管  的size是不固定的，  是size为  的，因此， 

在自回归的模型中，一个attention span被定义为  , 它允许每个token可以处理过去的所有其它位置。

在分解的self-attention中，被分解为树的依赖，例如对于没对  ,其中  , 存在一条路径链接  和  。

更加精确地说，集合  被划分为  个non-overlapping的子集，第  个子集被表示为  ，所以输出位置  和任意的  的路径有最大长度  ,例如，如果  是  和  的索引路径，我们有 

##### Sparse Factorized Attention

Sparse Transformer提出了两类分解的attention，

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015036520.png)
Strided attention(stride  ,在图像中,每个像素可以链接到所有到之前  个像素raster scanning顺序，然后那些像素在相同列中相互链接。 Fixed attention,一个小的tokens集合总结之前的位置并且向未来的位置传递信息： 

其中  是一个超参数.

##### Use Factorized Self-Attention in Transformer

存在三种方式使用sparse factorized attention模式的方法：

每个residual block的attention type，把它们交错起来，  ,其中  是当前residual模块的index;设置一个单独的head，它负责所有分解head负责的位置，  ;食欲哦那个一个multi-head attention机制，但是和原始的transformer不同，每个head可以接受上面的一种模式，1或者2.

稀疏Transformer还提出了一套改进方案，将Transformer训练到上百层，包括梯度检查点、在backward pass的时候重新计算attention和FF层、混合精度训练、高效的块稀疏实现等。

#### 采用局部敏感哈希 Locality-Sensitive Hashing：Reformer

Reformer模型旨在解决Transformer中的下面几个痛点：

具有N层的模型中的内存比单层模型中的内存大N倍，因为我们需要存储反向传播的activations。中间FF层通常相当大。长度为的序列上的注意矩阵通常在记忆和时间上都需要  的内存和时间；

Reformer进行了两种改变:

将dot-product的attention替换为locality-sensitive hashing(LSH) attention,这将时间复杂度  从降低为  ;将标准residual block替换为reversible residual layer，这样在训练期间只允许存储一次激活，而不是  次（即与层数成比例）。

##### Locality-Sensitive Hashing Attention

在attention  中，我们更加关注大的只，对于每个  ,我们在寻找  中于  最近的一个行向量，为了寻找它，我们在attention机制中加入：Locality-Sensitive Hashing (LSH)

如果它保留了数据点之间的距离信息，我们称hashing机制  是locality-sensitive的，这么做相近的向量可以获得相似的hash，Reformer中，给定一个固定的随机矩阵  ,其中  是超参数，hash函数为 

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015039222.png)
在LSH attention中，一个query只可以和在相同的hashing bucket中的位置进行交互，  ,

attention矩阵通常是稀疏的;使用LSH, 我们基于hash buckets可以对keys和queries进行排序设置  ,这样,一个bucket中的keys和queries相等，更便于批处理。有趣的是，这种“共享QK”配置并不影响Transformer的性能。使用  个连续的group在一起的query的batching，

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015042215.png)
##### Reversible Residual Network

Reversible Residual Network的动机是设计一种结构，使任何给定层的激活都可以从下一层的激活中恢复，只需使用模型参数。因此，我们可以通过在backprop期间重新计算激活来节省内存，而不是存储所有激活。

给定一层  , 传统的residual layer都是做的  ,但是reversible layer将输入和输出split为  ,然后执行下面的操作: 

reversing就是： 

我们将相同的思想应用到Transformer中得到： 

内存可以通过chunking 前向计算进行操作: 

#### 采用循环模型 Make it Recurrent：Universal Transformer

Universal Transformer将Transformer中的自我注意与RNN中的循环机制结合起来，旨在受益于Transformer的长期全局receptive field和RNN的学习inductive偏差。

Universal Transformer使用自适应计算时间动态调整步长。如果我们固定步数，一个通用变换器就相当于一个多层变换器，具有跨层共享的参数。

在较高的层次上，Universal Transformer可以看作是学习每个token的隐藏状态表示的递归函数。递归函数在标记位置之间并行演化，位置之间的信息通过self-attention进行共享。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015045434.png)
给定长度为  的序列，Universal Transformer在第步迭代更新表示  ，在第0步，  被出事为输入embedding矩阵，所以的位置编码在multi-head self-attenion中被并行处理，然后在经过一个recurrent transition function 

Transition(  )可以是一个 separable convolution或者fully-connected neural network。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613015047783.png)
在Universal Transformer的自适应版本中，循环步数  由ACT动态确定。每个位置都配有一个动态停止机制。一旦每令牌循环块停止，它将停止进行更多的循环更新，而只是将当前值复制到下一步，直到所有块停止或直到模型达到最大步长限制。

#### 
