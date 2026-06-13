---
title: "AI 在药物研发中的应用（讲座）"
subtitle: ""
date: 2021-11-06
draft: false
author: "Xiaopeng Xu"
description: "AI 在药物研发中的应用（讲座）相关笔记。"
tags: ["AI for Drug Discovery", "Lecture"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 总结

这个讲座，对于系统认识 AI 药物设计领域非常有帮助。核心的流程包括：生成、活性评估+RL、成药性筛选+RL、合成、测试、反馈。其中，生成用 AI model，评估用物理模型+AI，合成可以通过计算 retro-syntehsis path 来实现，测试用 AI 实验室，反馈是对实验结果做分析。

AI 在这个过程中，有多个应用点，核心是 生成和 RL优化。此外，活性预测、成药性预测、逆合成分析也很有应用价值。

我今年主攻的是生成，生成的应用点包括：从头分子生成、官能团替换和骨架跃迁。第一个已经比较熟悉，另外两个问题需要再调研下。另外，在优化（optimization）生成方向上，这篇文章没有多讲，只是在流程中提到强化/迁移学习。这块也得再多熟悉下。

指导性比较强，但离我现在的实践还比较远。短期内不打算深入物理模型+AI。先把 生成 + docking 做活性分析做好。


## 背景信息

晶泰科技首席科学家 张佩宇 讲座


晶泰科技(XtalPi)是一家世界领先的以计算驱动创新的药物研发科技公司，基于最前沿的计算物理、量子化学、分子动力学、人工智能与云计算等技术，为全球创新药企提供快速、精确的智能化药物研发科技，从而显著提高药物发现与发展关键环节的效率与成功率，降低研发成本，最终为患者带来更多优质高效的药物。


张佩宇博士，晶泰科技首席科学家，中国科学院博士，深圳市高层次人才。张佩宇博士曾任大连化学物理研究所副研究员，从事量子动力学方法和计算化学算法的开发工作，2015年加入晶泰科技，目前担任新药事业部总负责人。


从业以来，张佩宇博士一直致力于人工智能和高精度物理模型在新药研发中的应用，特别是在药物发现、晶型研究等领域的源头创新，在国际知名期刊发表论文四十余篇，申请专利二十余项。


作为晶泰科技ID4智能药物研发平台的缔造者，张佩宇博士带领团队将人工智能、高精度计算化学等前沿技术与专家经验及先进实验技术相结合，创造了深入结合产业需求，高效推动研发项目的创新研究路径，赋能全球药企，成功加速数十个新药管线达到里程碑。

## 新药研发寒武纪

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030642300.png)
## “高悬的果实”

* 借助 AI，可以更快的找到更好、更新、更难的药物。获取“高悬的果实”。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030647591.png)
## 全球 AI 药物研发现状

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030650319.png)
### 头部药企的 AI 布局

* 头部的 AI 制药企业包括诺华和阿斯利康。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030653827.png)
### 阿斯利康 AI 应用效果

* 50%小分子药应用 AI，效率提升70%，成功率 31%

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030657381.png)
## AI 的核心因素

* AI 三要素：数据、算法和算力

* 研发铁三角：人脑智能、智能计算、智能实验

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030700130.png)
### AI 技术突破有望改变药物研发

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030703309.png)
### AI 药物研发相关的突破性进展

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030706126.png)
* 核心突破：AlphaFold2，有很大价值，但还不能直接应用于大分子设计。小分子设计？

## 药物应用蓝图

* 分子生成-> scaffold network分析 -> 评估：物理模型模拟活性 -> 评估：AI 模型预测活性 -> RL 和 transfer learning 优化 -> 成药性过滤 -> 合成测试 -> 验证反馈 

## ![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030708519.png)

## 药物生成

* 从头分子生成、官能团替换、骨架跃迁。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030711358.png)
## 药物评估

### 物理模型

物理模型计算活性准确，精度高。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030714199.png)
### 物理模型案例-预测活性、选择性

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030717494.png)
### 案例-评估 hERG

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030720211.png)
### 案例- ABFE 预测骨架活性

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030723321.png)

### 案例- 评估溶解度

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030726289.png)


### 物理模型 vs AI 模型

* AI 模型速度高，物理模型解释性好

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030729069.png)
## 药物合成和验证

### 智能计算和智能实验的迭代模式

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030731822.png)
### 药物合成和验证相关应用

* 通过分子合成 synthesis，来指导智能实验，实现 AI 自动化验证。提升效率，支持洞见。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030735158.png)
## 晶泰科技 AI 药物研发场景

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030737744.png)
## 相关案例

* 其研发平台已经进入工业化阶段，已有多个药物研发管线正在进行。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030741196.png)
### 案例一：first in class 药物

* 合作方识别 PPI 靶点及配体结合口袋，晶泰科技计算 PPI 界面“热点”氨基酸残基，并发现 hits 和 leads。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030743561.png)

### 案例二：best in class 药物

* 13 个月内获得了活性、选择性和成药性较好的化合物，有很好的抑制作用。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030746721.png)
## 参考资料

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030749447.png)
