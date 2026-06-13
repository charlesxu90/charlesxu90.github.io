---
title: "AI 在药物研发中的应用"
subtitle: ""
date: 2021-04-15
draft: false
author: "Xiaopeng Xu"
description: "AI 在药物研发中的应用相关笔记。"
tags: ["AI for Drug Discovery"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Response to: AI has dispointed on Covid

Geeks piled in when the pandemic broke but great promise has not been fulfilled.

### Need:

   * Data & Method

### Result

* CS: ChEMBL 

* Wet lab: Examining the data from the ChEMBL SARS-CoV-2 drug repurposing screens

### Sources of data: Instrumental to the development of ML algorithms

* Frank et al., In vitro screening of a FDA approved chemical library reveals potial inhibitors of SARS-CoV-2 replication

* Tesia et al., Discovery of synergistic and antagonistic drug combinations against SARS-CoV-2 in vitro

* Bernhard et al., Indentification of inhibitors of SARS-CoV-2 in-vitro cellular toxicity in human (Caco-2) cells using a large scale drug repurposing collection 

### ML methods: COVID-motivated trends

* De-novo design: not relevant due to time constraints

* Virtual screening: limited to safe compounds

* Combinations are crucially important

* Tight integration of biology and chemistry

## Presentations

### Learning the language of viral evolution and escape -- Bonnie Berger (MIT, Science)

#### Problem: Viral escape

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030558175.png)
#### Alergy: Grammar & sematic change

#### Novel approach: learn both "grammaticality" and "semantics" using lanaguage model

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030600081.png)
#### Results: 

##### Learn viral sequence patterns

Learn "semantic embeddings" of viral sequences

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030602441.png)

##### Zero-shot prediction of escape mutations

Model not trained on known escape mutations

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030605087.png)

##### State-of-the-art preformance across viruses

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030607566.png)
##### Towards therapeutics and vaccines: identify target regions less prone to escape

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030609748.png)
Language modelling can shed light on those parts of a protein not prone to escape

#### Software: viral language learning

[https://github.com/brianhie/viral-mutation](https://github.com/brianhie/viral-mutation)

### Casual network models of SARS-CoV-2 and ageing for drug repurposing -- Caroline Uhler (MIT, Nature communication)

### Graph neural netwoks for COVID-19 drug repurposing

#### Problem: Never-before-seen disease

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030611980.png)
#### Problem: How to represent COVID-19? Map SARS-CoV-2 targets to the human interactome

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030614136.png)
##### COVID-19 subgraph

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030616343.png)![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030618515.png)
Gordon et al. expressed 26 of the 29 sars-cov-2 proteins and use ap-ms to identify 332 human proteins to which viral proteins bind.

[https://www.nature.com/articles/s41586-020-2286-9](https://www.nature.com/articles/s41586-020-2286-9)

##### Key insight: subgraphs

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030620353.png)
**Idea: Use the pradigm of embeddings to operationalize the concept of closeness in pharmacological space.**

#### Problem: Why are subgraphs challenging?

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030622964.png)
#### Problem formulation: Predict links between drug and disease subgraphs

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030625840.png)
#### Method: SubGNN -- Subgraph Neural networks

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030628509.png)
#### Results

##### Embedding space of COVID-19

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030631207.png)
[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7280907/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7280907/)

##### Experimental validations of predictions

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030634051.png)
##### Network drugs

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030636410.png)

#### Key ML lessions

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613030638774.png)


## 
