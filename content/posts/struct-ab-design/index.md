---
title: "基于结构设计抗体"
subtitle: ""
date: 2026-04-24
draft: false
author: "Xiaopeng Xu"
description: "基于结构的抗体设计笔记：方法、流程与工具。"
tags: ["Antibody Design", "Protein Design", "Structure"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 总体介绍

目前抗体圈主要是在英美。美国以 RosettaCommons 为核心，有好多人在做抗体设计。英国以 Oxford 的 Charlotte Deane 为代表，有很多研究人员做此方向。


Rosetta 目前被蛋白质设计相关组广为使用。主要是美国的一些科研机构在用。包含抗体序列numbering、抗体结构预测、抗体抗原 docking 和 抗体设计等项目的多个软件。Numbering 主要用的是 PyIgClassify (2015), 抗体结构预测包括 RosettaAntibody(2009), AbPredict (2016, 2019), 和 RosettaCM (2013)，抗体抗原 docking 包括 RosettaDock (2008) 和 *SnugDock(2010)，抗体设计包括 RosettaAntibodyDesign (RAbD, 2018) 和 AbDesign (2015)，通过引用量来看 RosettaCM (748)，RosettaAntibody (2009, 175)，RosettaDock (2008, 516) 和 SnugDock (2010, 122) 用的人较多。另外，Rosetta 有个在线平台 Rosie，提供在线服务，做蛋白质结构预测和 Docking 等，[https://rosie.rosettacommons.org/queue](https://rosie.rosettacommons.org/queue)。


以 DeepMind、Oxford 的 Charlotte Deane 为代表的英国很多机构和研究者也在做相关领域。其中， Charlotte Deane 开发了许多软件，用于做抗体结构相关分析。包括做 Numbering 的 ANARCI (2016, 124)，做结构预测的 AbodyBuilder (2016, 87)，做 cdr loop 区域预测的 ABlooper (2021, 1)。


### 下载安装 Rosetta 系列

从 [https://www.rosettacommons.org/software/license-and-download](https://www.rosettacommons.org/software/license-and-download) 注册申请 license，并下载对应的 src 压缩文件。


压缩包下载后，用 gunzip 解压。可以调整解压后文件的目录的名称位置。然后进入 main/source 目录，进行 build。build 好后，将下面的 bin/ 和 tools/ 目录加入 PATH 环境变量。

```powershell
gunzip rosetta_src_3.13_bundle.tgz
mv rosetta_src_3.13_bundle rosetta_v3.13
cd rosetta_v3.13/main/source
# build
./scons.py -j 100 mode=release bin 
# -j 100 define the number of cores to run.

# add environment variable
export ROSETTA_PATH=~/Desktop/Ab_design/ref_works/Rosetta/rosetta_v3.13/main/
```
## 抗体结构预测

目前看到有两种方法比较适合有模板的抗体结构预测问题， RosettaAntibody 和 AbPredict。

### RosettaAntibody 使用

ROSIE 平台任务提交入口：[https://rosie.rosettacommons.org/antibody/submit](https://rosie.rosettacommons.org/antibody/submit)

输入是 Fv 两个 chain 的序列的 fasta 文件。同时需要选择 graft 的 database 以及 blastp。

#### 安装依赖项

blastp 按照 blast 官方说明，下载源码并 build 即可，无需下载数据库。[https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download).

#### 运行代码

```powershell
$ROSETTA_PATH/source/bin/antibody.linuxgccrelease -fasta 4m5y_Fv.fasta -antibody::grafting_database $ROSETTA_PATH/database/additional_protocol_data/antibody -antibody:n_multi_templates 1 -exclude_pdbs 4m5y -antibody::blastp /home/xiaopeng/Desktop/Ab_design/Rosetta/blast-2.12.0/c++/ReleaseMT/bin/blastp
```
用 pymol 查看生成的模型
```powershell
pymol grafting/model-0.relaxed.pdb

# Input in pymol command line
fetch 4m5y  # fetch 4m5y as framework to compare
alignto  # alignto 4m5y for close comparison 
```
识别结构的 CDR loop 类别，即 North cluster
```powershell
$ROSETTA_PATH/source/bin/identify_cdr_clusters.linuxgccrelease -s grafting/model-0.relaxed.pdb -out:file:score_only north_clusters.log
```
North B, Lehmann A, Dunbrack RL. A new clustering of antibody CDR loop conformations. J Mol Biol 2011; 406:228-256.
### Ablooper 使用

使用 Ablooper 需要先获得蛋白结构，默认推荐用 AbodyBuilder 来预测结构。

ABlooper, a fast equivariant neural network for predicting CDR loop structures [1]. 

#### 创建基础模型

先用 AbodyBuilder 创建抗体模型，如下 web 页面所述。输入是 Fv 两个 chain 的序列。

[http://opig.stats.ox.ac.uk/webapps/newsabdab/sabpred/abodybuilder/](http://opig.stats.ox.ac.uk/webapps/newsabdab/sabpred/abodybuilder/)

用 AbodyBuilder 预测出的结构有些位置不太准确，差异较大。与 ref 对比： RMSD=0.353。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011801309.png)

#### 使用 ABlooper 预测 CDR loop 区域

输入是用 IMGT numbering 的 pdb 文件。AbodyBuilder 输出可满足。

```powershell
# 需在 python2 安装 biopython 依赖包
ABlooper Test_fv_model_rank1_imgt_scheme.pdb --output ABlooper_model.pdb --heavy_chain H --light_chain L
```
预测出的结构和 AbodyBuilder 差不多，但是有些区域的精度 (temperature) 比较差。官方文档说可以用 Rosetta 优化。与 ref 对比： RMSD=0.353。
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011803209.png)

#### 使用 ABlooper 优化预测精度

默认 Ablooper 输出的模型精度较差。可以用 PyRosetta 来优化精度。

##### 安装 PyRosetta

获取 license：[https://www.rosettacommons.org/software/license-and-download](https://www.rosettacommons.org/software/license-and-download)

下载 zip 文件包，见 [https://www.pyrosetta.org/downloads#h.abjy686qantw](https://www.pyrosetta.org/downloads#h.abjy686qantw) 说明。

打开 conda 环境，解压并用 安装 pyRosetta。

```powershell
conda activate ab-env # 激活环境
# 安装 pyRosetta
cd setup
python setup.py install
# 在 python 命令行中，测试是否正确安装
>>> import pyrosetta
>>> pyrosetta.init()
```
更多 PyRosetta 介绍见：[https://new.rosettacommons.org/docs/latest/scripting_documentation/PyRosetta/PyRosetta](https://new.rosettacommons.org/docs/latest/scripting_documentation/PyRosetta/PyRosetta)。
##### 运行 ABlooper 优化

```powershell
# 运行 ABlooper 优化
ABlooper ABlooper_model.pdb --output ABlooper_model_opt.pdb --side_chains
```
优化后，预测出的结构和解析出的结构已经极为相似了。与 ref 对比：RMSD = 0.391。
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613011805470.png)

## 抗体抗原 dock

目前看到有两种方法比较适合抗体抗原 Docking，即 RosettaDock 和 SnugDock。看的也有用 zDock 的。

### RosettaDock 使用

#### 安装依赖包

```powershell
# 需在 python2 安装 biopython 依赖包
sudo apt-get install python2
sudo apt-get install python-dev
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
sudo python2 get-pip.py
pip2 install biopython==1.76
```
#### 预处理用于 Docking 的输入模板

##### 清洗 PDB 文件

```powershell
# Get hemagglutinin (chains A and B) from 3GBM
python2 $ROSETTA_PATH/tools/protein_tools/scripts/clean_pdb.py 3GBM AB
python2 $ROSETTA_PATH/tools/protein_tools/scripts/pdb_renumber.py --norestart 3GBM_AB.pdb 3gbm_HA.pdb

# Get the antibody (chains H and L) from 3GBN
python2 $ROSETTA_PATH/tools/protein_tools/scripts/clean_pdb.py 3GBN HL

pymol 3GBN_HL.pdb
# Delete residue in pymol cmd and save. Residues 121-160 of the heavy chain (chain H) and residues 268-311 of the light chain (chain L)
sele to_delete, resi 121-160+268-311
remove to_delete
save 3GBN_trim.pdb, 3GBN_HL

# Numbering
python2 $ROSETTA_PATH/tools/protein_tools/scripts/pdb_renumber.py --norestart 3GBN_trim.pdb 3gbn_Ab.pdb
```
##### 封闭 chain break

这里需要封闭在 L 链的 Ser-127 and Val-128 之间的 chain break。Chain break 会在 docking 期间引起意外情况。因为这种 chain break 很小，远离对接的interface，所以可以简单快速的修复。 目标只是封闭二维结构元素内的 chain break，而不是严格构建这个 loop。 建立 10 个模型（以最小计算代价），选择一个分数较好且有代表性的结构。

```powershell
# show chain break residues
pymol 3gbn_Ab.pdb
as cartoon # or `as ribbon`
color red, resi 125-130  
# Prepare files for chain break fix, *.options and *.loops
vim chainbreak_fix.loops # write 'LOOP 125 130 0 0 1'
# cp chainbreak_fix.options from input_files folder

# Chain break fix ~10 min
$ROSETTA_PATH/source/bin/loopmodel.default.linuxgccrelease @chainbreak_fix.options -nstruct 10 >& chainbreak_fix.log

pymol 3gbn_Ab*pdb  # visulaze using pymol
sort -nk 2 chainbreak_fix.fasc # check best models
# Copy the best scoring model to 3gbn_Ab_fixed.pdb
cp 3gbn_Ab_0002.pdb 3gbn_Ab_fixed.pdb
```
##### Repack 或 relax 模板结构

通常需要重新包装 (repack) 以除去由晶体结构中的得分函数识别的小冲突。 HA 界面内的某些氨基酸严格保守，并且它们的构象已被证明对于对接的成功至关重要。 RosettAscripts 允许使用任务操作系统对这些细节进行精细控制。

**Repack.options:**

|Option|Details|
|:----|:----|
|in|-in:file:fullatom|
|out|-out:file:fullatom|
|linmem_ig|-linmem_ig 10|
|others|-ex1-ex2-use_input_sc-score:weights ref2015.wts|

**Repack.xml:**

|Mover|Score_function|Details|
|:----|:----|:----|
|Repack|REF2015|Ops=ifcl,rtr|
|Minimize_sc|REF2015|chi="1" bb="0" jump="0" type="dfpmin_armijo_nonmonotone" tolerance="0.0001"|

**Repack_HA.xml:**

|Mover|Score_function|Details|
|:----|:----|:----|
|Repack|REF2015|Ops=ifcl,rtr,prfrp|
|Minimize_sc|REF2015|chi="1" bb="0" jump="0" type="dfpmin_armijo_nonmonotone" tolerance="0.0001"|

```powershell
# Repack or relax the template structures
# Copy configuration files from input_files dir. 3 files: repack.xml, repack_HA.xml, repack.options
cp ../../tutorials/protein-protein_docking/input_files/repack* .
# Run XML script
$ROSETTA_PATH/source/bin/rosetta_scripts.default.linuxgccrelease @repack.options -s 3gbm_HA.pdb -parser:protocol repack_HA.xml -out:file:scorefile repack_HA.fasc >& repack_HA.log 

$ROSETTA_PATH/source/bin/rosetta_scripts.default.linuxgccrelease @repack.options -s 3gbn_Ab_fixed.pdb -parser:protocol repack.xml -out:file:scorefile repack_Ab.fasc >& repack_Ab.log

# Copy the best scoring HA model to 3gbm_HA_repack.pdb and the best scoring antibody model to 3gbn_Ab_repack.pdb.
cp 3gbm_HA_0001.pdb 3gbm_HA_repacked.pdb
cp 3gbn_Ab_fixed_0001.pdb 3gbn_Ab_repacked.pdb

```
##### 调整抗体到合适的起始构象

使用有关参与界面残基的可用信息可减少全局构象搜索空间。这提高了对接过程的效率和最终模型的质量。在此基准情况下，我们将使用理想的起始构象。

```powershell
# Copy 原始 PDB 文件到当前目录
cp ../../tutorials/protein-protein_docking/input_files/3gbm_native.pdb .
# 使用 PyMol 来对齐结构
pymol 3gbm_native.pdb 3gbm_HA_repacked.pdb 3gbn_Ab_repacked.pdb
align 3gbn_Ab_repacked, 3gbm_native
save 3gbm_HA_3gbn_Ab.pdb, 3gbm_HA_repacked + 3gbn_Ab_repacked

# Renumber the pdb from 1 to the end without restarting.
python2 $ROSETTA_PATH/tools/protein_tools/scripts/pdb_renumber.py --norestart 3gbm_HA_3gbn_Ab.pdb 3gbm_HA_3gbn_Ab.pdb

```
#### 使用 RosettaScripts 应用来做 Docking

##### 执行 docking，理解各配置文件内容

**Docking.options:**

|Option|Details|
|:----|:----|
|docking|-docking                    # the docking option group        -partners AB_HL     # set rigid body docking partners        -dock_pert 3 8       # set coarse perturbation parameters (degrees and angstroms)        -dock_mcm_trans_magnitude 0.1   # refinement translational perturbation        -dock_mcm_rot_magnitude 5.0      # refinement rotational perturbation|
|s|-s 3gbm_HA_3gbn_Ab.pdb                    # input model|
|run:max_retry_job|-run:max_retry_job 10                           # if the mover fails, retry 50 times|
|use_input_sc|-use_input_sc                                           # add the side chains from the input pdb to the rotamer library|
|out|-out                                     # out option group        -file                              # out:file option group                -scorefile docking.fasc   # the name of the model score file|
|others|-ex1        # increase rotamer bins to include mean +- 1 standard deviation-ex2       # increase rotamer bins to include mean +- 2 standard deviations-score:weights ref2015.wts       # Set ref2015 as default score function|

**Docking_full.xml:**

|Mover|Score_function|Details|
|:----|:----|:----|
|dock_low, Docking|REF2015|score_low="score_docking_low" score_high="REF2015" fullatom="0" local_refine="0" optimize_fold_tree="1" conserve_foldtree="0" ignore_default_docking_task="0" design="0" task_operations="ifcl,prfrp" jumps="1"|
|srsc, SaveAndRetrieveSidechains|REF2015|allsc="0" |
|dock_high, Docking|REF2015|score_low="score_docking_low" score_high="REF2015" fullatom="1" local_refine="1" optimize_fold_tree="1" conserve_foldtree="0" design="0" task_operations="ifcl,prfrp" jumps="1"|
|Minimize_interface, FastRelax|REF2015|repeats="1" task_operations="ifcl,rtr,rtiv,prfrp"|

```powershell
# 拷贝 Docking 的 xml 文件到当前目录，并理解其内容
cp ../../tutorials/protein-protein_docking/input_files/docking_full.xml .
# 拷贝 docking 的 options 配置文件，并理解其内容
cp ../../tutorials/protein-protein_docking/input_files/docking.options .
# Docking
$ROSETTA_PATH/source/bin/rosetta_scripts.default.linuxgccrelease @docking.options -parser:protocol docking_full.xml -out:suffix _full -nstruct 10 >& docking_full.log

```
##### 和 naive structure 做对比

通过 Rosetta energy function，最小化与实验验证结构之间的差异。和上面 docking 步骤相比，只是 protocol 不同，跳过了 coarse 和 fine resolution search 步骤，只留下最小化步骤。使得我们可以对相似结构做对比。

```powershell
# 拷贝 Docking 的 xml 文件到当前目录，并理解其内容。和上面 docking_full.xml 之间的差异只在 PROTOCOL 区域，dock_low, srsc, 和 dock_high 未被使用。
cp ../../tutorials/protein-protein_docking/input_files/docking_minimize.xml .
# Docking
$ROSETTA_PATH/source/bin/rosetta_scripts.default.linuxgccrelease @docking.options -parser:protocol docking_minimize.xml -out:suffix _minimize -nstruct 2 >& docking_minimize.log 
```
#### 模型说明并分析各 funnel 的数据

RosettAscript中有许多 movers 和 filters 可用于 model 的表征。InterfaceAnalyzer mover 将许多 movers 和 filters 结合到单个 mover 中。 RMSD filter 可用于基准测试。

在此步骤，上面清洁得到的 3gbm_native.pdb 用作比较的初始结构。需要完整的结构来做模型比较。通过 loop 建模或嫁接 3gbn.pdb 的片段修复缺失密度。


##### 通过 InterfaceAnalyzer mover 分析生成的模型，并用 RMSD filter 计算 RMSD

```powershell
# 拷贝分析的 xml 和 options 配置文件到当前目录，并理解其内容。
cp ../../tutorials/protein-protein_docking/input_files/docking_analysis.xml .
cp ../../tutorials/protein-protein_docking/input_files/docking_analysis.options .

# Docking analysis
$ROSETTA_PATH/source/bin/rosetta_scripts.default.linuxgccrelease @docking_analysis.options -in:file:s *full*pdb *minimize*pdb >& docking_analysis.log

# sort resulting file
sort -nk 7 docking_analysis.csv
# visualize using pymol
pymol 3gbm_native.pdb 3gbm_HA_3gbn_Ab_full_0001.pdb
align 3gbm_HA_3gbn_Ab_full_0001, 3gbm_native # pymol cmd
```
##### 对比 RMSD 与各种结构分值，如 total_score, dG_separated 等来识别 binding funnel (漏斗)

```powershell
# 用 libreoffice 画一个 scatter plot。
libreoffice docking_analysis.csv &

# 或者用提供的 R 脚本来画 score vs rmsd 图
cp ../../tutorials/protein-protein_docking/input_files/sc_vs_rmsd.R .
Rscript ./sc_vs_rmsd.R docking_analysis.csv total_score
Rscript ./sc_vs_rmsd.R docking_analysis.csv dG_separated
Rscript ./sc_vs_rmsd.R docking_analysis.csv dG_separated.dSASAx100
eog *png &
```


### SnugDock 局部优化

ROSIE 平台任务提交入口：[https://rosie.rosettacommons.org/snug_dock/submit](https://rosie.rosettacommons.org/snug_dock/submit)

说明：[https://rosie.rosettacommons.org/snug_dock/documentation](https://rosie.rosettacommons.org/snug_dock/documentation)

需要提交一个已经 dock 好的模板。试了用 RosettaDock 的结果作为输入是可行的。已提交任务，但是目测特别慢。[https://rosie.rosettacommons.org/queue](https://rosie.rosettacommons.org/queue)


### zDock

在 Rosetta 中，有进行支持。


### Absolut！只考虑 CDRH3

[https://doi.org/10.1101/2021.07.06.451258](https://doi.org/10.1101/2021.07.06.451258)

步骤：Steps to generate 3D-antibody-antigen binding complexes:

1. creates a lattice representation of the antigen, i.e. discretization, using LatFit (48) software

2. calculate the energetically optimal binding of a CDRH3 sequences to a lattice-discretized antigen. using Miyazawa-Jernigan energy potential

3. validatd that Absolut! generated dta reflects to a certain extent the biological complexity in experimental antibody-antigen binding

## 抗体设计

蛋白设计定义：Protein design seeks to find potential amino acid sequences that can maintain at least one previously determined, stable 3D protein structure.

抗体设计定义：Antibody design modifies the sequence of an antibody to improve antibody affinity, specificity, and breadth, guided by knowledge-based sampling strategies.

蛋白/抗体设计包括单状态设计 (single-state design， SSD) 和多状态设计 (multistate design，MSD)。设计的软件包括 RosettaAntibodyDesign  (RAbD) 和 AbDesign。


单状态设计的几个示例：

i. Design with Noncanonical Amino Acids. 

ii. Design of Supercharged Single-Chain Variable Fragments (scFv’s).

iii. Balancing between Sampling and Stability.


多状态设计的几个示例：

i. Multistate Design for Negative Design Tasks.

ii. Computational Design of Non-Immunoglobin Epitope Binders.
