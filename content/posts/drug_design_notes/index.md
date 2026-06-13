---
title: "药物设计笔记"
subtitle: ""
date: 2021-06-27
draft: false
author: "Xiaopeng Xu"
description: "药物设计笔记相关笔记。"
tags: ["Drug Design"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 导论

### 概述

#### 创新药物发现—从基因到药物

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031127380.png)

#### 药物 R&D

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031130004.png)
#### 药物设计 3W

* Why?

   * Unmet medical needs

   * Time-scale

   * Success rate

* What? 

   * Disease mechanism-Target identification & validation 

   * Lead generation

   * Lead optimization

* How?

   * Drug Design --The application of CADD in drug design

   * Bioinformatics, proteomics, Combi Chem/HTS

   * Target-drug interaction mode

   * Early ADME/T evaluation

#### 药物设计内涵：药物研究模式的转变

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031132901.png)
Lee JA, Berg EL. J Biomol Screen. 2013 Dec;18(10):1143-55

##### 药物研究模式的转变

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031135416.png)

#### 药物设计外延：相关学科的进步

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031137614.png)
#### 药物设计学课程简介

* 2001年率先在全国开设

* 全国第一本药物设计学教材

* 第一本计算机辅助药物设计教学参考书 l 2012年上海市精品课程

* 全国知名，有较大影响力

* 小班化授课

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031139825.png)
##### 教材

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031142452.png)
##### 辅助教材

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031144616.png)

### 基本原理

#### 受体理论（靶点学说）

靶点：药物发挥药效，需与机体内具有特定功能的生物大分子结合

* 一种有效的药物应符合以下两项要求：

   * **作用于靶点**（与机体内的某一种或多种靶点发生相互作用）（**药效学**要求）

   * **暴露于靶点**（药物到达靶点，达到适宜的浓度并维持足够的时间 AUC）（**药代动力学**要求）

##### 药物靶点的分类：

* 受体、酶、离子通道、细胞因子、核酸、脂质、糖蛋白…

#### 药物-受体相互作用理论

##### 锁钥原理，互补性

* 活性位点：药物结合在受体的部位

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031147143.png)
##### 诱导契合理论

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031149388.png)
##### 分子识别

药物通过分子间作用力（可逆）与靶点相结合，某些药物可以形成共价键（不可逆）。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031152043.png)
* 键合类型

   * 离子键

   * 氢键

   * 范德华力

   * 螯合作用

   * 电荷转移

   * 偶极-偶极作用

   * 卤键

   * 阳离子-pai

   * 共价键

* 结合动力学

   * ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031154007.png)

#### 一、小分子相似性 Similarity

定义：相似的化学结构具有相近或相关的活性

经典药物化学的基石：生物电子等排、药效团、肽拟似物、过渡态类似物、酶自杀性底物、优势结构……

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031155201.png)

##### “相似性”——Activity Cliff？

相似结构具有不同的活性

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031157017.png)
不同结构具有相似的活性

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031159037.png)
#### 二、多样性 Diversity

* 药物分子的多样性

   * 天然产物

   * 新合成化合物

   * 组合化学

* 药物靶点的多样性

   * 靶点类型的多样性

   * 靶点结构的复杂性

多样性是药物化学与药物发现在化学方面所要解决的基本问题

##### 同一靶点含多个结合口袋与不同分子结合

结构多样性抑制剂与微管蛋白复合物的单晶衍射图

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031200483.png)
GDP 结合部位周围三种结合口袋

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031202629.png)
Nature Reviews Cancer, 2004, vol4, 253.

##### 同一靶点的同一口袋可与结构多样性的分子结合

胆碱能神经损伤甲说的乙酰胆碱酯酶与不同药物的结合

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031204654.png)
### 先导化合物的发现途径

#### 先导化合物发现的两条途径

##### 筛选途径的药物发现

* 天然产物提取分离与结构鉴定

* 随机筛选/偶然发现

* 组合化学/高通量筛选/虚拟筛选

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031206751.png)

##### 合理药物设计

* 靶点学说

* 基于结构的药物设计(SBDD) 

   * 直接药物设计

   * 间接药物设计

* 成药性设计: 靶点暴露(药代/药动要求)：类药性，结构/性质的关系

* 基于片段的药物设计 ( FBDD)

#### 合理药物设计

##### 靶点学说

* 药物与靶点相互作用 

* 靶点的发现

* 靶点的验证

* 靶点结构的确证

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031208551.png)
#### 基于结构的药物设计 Structure based drug design

* 直接药物设计 direct drug design

   * 基于受体三维结构![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031210773.png)

* 间接药物设计 indirect drug design

   * 基于配体三维结构![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031213031.png)

#### 先导化合物的成药性设计优化

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031215012.png)
配体性质：溶解度、分子大小、渗透性、氢键、酸碱性、立体异构

#### 基于片段的药物设计 (Fragment Based Drug Design, FBDD)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031216818.png)
##### FBDD protocol

A real-world evolvement of de novo drug design

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031219099.png)
##### 通过FBDD途径发现的临床在研新药

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031221347.png)
#### 假阳性问题

* PAINS: (pan-assay interference compounds)

   * 2013年的一项研究发现了七种在筛选时能够与超过三分之一蛋白质发生作用的干扰化合物，但是这 篇论文并未得到应有的关注。一个典型的学术药物筛选数据库中往往有5~12%的化合物属于PAINS

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031223350.png)
### The Long Path from Idea to Drug

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031226683.png)

### Qualification for Drug Hunters

* **Professional training**

   * Medicinal Chemistry

   * Biochemistry & Organic Chemistry & Physical chemistry & Analytical Chemistry 

   * Pharmacology

   * Chemical Biology

   * Rational Drug Design & CADD & Structural Biology

* **Specialized disease knowledge**

* **Technical Savvy**


## 靶点

### 靶点的概念

#### 乙酰水杨酸的发现及研究历程

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031229955.png)
##### 阿司匹林作用机制的阐明

1971年 阿司匹林的作用机制阐明: 不可逆抑制 cyclooxygenase (COX) 活性

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031231905.png)
#### 靶点的概念 (The Concept of Drug Target)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031233398.png)
Strebhardt, K, et al. Nat Rev Cancer, 2008 Jun;8(6):473-80.

### 靶点的假设

#### 靶点理论 (Hypothesis of Drug Target)

* 对药物的要求:

   * 与靶点发生相互作用(药效学要求); 

   * 暴露于靶点，药物到达靶点、达到适宜的浓度 (Cmax) 且/或维持足够长的时间 AUC(药代动力学要求); 

   * 减少脱靶(off-target)效应

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031236138.png)
#### 仿制药一致性评价

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031237860.png)

### 靶点的分类

#### 靶点分类 (Classification of Drug Targets)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031239797.png)
#### 药物靶点举例

##### 细胞膜受体


![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031241541.png)
##### 靶酶

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031243371.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031245321.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031247702.png)


### 靶点的要求

#### 靶点的要求 (Relevance of Drug Targets)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031249379.png)
* 可成药性 (Druggability) -- 最重要

   * 该靶点或靶点所属类型已有代表性治疗药物上市

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031251143.png)
### 经典与现代药物发现

#### 经典药物发现 -- Observation driven

神农尝百草

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031252405.png)
* 化学家提供化合物，生物学家利用组织、细胞或动物进行筛选；

* 生物学家根据所关注的表型挑选‘活性’化合物；

* 可确定作用机制(但非必要)；

* 项目的起点通常为先导化合物或者某一病理或生理现象

##### 缺点

* 确定作用机制比较困难或者存在滞后的问题;

* 筛选策略、关键路径随机偶然问题; 

* 药物化学家对先导进行构效关系分析及结构优化时比较困难

* 药物作用的分子机制不明确

* 筛选通量较低

* 药物发现的关键取决于先导化合物及疾病模型表型

#### 经典药物发现 -- Hypothesis-driven

Folkman, J. Nat Rev Drug Discov. 2007 Apr;6(4):273-86.

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031253891.png)
* 生物化学家利用纯化蛋白(靶点) 对化合物进行亲和力筛选；

* ‘苗头’化合物通过体外功能检测 确立；

* 通过疾病动物模型评估药物作用；

* 项目的起点通常为假设的疾病靶点

##### 缺点

* 所选‘靶点’的成药性问题;

* 先导化合物的发现成功率低且成本极高;

* 对于‘脱靶效应’的预测能力不及预期

* 研究的对象为‘药物-靶点’关系而非‘药物-疾病’关系

* 标准化、简单化，同一靶点需要面对更激烈的同行竞争

* 药物发现的关键取决于靶点的成败


## 基于结构的药物设计 (SBDD)

### 概述

#### 基本思想

是根据配体 (ligand)，即外源性小分子药物或内源性活性物资，与生物体内的靶点 (target) 相互作用产生生物活性，从而治疗靶点相关的疾病。

#### 基本原理

基于受体与配体的“锁-钥”原理，即配体像一把钥匙，通过形状、化学性质等互补匹配受体活性位点的锁芯，从而使受体-配体紧密结合。

#### 分类

##### 基于**受体结构**的药物设计 (**receptor** structure-based drug design)

直接设计(direct design)方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031256115.png)

##### 基于**配体结构**药物设计 (**ligand** structure-based drug design)

间接设计(indirect design) 方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031300315.png)
#### 源于 SBDD 的治疗药物

20 世纪 90 年代，很多 SBDD 研发的新药上市

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031302613.png)

#### 计算机辅助药物设计 (CADD) 基本策略与流程

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031304441.png)
### 基本理论、技术和方法

#### 基本理论

##### 药物受体相互作用理论——受体理论

一种有效的药物必须符合以下两个要求:

1. 与机体内的某一种或多种分子靶点发生相互作用(药效学要求)

2. 到达靶点(药动学要求)

##### 核心概念

* 靶点：生物大分子，能识别和结合生物活性的分子，并产生生物效应

* 受体：能识别和结合生物活性物质，并产生生物效应

* 内源性活性调节物与受体的相互作用是维持机体机能的基本生理学机制

* 外源性药物可以作用在受体而干预生理生化作用

* 受体激动剂 (agonist)：启动了受体的生物学功能，如一些内源性物质

* 受体拮抗剂 (antagonist)：药物与受体结合后阻碍了内源性物质与受体 结合，而导致生物作用的抑制

##### “锁-钥”原理

* 空间形状契合

* 相互作用力契合

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031306740.png)

##### “诱导契合”原理

* 配体构象变化

* 受体构象变化

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031308205.png)
##### 计算机模拟过程中的应用

计算机模拟过程中，也是从刚性对接到柔性对接的过程：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031310009.png)
#### 药物-靶点相互作用力的类型

分子识别 (molecular recognition)：生物分子之间发生特殊的、专一性的相互作用，通过分子间相互作用力(interaction force)而结合。

##### 三种主要受体-配体相互作用类型

* 静电作用

* 氢键

* 疏水作用

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031311705.png)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031313789.png)
##### 共价键 (covalent bond):

* 键能高，约140~800 KJ / mol，结合牢，不可逆;高活性，缺乏特异选择性，驻留时间较长，治疗指数高，能克服耐药性

##### 范德华力 (van der Waals Force, VDW)

* 相邻的电中性原子之间存在的微弱的吸引力，它由瞬间偶极引起，极性分子和非极性分子都存在着这种力

* 主要的分子间作用力

* 原子间距离为0.3~0.5 nm，范德华力的能量为1.9 KJ / mol

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031315264.png)

##### 疏水键 (hydrophobic bond):

* 两个不溶于水的分子间的相互作用

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031316738.png)

##### 氢键 (hydrogen bonding)

* 重要的生物大分子-药物作用方式

* 氢原子与负电性杂原子共价结合后，与另一具有未共用电子对的杂原子形成一种弱的静电引力，键能约5 KJ / mol。

* 形成氢键需要有氢键供体 (hydrogen bond donor, HD) 和氢键受体 (hydrogen bond acceptor, HA) 

* 氢键相互作用 (X, Y一般为N, O, F), ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031318276.png)

   * X—Y距离 < 3.5 Å 

   * X—H-----Y三原子形成的角度 > 60°


##### 静电作用(electrostatic interaction)

* 离子键(ionic bonding)

* 偶极-偶极(dipole-dipole interaction)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031319539.png)
##### 电荷转移作用(charge transfer interaction)

* 通过供体分子的电子从最高占据分子轨道(HOMO)转移到靶点分子的最低空缺分子轨道(LUMO)

##### 螯合作用 (chelation)

* 是由含有二个或二个以上供电子基团(配体)的化合物 (通称螯合剂, chelator) 与金属离子通过离子键、共价键或配价键相连接，形成环状结构的螯合物的过程

* 二齿配位体 (bidentate); 三齿 (tridentate) 或多齿配位体 (polydentate)

### 分子三维结构的理论计算方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031321067.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031322756.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031324236.png)
* **量子论：**原子中的电子只能处于包含基态在内的定态上，电子在两个定态间跃迁改变它的能量，同时辐射出一定波长的光，光的波长取决于定态之间的能量差。

* **量子力学：**研究微观粒子运动规律的理论。用波函数描写粒子的运动状态，以薜定谔方程确定波函数的变化规律，并对各物理量进行计算。

* **量子化学：**以量子力学的基本原理和方法来研究化学问题的学科。可计算分子的各种参数，如分子结构、电子结构、系统总能量和各个轨道信息。

#### 三种量子化学计算方法

* 从头计算法 (Ab initio) 

* 密度泛函方法 (DFT) 

* 半经验计算法 (Semi-imperical)


##### 从头计算法 (Ab initio methods)

* 以基本物理常数以及元素的原子序数，不借助于任何经验参数，求解薜定谔方程 (Schrōdinger Equation): Ĥψ(r) = E ψ(r)

* 计算结果精度高，可靠性大，但是计算量极大，消耗计算机时太多

* 从头计算法的软件有 Gaussian，SPARTAN 等

##### 密度泛函方法 (Density Function Theory, DFT)

* 用电子密度取代波函数做为研究的基本量，其将电子能量分为几个部分，动能、 电子-核相互作用、库仑排斥，以及其余部分的交换相关项，所有项只是电子密度的函数。

##### 半经验计算法 (Semi-empirical methods)

* 采用实验值拟合的经验参数，大大提高计算速度，计算精度较差

* 半经验计算法的软件有: MOPAC 和 AMPAC 等

##### 量子化学计算的优缺点

* 优点：

   * 可计算出分子的理化参数、分子结构的电子结构，几何构型和易与亲电试剂或亲核试剂反应的部位

* 缺点：

   * 只适用于计算分子量较小分子，计算时间长

#### 分子力学 (Molecular mechanics)

##### 力场方法 (Force field methods)

* 基于经典牛顿力学方程的一种计算分子的平衡结构和能量的方法，来研究分子体系的结构和性质

* 计算量小，分子力学可研究包括成千上万个原子的分子体系， 包括有机小分子、生物大分子

* 场总能量，即分子总能量 = 键合作用 + 非键作用


分子力学计算时采用的一套参数和方程进行体系总能量计算

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031325461.png)

* 成键相互作用(bonded interaction)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031326968.png)

   * 键的伸缩、弯曲和扭转

* 非键相互作用(non-bonded interaction)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031328742.png)

   * 静电作用和范德华作用

为了确定分子低能构象，就需要求解与其相对应的分子势能面上的极小值，这一过程称为能量优化(energy minimization)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031330450.png)

##### 分子力学能量优化算法

* 最陡下降法(SD) 一阶

* 共轭梯度法(CG) 一阶

* 牛顿-拉普森法(Newton-Raphson) 二阶

* BFGS(Broyden、Flecher、Goldfarb和Shanno)方法 二阶

##### 分子力学计算的优缺点

* 优点

   * 可计算出分子的总能量 

   * 计算速度快

* 缺点

   * 计算优势构象时易于陷于局部最小的能量 

   * 不能计算与化学键形成和断裂相关的体系

#### 量子力学和分子力学混合方法 (QM/MM)

* 将量子力学方法 (QM) 的准确性和分子力场方法 (MM) 的高效性有机地结合在一起对体系进行不同尺度的计算;

* 该方法基本思想是用精确的量子力学处理感兴趣的化学反应中心，如酶和底物的结合位点，该部位划分为 QM 区域，其余部分如酶以及其它溶液环境区域用经典分子力学来处理，划分为 MM 区域

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031331961.png)
#### 分子动力学 (molecular dynamics)

* 分子动力学是研究分子构象及其它性质随时间变化的重要工具。

* 分子动力学是在分子力学的基础上描述分子运动随时间演化的方法

* 分子动力学在由分子体系的不同状态构成的系综中抽取样本，从而计算体系的构象和能量，并以此为基础计算体系的热力学量和其他宏观性质。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031334363.png)
##### 分子动力学计算的优缺点

* 优点：

   * 可给出体系的动态信息，用于研究生物大分子结构和功能的关系， 给出药物与靶点作用的动态信息。

* 缺点：

   * 计算结构的准确性取决于选择正确的力场和参数值。

### 分子模型技术

* 名称：

   * 计算机分子模型技术, computer aided molecular modeling, CAMM 

   * 分子模型技术 computerized molecular modeling, CMM 

   * 分子模拟 molecular modeling，MM 

* 利用计算机图形学进行分子模拟的技术

* 为三维结构研究的有效手段——利用计算机来构造、显示、分析和贮存复杂的分子模型，提供直观的分子立体形象，观察分子间的相互作用

#### 表示分子结构的实体模型

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031336132.png)

#### 分子结构的计算机分子模型

* 以各种不同的方式显示

* 在屏幕上随心移动分子

   * –围绕假定的轴旋转

   * –翻转并移向某个部位

   * –可使特定的键转动

* 在屏幕上随心操作分子

   * 剪裁、连接、装配、组合、建造、叠合 

* 计算分子的性质

   * 原子间距、角度、分子体积、表面积、分子形状

   * 分子的电子特性、氢键、供体/受体或带电基团的性质 

* 显示分子间的相互作用

#### 分子三维结构的展示方式（多巴胺为例）

* 线、棍、球棍、线和表面、表面![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031338849.png)

* 网状表面、不透明实体、半透明体、分子周围等电子密度、等静电势![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031341134.png)

* Homo 轨道、LUMO 轨道![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031343506.png)

#### 生物大分子结构的表示方式（多巴胺受体为例）

* 线形、缎带、卡通![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031345715.png)

* 上方缎带，下方表面![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031348205.png)

* 缎带卡在膜上，线型展示活性区域![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031350989.png)


* 蝎毒

   * 静电表面![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031352880.png)

   * 结合后的展示![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031355026.png)

* 其他几种毒素![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031357935.png)

* 立体显示技术![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031400629.png)

### 直接药物设计 (Direct Drug Design)

* 直接药物设计是指基于受体结构的药物设计

   * Direct drug design = structure-based drug design (SBDD)

   * The structure of the target protein should be known.

   * The location of the active site should be known.

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031403322.png)

#### 直接药物设计方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031405659.png)

### 全新药物设计 (De novo drug design)基本流程

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031408317.png)
#### 一、活性位点分析 active site analysis

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031410092.png)
#### 二、分子对接 Molecular Docking

分子对接:将配体分子放置到受体大分子的活性位点中，预测小分子与受体结合构象及作用能的过程

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031412813.png)
* Docking is most often used to predict favorably docked complexes between a receptor and a ligand.

* Given a drug-like molecule, will it fit into the binding site and is it predicted to bind better or worse than another molecule.![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031414316.png)

##### 分子对接原理

* 根据几何匹配和能量匹配，寻找两个分子之间最佳相互作用模式

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031415874.png)
* Receptor: enzyme, ion channel, antibody... 

* Ligand: drug, peptide, antigen, polysaccharide... 

* Receptor-Ligand Interactions: electrostatic interaction, hydrogen bond, hydrophobic interaction... 

##### 分子对接核心步骤

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031417955.png)


* 搜索算法

   * 搜索配体与受体的可能结合模式

      * 配体的可能构象

      * 配体在活性位点的可能取向

* 打分函数

   * 对配体与受体的结合模式进行打分寻找最合理的结合

      * 经验打分函数

      * 能量打分函数 

      * 一致性打分(Consensus Score)

##### 分子对接的分类

* 刚性、半柔性、柔性

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031419755.png)

##### 分子对接的难点

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031421865.png)

Problem in docking :

* You have one or more molecules and you want to see how and how strongly they might bind to a particular receptor.

* In order to speed the calculations, the energy is often pre-calculated on a grid that is later used as a lookup table.

* Issues such as ligand and protein flexibility, and method for scoring are the most serious ones

##### 通过分子对接进行虚拟筛选 (Docking of Ligands: In Silico Virtual Screening)

分子对接可进行虚拟筛选， 它将三维数据库中的小分子放置于受体的活性部位，搜寻配体合适的取向和构象，使得配体和受体的形状和相互作用的匹配最佳，进而利用打分函数打分。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031423901.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031426300.png)

#### 三、基于活性位点构建药效团模型

* 结合部位认定的自动分析方法:

   * 利用探针分析活性位点的结构，即用探针原子或基团探测能与靶点产生较好相互作用的部位

   * 主要软件: Sybyl; Discovery Studio; Schorodinger

* “负片”映射:![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031428503.png)

### 基于片段的药物设计 (Fragment Based Drug Design, FBDD)

#### 1、小分子化合物库的建立

* 化合物拆分的11种键![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031430002.png)

#### 2、活性小分子片段的筛选技术

* NMR技术

* X-射线单晶衍射

* 高浓度筛选

* 表面等离子共振技术

* 热漂移检测

* 恒温滴定量热法

* 干涉测量法

#### 3、活性小分子片段的筛选过程

* **初步筛选：**这一步筛选需要迅速缩小筛选范围，因此选择具有高通量性质的利用等温滴定量热仪( ITC )方法比较合适，利用ITC可以将待筛选化合物迅速缩小;

* **特异性结合的确认验证：**主要是基于核磁共振技术来验证小分子片段与靶点的结合是否是特异性的，只有特异性的结合才能进入下一步筛选;

* **鉴定和表征：**利用X-Ray单晶衍射法或者恒温滴定热量法来一一分析小分子片段与靶点的相互作用，从中筛选出活性最好的先导化合物进行下一步优化

#### 4、活性片段的优化和组装

* (1) 片段连接法![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031431307.png)

* (2) 片段自我组装法![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031433041.png)

* (3)片段优化法![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031434542.png)

* (4)片段生长法![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031436004.png)


### 全新药物设计对配体的要求

* 结合状态中呈稳定的构象

* 分子具有柔性

* 易于合成，避免过多的手性中心

#### 全新药物设计的优缺点

* 优点

   * 配体结构可能是全新的，不受现有知识的约束,也不受人的思维束缚

   * 该方法既可用于先导化合物的发现，也可用于对先导化合物的结构优化

* 缺点

   * 可能只是理论分子，仅对接有效，且可能不易合成

### 间接药物设计 (Indirect Drug Design)

* Indirect drug design - drug design based on structures and activities of inhibitors, not on the structures of the receptors!

   * The basic molecular structures of the inhibitors must be known.

   * The active conformation of the compounds must be determined

#### 间接药物设计方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031437740.png)
#### 一、基于配体药效团模型的药物设计

##### 药效基团模型法 (Pharmacophore modeling)

* 对一系列活性化合物进行3D-QSAR研究，并结合构象分析，得出该类药物的药效基团模型。

* 可在受体三维结构未知的情况下，构造出虚拟的药效基团模型，再由此出发，进行药物设计。

##### 基于配体的药效基团 (ligand-based pharmacophore)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031439943.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031441422.png)
* 药效团是药效基团 (pharmacophoric elements) 单元的集合

* 药效基团单元——组成药效基团所共有的一组原子(团)

* 药效基团单元中的原子或官能团可通过氢键、静电作用、范德华作用和疏水键等与受体中活性位点发生结合

* 药效基团中的药效基团单元往往用点来定义，若干个点构成平面或空间的结构

##### 药效基团的表征

* 阿片类止痛药的非骨架型药效基团![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031443093.png)

* 多巴胺的药效基团![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031444690.png)

##### 药效基团的获取 (Pharmacophore perception)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031446201.png)
* 多巴胺活性小分子药效团![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031447704.png)

##### 药效基团识别的方法

* 1. 分子叠合

   * 处于同一区域的药效基团单元![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031450007.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031452632.png)

   * 简化方法:最强活性化合物的优势构象![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031454312.png)

   * 简化方法:刚性药物模板

      * 右旋氯筒箭毒碱——N2受体拮抗剂![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031456038.png)

* 2. 活性类似物法(Active Analogue Approach, AAA)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031457760.png)

#### 二、基于配体相似性的虚拟筛选 (ligand similarity-based virtual screening)

##### 基于药效基团的三维结构搜寻

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031459229.png)
##### 虚拟筛选的优缺点

* 优点：

   * 有可能迅速获得化合物的样品进行生物活性测定

* 缺点：

   * 受限于已有的知识

   * 所筛选的化合物库中未必有适合给定靶标的配体分子  

#### 三、基于定量构效关系 (QSAR) 的药物设计

* 定量构效关系 (Quantitative structure-activity relationship, QSAR) —— 揭示一组化合物的生物活性与其分子结构特征之间的相互关系，以数学模型表达和概括出量变规律，以此设计新的化合物

   * 活性 = f (分子或片断性质)

* Quantitative Structure Activity Relationships (2D and more recently 3D).

* Attempts are made to identify (non)linear relationships that exist between physical and/or chemical properties and activity (inhibition).

   * Chemical properties: **logP, hydrophobicity/hydrophilicity, frontier molecular orbitals (HOMO, LUMO), solubility/free energy of hydration, pKa(s)**, etc.

##### QSAR 分析方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031501254.png)
##### 药物设计中的数据统计方法

广泛使用计算机的计算和人工智能

* 人工智能 —— 计算机科学中研究使计算机能够模仿智能的某些方面，如识别 、推理、演绎、从经验中学习的能力以及从不完全的信息中进行推理的能力。![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031504206.png)

* 数据统计中广泛使用的计算和人工智能![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031505940.png)

##### 3D-QSAR (Three-Dimensional Quantitative Structure-Activity Relationships) 方法

* 拟合出药物的理化和三维结构参数与药效的定量关系，以此关系设计新的化合物

##### 3D-QSAR的基本流程

1. 计算一系列化合物的优势构象，并求出药效构象

2. 计算化合物与环境的作用能

3. 计算作用能与活性的关系，并以图形表达计算结果

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031507646.png)
##### 作用能的计算方法

* 测定探针与化合物的相互作用能， 以确定化合物分子周围各种作用力 场(空间场和静电场)的空间分布

* 探针:Csp3, C+![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031510281.png)

##### 比较分子力场分析法 (Comparative Molecular Field Analysis, CoMFA) 

* CoMFA is a widely-used tool for 3D-QSAR

* 3-D QSAR approaches use statistical methods to **correlate** the **variation** in biological or chemical activity with information on **3-D structure** for a series of compounds

* The underlying idea of the CoMFA is that differences in a target property (e.g. biological activity) are often closely related to equivalent changes in the shapes and strengths of the non-covalent interaction fields surrounding the molecules

* The CoMFA methodology ultimately allows one to design and predict activities of molecules.


* 比较分子力场分析法 (CoMFA) 测定探针与化合物的相互作用能![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031512372.png)

* CoMFA 结果的表达形式![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031514202.png)

* 

##### 比较分子相似性指数分析法 (Comparative Molecular Similarity Indices Analysis, CoMSIA) 

* CoMFA的扩展方法

* 分子场的计算采用5种不同的相似性场计算:

   * 立体场

   * 静电场

   * 氢键场(包括氢键供体和氢键受体)

   * 疏水场

* 由于力场考虑更全面，三维构效模型更优

##### 3D-QSAR 的优缺点

* 优点

   * 不必知道靶点的结构

   * 不必输入实验测定或理论计算的理化参数值

   * 给出可视图易于解释 QSAR 结果

   * 不限于研究相似分子结构，只须有相同的药效团以相似的方式与靶点作用

   * 可预测新分子的活性，而不必先合成

* 缺点

   * 预测仅限于由训练集包络的空间之内

   * 不能可靠地预测出原模型范围之外的取代基结构 

   * 分析的准确性取决于采用的空间结构

## 先导化合物性质设计优化

### 1. 药物的基本性质

#### 有效性

* 与靶点相互作用 (基于结构的药物设计)

* 到达作用部位且达到有效浓度 (合理的药动学性质)

#### 安全性

* 与非靶点作用

* 分布、结合、代谢 (药动学性质问题)

#### 药代动力学(PK)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031516595.png)
#### 新药开发失败的主要因素

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031519215.png)
* Prentis RA, et al. Br J Clin Pharm, 1988, 25, 387. 

* Kola I, Landis J. Nat. Rev. Drug Discov, 2004, 3, 711.

#### 研发早期性质评价

* 在可行性分析阶段，以适宜的药动学特征作为先导化合物优化的目标

* 在非临床开发阶段，以成药性作为候选药物评价的指标

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031521111.png)
#### 基于性质的药物设计

* **基于性质的药物设计(Property-Based Drug Design, PBDD)：**针对先导化合物或候选药物的结构进行药代动力学性质的设计与优化，以实现先导化合物或候选药物的良好口服吸收 (A)、定向分布 (D)、 可控代谢 (M)、优化消除 (E) 或降低毒性和不良反应 (Tox)。

* 基于性质的药物设计优化的最终目标：获得具有合理药代动力学性质的候选药物。

### 2. 构动关系和药动基团 (SPR and Kinetophore)

* 构动关系 (Structure-Pharmacokinetics Relationship, SPR): 化合物的结构特征和理化性质与其 ADME 特征和药动学性质之间的关系。

* 结构-性质关系 (Structure-Property Relationship, SPR)

* 药动基团 (Kinetophore)：化合物分子中影响ADME特征和药动学性质的结构部分或官能团。

#### 药动基团举例：β1受体拮抗剂

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031523393.png)

   * 亲水性，胃肠吸收较差

   * CNS副作用小

   * 主要经肾脏排泄

   * 中长效

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031524894.png)

   * 亲脂性，易吸收

   * 能透过血脑屏障 (BBB)，中枢副作用

   * 经肝脏代谢，首过效应

   * 短效

* ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031526407.png)

   * 酯酶水解

   * 超短效

### 3. 药物宏观性质与药动学性质的关系

#### 建立药动学性质与药物宏观性质的关联

基于表型的药物发现 (Phenotype-based drug discovery, PBDD)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031528170.png)
##### 药物的宏观性质与PK性质

* 分子量：反映分子大小的参数，与透膜吸收和代谢有关

* 水溶性：口服吸收的前提，氢键可增加化合物的水溶性

* 亲脂性：亲脂性有利于跨膜被动扩散

* 离解性：与溶解性和透膜性密切相关

* 柔性：反映分子形状的重要参数

* 极性表面积：比氢键更能反映分子极性的真实情况

#### 药物的宏观性质之一、分子量

**分子量**是**选取先导物和临床候选药物**的重要因素，对于提高新药研制的成功率**有重要意义**


* 分子量大的化合物，功能基团多，增加了与受体结合的机会和强度

* **分子量过大影响化合物的水溶性**，且被动扩散过程中难以渗透生物膜上脂肪链有序紧密排列的磷脂双分子层，**不利于透膜和吸收**

* **分子量大的化合物可能含有易被代谢的基团和毒性结构**，不适宜作为先导物


上市口服药物/临床候选药物的分子量分布 (1985-2000年)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031530424.png)
Wenlock MC. J Med Chem, 2003, 46, 1250.

#### 药物的宏观性质之二、水溶性

**水溶性**是口服吸收的前提条件，是穿透细胞膜的必要条件。


* 氢键可**增加化合物的水溶性**。

* 化合物只有在氢键破坏后才能渗透磷脂双分子层，因此，**氢键数过多不利于从水相经被动扩散**分配到磷脂层。

* 水溶性影响候选药物在体内外的活性筛选质量

* 水溶性影响制剂的选择和质量


##### 示例：增加氢键，提高水溶性

* 屠呦呦——2015年诺贝尔生理学与医学奖![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031532266.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031534026.png)

#### 药物的宏观性质之三、亲脂性

适宜的亲脂性有多层次的贡献：

* **药效：**亲脂性基团或片断参与同靶标的结合;

* 药代动力学：**整体药物的亲脂性可影响透膜(穿透细胞膜磷脂层)**; **与血浆蛋白结合；组织分布(脂肪组织蓄积)**；**穿越血脑屏障的能力**; **代谢稳定性**;

* **生物药剂学**：影响药物分子在剂型中的溶出度、分散度以及制剂的稳定性。

* **LogP** 和 **LogD7.4**

上市口服药物的亲脂性比较

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031536282.png)
##### 示例：增加亲脂性，提高透脑率

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031538223.png)
#### 药物的宏观性质之四、离解性

离解性是化合物在介质中携带电荷的能力，与**溶解性**和**过膜性**密切相关


* 增加化合物的离解性增加了极性，提高水溶解度;

* **呈离解态的物质不利于过膜**：强酸或季铵盐不利于过膜；碱性过强也难以穿越 BBB

* **可离解药物在不同 pH 环境下离解态和中性分子比例不同**

* ***pKa***


##### 示例：pKa对透膜性的影响

* 苯巴比妥在生理 pH 下以分子形式存在，才能透 BBB 起效![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031539767.png)

#### 药物的宏观性质之五、柔性

分子柔性是**反映分子形状**的重要参数，在优化改造中要权衡利弊


* 增加柔性有利于分子与不同靶点发生结合。

* **分子柔性过高，不利于分散在水性环境中，也不利于透膜**。

* 分子柔性参数通常用**可旋转键数目 (RB)**表示。


##### 可旋转键 (Rotatable Bonds，RB)

* 可旋转键：与非末端的非氢原子连接的非环单键

* 酰胺 C-N 单键、磺酰胺 S-N单键不可旋转

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031541514.png)
#### 药物的宏观性质之六、极性表面积

极性表面积 (Polar Surface Area, PSA) 是分子中极性原子表面的总和；**比氢键更能反映分子极性的真实情况**。


* 根据分子结构计算获得的极性表面积也称为**拓扑极性表面积 (tPSA)**

* PSA越大，分子越难以过膜，吸收性越差

* **口服非 CNS 药物：PSA ≤ 140Å^2**

* **CNS 药物：PSA ≤ 90Å^2**

##### 极性表面积与吸收性的关系

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031543035.png)
### 4. 类药性与经验规则

#### 类药性(Drug-likeness)

**类药性是理想化药物应具有的良好性质**，是药物所表现出来的**结构特征**(如氢键供/受体、环结构、可旋转键数目等)和**理化性质**(如相对分子质量、脂水分配系数等)**在体内的综合反映** (ADME/T 性质)。

* **类药性**是对**理想药物结构**的要求

* **类先导性 (Lead-likeness)**是对**先导化合物结构**的要求

#### Lipinski规则——五倍率 (Rule of Five， Ro5)

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031544785.png)

* 相对分子质量 MW ≤ 500

* 计算脂水分配系数 CLogP ≤ 5

* 氢键供体数 (NH+OH) ≤ 5

* 氢键受体数 (N+O) ≤ 10

当不符合上述两项及以上规则时，化合物可能会出现口服不吸收及透生物膜能力差的问题。

Lipinski CA, et al. Adv Drug Delivery Rev, 1997, 23, 3.

##### 五倍率的适用性

* 仅适用于被动转运的情况

* 对抗生素、抗真菌药、维生素及强心苷等具有主动转运特征的药物不适用

* 五倍率成为药物发现和虚拟筛选的标准环节

#### Veber 规则

与大鼠口服生物利用度相关的规则——五倍率的补充:

* 可旋转键数目 (Rotatable bonds) RB ≤ 10 或分子中环的数目 rings ≤ 4

* 极性表面积 (Polar surface area) PSA ≤ 140Å^2 或氢键总数(供体和受体) ≤ 12

Veber DF, et al. J Med Chem, 2002, 45, 2615.

##### 可旋转键 (Rotatable Bonds，RB)

* 可旋转键：与非末端的非氢原子连接的非环单键

* 酰胺 C-N 单键、磺酰胺 S-N单键不可旋转

* 可旋转键数与分子柔性相关，影响药物吸收

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031547041.png)
#### 其他规则

Lipinski CA. Drug Discovery Today: Technologies 2004, 1, 337.

##### Clark’s BBB rules:

* N+O ≤ 6

* PSA ≤ 90Å2

* MW ≤ 450

* LogD = 1-3

* CLogP-(N+O)>0

##### Rule of 3 (Lead-like):

* N+O ≤ 3

* NH+OH ≤ 3

* MW ≤ 300

* CLogP ≤ 3

* RB ≤ 3

### 5.成药性的概念及其体内外评价方法

#### 类药性与成药性的概念

——郭宗儒. 药物分子设计的策略: 药理活性与成药性. 药学学报 2010, 45 (5): 539−547


* **类药性 (Druglikeness)** 代表了理想化药物所具有的特点, 是药物所表现出来的结构特征（如环结构、可选转键数目等）和理化性质（如相对分子质量、脂水分配系数等）在体内的综合反映（ADME/T性质）。

* 类药性是对**理想药物**结构的要求；类先导性是对先导化合物结构的要求。


* **成药性 (Developability)**是药物除药理活性以外，**与药代动力学和安全性 (PK/T) 相关的所有其他性质**, 是化合物能够进入临床 I 期试验的特征指标。 成药性是对**药物或候选药物**(Candidate)属性的要求。

#### 成药性 (Developability)

决定候选药物是否能够转化为临床应用药物的性质

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031548809.png)
#### 成药性测定方法

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031551088.png)
#### 成药性优化

* **成药性**是药物所表现出来的**结构特征**和**理化性质**在体内的综合反映(包括**药动学性质和毒性**)。

* 成药性的表观性质是药代动力学和安全性，但归根结底是由分子的结构特征所决定。

* 成药性优化的根本，实质上是**化学结构的优化**。

### 6.CYP450 抑制作用与药物毒性

#### 细胞色素P450家族同工酶

细胞色素氧化酶P450(Cytochrome P450 proteins，CYP450)

* 一组结构和功能相关的超家族基因编码的同工酶，由**血红素蛋白、黄素蛋白 (NADPH-细胞色素C还原酶)及磷脂**三部分组成。

* 主要存在于肝脏细胞平滑肌内质网内，也称肝微粒体混合功能氧化酶。

* 在还原状态下可与CO结合，在波长450nm处有特征强吸收峰而得名。

#### 细胞色素P450同工酶的功能

细胞色素氧化酶P450(Cytochrome P450 proteins，CYP)

* 参与体内内源性物质(如脂肪酸、维生素、胆酸)和外源性物质(如药物)的**代谢**，主要**负责化合物体内的氧化、还原和水解3种I相代谢反应**，使它们易于从体内排出。

* P450酶系被认为已经存在了350万年，在细菌、真菌及动植物中都能发现其存在。

#### 细胞色素P450酶的命名

* 族：40%以上的同源性，族用阿拉伯数字表示，如CYP1、CYP2

* 亚族：55%以上的同源性，亚族用大写英文字母表示，如CYP1A、CYP2D 

* 具体的酶：用阿拉伯数字区分，如CYP1A2、CYP2D6

#### CYP450酶的特点

* 特异性低

* 活性有限

* 个体差异大

* 可被药物诱导或抑制

#### CYP450酶的临床意义

* 底物竞争性抑制

* 非线性药代动力学(安全性小) 基因多态性，个体化治疗

* 药物代谢性相互作用

#### 与药物代谢相关的 CYP450 酶

* 涉及药物代谢的主要为 **CYP1、CYP2、CYP3** 家族，约占肝脏总 CYP450酶 的70%

* 7 个重要的 CYP450：**CYP1A2、CYP2A6、CYP2C9、 CYP2C19、CYP2D6、CYP2E1和CYP3A4**

* 承担了CYP450酶系 90% 的功能和作用，参与了70%的药物代谢，肠道 I 相代谢 70% 由**CYP3A4** 催化

#### 细胞色素P450的抑制类型

* **竞争性抑制：**两种药物都是同一个酶的底物时，会产生底物之间的竞争，抑制彼此的代谢

* **机制基础抑制：**也叫自杀性抑制，如大环内酯类经CYP3A4代谢，代谢物可与P450分子中的血红蛋白中的亚铁形成亚硝基烷烃复合物而失活

* **非选择性抑制：**指药物对多个同工酶都有抑制作用，缺乏选择性。如西咪替丁可以同时抑制CYP1A2、CYP2D6、CYP3A4

#### 针对P450的药物改造实例(1)

##### 防止 CYP3A4 代谢的结构修饰，降低肝毒性

* 阿莫地喹![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031554344.png)

* 奈法唑酮![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031555657.png)

##### 阻断代谢位点，提升代谢稳定性

* 去掉甲苯磺丁脲中的苯甲基，极大提高了代谢稳定性![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031557456.png)

* 引入氟封闭代谢位点，去除易代谢的官能团，替换不稳定基团 ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031559460.png)

   * **重磅炸弹药物**

### 7.hERG毒性及药物优化策略

#### hERG简介

* 在心肌细胞中，hERG (human Ether-a-go-go Related Gene) 编码钾通道蛋白 (Kv11.1)，该蛋白介导一种延迟整流钾电流 (IKr)。

* 抑制心肌细胞中的hERG会诱发获得性QT间期延长综合症 (LQTS)，导致严重的心律失常。

* 目前，检测化合物对hERG钾通道的作用已是临床前评价化合物心脏安全性的关键步骤，也是美国食品药品管理局 (FDA) 和欧洲药品评价局 (EMEA) 等管理机构要求的新药报批必备资料，以此规避药物心脏毒性的风险。

#### 药物心脏毒性的机制及应对

* 药物引起QT间歇延长的主要机制: 

   * 1. 直接抑制 hERG 钾通道蛋白

   * 2. 阻碍 hERG 钾通道蛋白的转运

* 降低药物hERG毒性的主要策略: 

   * 1. 降低脂溶性

   * 2. 降低碱性，增加酸性

   * 3. 构象限制

##### 降低药物hERG毒性实例(1) - A2A受体拮抗剂先导化合物

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031601452.png)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031602701.png)
##### 降低药物hERG毒性实例(2)- 非索非那定
