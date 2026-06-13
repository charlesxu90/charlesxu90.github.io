---
title: "图深度学习：成果、挑战与未来"
subtitle: ""
date: 2020-11-20
draft: false
author: "Xiaopeng Xu"
description: "图深度学习：成果、挑战与未来相关笔记。"
tags: ["GNN", "Deep Learning"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

**本文最初发表在 TowardsDataScience 博客，经原作者 Michael Bronstein 授权，InfoQ 中文站翻译并分享。**

**2020-01-15**

**来源：**[https://towardsdatascience.com/deep-learning-on-graphs-successes-challenges-and-next-steps-7d9ec220ba8](https://towardsdatascience.com/deep-learning-on-graphs-successes-challenges-and-next-steps-7d9ec220ba8)

来自一个系列：[https://towardsdatascience.com/graph-deep-learning/home](https://towardsdatascience.com/graph-deep-learning/home)

## **引言 & 介绍**

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031632982.png)

图深度学习，也称为几何深度学习（Geometric deep learning，GDL）【1】、图表示学习（Graph representation learning，GRL）或关系归纳偏置（Relational inductive biases）【2】，最近已成为机器学习中最热门的主题之一。虽然关于图学习的早期研究至少可以追溯到十年前【3】，甚至是二十年前【4】，但无疑由于过去几年的进步，让这些方法从一个小众[成为机器学习社区的焦点](https://twitter.com/prlz77/status/1178662575900368903)，甚至是大众科学媒体的焦点（《量子杂志》（Quanta Magazine）刊登了一系列关于几何深度学习的优秀文章，用于[流形研究](https://www.quantamagazine.org/an-idea-from-physics-helps-ai-see-in-higher-dimensions-20200109/)、[药物发现](https://www.quantamagazine.org/machine-learning-takes-on-antibiotic-resistance-20200309/)和[蛋白质科学](https://www.quantamagazine.org/new-machine-learning-system-decodes-how-proteins-interact-20200603/)）。

图是一种强大的数学抽象，可以描述从生物学、高能物理学到社会科学和经济学等领域的复杂关系和互动系统。由于目前在这些领域中产生的图结构数据量巨大（最突出的例子是像 Twitter 和 Facebook 等社交网络），因此，在这些领域中尝试应用深度学习技术是非常诱人的，这些技术在其他数据丰富的环境中取得了显著的成功。

图学习问题有多种类型，这些问题在很大程度上与应用相关。一种是节点问题和图问题之间的二分法，前者尝试预测图中单个节点的属性（例如，识别社交网络中的恶意用户），而后者则试图预测整个图（例如，预测分子的溶解度）。此外，与传统的机器学习问题一样，我们可以区分有监督和无监督（或自监督）设置，以及直推式（Transductive）和归纳式（Inductive）问题。

与图像分析和计算机视觉中使用的卷积神经网络类似，对图进行高效学习的关键是设计具有共享权重的局部操作，在每个节点与它的邻居之间进行消息传递【5】。与处理网格结构数据的经典深度神经网络的一个主要不同之处在于，在图上，这种操作是置换不变（Permutation-invariant）的，即与邻近节点的顺序无关，因为通常没有对它们进行排序的规范方法。

尽管它们的前景光明，并已有一系列图表示学习的成功案例（其中，我出于私心地举出 [Twitter 收购 Fabula AI](https://blog.twitter.com/en_us/topics/company/2019/Twitter-acquires-Fabula-AI.html) 的案例，Fabula AI 是一家由我和我的学生一起创立的基于图的假新闻检测初创公司），但到目前为止，我们还没有见过任何类似卷积网络在计算机视觉领域取得同等成功的案例。在本文中，我将试着概述一下我对可能原因的看法，以及该领域在未来几年将如何取得进展。

## 数据 Benchmark

像 ImageNet 这样的**标准化基准**无疑是计算机视觉领域深度学习成功的关键因素之一，有些人甚至认为【6】，在深度学习革命中，数据比算法更重要。在图学习社区中，我们在规模和复杂性方面还没有类似 ImageNet 的东西。2019 年推出的 [Open Graph Benchmark](https://ogb.stanford.edu/) 或许是朝着这一目标的首次尝试，试图在有趣的现实图结构化数据集上引入具有挑战性的图学习任务。其中一个障碍是，由于对 GDPR 等隐私法规的担忧，科技公司不愿分享数据，他们从用户的活动中生成了多样而丰富的图。一个值得注意的例外是 Twitter，它在一定的隐私保护限制下，向研究界提供了由 1.6 亿条推文组成的数据集以及相应的用户参与度图作为 [ResSys 挑战赛](https://recsys-twitter.com/)的一部分。我希望，未来有很多公司也会效仿 Twitter 的做法。

## 软件库 library

公共领域中可用的**软件库**在深度学习“民主化”和使其成为流行工具方面发挥了最重要的作用。如果说直到最近，图学习的实现主要是一些编写得很烂、几乎没有经过测试的代码，那么现在有些库，如 [PyTorch Grometric](https://pytorch-geometric.readthedocs.io/en/latest/) 或 [Deep Graph Library](https://www.dgl.ai/)（DGL），是在行业赞助的帮助下，由专业人士编写并维护。每当在 arXiv 上出现新的图深度学习架构，数周之后，就可以看到它的实现，这种情况并不少见。

## 要点：可伸缩性 & 动态图

**可伸缩性**是限制工业应用程序的关键因素之一，这些应用程序通常需要处理非常大的图（想想 Twitter 社交网络，它有数亿个节点和数十亿条边）和低延迟约束。直到最近，学术研究界几乎忽略了这一方面，文献中描述的许多模型完全不适合大规模的设置。此外，图硬件（GPU）与经典的深度学习架构的完美结合是推动它们共同成功的主要力量之一，但它不一定是图结构数据的最佳选择。从长远来看，我们可能需要专门用于图的硬件。

**动态图**是文献中很少提及的另一方面。虽然图是对复杂系统建模的一种常用方式，但这种抽象通常过于简单，因为现实世界中的系统是动态的，并且随着时间的推移而变化。有时是时间行为提供了关于系统的重要见解。尽管近年来取得了一些进展，但是设计能够有效地处理标识为节点或边时间流的连续时间图的图神经网络模型，仍然是一个有待研究的问题。

众所周知，**高阶结构**如 motifs、graphlets 或 simpleicial complexes 在复杂网络中具有重要意义，例如描述蛋白质交互作用在生物学中的应用。然而，大多数图神经网络只限于节点和边。将这种结构纳入到消息传递机制中，就可以为基于图的模型带来更多的表达能力。

人们对图神经网络表达性的**理论认识**是相当有限的。在某些情况下，使用图神经网络能够显著提高性能，而在其他设置中几乎没有什么差别，这种情况很常见。因为目前还不完全清楚什么时候以及为什么图神经网络运作良好或失败。这个问题很难解决，因为我们必须同时考虑底层图的结构以及图上的数据。对于仅涉及图连通性的图分类问题，最近的研究表明，图神经网络等价于 Weisfeiler-Lehman 图同构检验【8】（一种用于解决图论中一个经典问题的启发式方法，即确定两个图在其节点的排列上是否完全相同）。这个形式主义解释了为什么，例如，图神经网络在非同构图的实例上失败，而这些实例不能通过这个简单的测试来区分。如何在保持低线性复杂度的同时，超越 Weisfeiler-Lehman 测试层次结构，使图神经网络如此具有吸引力，这是一个有待研究的问题。

图神经网络在存在噪声数据或收到对抗性攻击时的**健壮性和性能保证**【9】是另一个有趣的研究领域，基本上还是一片处女地。

## 应用 Application

**应用**可能是该领域中最令人满意的部分。自从事图学习工作多年以来，我已经与粒子物理学家【10】、临床医生【11】、生物学家和化学家【12】结下了深厚的友谊，要不是我们致力于各自领域的应用，我很可能不会遇到他们。

如果让我只押注一个领域的话，鉴于图深度学习可能在未来几年产生最大影响，我会押注**结构生物学**和**化学**。在这些领域，基于图的模型既可以作为分子的低层模型【5】，也可以作为分子之间相互作用的高层模型【13,11】。将这些结合起来可能是达到对制药行业有用的水平的关键——我们看到了这方面的初步迹象，在今年早些时候，图神经网络被用于发现一类新的抗生素 u【14】或预测蛋白质之间的相互作用【12】。如果图深度学习实现了它的诺言，那么发现、开发和测试新药这一传统上极其漫长而昂贵的过程有可能永远和以前不一样了。

## 参考文献

【1】M.M.Bronstein 等人：《[几何深度学习：超越欧几里得数据](https://arxiv.org/abs/1611.08097)》（Geometric deep learning: going beyond Euclidean data），2017 年，《IEEE Signal Processing Magazine 》34(4)：18–42。

【2】P. Battaglia 等人：《[关系归纳偏置、深度学习和图网络](https://arxiv.org/abs/1806.01261)》（Relational inductive biases, deep learning, and graph networks），2018 年，arXiv：1806.01261。

【3】F. Scarselli 等人：《图神经网络模型》（The graph neural network model），2008 年，IEEE Transactions on Neural Networks 20(1)：61–80。

【4】A. Küchler、C. Goller：《基于结构驱动递归神经网络的符号域归纳学习》（Inductive learning in symbolic domains using structure-driven recurrent neural networks），1996 年，Proc. Künstliche Intelligenz。

【5】J. Gilmer 等人：《[量子化学中的神经信息传递](https://arxiv.org/abs/1704.01212)》（Neural message passing for quantum chemistry），2017 年，ICML。

【6】A. Wissner-Gross：《[算法上的数据集](https://www.edge.org/response-detail/26587)》（Datasets over algorithms ），2016 年。

【7】C.-Y. Gui 等人：《[图处理加速器研究综述：挑战与机遇](https://arxiv.org/pdf/1902.10130.pdf)》（A survey on Graph Processing accelerators: Challenges and Opportunities），2019 年，arXiv：1902.10130。

【8】K. Xu 等人：《[图神经网络有多强大？](https://arxiv.org/abs/1810.00826)》（How powerful are graph neural networks?），2019 年，ICLR。

【9】D. Zügner 等人：《[针对图数据神经网络的对抗性攻击](https://arxiv.org/abs/1805.07984)》（Adversarial attacks on neural networks for graph data），2018 年，Proc. KDD。

【10】N. Choma 等人：《[用于 IceCube 信号分类的图神经网络](https://arxiv.org/abs/1809.06166)》（Graph neural networks for IceCube signal classification ），2018 年，ICMLA。

【11】K. Veselkov 等人：《[HyperFoods：十五中抗癌分子的机器智能测绘](https://www.nature.com/articles/s41598-019-45349-y)》（HyperFoods: Machine intelligent mapping of cancer-beating molecules in foods），2019 年，Scientific Reports 9。

【12】P. Gainza 等人：《[利用几何深度学习解读蛋白质分子表面相互作用指纹](https://www.biorxiv.org/content/10.1101/606202v1)》（Deciphering interaction fingerprints from protein molecular surfaces using geometric deep learning），2020 年， Nature Methods 17：184–192。

【13】M. Zitnik 等人：《基[于图卷积网络的多重用药副作用建模](https://arxiv.org/abs/1802.00543)》（Modeling polypharmacy side effects with graph convolutional networks ），2018 年， Bioinformatics 34(13)：457–466。

【14】J. Stokes 等人：《抗生素发现的深度学习方法》（A deep learning approach to antibiotic discovery），2020 年，Cell，180(4)。

**作者介绍：**

Michael Bronstein，伦敦帝国理工学院教授，Twitter 图机器学习研究负责人，CETI 项目机器学习领导、Twitter 图机器学习负责人、研究员、教师、企业家和投资者。
