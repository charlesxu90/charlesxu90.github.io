---
title: "GROMACS 分子动力学模拟"
subtitle: ""
date: 2025-01-01
draft: false
author: "Xiaopeng Xu"
description: "GROMACS 分子动力学模拟相关笔记。"
tags: ["GROMACS", "Molecular Dynamics"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## MD simulation \(Gromacs\)



相关代码库见 https://github\.com/charlesxu90/enzyme\-md。

## 请求 Shaheen 资源并运行

```Plain Text
srun --time=4:00:00 --nodes=1 --cpus-per-task=8 --ntasks=1 --mem=20G --pty bash -c '/bin/bash'
```

## MD结构预处理

AF２ 预测的结构无需特殊处理，直接按照上述步骤执行即可．

PDB 中真实的蛋白结构，需要做预处理，如加氢，修补缺失氨基酸等．可以使用 [PDBFixer](https://github.com/openmm/pdbfixer) 来做．

### AF2 预测蛋白结构，后面可以用 chai\-1 /AF3来预测结果

1. 将多序列 fasta 转化为单序列 fasta

```PowerShell
awk 'BEGIN{RS=">";FS="\n"} NR>1{fnme=$1".fasta"; print ">" $0 > fnme; close(fnme);}' final_sel_pos_seq.csv_polym_290.fasta
```

2. local\_colabfold 预测蛋白结构

```PowerShell
colabfold_batch --templates --amber /home/xiaopeng/Desktop/Polym_design/Taq_pol/Taq_opt/data/round0/mut_compute/af2 /home/xiaopeng/Desktop/Polym_design/Taq_pol/Taq_opt/data/round0/mut_compute/af2/outputdir
```

注意：最好在 localcolabfold 项目目录下运行上述命令，不然需要下载 AF2 的模型结，会多耗时间．

## 跑 MD simulations

1. 下载文件，并上传到 shaheen，并解压

```PowerShell
# scp xux@10.73.43.118:/home/xux/Laptop-backups/Desktop/BestzymeP/MD/MD_results/2nd_round/Round2_pdbs.zip .
scp -r xux@10.73.43.118:/home/xux/Laptop-backups/Desktop/BestzymeP/MD/MD_results/4th_round .
unzip Round2_pdbs.zip
rm Round2_pdbs.zip
```

2. 对每个文件创建对应的文件夹

```PowerShell
cd Round2_pdbs
# AF2 pdbs
for i in *.pdb; do mkdir -p "${i%.*}"; mv $i "${i%.*}"/original.pdb ; done

# Chai-1 pdbs
for i in `ls -d */`; do echo $i; mv $i/pred.model_idx_0.pdb $i/original.pdb ; done

# mv mt96/mt96.pdb to mt96/original.pdb
for i in `ls -d */`; do echo $i/*.pdb; mv $i/*.pdb $i/original.pdb; done
```

3. 拷贝对应的任务运行脚本到各文件夹

```PowerShell
for i in `ls -d */`; do echo $i; cp /home/xux/k10098/enzyme-md/enzyme-md-git/example/prepare_md.sbatch $i; done
for i in `ls -d */`; do echo $i; cp /home/xux/k10098/enzyme-md/enzyme-md-git/example/run_md.sbatch $i; done
```

4. 运行预处理任务（可省略）

```PowerShell
# prepare_md.sbatch
for i in `ls -d */`; do cd $i; sbatch prepare_md.sbatch; cd .. ; done

# copy and run at the same time
for i in `ls -d */`; do echo $i; cp prepare_md.sbatch $i; cd $i; sbatch prepare_md.sbatch; cd ..;  done
for i in `ls -d md_pdbs1/*/`; do echo $i; cp prepare_md.sbatch $i; cd $i; sbatch prepare_md.sbatch; cd ../..;  done
```

5. 拷贝到6份，运行 MD 任务

```PowerShell
mv Round2_pdbs/ run1
for i in {2..6}; do echo run$i; cp -r run1 run$i; done

# Run each copy individually
cd run1
for i in `ls -d */`; do cd $i; sbatch run_md.sbatch; cd .. ; done

# Run all copies together
for i in `ls -d run*/*/`; do cd $i; sbatch run_md.sbatch; cd ../.. ; done

# copy and run at the same time
 for i in `ls -d */*/`; do echo $i; cp run_md.sbatch $i; cd $i; sbatch run_md.sbatch; cd ../..;  done
```

6. 压缩为 tar\.gz 文件，并传到本地

```PowerShell
# Count total number of rmsf.xvg files
# ls 5th_round/md_pdbs*/*/rmsf.xvg | wc -l

# check which is not finished
cd 5th_round/md_pdbs1/
for i in `ls -d */`; do cd ..; echo $i; ls md_pdbs*/$i/rmsf.xvg| wc -l; cd md_pdbs1; done >> results_count.log
# modify log in vim using: :%s/\/\n/\t/g
tar -cvf 5th_round_results.tar 5th_round/md_pdbs*/*/rmsf.xvg
gzip 5th_round_results.tar
scp 5th_round_results.tar.gz xux@10.73.43.118:/home/xux/Laptop-backups/Desktop/BestzymeP/MD/MD_results/2nd_round/
mv 5th_round_results.tar.gz 5th_round
```



### Check quota

```PowerShell
sb k10098
lfs quota -uh $USERNAME /scratch

# 个人磁盘空间
$ kuq
Disk quotas for usr xux (uid 129052):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
       /scratch  4.683T      0k      0k       -  719410       0 1000000       -
       /project  6.715T      0k      0k       - 1000000*      0 1000000       - 

# 项目磁盘空间
$ kpq k10098
---------------------------------
PI quota for : Xin Gao
---------------------------------
Filesystem  used   quota   limit   grace   files   quota   limit   grace
/project  6.715T      0k     80T       - 1025376       0       0       -
/scratch    208k      0k      0k       -      16       0       0       -
```

## MD 测试分析结果运行过程

按上述步骤跑单个批次的任务。

通常需要针对不同条件重复下。因此需要针对性的一些脚本。

1. 创建重复的样本文件夹

```PowerShell
for i in `ls -d */`; do echo $i; mkdir /home/xux/scratch_sh/enzyme_md/savi_test/ph8/md_pdb1/$i; done
```

2. 拷贝对应的样本和脚本到相应的文件夹

```PowerShell
for i in `ls -d */`; do echo $i; cp $i/original.pdb /home/xux/scratch_sh/enzyme_md/savi_test/ph8/md_pdb1/$i; done
for i in `ls -d */`; do echo $i; cp $i/prepare_md.sbatch /home/xux/scratch_sh/enzyme_md/savi_test/ph8/md_pdb1/$i; done
for i in `ls -d */`; do echo $i; cp $i/run_md.sbatch /home/xux/scratch_sh/enzyme_md/savi_test/ph8/md_pdb1/$i; done
```

1. 拷贝对应的样本和脚本到相应的文件夹

### 分析 MD 结果

```PowerShell
conda activate /lustre2/project/k10098/xux/miniconda3/envs/enzyme-md-env
python /home/xux/k10098/enzyme-md/enzyme-md-git/scripts/analyze_rmsf.py -d ./  -r 3-268
```

## 跑含 Ca2\+ 的常规 MD

### 手动通过 ChimeraX 添加 Ca２\+

打开野生型含 ca的文件，删除除钙离子以外的其他原子．然后将删除后的文件与其他新的AF２预测结构进行 combine

```Scheme
combine #1,24 model #47
```

删除完毕后，选择combine结果，并将其对保存为 pdb 结构．

最好手动再检查一遍 combine 的结果．

### 将对应的文件拷贝进样本目录，并提交任务

```PowerShell
# Prepare for MD
for i in `ls -d md_pdbs1/*/`; do echo $i; cp *.mdp $i; cp prepare_md.sbatch $i; cd $i; sbatch prepare_md.sbatch; cd ../..;  done

# Copy for 5 Runs
for i in {2..5}; do echo md_pdbs$i; cp -r md_pdbs1 md_pdbs$i; done

# Run MD
 for i in `ls -d */*/`; do echo $i; cp run_md.sbatch $i; cd $i; sbatch run_md.sbatch; cd ../..;  done
```

#### 将原子分组 

```PowerShell
gmx make_ndx -f EM.gro -o index.ndx

1 & a CA  # Create Calcium group
2 | 17    # Create Calcium+Protein group 
name 18 Protein_CA # Rename the group name
! 18    # Create the group of the rest atoms
name 19 SOL_NA_CL # Rename the group name
q # 

# into one line
{ echo -e '1 & a CA'; echo -e '2 | 17'; echo -e 'name 18 Protein_CA'; echo -e '! 18'; echo -e 'name 19 SOL_NA_CL'; echo -e 'q'; } | gmx make_ndx -f EM.gro -o index.ndx

echo -e "1 & a CA \n 2 | 17 \n name 18 Protein_CA \n ! 18 \n name 19 SOL_NA_CL \n q\n" | gmx make_ndx -f EM.gro -o index.ndx
```

#### 运行MD

```PowerShell
# copy config files, copy and run prepare md
for i in `ls -d md_pdbs1/*/`; do echo $i; cp *.mdp $i; cp prepare_md.sbatch $i; cd $i; sbatch prepare_md.sbatch; cd ../..;  done

# copy into 5 replicas, and run md
for i in {2..5}; do echo md_pdbs$i; cp -r md_pdbs1 md_pdbs$i; done
for i in `ls -d */*/`; do echo $i; cp run_md.sbatch $i; cd $i; sbatch run_md.sbatch; cd ../..;  done

# proprocess the resulting trajectories
conda activate /lustre2/project/k10098/xux/miniconda3/envs/enzyme-md-env
echo -e "18\n" |  gmx trjconv -f MD.xtc -s MD.tpr -ur compact -pbc mol -o MD-compact.xtc -n index.ndx -dt 20
```

## Lasa MD

### 将 AF３ 预测的 PDB 拷贝到文件夹，并准备配置文件

```PowerShell
scp xux@10.67.24.210:/home/xux/Desktop/BestzymeP/Savi_opt/data/benchmark_md/top40_lasa_R4.csv-af3.tar.gz .
tar xvf top40_lasa_R4.csv-af3.tar.gz
cd top40_lasa_R4.csv-af3
for i in `ls -d */`; do echo $i; cp -r /home/hew/run/xux/lasa/top40_lasa_R4.csv-af3/lasa_template/* $i; done

# run prepar_md.sbatch
for i in `ls -d md_pdbs1/*/`; do echo $i; cp lasa_template/prepare_lasa_md.sbatch $i; cd $i; sbatch prepare_lasa_md.sbatch; cd ../..; done

# copy into 5 replica
for i in {2..5}; do echo md_pdbs$i; cp -r md_pdbs1 md_pdbs$i; done

# submit all MD jobs
for i in `ls -d md_pdbs*/*/`; do echo $i; cp lasa_template/run_lasa_md.sbatch $i; cd $i; sbatch run_lasa_md.sbatch; cd ../..; done
```

### 提交预处理任务并提交 MD 任务

```PowerShell
scp xux@10.67.24.210:/home/xux/Desktop/BestzymeP/Savi_opt/data/benchmark_md/top40_lasa_R4.csv-af3.tar.gz .
tar xvf top40_lasa_R4.csv-af3.tar.gz
cd top40_lasa_R4.csv-af3
for i in `ls -d */`; do echo $i; cp -r /home/hew/run/xux/lasa/top40_lasa_R4.csv-af3/lasa_template/* $i; done

# run prepar_md.sbatch
for i in `ls -d md_pdbs1/*/`; do echo $i; cp lasa_template/prepare_lasa_md.sbatch $i; cd $i; sbatch prepare_lasa_md.sbatch; cd ../..; done

# copy into 5 replica
for i in {2..5}; do echo md_pdbs$i; cp -r md_pdbs1 md_pdbs$i; done

# submit all MD jobs
for i in `ls -d md_pdbs*/*/`; do echo $i; cp lasa_template/run_lasa_md.sbatch $i; cd $i; sbatch run_lasa_md.sbatch; cd ../..; done
```

## 查看并录制 MD 视频

### 查看 MD 视频

```PowerShell
# create pdb file
for i in `ls -d run*/*/`; do cd $i;   echo "1" |  /lustre2/project/k10098/xux/enzyme-md/gmx_cph/install/bin/gmx trjconv -s MD.tpr -f MD.xtc -o prod_center_noSOL.pdb -dump 0 -n index.ndx ; cd ../.. ; done

# create xtc file
for i in `ls -d run*/*/`; do cd $i; echo -e "1\n1" > step5.input; cd ../.. ; done
for i in `ls -d run*/*/`; do cd $i;  /lustre2/project/k10098/xux/enzyme-md/gmx_cph/install/bin/gmx trjconv -s MD.tpr -f MD.xtc -o prod_center_noSOL.xtc -pbc mol -center -ur compact < step5.input; cd ../.. ; done


# open MD files with Pymol
pymol prod_center_noSOL.pdb prod_center_noSOL.xtc

# clear molecules other than protein
# remove hydrogens
# select water, resn hoh
# hide all
# show cartoon, not water

# play by click the "Play" button
```

### 录制 MD 视频

```PowerShell
# Use the default video tool in MacOS for recording
Shift-Command-5
```

## Ys MD 
