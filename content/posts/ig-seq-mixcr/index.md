---
title: "Ig-seq 操作说明"
subtitle: ""
date: 2024-02-08
draft: false
author: "Xiaopeng Xu"
description: "Ig-seq（免疫组库测序）操作说明：数据下载与 MiXCR 分析流程。"
tags: ["MiXCR", "Immunology", "Bioinformatics"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 数据下载

从 NCBI SRA 平台下载对应的 Ig seq 项目数据。

* [https://www.ncbi.nlm.nih.gov/Traces/study/](https://www.ncbi.nlm.nih.gov/Traces/study/)

先导入 google cloud 的 bucket 中，然后通过 gsutils 下载到本地或 ibex 文件夹中。

## MiXCR 数据分析

### 安装  MiXCR

```powershell
conda install -c imperial-college-research-computing mixcr
```
### Ig-seq 快速使用

```powershell
# Align
Align: mixcr align–library my_library -t 8 -r align_log.txt R1 R2 alignments.vdjca -s hs
# What is the my_library used here

# Assemble
Assemble: mixcr assemble -r assemble_log.txt -OseparateByV = true -OseparateByJ = true -OseparateByC = true align-
ments.vdjca clones.clns
```


### 使用介绍

典型的 MiXCR 工作流程主要由三个部分构成：

* [align](https://links.jianshu.com/go?to=https%3A%2F%2Fmixcr.readthedocs.io%2Fen%2Fmaster%2Falign.html%23ref-align)：将测序结果比对到 T 细胞或 B 细胞受体的V、D、J、C基因参考序列上

* [assemble](https://links.jianshu.com/go?to=https%3A%2F%2Fmixcr.readthedocs.io%2Fen%2Fmaster%2Fassemble.html%23ref-assemble)：利用前一步骤获得的比对结果拼接 clonotypes（为了提取特定的基因区域信息，比如CDR3）

* [export](https://links.jianshu.com/go?to=https%3A%2F%2Fmixcr.readthedocs.io%2Fen%2Fmaster%2Fexport.html%23ref-export)：输出比对结果（exportAlignments 模块）或者 clones 信息（exportClones 模块），生成可读文件


MiXCR 的 assemble 模块有几种不同的拼接方法可以选择：

* assembleContigs：拼接完整的 TCR 或者 IG 受体 clonotype 序列

* 对于RNA-Seq or non-targeted DNA data, 工作流程可能包括以下两部分：

   * assemblePartial：将有重叠区域的序列片段拼接成相对较长的包含 CDR3 区域的 contigs

   * extend: 估算测序和比对质量较好但长度较短的 TCR 比对序列的 germline 序列

为了简化输入命令，MiXCR提供了 analyze 命令模块，打包了整个分析流程

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011628168.png)
支持的数据类型：

fasta，fastq，fastq.gz，paired-end fastq和fastq.gz。作为每一步骤的输出结果，MiXCR 生成包含各种信息的二进制压缩文件（比对生成 alignments，拼接生成 clones）。利用exportAlignments 和 exportClones 命令模块，每一个二进制文件都可以转化成 tab 分割的可读文本文件。

#### 默认流程 multiplex-PCR

利用 analyze amplicon 命令分析 multiplex-PCR 扩增的 TCR/BCR 基因 DNA 片段

```shell
>mixcr analyze amplicon --species hs --starting-material dna --5-end v-primers --3-end j-primers --adapters adapters-present --receptor-type IGH input_R1.fastq input_R2.fastq analysis
```
只有一个参数修改为非默认值（--receptor-type IGH），这个参数的改变可以让MiXCR 调用针对B细胞优化的比对模块并且只输出IGH序列。其实这个参数是可以缺省的，缺省状态下MiXCR会调用默认的比对模块并输出样本中所有的TCR/BCR序列。
生成的文件（analysis.clonotypes.IGH.txt）是一个 tab 分隔的表格，包含 CDR3 序列拼接的所有clonotypes（克隆丰度，CDR3序列， VDJ基因等）。


分步骤执行的命令：

```powershell
# 1. Align 把原始序列比对到IGH基因的VDJ基因序列片段上
> mixcr align -s hs -p kAligner2 input_R1.fastq input_R2.fastq alignments.vdjca
# 2. Assemble 拼接 clonotypes
> mixcr assemble alignments.vdjca clones.clns
# 3. Export 将包含clones列表的二进制文件（analysis.clna）导出为可读的文本文件
> mixcr exportClones --chains IGH clones.clns clones.txt
```
#### 基于 5'RACE 扩增实验的数据分析

考虑基于 5'RACE（一个 read 覆盖 CDR3 区域和临近序列，另一个 read 覆盖 V 基因的 5'UTR 和下游序列）实验准备的 IGH 基因 cDNA 文库双端测序的数据处理流程，全部分析流程可以通过analyze amplicon 命令实现:

```shell
> mixcr analyze amplicon --species hs --starting-material rna --5-end v-primers --3-end j-primers --adapters adapters-present input_R1.fastq input_R2.fastq analysis
```
结果文件（analysis.clonotypes.<chains>.txt）包含详细的 clonotypes 信息。
分步骤执行的命令：

```powershell
# 1. Align 把原始序列比对到IGH基因的VDJ基因序列片段上
> mixcr align -s hs -OvParameters.geneFeatureToAlign=VTranscript --report analysis.report input_R1.fastq input_R2.fastq analysis.vdjca
# 2. Assemble 拼接 clonotypes
> mixcr assemble --report analysis.report analysis.vdjca -a analysis.clna
# 3. Export 将包含clones列表的二进制文件（analysis.clna）导出为可读的文本文件
> mixcr exportClones --chains TRA analysis.clna analysis.clonotypes.TRA.txt
> mixcr exportClones --chains TRB analysis.clna analysis.clonotypes.TRB.txt
```
1. 用来比对 V 基因的非默认基因特征（-OvParameters.geneFeatureToAlign=VTranscript）同时利用了两个 reads 的信息，为了让 MiXCR 利用 CDR3 反向 read 比对V基因的 5'UTRS 和部分 5'端编码区域。MiXCR 还会生成 report 文件（通过可选参数 --report 指定），其中包含的具体运行统计信息。可以利用 exportAlignments 命令将比对生成的二进制结果（analysis.vdjca）转化为可读的文本文件。

1. 步骤会校正 PCR 和测序错误并建立 clonotypes，默认情况下 clonotypes 会拼接 CDR3 序列；可以通过设置 assemble 模块的参数来制定其他的基因区域（参考assemble documentation），可选的 report 文件 analysis.report 包含各种调试信息。

2. 导出的各种选项详见 [export](https://links.jianshu.com/go?to=https%3A%2F%2Fmixcr.readthedocs.io%2Fen%2Fmaster%2Fexport.html%23ref-export) 文档，上述的所有步骤都可以根据特定研究的分析流程进行个性化设置。

#### 高质量全长 IG 免疫组库分析

对于基于 cDNA 全长的 IG 免疫组库分析，我们一般推荐 UMI 标签制备文库并使用非对称双端测序 350 bp + 100 bp Illumina MiSeq测序方法（详情参考[Nature Protocols paper](https://links.jianshu.com/go?to=http%3A%2F%2Fwww.nature.com%2Fnprot%2Fjournal%2Fv11%2Fn9%2Ffull%2Fnprot.2016.093.html)）。这种方法可以获得长片段高质量测序结果，而且可以利用 [MiGEC software](https://links.jianshu.com/go?to=https%3A%2F%2Fmilaboratory.com%2Fsoftware%2Fmigec%2F) 有效去除 PCR 和测序错误。获得的高质量数据可以进一步利用 MiXCR 处理，以提取全长 IGH 或 IGL 组库。


**使用**[analyze amplicon](https://links.jianshu.com/go?to=https%3A%2F%2Fmixcr.readthedocs.io%2Fen%2Fmaster%2Fanalyze.html%23ref-analyze-amplicon)**命令分析:**

```powershell
> mixcr analyze amplicon --species hs --starting-material rna --5-end v-primers --3-end j-primers --adapters adapters-present --receptor-type BCR --region-of-interest VDJRegion --only-productive --align "-OreadsLayout=Collinear" --assemble "-OseparateByC=true" --assemble "-OqualityAggregationType=Average" --assemble "-OclusteringFilter.specificMutationProbability=1E-5" --assemble "-OmaxBadPointsPercent=0" input_R1.fastq input_R2.fastq analysis
```
 这一步骤会生成以下结果文件（analysis.clonotypes.IGH.txt，analysis.clonotypes.IGK.txt 和analysis.clonotypes.IGL.txt），其中包括详细的 clonotypes 信息。这里我们要强调几个可选参数：
* **--receptor-type BCR:** 需要 MiXCR 调用 B 细胞优化的比对模块（等同于对 align 模块使用 -p kAligner2 参数）并且只输出 IG 序列。

* **region-of-interest VDJRegion:** 对 assemble 模块使用 -OassemblingFeatures=VDJRegion 参数

* **--only-production** 在 export 输出的 clonotypes 中过滤掉 out-of-frame 和 stop codon

* **--align <option>** 在 align 过程中设置其他的参数

* **--assemble <option>** 在 assemble 过程中设置其他参数


**分步骤执行的命令：**

```powershell
# 1. 合并双端 reads 并比对 alignment：MiXCR 的 align 模块可以合并双端 reads 并比对到参考的 V/D/J 和 C 基因上，我们推荐使用 KAligner2 处理 IG 数据
> mixcr align -p kaligner2 -s hs -r alignmentReport.txt -OreadsLayout=Collinear -OvParameters.geneFeatureToAlign=VTranscript read_R1.fastq.gz read_R2.fastq.gz alignments.vdjca
# 2. Assemble拼接clones
> mixcr assemble -r assembleReport.txt -OassemblingFeatures=VDJRegion -OseparateByC=true -OqualityAggregationType=Average -OclusteringFilter.specificMutationProbability=1E-5 -OmaxBadPointsPercent=0 alignments.vdjca clones.clns
# 3. Export输出clones结果
> mixcr exportClones -c IGH -o -t clones.clns clones.txt
```
1. 选项 **-s**用来指定物种（e.g. homo sapiens - hsa, mus musculus - mmu），参数 **-OreadsLayout** 用来设定 reads 方向（Collinear, Opposite, Unknown）。这里需要注意的是，经过 MiGEC 分析的双端 reads 方向是 Collinear。除了 KAligner2，也可以使用默认的MiXCR 比对模块，只是也许会忽略一些亚变异类型，这些变异类型是由 V 基因片段的若干核苷酸插入形成的。

2. **-OseparateByC=true** 把 clones 按照不同的抗体亚型分类, **-OcloneClusteringParameters=null** 关闭基于频率的 PCR 错误校正。 根据数据质量，可以通过设置 **-ObadQualityThreshold**参数来调节输入数据的阈值来优化 clonotypes 的提取。

3. 选项 **-o**和 **-t**用于过滤包含 out-of-frame 和 stop codon 的 clonotypes，**-c**指定哪条链的数据应该被提取（e.g. IGH, IGL）。


#### RNA-Seq数据分析

MiXCR 可以用于提取 RNA-Seq 数据中 TCR 和 BCR 的 CDR3 组库，提取效率取决于样本红 T/B 细胞的丰度和测序长度。推荐 2x150bp 或者 2x100bp 的双端测序方法。不过在双端 2x50bp 的 RNA-Seq 数据（比如肿瘤样本中），主要 clonotypes 信息也可以被提取。

**用 analyze shotgun 命令分析：**

```powershell
> mixcr analyze shotgun --species hs --starting-material rna --only-productive input_R1.fastq input_R2.fastq analysis
```
生成的结果文件（analysis.clonotypes.TRA.txt, analysis.clonotypes.IGH.txt 等）包含clonotypes 的详细信息。

**分步骤操作流程：**

```powershell
# 1. Align 比对reads
> mixcr align -s hs -p rna-seq -OallowPartialAlignments=true data_R1.fastq.gz data_R2.fastq.gz alignments.vdjca
# 2. Assemble parial reads拼接部分reads，2 次迭代最优
> mixcr assemblePartial alignments.vdjca alignmentsRescued_1.vdjca
> mixcr assemblePartial alignmentsRescued_1.vdjca alignmentsRescued_2.vdjca
# 3. 利用已有 V 和 J 基因和 germline 覆盖度不全的 CDR3s 序列延长 TCR 比对结果
> mixcr extendAlignments alignmentsRescued_2.vdjca alignmentsRescued_2_extended.vdjca
# 4. Assemble拼接clones
> mixcr assemble alignmentsRescued_2_extended.vdjca clones.clns
# 5. Exporting导出clones
> mixcr exportClones -c TRA -o -t clones.clns clones.txt
```
1. 所有mixcr align的参数都可以在这里使用（比如 -s 来指定物种）： **-OallowPartialAlignments=true**选项保留部分比对结果用于后续的 assemblePartial 模块

2. 为了获得包含 CDR3 全长序列的拼接 reads，建议使用迭代 mixcr 的 **assemblePartial**模块多次迭代拼接结果。多次迭代需要 **-p**参数，根据我们的经验，两次迭代后结果最优

3. 注意 extend 时用的数据

4. 所有 mixcr assemble 的参数都可以在这里使用：

   1. 对于低质量数据，建议降低输入质量阈值（e.g. -ObadQualityThreshold=15）

   2. 用错误校正算法合并克隆丰度，可增加：**OaddReadsCountOnClustering=true**

5. 可以指定导出感兴趣的免疫受体链（**-c TRA** 或者 **-c TRB**等），也可以去除包含 out-of-frame （选项 **-o**）和 stop codon 的突变体（选项 **-t**）。

#### 组装小鼠 TRB 样本的基于 CDR3 克隆类型

[https://mixcr.readthedocs.io/en/master/quickstart.html#assembling-of-cdr3-based-clonotypes-for-mouse-trb-sample](https://mixcr.readthedocs.io/en/master/quickstart.html#assembling-of-cdr3-based-clonotypes-for-mouse-trb-sample)

### 参数解读

|模块名称|模块功能|
|:----|:----|
|analyze|对指定输入文件执行 MiXCR 整套分析流程|
|align|对输入测序 reads 生成 V/D/J/C 基因比对序列|
|assemble|拼接 clones|
|assembleContigs|拼接全长序列|
|assemblePartial|拼接部分比对 reads 生成更长的序列|
|extend|用 germline 序列预测比对序列或 clones|
|exportAlignments|将 V/D/J/C 比对结果导出为 tab 分隔文件|
|exportAlignmentsPretty|导出比对结果的详细信息|
|exportClones|将拼接的 clones 导出为 tab 分隔文件|
|exportClonesPretty|导出 clones 的详细信息|
|exportReadsForClones|从 clones &比对结果（*.clna）中导出特定 clone 的 reads，如果没有指定 clone，所有对应的 reads 都会被导出|
|exportAlignmentsForClones|从 clones&比对结果（*.clna）中导出特定 clone 的比对结果|
|exportReads|从 vdjca 文件导出原始 reads|
|mergeAlignments|将若干 *.vdjca 文件合并为一个比对文件|
|filterAlignments|过滤比对结果|
|sortAlignments|根据 read ID 排序 vdjca 文件中的比对结果|
|alignmentsDiff|计算两个 vdjca 文件的差异|
|clonesDiff|计算两个 clns 文件的差异|
|slice|分割 clna 文件|

### 结果解读

输出文件包含内容：

|输出表头|注释内容|
|:----|:----|
|cloneId|clone 识别号码|
|cloneCount|clone 数量|
|cloneFraction|clone 比例|
|targetSequences|目标序列|
|targetQualities|目标质量|
|allVHitsWithScore|所有 V基因命中和评分|
|allDHitsWithScore|所有 D 基因命中和评分|
|allJHitsWithScore|所有 J 基因命中和评分|
|allCHitsWithScore|所有 C 基因命中和评分|
|allVAlignments|所有 V 基因比对结果|
|allDAlignments|所有 D 基因比对结果|
|allJAlignments|所有 J 基因比对结果|
|allCAlignments|所有 C 基因比对结果|
|nSeqFR1|FR1 核苷酸序列|
|minQualFR1|FR1 最小质量|
|nSeqCDR1|CDR1 核苷酸序列|
|minQualCDR1|CDR1 最小质量|
|nSeqFR2|FR2 核苷酸序列|
|minQualFR2|FR2 最小质量|
|nSeqCDR2|CDR2 核苷酸序列|
|minQualCDR2|CDR2 最小质量|
|nSeqFR3|FR3 核苷酸序列|
|minQualFR3|FR3 最小质量|
|nSeqCDR3|CDR3 核苷酸序列|
|minQualCDR3|CDR3 最小质量|
|nSeqFR4|FR4 核苷酸序列|
|minQualFR4|FR4 最小质量|
|aaSeqFR1|FR1 氨基酸序列|
|aaSeqCDR1|CDR1 氨基酸序列|
|aaSeqFR2|FR2 氨基酸序列|
|aaSeqCDR2|CDR2 氨基酸序列|
|aaSeqFR3|FR3 氨基酸序列|
|aaSeqCDR3|CDR3 氨基酸序列|
|aaSeqFR4|FR4 氨基酸序列|
|refPoints|参考点|
