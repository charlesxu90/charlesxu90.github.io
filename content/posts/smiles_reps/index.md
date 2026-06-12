---
title: "SMILES 化学表示"
subtitle: ""
date: 2026-04-23
draft: false
author: "Xiaopeng Xu"
description: "SMILES 化学表示简介：分子的字符串表示与常见用法。"
tags: ["SMILES", "Cheminformatics"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

参考：

* SMILES:一种简化的分子语言：[https://www.jianshu.com/p/8c915de5ad4d](https://www.jianshu.com/p/8c915de5ad4d)

* [https://chem.libretexts.org/Courses/University_of_Arkansas_Little_Rock/ChemInformatics_(2017)%3A_Chem_4399_5399/2.3%3A_Chemical_Representations_on_Computer%3A_Part_III](https://chem.libretexts.org/Courses/University_of_Arkansas_Little_Rock/ChemInformatics_(2017)%3A_Chem_4399_5399/2.3%3A_Chemical_Representations_on_Computer%3A_Part_III)

## 简介

SMILES，全称是 Simplified Molecular Input Line Entry System，是一种用于输入和表示分子反应的线性符号。

### 示例

下面看一些例子:

#### 分子表示

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011730158.png)
#### 反应表示

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011732145.png)

### 应用

* 数据库关键字访问

* 研究人员交流化学分子信息

* 化学数据输入

* 人工智能和化学专家的语言

## SMILES 的优点

### 唯一性

SMILES强大的一点就是存在一种唯一的 SMILES，使用标准的 SMILES，分子是唯一的。也比较通用。

### 节省空间

SMILES的另一个重要特性是，与大多数其他表示结构的方法相比，它能节省存储空间。且 SMILES 的压缩非常有效。

## SMILES 的表示规则

SMILES 表示法由一系列不包含空格的字符组成。 可以省略氢原子（氢抑制图）或不省略氢原子（氢完全图）。芳香结构可以直接指定或以 Kekulé 形式指定。

有五种通用的 SMILES 编码规则，对应于原子、键、分支、闭环和断开的规范。

### 原子 Atoms

1. 原子用它们的原子符号表示：这是 SMILES 中唯一需要使用的字母，每个非氢原子由其括在方括号 [] 中的原子符号独立指定。

2. B，C，N，O，P，S，F，Cl，Br 和 I,如果连接的氢原子数量和原子的最低正化合价相同，则[]可以省略。

3. 双字符符号的第二个字母必须以小写字母输入。

4. 芳香环中的原子由小写字母表示,脂肪族碳由大写字母C表示，芳族碳由小写字母c表示

以下原子符号是有效的SMILES符号:

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011733636.png)
在括号内，必须始终指定连接的氢原子数量和原子当前的化合价。氢的数量用符号 H 表示，后跟可选数字。类似地，化合价由符号+或 - 之一表示，后跟可选数字。如果未指定，则对于括号内的原子，就假定连接的氢和电荷的数量为零。[Fe +++]形式的构造与[Fe + 3]形式同义。 例子是：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011735100.png)

### 键 Bonds

1. 单键，双键，三键和芳香键分别用符号 - ，=，＃和：表示。

2. 假设相邻原子通过单键或芳香键相互连接（可以总是省略单键和芳键）。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011736850.png)
 对于线性结构,SMILES和传统的图解符号相比,只是省略了H和单键,例如6-羟基-1,4-己二烯可有许多同等有效的SMILES代表，包括以下三 种：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011738558.png)

### 分支 Branches

1. 带有分支的原子写在左侧，通过()指定，可以堆叠。分支上的元素写在右侧

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011739799.png)

### 闭环 Cyclic structures

通过在每个环中断开一个键来表示环状结构。 该键以任何顺序编号，在每个闭环时紧跟原子符号后用数字表示开环（或闭环）键。这就让一个连接起来的非循环图使用上述三个规则写为非循环结构。 环己烷是一个典型的例子：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011741568.png)
通常同一个闭环有不同的有效 SMILES

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011742787.png)
如果需要，表示环闭合的数字可以重复使用。例如，数字1在规范中使用了两次：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011744063.png)

### 断开 

1. 断开的化合物被写成由`.`分隔的单独结构,列出离子或配体的顺序是任意的。

2. 如果需要，可以将一种离子的SMILES嵌入另一种离子中。

如苯酚钠的实例所示

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011745289.png)
由点 `.` 分隔的相邻原子意味着原子彼此不键合 


### 化学异构 Stereo-chemistry

这里介绍用于指定同位素的SMILES规则，关于双键的配置和手性。术语异构体SMILES统称为使用这些规则编写的SMILES。SMILES异构体规则允许为任何结构完全指定手性，因此，SMILES 中的所有异构体规范规则都是可选的。缺少任何属性的规范意味着未指定该属性的值。


#### 同位素规则

同位素规范是指在原子符号前面用一个数字表示所需的原子质量的数目。原子质量只能在括号内指定。例如：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011746536.png)

#### 围绕双重建的配置

双键周围的配置由`/`和 `\` 指定，它们是“方向键”，可以被认为是单键或芳香键（例如默认键）的种类。 这些符号表示连接原子之间的相对方向性，并且只有当它们出现在两个双键连接的原子上时才有意义。 例如，以下SMILES均适用于E-和Z-1,2-二氟乙烯。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011748314.png)
SMILES手性惯例与其他手段（如CIP）之间的一个重要区别是 SMILES 使用局部手性表示（与绝对手性相反），下面举例说明：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011749542.png)

#### 四面体规范- 四面体中心周围的配置

SMilES 使用基于局部手性的非常普遍的手性规范。取代使用基于规则的编号方案来排序手性中心的邻近原子，取向基于邻居在SMILES字符串中出现的顺序

最简单和最常见的手性是四面体，四个相邻原子在一个中心原子上均匀排列，称为“手性中心”。如果所有四个邻居以不同的方式彼此不同，则该结构的镜像将不相同。这两个镜像被称为“对映体”，是一个四面体中心的唯一的两种形式。如果两个（或多个）四个邻居彼此相同，则中心原子将不是手性的（它的镜像可以叠加在空间中）。

在SMILES中，四面体中心可以用一个简化的手性规范（@或@@）来表示，这是一个原子属性，它遵循手性原子的原子符号。如果手性规范不存在于手性原子中，则其手性不指定。例如：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011751062.png)

从氨基 N 到手性 C（如 SMIELS 所写），其他三个邻居按照它们写在顶部 SMILES 中的顺序逆时针出现，N[C@](C)(F)C(=O)O（甲基-C，F，羧基-C），在底部顺时针， N[C@@](F)(C)C(=O)O。 符号“@”表示以下邻居是逆时针列出的 “@@”表示邻居是顺时针列出的（反时针方向）。

如果中心碳不是 SMILES 中的第一个原子并且具有附着的隐含氢（它可以具有至多一个并且仍然是手性的），则隐含的氢被认为是跟随的三个邻居的第一个邻近原子。如果中心碳首先出现在SMILES 中，则隐含的氢被认为是“来自”原子。 氢可以总是明确写出（如[H]），在这种情况下，它们被视为与任何其他原子一样。在每种情况下，隐含的顺序与 SMILES 中的顺序完全相同。一些有效的丙氨酸 SMILES 是：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011752809.png)
环闭合键的手性顺序由环闭合数字出现在手性原子上的词汇顺序暗示（不是“取代基”原子的词汇顺序）。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011754620.png)
## SMILES公约

除上述规则外，SMILES中普遍使用少量约定。这里简要讨论

### 氢 Hydrogen

在为大多数有机结构编写SMILES时，通常不需要指定氢原子。氢的存在可以通过三种方式指定：

1. 对于没有括号指定的原子，从正常的价假设。

2. 在括号内，通过提供的氢计数明确计数；如果未指定，则为零。

3. 作为显式原子……[H]原子。


“有机”和“无机” SMILES 命名法之间没有区别。可以指定任何 SMILES 中任何原子的连接氢的数量。例如，丙烷可以作为[CH3][CH2][CH3]而不是CCC输入。


有四种情况需要明确氢气规范的规范：

1. 带电的氢，即质子，[H+]

2. 与其他氢连接的氢，例如分子氢，[H][H]

3. 氢连接到除另一个原子以外的氢

4. 同位素氢规格，例如在重水中，[2H]O[2H]


### 芳香性 Aromatics

SMILES 算法使用 Hueckel 规则的扩展版本来识别芳香分子和离子。为了具有芳香性，环中的所有原子必须是 sp2 杂化的，并且可用的“过量”p电子的数量必须满足 Hueckel 的 4N+2 标准。例如，苯写成c1ccccc1，但C1=CC=CC=C1-环己三烯（Kekulé形式）的条目导致芳香性的检测并导致内部结构转换为芳香族表示。相反，c1ccc1和c1ccccccc1的条目将产生环丁二烯和环辛四烯的正确抗芳香结构，C1=CC=C1和C1=CC=CC=CC=C1。在这种情况下，SMILES 系统寻找一种结构，该结构保留隐含的sp2杂交，隐含的氢计数和指定的正式电荷（如果有的话）。但是，某些输入可能不仅是不正确的，而且也是不可能的，例如c1cccc1。这里c1cccc1不能转化为C1=CCC=C1，因为其中一个碳原子是sp3，带有两个连接的氢。在这种结构中，不能进行交替的单键和双键分配。SMILES系统会将此标记为“不可能”的输入。请注意，以下列表中的原子只能被视为芳香族：C，N，O，P，S，As，Se和*（通配符）。此外，环外双键不会破坏芳香性。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011756360.png)
重要的是要记住，SMILES芳香性检测算法的目的仅仅是为了化学信息表示！


### 键约定 Bond

SMILES没有规定应该使用哪种化合价来模拟分子结构。事实上，使用 SMILES 的一个优点是它能够描述相同结构的各种价模型。可以连接原子并根据需要显示电荷分离。例如，硝基甲烷可以在 SMILES 中表示为 CN(=O)=O 或电荷分离 C[N+](=O)[O-] (我们倾向于使用前者用于数据库工作，因为它保持对称性)。两者都是“正确的”，因为它们代表了物质的不同的，有用的模型。一般来说，当对称性不成问题时，大多数化学家更喜欢电荷分离结构，如果它们可以避免代表处于不寻常价态的原子，例如，重氮甲烷写成 C=[N+]=[N-] 而不是 C=[N]=[N]。


### 互变异构体 Tautomers

在 SMILES 中明确指定了互变异构结构。没有“互变异构键”，“移动氢”，也没有“移动电荷”规范。选择一种或所有互变异构结构留给使用者并且很大程度上取决于应用。给定一种互变异构形式，如果需要，大多数化学信息系统将报告所有已知互变异构体的数据。SMILES 的作用是确切地指定请求哪种互变异构形式，以及哪些有数据。一个简单的例子，有两种可能的互变异构形式，如下所示：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011757807.png)

## SMILES 规范

SMILES把分子结构表示为 任意的手性特征图，这本质上就是分子描述分子结构的二维图片。仅仅描述分子图（即原子和键，没有手性或者同位素信息）的 SMILES 叫做一般 SMILES。对于给定的结构，通常有很多一般 SMILES 表示方法；规范化算法用于在所有有效可能性中生成一个特殊的通用 SMILES，这个特殊的 SMILES 叫做唯一的 SMILES；用同位素和手性规格书写的 SMILES 叫做异构体 SMILES；唯一的异构体 SMILES 叫做绝对 SMILES。看下面的例子

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011759496.png)
## SMILES 的局限性

SMILES 是专有的，它不是一个开放项目。 这导致不同的化学软件开发人员使用不同的 SMILES 生成算法，从而导致同一化合物产生不同的 SMILES 版本。 因此，从不同数据库或研究小组获得的 SMILES 字符串是不可互换的，除非它们使用相同的软件生成 SMILES 字符串。 为了解决 SMILES 的这种互换性问题，一个开源项目已经启动，以开发一种名为 [OpenSMILES](http://opensmiles.org/) 的 SMILES 语言的开放标准版本。然而，该领域最引人注目的社区努力是 InChI 的开发。
