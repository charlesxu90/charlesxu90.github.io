---
title: "Slurm 常用命令"
subtitle: ""
date: 2020-10-24
draft: false
author: "Xiaopeng Xu"
description: "Slurm 作业调度常用命令速查（HPC 集群）。"
tags: ["Slurm", "HPC", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 相关培训

[https://www\.hpc\.kaust\.edu\.sa/content/data\-science\-training](https://www.hpc.kaust.edu.sa/content/data-science-training)

包括：

1. Trillion\-parameter scale model training and inference with DeepSpeed

    1. Codes: [https://github\.com/kaust\-rccl/deepspeed\_workshop/tree/master/HelloDeepSpeed](https://github.com/kaust-rccl/deepspeed_workshop/tree/master/HelloDeepSpeed), [https://github\.com/microsoft/Megatron\-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed)

2. Introduction to Containers on KSL Platforms

3. High Throughput Hyperparameter Optimization on KSL platforms

4. Distributed Deep Learning on KSL platforms

5. Data Science on\-boarding on KSL platforms

## 基础操作

### 登录 iBex

外网时，需要先连接 KAUST VPN。通常使用 Cisco anyconnect

登录 iBex：

```PowerShell
ssh -X xux@glogin.ibex.kaust.edu.sa
```

### sinfo 查看系统资源池

```Plaintext
sinfo # 系统资源及其状态/可用性的简明视图
sinfo --Node --long # 查看 node 信息，更清晰
```

结果：

```Shell
Sat Nov 13 20:44:08 2021
NODELIST      NODES  PARTITION       STATE CPUS    S:C:T MEMORY TMP_DISK WEIGHT AVAIL_FE REASON
besest112-02      1     batch*       mixed 80     8:10:1 152000        0   1540 ibex2017 none
cn506-02-l        1     batch*       mixed 128    2:64:1 486400        0    150 dragon,c none
cn506-02-r        1     batch*       mixed 128    2:64:1 486400        0    150 dragon,c none
```

### ginfo 查看 GPU 资源池

```Plaintext
ginfo # 用于查询 Ibex 集群上的 GPU 资源状态的内部工具
```

结果：

```Shell
GPUS currently in use:
GPU Models:          Total  Used  Free
gtx1080ti               64    10    54
p100                    12     2    10
p6000                    4     0     4
rtx2080ti               32     5    27
v100                   274   236    38
              Total:   386   253   133
```

### squeue/scancel 查看和释放计算资源

```Python
squeue -u $USER 
# squeue 可以查看用户下的 job 列表
scancel $job_id
# 取消 job，也可用 scancel -u $USER -i 交互式的取消任务或用 
```

### 查看任务详情

```Python
scontrol show jobid -dd 35126195
# JobId=35126195 JobName=run_scripts.slurm
#    UserId=xux(129052) GroupId=g-xux(1129052) MCS_label=N/A
#    Priority=341 Nice=0 Account=pi-gaox QOS=normal
#    JobState=PENDING Reason=Priority Dependency=(null)
#    Requeue=1 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
#    DerivedExitCode=0:0
#    RunTime=00:00:00 TimeLimit=17:00:00 TimeMin=N/A
#    SubmitTime=2024-09-15T11:31:59 EligibleTime=2024-09-15T11:31:59
#    AccrueTime=2024-09-15T11:31:59
#    StartTime=2024-09-15T18:13:43 EndTime=2024-09-16T11:13:43 Deadline=N/A
#    SuspendTime=None SecsPreSuspend=0 LastSchedEval=2024-09-15T13:11:18 Scheduler=Main
#    Partition=gpu,gpu24,gpu72 AllocNode:Sid=login510-27:2042328
#    ReqNodeList=(null) ExcNodeList=(null)
#    NodeList= SchedNodeList=gpu108-23-r
#    NumNodes=1-1 NumCPUs=4 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
#    ReqTRES=cpu=4,mem=32G,node=1,billing=4,gres/gpu=2
#    AllocTRES=(null)
#    Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
#    MinCPUsNode=1 MinMemoryNode=32G MinTmpDiskNode=0
#    Features=a100 DelayBoot=00:00:00
#    OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
#    Command=/ibex/user/xux/Enzyme_design/Savinase_AAPF_opt/second_round/run_scripts.slurm
#    WorkDir=/ibex/user/xux/Enzyme_design/Savinase_AAPF_opt/second_round
#    StdErr=/ibex/user/xux/Enzyme_design/Savinase_AAPF_opt/second_round/log-run_scripts.slurm-35126195.out
#    StdIn=/dev/null
#    StdOut=/ibex/user/xux/Enzyme_design/Savinase_AAPF_opt/second_round/log-run_scripts.slurm-35126195.out
#    CpusPerTres=gres/gpu:2
#    TresPerNode=gres/gpu:2
```

### 查看任务使用的 CPU 数和核数

```Python
squeue -o"%.7i %.9P %.8j %.8u %.2t %.10M %.6D %C" -u xux
#   JOBID PARTITION     NAME     USER ST       TIME  NODES CPUS
# 3487192     workq Bestzyme      xux  R      54:06      1 64
```

## 交互式命令运行

注意：退出后，任务会关闭。

### salloc 申请计算资源

#### 示例：1 GPU，4 CPU，16G 内存，24 小时

```Python
# Apply gpu node
salloc --cpus-per-task=1 --gres=gpu:1 --mem=64GB --time=24:00:00
# gpu510-17 is allocated
```

### 请求资源，并交互式运行 （开发测试用）

```Python
srun --pty bash -i 
# 或用 srun --jobid=16168977 -u --pty bash -i

# iBex
srun --time=4:00:00 --nodes=1 --gpus-per-node=1 --cpus-per-task=10 --ntasks=1 --mem=20G --constraint='a100' --pty bash -c '/bin/bash'

# Shaheen
srun --time=4:00:00 --nodes=1 --cpus-per-task=8 --ntasks=1 --mem=20G --pty bash -c '/bin/bash'
```

### 运行命令

```Python
python HelloWorld.py
```

## 磁盘空间操作

### iBex 查看磁盘空间

```Shell
# 个人磁盘空间
$ bquota                                                [22:12:27]
Quota information for IBEX filesystems:
Scratch  (/ibex/scratch):  Used: 37.09 GB Limit: 1536.00 GB
 
# 项目磁盘空间
$ bquota -g ibex-c2108                                  [22:39:38]
Quota information for IBEX filesystems:
Fast Scratch (/ibex/fscratch): Used: 0.00 GB Limit:  0.00 GB
Projects (/ibex/scratch/projects): Used: 8894.87 GB Limit: 8192.00 GB

# 加密磁盘空间
 df -Th /ibex/project/e3017
```

### Shaheen 查看磁盘空间

```Shell
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

### 转移数据到另一个项目

```Shell
# 拷贝数据到新项目
cp -r old-folder new-path
 
# 删除原数据
rm -rf old-folder
```

## 运行 Jupyter lab 交互分析

### sbatch 脚本示例: run\-jupyter\-server\.sbatch

```PowerShell
#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH --partition=debug
#SBATCH --constraint=intel
#SBATCH --job-name=jupyterlab
#SBATCH --mail-type=ALL
#SBATCH --output=./%x-%j.out
#SBATCH --error=./%x-%j.err

# use srun to launch Jupyter server in order to reserve a port
srun --resv-ports=1 ./run-jupyter-server.srun
```

### srun 脚本: run\-jupyter\-server\.srun

参考：[https://github\.com/kaust\-vislab/sklearn\-data\-science\-project/blob/master/bin/launch\-jupyter\-server\.srun](https://github.com/kaust-vislab/sklearn-data-science-project/blob/master/bin/launch-jupyter-server.srun)

```PowerShell
#!/bin/bash

# setup the environment
#module purge
#conda activate ./env

# setup ssh tunneling
export XDG_RUNTIME_DIR=/tmp
IBEX_NODE=$(hostname -s)
KAUST_USER=$(whoami)
JUPYTER_PORT=$SLURM_STEP_RESV_PORTS

echo "Creat a port tunnel using the command below in the local machine:
ssh -NfL ${JUPYTER_PORT}:${IBEX_NODE}:${JUPYTER_PORT} ${KAUST_USER}@glogin.ibex.kaust.edu.sa
" >&2

# launch jupyter server
jupyter lab --no-browser --port=${JUPYTER_PORT} --ip=${IBEX_NODE}
```

ssh \-NfL 12481:dgpu609\-14:12481 xux@ilogin\.ibex\.kaust\.edu\.sa

### 运行程序

```Plaintext
sbatch run-jupyter-server.sbatch
```

### 接口转发

#### ssh tunnel 服务端口转发

要在本地使用 Jupyter lab，因为不能访问 ibex gpu 端口的原因，需要使用 ssh tunnel 来做一下转发。

```Python
ssh -NfL 8888:gpu510-12:8888 xux@glogin.ibex.kaust.edu.sa
# 其中，gpu510-12:8888 是所分配节点的名称和端口
# ssh time is short
```

#### 关闭接口转接

```Python
ps aux | grep ssh
#xux              34504   0.0  0.1  4321984  15856   ??  Ss    1:37PM   0:00.11 ssh -NfL 12481:dgpu609-14:12481 xux@ilogin.ibex.kaust.edu.sa
kill 34504
```

### 在本机端口上访问 Jupyterlab

```Python
http://localhost:8888/lab?token=<YOUR_TOKEN>
# 其中，port 和 token 要根据 jupyterlab.err 中的信息进行更新
```

## 提交运行 Python 脚本

参考：[https://github\.com/kaust\-vislab/pytorch\-gpu\-data\-science\-project](https://github.com/kaust-vislab/pytorch-gpu-data-science-project)

### sbatch 脚本示例

参考：[https://github\.com/kaust\-vislab/sklearn\-data\-science\-project/blob/master/bin/launch\-jupyter\-server\.sbatch](https://github.com/kaust-vislab/sklearn-data-science-project/blob/master/bin/launch-jupyter-server.sbatch)

```Python
#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH --partition=debug
#SBATCH --constraint=intel
#SBATCH --job-name=run_chem_lstm
#SBATCH --mail-type=ALL
#SBATCH --output=./%x-%j-slurm.out
#SBATCH --error=./%x-%j-slurm.err

# Run script
#python -m smiles_lstm_hc.distribution_learning
python -m smiles_lstm_hc.goal_directed_generation
python -m smiles_lstm_hc.train_smiles_lstm_model
#python -m smiles_lstm_ppo.goal_directed_generation
```

#### Request resources for distributed learning

```Plaintext
#!/bin/bash 
#SBATCH --nodes=2
#SBATCH --gpus-per-node=8
#SBATCH --cpus-per-gpu=2 
#SBATCH --mem=64G 
#SBATCH --constraint="v100" 
#SBATCH --time=24:00:00 
#SBATCH --partition=batch 
#SBATCH --output=log-%x-slurm-%j.out 
#SBATCH --error=log-%x-slurm-%j.err
```

### sbatch 脚本提交

```Python
sbatch run_lstm.sbatch
```

## 其他

### module load 安装包

对于一些系统底层依赖，自己又无 sudo 权限安装时，需要用 module load 来安装已经提供的包。典型的问题：lib64/libstdc\+\+\.so\.6: version \`GLIBCXX\_3\.4\.26' not found

```Python
module avail #查看可用包
module load gcc/11.1.0 #安装包
module unload gcc/11.1.0 #卸载包
```

- Conda：[Introduction to Conda for \(Data\) Scientists](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)

- Shaheen II：[https://www\.hpc\.kaust\.edu\.sa/user\_guide](https://www.hpc.kaust.edu.sa/user_guide)
