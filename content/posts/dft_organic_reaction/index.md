---
title: "DFT 有机反应建模"
subtitle: ""
date: 2025-10-20
draft: false
author: "Xiaopeng Xu"
description: "DFT 有机反应建模相关笔记。"
tags: ["DFT", "Chemistry"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 密度泛函理论 \(DFT\) 简介

密度泛函理论 \(DFT\) 是一种计算量子力学建模方法，用于物理学、化学和材料科学，研究多体系统（特别是原子、分子和凝聚相）的电子结构（或核结构）（主要是基态）。利用该理论，可以通过使用泛函来确定多电子系统的属性 \- 即接受函数作为输入并输出单个实数的函数。对于 DFT，这些是空间相关电子密度的泛函。DFT 是凝聚态物理学、计算物理学和计算化学中最流行和用途最广泛的方法之一。

## Gaussion 16 介绍

Gaussian 16 从量子力学的基本定律出发，预测各种化学环境中化合物和反应的能量、分子结构、振动频率和分子特性。Gaussian 16 的模型既可以应用于稳定物种，也可以应用于难以或无法通过实验观察到的化合物，无论是由于其性质（例如毒性、可燃性、放射性）还是其固有的短暂性（例如短暂的中间体和过渡结构）。

使用 Gaussian 16，您可以彻底研究您感兴趣的化学问题。例如，您不仅可以快速可靠地最小化分子结构，还可以预测过渡态的结构，并验证预测的驻点实际上是最小值还是过渡结构（视情况而定）。您可以继续按照本征反应坐标 \(IRC\) 计算反应路径，并确定哪些反应物和产物由给定的过渡结构连接。一旦您完全了解了势能面，就可以准确预测反应能量和障碍。您还可以预测各种化学性质。

支持网站：https://gaussian\.com/techsupport/

### 使用简介

iBex 上面已经有这个程序，可以直接使用。

```PowerShell
module load gaussian16

# Demo case
g16 < test.gjf > test.out
```

其中的关键是 gjf 配置文件和 slurm 运行脚本。

参考链接：[Running Gaussian 16 on CCAST Clusters](https://kb.ndsu.edu/it/page.php?id=135576#:~:text=Gaussian%2016%20uses%20a%20plain,other%20parameters%20for%20the%20calculation.)。

### gjf 配置文件

参考：[Running Gaussian](https://gaussian.com/running/)。

```PowerShell
%nprocshared=4
%mem=4gb
%rwf=crotonophenone.rwf
%nosave
%chk=crotonophenone.chk
%lindaworkers=
#p opt=cartesian b3lyp/3-21g nosymm

! this is a comment, and it is ignored by Gaussian
water molecule energy and geometry optimization

Structure optimization 3-methyl-2-cyclopenten-1-one

0 1
  C       -4.534810        -0.132847        -0.003819
  C       -3.414537         0.893678        -0.013650
  C       -2.139283         0.169386        -0.008537
  C       -3.820202        -1.496587         0.007301
  H       -5.160304         0.007832        -0.876638
  H       -5.158770         0.022860         0.867546
  C       -2.341859        -1.150612         0.003016
  H       -4.071150        -2.101454        -0.858358
  H       -4.069611        -2.086443         0.883697
  C       -1.304643        -2.225378         0.011365
  H       -0.303458        -1.815725         0.006958
  H       -1.414552        -2.868650        -0.856502
  H       -1.413021        -2.853601         0.890377
  H       -1.193705         0.670893        -0.013693
  O       -3.569596         2.104036        -0.023940
```

### slurm 运行脚本

参考 iBex 上 gaussion 16 的 example。

```PowerShell
#!/bin/bash
#SBATCH --partition=batch
#SBATCH --job-name="gaussian16"
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:8
#SBATCH --constraint=v100
#SBATCH --time=4:00:00
#SBATCH --err=std.err
#SBATCH --output=std.out
#----------------------------------------------------------#
module load gaussian16/c.02
ulimit -c 0
ulimit -d hard
ulimit -f hard
ulimit -l hard
ulimit -m hard
ulimit -n hard
ulimit -s hard
ulimit -t hard
ulimit -u hard
export GAUSS_SCRDIR=`pwd`
#----------------------------------------------------------#
echo "The job "${SLURM_JOB_ID}" is running on "${SLURM_JOB_NODELIST}
export OMP_NUM_THREADS=8 # Please use this to control the number of cores for shared memory parallelization

#---  Edit Below according to your needs:  ----------------#
#
# !!! Notes - GPU is not always fast as you expected:
# !!!   See https://gaussian.com/gpu/ for limitatons/caveats of GPU runs
#
# Set GAUSS_CDEF; This will be overridden by %cpu in the input file
export GAUSS_CDEF=0-7
# Set GAUSS_GDEF; This will be overridden by %gpucpu in the input file
export GAUSS_GDEF=1=0
#----------------------------------------------------------#
#Gaussian Efficiency Considerstions: http://www.lct.jussieu.fr/manuels/Gaussian03/g_ur/m_eff.htm
#Gaussian_Error_Messages: https://www.ace-net.ca/wiki/Gaussian_Error_Messages
time ${GAUSSIAN16_HOME}/g16 < test.gjf > test.out
```
