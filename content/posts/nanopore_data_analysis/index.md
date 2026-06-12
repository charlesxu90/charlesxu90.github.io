---
title: "Nanopore 分析流程"
subtitle: ""
date: 2026-05-02
draft: false
author: "Xiaopeng Xu"
description: "Nanopore 测序数据的基础分析流程笔记。"
tags: ["Nanopore", "Bioinformatics"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 基础的分析流程：

1. Base calling 从电信号中识别碱基序列。原始电信号是Fast5/Pod5格式，需要转为 Fastq 格式。 Fast5/Pod5-> Fastq。

2. Alignment 比对到参考基因组。常用工具是 minimap2。

3. Call variants 获取突变数据，包括 GATK，VarScan 等。

4. Calculate gene expression 获取基因表达情况。


## Basecalling 识别碱基序列

默认在 ONT 的 MinKNOW 系统运行中，会执行 basecalling。原来常用的是 Guppy，现在常用的是 Dorado，其实是 C++版本的 Bonito。原始电信号文件是fast5或者pod5格式，最终得输出文件是fastq格式。


## Alignment 比对到参考基因组

这一步需要将上一步得到的fastq文件中的 reads比对到参考基因组，常用的工具是minimap2。


### 下载参考基因组

通常是从 UCSC、Ensembl 等数据库下载参考基因组。对于人常用的是 hg38。

```powershell
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/md5sum.txt

# check md5sum to ensure file matches
md5sum hg38.fa.gz
```


### Minimap2 比对

minimap2 可以从 conda下载，或者其他方式安装：

```powershell
conda install -c bioconda minimap2 
```


#### 做全基因组比对

##### 对参考基因组建立索引

```powershell
minimap2 -d hg38.mmi hg38.fa.gz        # indexing hg38 939M, ~2min
```
##### 全基因组比对

```powershell
minimap2 -a /mnt/data/data_repository/nanopore/ref_seq/hg38.mmi ./NA12878-DirectRNA_All_Guppy_4.2.2.fastq > NA12878-DirectRNA_align.sam   # alignment 24G/10,655,945 reads, ~105 min
```
#### 做转录组比对

##### 生成 bed 文件

需要从 GTF 文件中生成转录本的 BED 文件

```powershell
awk '$3 == "gene"' ~/c2066/TCGA/annotation/gencode.v44.annotation.gtf > gencode.v44.gene.gtf

awk -F "\t" '{OFS="\t"}{print $1,$4,$5,substr(substr($9,index($9,"gene_id")),9,index(substr($9,index($9,"gene_id")),";")-9)":"substr(substr($9,index($9,"gene_type")),11,index(substr($9,index($9,"gene_type")),";")-11)":"substr(substr($9,index($9,"gene_name")),11,index(substr($9,index($9,"gene_name")),";")-11),substr(substr($9,index($9,"level")),6,index(substr($9,index($9,"level")),";")-6),$7}' gencode.v44.gene.gtf | sed s/\"//g > gencode.v44.gene.bed
```
先从 GENCODE 下载 GTF 文件，然后用如上代码，获取基因的 GTF，然后获取BED 文件。
注意：BED文件和 GTF 文件的其实位置不一样，GTF coordinates start from "1", while BED starts from "0". [https://groups.google.com/g/rseqc-discuss/c/YAOBQqYepS4](https://groups.google.com/g/rseqc-discuss/c/YAOBQqYepS4) 但对一个基因，通常特别长，这个影响不大。


##### Minimap2 比对

minimap 中匹配时候必须参考 junction 信息，否则肯定有很多匹配错误。需要先自己创建匹配的 bed 文件，然后在 minimap 匹配时候用它来做匹配。

```powershell
paftools.js gff2bed gencode.v44.annotation.gtf > gencode.v44.junc.bed
# /mnt/data/data_repository/nanopore/ref_seq/gencode.v44.junc.bed
```
合并 fastq 并比对
```powershell
cat fastq_pass/*.fastq.gz > fastq_pass_all.fastq.gz

minimap2 -ax splice:hq --junc-bed ../../ref_seq/gencode.v44.junc.bed -uf -I 64G ../../ref_seq/hg38.mmi ./fastq_pass_all.fastq.gz -o ./fastq_pass_all.sam
```


### 查看 SAM 比对结果

#### 查看 SAM 文件

SAM 是文本格式文件，可以直接查看。

```powershell
less NA12878-DirectRNA_align.sam 
```


#### SAM 文件说明

##### 注释信息

注释信息 (header) 包括：

* @HD：VN表示版本，SO表示排序方式。

* @SQ：SN表示参考序列的名称，LN表示参考序列的长度。

* @PG：比对时使用的工具指令。

* @RG：样本信息。

* @CO：其他注释信息。

```powershell
@HD     VN:1.6  SO:unsorted     GO:query
@SQ     SN:chr1 LN:248956422
@SQ     SN:chr10        LN:133797422
...
@SQ     SN:chrM LN:16569
@SQ     SN:chrUn_KI270302v1     LN:2274
...
@SQ     SN:chrY LN:57227415
@SQ     SN:chrY_KI270740v1_random       LN:37240
@PG     ID:minimap2     PN:minimap2     VN:2.26-r1175   CL:minimap2 -a /mnt/data/data_repository/nanopore/ref_seq/hg38.mmi ./NA12878-DirectRNA_All_Guppy_4.2.2.fastq
```
##### 比对结果

[https://www.samformat.info/sam-format-alignment-tags](https://www.samformat.info/sam-format-alignment-tags)

比对结果主要包括11列信息：

<!-- TODO image: re-host on Aliyun OSS, then replace with ![nanopore_data_analysis](OSS_URL). Original saved at nanopore_data_analysis_images/nanopore_data_analysis_1.jpg -->
* 1. QNAME：reads名称。

* 2. FLAG：reads比对情况。不同的情况对应不同的值，这里的数字是所有情况的和。

* 3. RNAME：比对至参考序列的名称。

* 4. POS：比对到的位置。

* 5. MAPQ：比对质量。

* 6. CIGAR：比对情况信息。

* 7. RNEXT：与之配对的另一条reads所在的参考序列名称。"="表示位于同一个参考序列上，"*"表示没有另一条reads。

* 8. PNEXT：与之配对的另一条reads所在的位置。

* 9. TLEN：插入片段长度。

* 10. SEQ：reads序列。

* 11. QUAL：reads序列质量。


除了这11列信息外，还有一些其他信息：

* NH:i:n 表示reads比对到参考序列位置的个数。

* AS:i:n 表示比对得分。

```plain
e86d4fab-e29d-4c34-b741-c0cb61f58051    16      chr5    150401639       60      8S23M1D18M1D11M1D33M2D11M3I5M1D34M2D7M3D66M1D15M1D66M1I2M1D78M3D73M1I9M1D44M1I10M1D12M5D7M2D32M1D33M667S        *       0       0 
GCAGTTTTTTCTAATTACTACCTTTTATTCTTTATGAACCATGGCCCTGAAGCTGATAACAGCTTGGCTGAGCAGAGGGAACTTGGGGTCGGCAAAGGATTATGGGAGGTGGAAACATTGGCTCTTCCTTGGGGAGTGATGCTGGGAAGGGAAAGTGGCTCAGCCTGCAGGTAAATAGGCTAGAGAAGCCAAGGCCAAAGGCTGGAAGGGAGAGGACAGCAGCATGTCCAGCCTGGGTCTGGGTGTAGGGTTATCCCTTCTCCCTGTGCCTTCCCATCTCGTCCATAAGCCTAGGTCTTGAGAACTTGTGTTGGAGGCTGCTGTGATGTCAGGAACGGGGATCTGTCTAGCTTTTGGCCACTTCCTGGGACCTCACGCCCCTGACAGATGGAGATTGGGCAGCAGGGCCTTGCTGCATTGTTATCTGCTGTTCCGACTTGGTTTGTCTTGTCCAGAGGGTGACGAAGAGCCAGGCACCAGGGTCTCATGGGATGAGGTACAGGGTGGGTAGATGGGGGAGGGCTGGGGGCTGAGCAAGAGCTGTAGCTGTGTGGGGCTGGCAGGATGTTGAGACCGCCTCTGCTGCTCTCACATGGGGACTGGGCCCAGGATCCTGCTTGGTCACACCCCAGCCCAGAAACGGGTCCTCCAGTTCCAGTGACTCTCGGTGGAGCGTCAGTGGGCTTTTGCTCCAAGGAGTGCCTGCTCATTTCAGAAGACAGGAGCCAATGGTGCATCCAGCTCTCAAAGACCTTCCAGTCTGTGGTCTCCATGGTGTTCTTAAGGTGTCTCAGGTTCTCCGGGGAAGCTCCTTCAGTAAGGCGGGTACACTCAGGGGGTCAGCATTCTGGAGCAGGTGCATCACGGTCCTCCTCTGTCATGATGCTACTTGGTGGCATTTCTGCATGGGCCCTGGGGCAGGGCTCTAATGGGCAGCGCCTATCAGCAGCGGGGTGGCCAGCGCATCTTGCTCACAGGCTGGAGGCTTGGGAAGCTTCACCGCAGGTTCTCCAGCTGCAGGGTTCTGGGAGGTGACCGCTATTGTCCAGCTGGCCCTGCTGCTGGTACAGGAAGTAGGCGGTGGCCTGGCCAGCGGAGCAGAGGTCACAGGATGGAAGAGCCTGTGTACAGGGCTCCGCGGCTGCACTTGCTCTCCGGGGCCCCAGGGCGCCGGCCCAGCATGGGCAGTTGCTCATTGTTGGAGATAAGGTCGCGCTGGTCATCCATGACTGGCTTCTGATCTTCCGACAGCTCCTGCTTCTCCTCCTGT  
$$#&$%%&&86;80*-:7:=>?OF<97;252%%'&%(@/3)45=HCA>9./5D5:8@A:?A)8F=>=J?A6(69&&52:4;>8/98:3;74;//'+-+().*%.4-$)))450/10677599>7332365:::0*,+-6<?ADD7:)(,,%(+0=;9>>C:A<:;=::<<97:.9475<G@9%''2)??==3<7462%&9==@91((22/%))+&&-0)(',1(0;>7:>=9:BHF879<3:-,87<<<8::>E<BB;?9B;?B@D:><=C>,/7?=7<?6/01-#%$&33<6-78AD88%&)&8774.2///-+=;@89@55++53;;=<93/.3?>?-7<;<>4=59?=TD?A;?>:C8A9:=?IC?33>0=2+;<:=4+)*4/((%%0*200496?9=867;>?B;HF/:/>9>;=2%2@8<;<<522425>93HCGE>>;A9:;-4:+.1'%&96224./(&'4?ABC==7;<?9E:.*671%%42139?6?267>>8696=*&%0-9>:6;31&;>=<AF=;95941*06<0(77?>H=.7:3(6<,1;@:>AB::=74C=::=?6/=08<GG@?A>@9=7<28629)9C>='26=7B;60%%'%44-/'35(('2471&6:=D:B45566&/(%+,-)031*68;@GC58<.$)6;0>955%%%01,156<=97@==?A?C>>-=:=@4:68ABCAD9>>@=/,688/%(&&:>891*)58:7:?;..8==.0:62/BDDA&($,EFA>39;/22:1,3*/:>.0'#$-$123;C20/7<<>?16-7A?<:3?4<87;)6D?9C993/(($#%%-625100/7685;;?>989*59*+/3:6;==2<:97D>>79??0''&&'(0<<1C.)*,/*&)>9928<<8D<:D:90+6==<-%*.4<@;:;9?=@7<8>0+:.,&$12>:;:=+2B:.$-DA?;8<.=?>;>;87,.8857>EC=OG@<?>:3=:6./)4(=;2.0;5'-4(?@=8%))744;;,>:>/1==E@>83>>7=CAB>@1,&%#$/%&*00,,,<E-/;/@+?556<;6428=:@(%2456'+(,-+7/%%$#$6*:/FB?A:,('((643&$%$%(&43;287=3-&#%16750,38:<.>;7389?918=E@D?F:<;8<@:BC@:AA@><AB@:<7-8*1=8CC7>4;;1??981*0-9<>=<A=D@44=/-<88>AF?::8@0)F5:CGE???2<:C@E>;J@83(,97@;8917>;,6C:;)+'13+3551/.*($  
NM:i:40 ms:i:1003       AS:i:990        nn:i:0  tp:A:P  cm:i:52 s1:i:400        s2:i:0  de:f:0.0443     SA:Z:chr5,150407152,-,984S168M7D118S,50,17;chr5,150412625,-,1150S120M1D,60,1;chr5,150404683,-,664S87M3I516S,30,3;       rl:i:0
```
### Samtools 操作 BAM 文件

#### 查看 BAM 文件

使用 SAMTools 索引对比结果文件 

[https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/data_manipulation_tools/samtools/running_samtools_commands/](https://hcc.unl.edu/docs/applications/app_specific/bioinformatics_tools/data_manipulation_tools/samtools/running_samtools_commands/)

#### 将SAM转换为BAM格式

BAM 为 SAM 的二进制格式，可以压缩存储空间。约1/2左右。

```powershell
samtools view -S NA12878-DirectRNA_align.sam -b > NA12878-DirectRNA_align.bam # 37min
```
#### sort BAM 排序

对BAM文件排序。

```powershell
samtools sort -l 4 -o NA12878-DirectRNA_align-sorted.bam NA12878-DirectRNA_align.bam
```
#### index 建立 BAM 索引

```powershell
samtools index NA12878-DirectRNA_align-sorted.bam  # ~20min
```
#### flagstat 查看整体比对情况

```powershell
$ samtools flagstat NA12878-DirectRNA_align-sorted.bam
33576710 + 0 in total (QC-passed reads + QC-failed reads)
14971421 + 0 primary
10629060 + 0 secondary
7976229 + 0 supplementary
0 + 0 duplicates
0 + 0 primary duplicates
29137799 + 0 mapped (86.78% : N/A)
10532510 + 0 primary mapped (70.35% : N/A)
0 + 0 paired in sequencing
0 + 0 read1
0 + 0 read2
0 + 0 properly paired (N/A : N/A)
0 + 0 with itself and mate mapped
0 + 0 singletons (N/A : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
```
### IGV 查看BAM文件

[https://scienceparkstudygroup.github.io/rna-seq-lesson/04-bioinformatic-workflow/index.html](https://scienceparkstudygroup.github.io/rna-seq-lesson/04-bioinformatic-workflow/index.html)

#### 安装 IGV

从 [https://software.broadinstitute.org/software/igv/download](https://software.broadinstitute.org/software/igv/download) 下载最新版本

```powershell
unzip IGV_Linux_2.16.2_WithJava.zip
mv IGV_Linux_2.16.2 /opt/ 
alias igv='/opt/IGV_Linux_2.16.2/igv.sh'
```
#### 使用 IGV

命令行运行 igv 运行程序

```powershell
igv
```
在 IGV 中选择要加载的 BAM 文件，其对应的 BAI 文件应该有相同的文件名。
加载成功后，在搜索框中输入基因名，即可查看数据。

<!-- TODO image: re-host on Aliyun OSS, then replace with ![nanopore_data_analysis](OSS_URL). Original saved at nanopore_data_analysis_images/nanopore_data_analysis_2.png -->
有时候程序运行正常，但会出现无基因 reads的情况。这种情况需要考虑是否测序数据中就没有这个基因。如，非血液样本的测序中，没有 HBB、HBA1和HBA2。

## 获取 reads 比对信息

做更细的分析，如甲基化分析，需要对单条 read 做处理。因此需要针对性的注释 reads。

### BAM文件中增加基因和转录本注释

```powershell
tagBam -i $samid.sorted.bam  -s -files $ref_folder/gencode.v44.gene.bed -names -f 0.1 > $samid.sorted.addGene.bam
```
### 获取 reads 比对信息

```powershell
samtools view $samid.sorted.addGene.bam | awk '{OFS="\t"}{print $1,$3,$4,$5,$NF}' > $samid.sorted.addGene.bam.anno.txt

awk '$4 > 5' $samid.sorted.addGene.bam.anno.txt  | grep -v 'rl:i:' > $samid.sorted.addGene.bam.anno.txt.filt
```
## 甲基化分析
