---
title: "组学数据下载"
subtitle: ""
date: 2023-10-01
draft: false
author: "Xiaopeng Xu"
description: "组学原始数据下载方法速查。"
tags: ["Bioinformatics", "Data"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 原始数据下载

### European Nucleotide Archive (ENA) 

[https://www.ebi.ac.uk/ena/browser/view/PRJEB40872](https://www.ebi.ac.uk/ena/browser/view/PRJEB40872)

选择后，会生成 bash 脚本，包括 wget 命令。直接运行脚本即可。


### SRA 数据库

大部分测序的原始数据都在 SRA。可以安装 SRA-tools 来下载相关的数据。


选择数据后，下载 access_list，会生成一个包含样本编号的 txt 文件。


需要先按这里的说明来安装和配置 SRA-tools。

[https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump)

#### 安装 SRA-tools

[https://www.metagenomics.wiki/tools/short-read/ncbi-sra-file-format/sra-tools-install](https://www.metagenomics.wiki/tools/short-read/ncbi-sra-file-format/sra-tools-install)
