---
title: "CL 对比学习介绍"
subtitle: ""
date: 2021-01-07
draft: false
author: "Xiaopeng Xu"
description: "CL 对比学习介绍相关学习笔记。"
tags: ["Contrastive Learning", "Self-supervised Learning"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 对比学习简介 2021-01-07

参考：Understanding Contrastive Learning [https://towardsdatascience.com/understanding-contrastive-learning-d5b19fd96607](https://towardsdatascience.com/understanding-contrastive-learning-d5b19fd96607)

对比学习是一种机器学习技术，通过教导数据点相似或不同，让模型无需标签就能学习到数据集的一般特征。

背景：和 word2vec 类似，将样本投射到另一个空间维度，成为一个 vector，相似的样本 cosine 距离小，不相似的距离大。

开闹洞：距离->抽象: 难以解释的距离，产生的新的抽象。万有引力定律。


### 举例说明 SimCLR

Contrastive learning 典型例子是 SimCLR。主要是在图片上做，用 cnn。后面加 ann 提升 embedding 效果。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014845917.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014848884.png)
1. 核心：

   1. Loss 的定义![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014850612.png)InfoNCE![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014852340.png)

   2. 模型结构：是否 resnet，layer 数

### 应用：半监督学习

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014853784.png)
## 对比学习研究进展精要 2021-04-24

参考：对比学习（Contrastive Learning）：研究进展精要 [https://zhuanlan.zhihu.com/p/367290573](https://zhuanlan.zhihu.com/p/367290573)

指导原则：通过自动构造相似实例和不相似实例，要求习得一个表示学习模型，通过这个模型，使得相似的实例在投影空间中比较接近，而不相似的实例在投影空间中距离比较远。

对比学习方法（从防止模型坍塌的角度）：

1. 基于负例的对比学习方法，例如 SimCLR

2. 基于对比聚类的方法、

3. 基于不对称网络结构的方法

4. 基于冗余消除损失函数的方法


### SimCLR 基于负例的对比学习方法

SimCLR 包含的构件：Encoder、Projector、图像增强、InfoNCE损失函数。其核心是Encoder，其它所有构件以及损失函数，只是用于训练出高质量Encoder的辅助结构。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014855992.png)

SimCLR最大的贡献，我个人觉得有两个：

1. 一个是证明了复合图像增强很重要；

2. 另外一个就是这个Projector结构。

这两者结合，给对比学习系统带来很大的性能提升，将对比学习性能提升到或者超过了有监督模型，在此之后的对比学习模型，基本都采取了Encoder+Projector的两次映射结构，以及复合图像增强方法。

#### 对比学习在做特征表示相似性计算时，要先对表示向量做L2正则，之后再做点积计算，或者直接采用Cosine相似性，为什么要这么做呢？

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014857813.png)
现在很多研究表明，把特征表示 [公式] 映射到单位超球面上，有很多好处。这里有两个关键，一个是单位长度，一个是超球面。

1. 首先，相比带有向量长度信息的点积，在去掉长度信息后的单位长度向量 [公式] 上操作，能增加深度学习模型的训练稳定性。

2. 另外，当表示向量 [公式] 被映射到超球面上，如果模型的表示能力足够好，能够把相似的例子（比如带有相同类标号的数据）在超球面上聚集到较近区域，那么很容易使用线性分类器把某类和其它类区分开（参考上图）。在对比学习模型里，对学习到的表示向量 [公式] 进行L2正则，或者采用Cosine相似性，就等价于将表示向量 [公式] 投影到了单位超球面上进行相互比较。很多对比学习模型相关实验也证明了：对表示向量进行L2正则能提升模型效果。这是为何一般要对表示向量进行L2正则操作的原因。

#### 好的对比学习系统，应该具备怎样的潜在能力呢？

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014900003.png)
论文“Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere”对这个问题进行了探讨。它提出了好的对比学习系统应该具备两个属性：Alignment和Uniformity（参考上图）。

1. 所谓“Alignment”，指的是相似的例子，也就是正例，映射到单位超球面后，应该有接近的特征，也即是说，在超球面上距离比较近；

2. 所谓“Uniformity”，指的是系统应该倾向在特征里保留尽可能多的信息，这等价于使得映射到单位超球面的特征，尽可能均匀地分布在球面上，分布得越均匀，意味着保留的信息越充分。乍一看不好理解“分布均匀和保留信息”两者之间的关联，其实道理很简单：分布均匀意味着两两有差异，也意味着各自保有独有信息，这代表信息保留充分。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014902706.png)
Uniformity特性的极端反例，是所有数据映射到单位超球面同一个点上，这极度违背了Uniformity原则，因为这代表所有数据的信息都被丢掉了，体现为数据极度不均匀得分布到了超球面同一个点上。也就是说，所有数据经过特征表示映射过程后，都收敛到了同一个常数解，一般将这种异常情况称为模型坍塌（Collapse）。如果对比学习的损失函数定义不好，非常容易出现模型坍塌的情形（参考上图）。

#### InfoNCE损失函数

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014905066.png)
分子部分体现出“Alignment”属性，它鼓励正例在单位超球面的距离越近越好；而分母里的负例，则体现了“Uniformity”属性，它鼓励任意两对负例，在单位超球面上，两两距离越远越好。这种实例两两之间的推力，会尽量让特征均匀得分布在单位超球面上，保留了尽可能多的有用信息。

InfoNCE其实是在 Alignment 和 Uniformity 之间寻找折中点，因为如果只有 Alignment 特性，很明显，模型会快速坍塌到常数解。可以说，所有在损失函数中采用负例的对比学习方法，都是靠负例的 Uniformity 特性，来防止模型坍塌的，这包括 SimCLR 系列及 Moco 系列等很多典型对比学习模型。

InfoNCE损失函数里，有个神秘的温度超参。那么，这个温度超参有什么作用呢？这其实是个好问题。目前很多实验表明，对比学习模型要想效果比较好，温度超参要设置一个比较小的数值，一般设置为 0.1 或者 0.2 。问题是：将这个超参设大或设小，它是如何影响模型优化过程的呢？目前的研究结果表明，InfoNCE是个能够感知负例难度的损失函数，而之所以能做到这点，主要依赖超参。

### Moco V2 基于负例的对比学习：Batch之外添加负例

很多实验证明：在基于负例的对比学习中，负例数量越多，对比学习模型效果越好。

Moco V2是吸收了 SimCLR 的 **Projector** 结构，以及更具难度的**图像增强方法**之后，针对Moco 的改进版本，但是效果比Moco 有明显的提升，所以我们以Moco V2来讲解。

1. Moco V2的下分枝，也由序列的Encoder和Projector两次非线性映射构成，两个构件的模型结构和上分枝对应结构保持一致，但是自身独有一套参数。其中一套模型参数的更新，并不是通过常规的损失函数反向传播来进行梯度更新，而是采用如下的移动平均（Moving Average）机制进行更新 ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014906344.png)。m 一般是较大 （0.9至0.99），这意味着，相对上分枝参数，下分枝的参数变动缓慢而稳定，从随机数值一点一点更新，“小步慢走”地向最优值进行迭代。

2. Moco V2维护了一个较大的负例队列，当对比学习需要在正例和负例之间进行对比计算时，就从这个负例队列里取K个，K数值可以根据需要调整大小，但是已经不局限于Batch Size的限制了。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014907417.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014910053.png)
### SwAV 对比聚类模型：负例隐身术

1. 根据Sinkhorn-Knopp算法，在线对Batch内数据进行聚类

2. 损失函数采用输出向量 z 和Prototype中每个类中心向量的交叉熵![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014912282.png)

3. 对称结构中的对比例子，需要映射到参考示例的类别中。被称为 swapped prediction。![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014913720.png)

SimCLR这种模式，当温度超参设的比较小的时候，容易出现误判的负例，而聚类模型无疑在容忍负例误判方面，天然有很好的包容力，这也许是聚类方法效果好的原因之一。

目前 (2021-04-24) 来看，SwAV和DeepCluster-V2是效果最好的对比学习模型之一。

### BYOL & SimSiam 只用正例，非对称结构

BYOL: 只有正例，在 Moco V2 上增加了 predictor，修改了loss，去掉了负例队列。模型未坍塌，原因不详。BYOL 是目前效果最好的对比学习模型之一。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014914911.png)
SimSiam进一步对BYOL进行了简化，我们可以大致将SimSiam看作是：把BYOL的动量更新机制移除，下分枝的Encoder及Projector和上分枝对应构件参数共享版本的BYOL。从后续文献的实验对比来看，SimSiam效果是不及BYOL的。


![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014917146.png)
### Barlow Twins 只用正例，对称结构

Barlow Twins 既没有使用负例，也没有使用不对称结构，主要靠替换了一个新的损失函数，可称之为“冗余消除损失函数”，来防止模型坍塌。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014919330.png)
#### Barlow Twins的损失函数

Barlow Twins则不然，它对Aug1和Aug2里的正例分别做了类似BN的正则。之后，顺着Batch维，对Aug1和Aug2两个正例表示矩阵做矩阵乘法，求出两者的关联矩阵，其损失函数定义在这个关联矩阵上：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014921521.png)
### Self-supervised 模型比较

论文“How Well Do Self-Supervised Models Transfer?”对13个知名自监督模型，在40多种数据集上进行相对公平地对比测试，得出了一些很有价值的结论。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014922714.png)
从Many-Shot分类的测试角度，这个考察的是自监督模型从ImageNet习得的知识，迁移到其它数据集合的能力。结果可参考上图，从图中数据，我们可以看出，**DeepCluster-v2、SwAV、BYOL**三个模型表现突出，而且基本都超过了监督学习模型的效果。除此外，SimCLR-v2的效果也比较好。这说明对于这些表现优秀的模型，确实能够很好地将某个数据集学习到的知识，迁移到其它数据集。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014924924.png)
上图展示了Few-shot分类的测试效果，结论和 Many-shot 类似，也是 **BYOL、SwAV、DeepCluster-v2** 效果比较突出，但是大多数 Few-shot 分类任务，自监督模型效果不及有监督模型。


除了分类任务，它还测试了物体识别与实例分割等其它类型的任务，总体而言，在这些任务中，**SimCLR-v2 和 BYOL** 模型相对效果比较突出。

### 记录一下我以前不知道的内容（From 知乎）：

1. 对比学习迫使表示模型能够忽略表面因素，学习图像的内在一致结构信息，即学会某些类型的不变性，比如遮挡不变性、旋转不变性、颜色不变性等。

2. SimCLR有两次非线性变换：Encoder、projector。Encoder学习到特征hi后，可进一步将学习到的特征迁移到下游任务projector中。

3. SimCLR看着有很多构件，但最后要的只是Encoder，而其它所有构件以及损失函数，只是用于训练出高质量Encoder的辅助结构。

4. 蒸馏温度可以区分hard负样本，温度系数越小，区分力度越大，但也不能太小，防止把正样本误当成负样本。


## 对比表示学习介绍 2021-05-31

参考：Contrastive Representation Learning [https://lilianweng.github.io/lil-log/2021/05/31/contrastive-representation-learning.html](https://lilianweng.github.io/lil-log/2021/05/31/contrastive-representation-learning.html)

### 对比学习目标函数

##### Contrastive Loss 2005

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014927303.png)
其中，ϵ 是不同类别样本的最小距离阈值，是一个超参数。

##### Triplet Loss 2015

最初在 FaceNet 上提出，用于识别同一个人不同姿势角度的照片。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014928787.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014930250.png)
这里，最重要的是选择比较有挑战性的负样本，来提升模型质量。

##### Lifted Structured Loss 2015

Lifted Structured Loss 使用一个训练批次内所有样本的 pairwise edges 来提升计算效率。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014931437.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014933475.png)
P 包含正样本，N 包含负样本。公式的红色部分会导致局部最优问题，所以可以用如下方程代替。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014934880.png)
同时，文章中提出在 batch 中可以增加复杂的负样本，来提升负样本的质量。

##### N-pair Loss 2016

Multi-Class N-pair loss 将 triplet loss 做了修改，可以用于比较多个负样本。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014935941.png)
如果此处每类中只选择一个负样本，就相当于多分类中的 softmax loss。

##### NCE Loss 2010

Noise Contrastive Estimation, 简称 NCE，是一个估计统计模型参数的方法。主要思想是通过 logistic regression 来将目标数据和 noise 区分开。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014937688.png)
其中，p 是目标分布，q 是 noise 分布。

最初的 NCE loss 如下，

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014938777.png)
这个只针对一个正例和一个负例的情况。在很多后续的工作中，支持多个负例的对比 loss 也会被称为 NCE。

##### InfoNCE Loss 2018

InfoNCE Loss 受到 NCE Loss 的启发，它的主要变更是使用 cross-entropy loss 来从无关的负例中识别正例。

假设负例服从 p(x) 分布，正例服从 p(x|c) 分布。从一个含 N-1 个负例，一个正例的向量 c 中，正确识别正例的概率如下。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014940015.png)
其中，![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014941569.png)

InfoNCE  loss 如下，它优化正确识别正样本的 log probability。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014942800.png)
##### Soft-Nearest Neighbors Loss 2007/2019

Soft-Nearest Neighbors Loss 或者叫 SNN loss，将 InfoNCE loss 拓展到多个正例的场景。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014944173.png)
其中，τ 是温度常数，表述特征在表示空间的聚集程度，B 是类别数目。

##### Soft-Nearest Neighbors Loss 常用设置 Common Setup

1. 通过使用 data augmentation 来创建有差别的正例样本，用以创建 SNN loss 中的 class 和 label 数据。

2. 目前大部分对比学习模型会使用多组正例/负例样本。根据 [Wang & Isola 2020](https://arxiv.org/abs/2005.10242) ，正负例样本需要符合如下关系. 其中 p(x) 是样本对在数据空间的概率分布, p(x,x) 是样本对在数据空间的关联分布。

   1. 对称性：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014945184.png)

   2. 匹配边缘：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014946226.png)

3. 要学习编码器 f(x) 来学习 L2标准化特征向量，对比学学习目标是：![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014947515.png)

### 核心组成部分 Key Ingredients

##### 非常重的数据增强 Heavy Data Augmentation

给定训练样本，需要通过数据增强技术来创建类似的样本，以作为 loss 中的正样本。适当的数据增强对于学习高质量的通用 embedding 特征至关重要。它在不修改语义含义的情况下，向样本中引入不重要的变化，因此可以鼓励模型学习重要部分。

例如，SIMCLR 的实验表明，随机裁剪和随机颜色失真的组件对于学习图像视觉表示的良好性能至关重要。

##### 使用大批次 Large Batch Size

在训练期间使用大批次是许多对比学习方法的成功（例如 SIMCLR，CLIP）的另一个关键成分，尤其是只使用批次内负样本的方法。只有在批次够大时，损失函数才能覆盖多样化的阴性样本，才能让模型学到区分不同的例子的有效表示。

##### 有难度的负样本挖掘 Hard Negative Mining

有难度的负样本和锚定样本有不同标签，但具有非常接近的 embedding 特征。在有真实标签的监督学习场景下，很容易找出特定任务下有难度的负样本。例如，当学习文本的 embedding 时，我们可以将标记为“矛盾”的句子作为有难度的负样本（例如 SIMCSE，或使用 BM25 返回大多关键词匹配的最相关的不正确的候选者（DPR; Karpukhin，2020）。

然而，在无监督学习场景下，找到有难度的负样本非常难。增加训练时的批次大小或内存 bank 尺寸隐含地引入了更多难的负样本，但它也导致了很大的内存使用量。

Chuang et al. (2020) 研究了对比学习中的抽样偏见，提出了debiased loss。在无人监督的环境中，由于我们不知道实际标签，我们可能会意外地抽取到假阴性样本。采样偏见可能会导致显着的性能下降。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014948955.png)

### 视觉：图片 embedding

#### 图片增强 Image Augmentations

在视觉域中的对比表示学习的大多数方法依赖于通过应用一系列数据增强技术来创建样本的噪声版本。增强应显著改变其视觉外观，但保持语义含义不变。

##### 基本图像增强

在保留其语义含义时，有很多方法可以修改图像。我们可以使用以下任何一个增强或多个操作。

1. 随机裁剪，然后调整回原始大小。

2. 随机颜色扭曲

3. 随机高斯模糊

4. 随机颜色抖动

5. 随机水平翻转

6. 随机灰度转换

7. 多作物增强：使用两个标准分辨率作物和样本一组额外的低分辨率作物，覆盖图像的小部分。使用低分辨率作物降低了计算成本。 （SWAV）

8. 还有很多 …

##### 增强策略

许多框架专为学习良好的数据增强策略（即多种变换的组成）。这是一些常见的。

* AutoAugment（Cubuk，et al。2018）：由NAS的启发，自动化框架学习最佳数据增强操作（即剪切，旋转，转换等）的问题，用于图像分类作为RL问题，寻找导致的组合评估集的最高准确性。

* RandAugment（Cubuk等，2019）：Randaugment通过控制单个幅度参数控制不同变换操作的大小来极大地减少自动化的搜索空间。

* PBA（Population based augmentation 基于人口的增强; Ho等，2019）：PBA联合PBT（Jaderberg等，2017）与自动化，使用进化算法并行培训儿童模型的群体，以发展最佳的增强策略。

* UDA（Unsupervised Data Augmentation 无监督的数据增强;谢等，2019）：在一系列可能的增强策略中，UDA选择那些以最小化未标记的示例和其未标记的增强版本之间的预测分布之间的KL发散。

##### 图像混合物

图像混合方法可以从现有数据点构建新的训练示例。

1. Mixup（Zhang等，2018）：它通过创建两个现有图像I1和I2的加权像素组合来运行全局级别的混合。

2. Cutmix（Yun等，2019）：通过将一个图像的局部区域与其他图像的其余部分组合来生成新示例，Cutmix 通过生成新示例来实现区域级混合。

3. MoCHi（Mixing of Contrastive Hard Negatives 混合对比学习困难的负样本; Kalantidis等人。2020）

#### 并行增强 Parallel Augmentation

这类方法产生了一个锚图像的两个噪声版本，并旨在学到这两个增强的样本共享相同的 embedding。

##### SimCLR

SimCLR (Chen et al, 2020) 提出了一个简单的框架，用于视觉表现的对比学习。它通过最大限度地通过潜在空间中的对比损失来最大化同一样本的不同增强视图之间的同步的协议来了解视觉输入的表示。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014951161.png)
SimCLR 对比学习的框架

SimCLR Loss：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014952614.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014953684.png)
##### Barlow Twins

Barlow Twins（Zbontar等，2021）将两个扭曲的样本扭曲到同一网络中以提取特征，并学习在靠近身份的这两组输出特征之间进行关联矩阵。目标是保持一个样本的不同扭曲版本的表示向量相似，同时最小化这些向量之间的冗余。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014954906.png)
Barlow Twins Loss 函数

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014956529.png)
##### BYOL

BYOL (Bootstrap Your Own Latent; Grill, et al 2020) 声称在不使用负样本的情况下实现新的SOTA 结果。它有两个神经网络，分别称为 online 和 target 网络，彼此相互作用和学习。目标网络（由 ξ 参数化）具有与在线架构相同的架构（由 θ 参数化），但是通过 Polyak 平均权重，ξ ← τ ξ + (1-τ) θ。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014957794.png)
#### 记忆库 Memory Bank

在每个批次中计算大量负样本的 embedding 非常耗费资源，一种常见方法是将内存中存储的这些样本的 embedding 以防止数据僵化和降低计算成本。

##### Instance contrastive learning 实例对比学习

实例对比学习（Wu等，2018）通过将每个实例视为自己的独特类别来促使基于类别的监督。它意味着“类”的数量将与训练数据集中的样本数相同。因此，用所有样本来计算 Softmax 层是不可行的，但它可以通过 NCE 近似。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613014959503.png)
##### MoCo & MoCo-V2

InfoNCE loss 1 个正例，N-1 个负例。

##### CURL 2020

#### 特征聚类 Feature Clustering

##### DeepCluster 2018

##### SwAV 2020

#### 在有监督数据集的情况下使用 Working with Supervised Datasets

##### CLIP 2021

##### 有监督对比学习 Supervised Contrastive Learning 2021

### 语言：文本 embedding

#### 文本增强 Text Augmentation

##### 词汇编辑 Lexical Edits

EDA（Easy Data Augmentation 简易数据增强; Wei＆Zou 2019）定义了一组简单但强大的文本增强操作。鉴于句子，EDA随机选择并应用四个简单操作中的一个：

1. 同义词替换（SR）：用它们的同义词替换 n 随机的不间断单词。

2. 随机插入（RI）：在随机位置放置随机选择的句子中的随机选择的不间断字的同义词。

3. 随机交换（RS）：随机交换两个单词并重复 n 次。

4. 随机删除（RD）：随机删除具有概率 p 的句子中的每个单词。


在上下文增强 Contextual Augmentation (Sosuke Kobayashi, 2018) 中，可以从给定的概率分布平滑地采样新的由BERT这样的双向LM预测的替代词。

##### 反向翻译 Back-translation

CERT（Contrastive self-supervised Encoder Representations from Transformers; Fang 等人，2020）通过反向翻译生成增强句子。 可以使用不同语言的各种翻译模型来创建不同版本的增强版。

##### Dropout and Cutoff

根据跨视图训练的灵感，Shen 等人（2020）建议将 cutoff 措施应用于文本增强，他们提出了三项 cutoff 增强策略：

1. Token cutoff 删除了一些选定令牌的信息。为确保没有数据泄露，输入，位置和其他相关嵌入矩阵中的对应令牌都应该归零。，

2. Feature cutoff 删除了一些特征列。

3. Span cutoff 删除了一个连续的文本块。


SimCSE (Gao et al. 2021) 通过将原句子从其通过 dropout 衍生的句子中区分开，来实现无监督的学习。换句话说，它们将 dropout 作为文本序列的数据增强。用不同的 dropout mask 生成两个样本，以此对样本为正例，批次中其他样本就是此样本的负例。它和 cutoff 增强非常相似，但 dropout 更灵活，对屏蔽掉的内容的语义较少明确的限定。


#### 来自自然语言推理的监督 Supervision from NLI

已经发现没有任何微调 (fine-tuning) 的预训练的 BERT 句子 embedding 对语义相似性 (semantic similarity) 任务的表现不佳。因此，相比直接使用原始 embedding，我们需要是通过进一步进行微调来改进 embedding。


自然语言推理（Natural Language Inference，NLI）任务是提供用于学习句子 embedding 的主要有监督数据源，如 SNLI，MNLI 和 QQP。

##### Sentence-BERT

SBERT（Sentence-BERT）（REIMERS＆GUEVYCH，2019）依赖于 siamese 和 triplet 网络架构来学习句子 embedding，使得句子相似度可以通过嵌入对之间的余弦相似估算。请注意，学习 SBERT 取决于监督数据，因为它在几个 NLI数 据集中进行了微调。


##### BERT-flow

BERT-Flow（Li等，2020;代码）通过将 embedding转化到一个平滑和各向同性高斯分布。


#### 无人监督的句子 embedding 学习 Unsupervised Sentence Embedding Learning

##### Context Prediction 内容预测

快速思想（QT）向量（Quick-Thought vectors， Logeswaran＆Lee，2018）将句子表示学习作为分类问题：给定句子及其上下文，分类器根据其向量表示（“cloze test”）区分背景句子从其他对比句子 。 这种方法消除了导致训练放缓的 Softmax 输出层。


##### 相互信息最大化 Mutual Information Maximization

IS-BERT（INFO-CHINESE BERT）（ZHANG等人。2020）基于相互信息最大化的自我监督的学习目标，以便在无人监督的举止中学习良好的句子嵌入。
