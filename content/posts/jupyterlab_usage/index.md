---
title: "Jupyterlab 使用"
subtitle: ""
date: 2026-05-14
draft: false
author: "Xiaopeng Xu"
description: "JupyterLab 使用笔记：常用操作与配置技巧。"
tags: ["JupyterLab", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 本地命令行打开 JupyterLab

```Plaintext
jupyter lab # 基础命令
nohup  jupyter-lab --no-browser --ip="0.0.0.0" 2>&1 & # 后台运行命令
```

## Slurm 运行 Jupyter lab 交互分析

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

## Jupyter AI 安装 及使用

### 安装

```Python
pip install "jupyter-ai==3.0.0b7"
```

安装完成后，请导航到工作目录并通过输入 `jupyter lab` 启动 JupyterLab。您现在应该可以在左侧边栏看到聊天气泡图标。

注意：3\.0\.0b8 测试版是在本课程录制后发布的。欢迎您探索最新版本，因为它具有增强的用户界面。

### 在 JupyterLab 中设置 LLM 提供商

在开始与 Jupyter AI 交互之前，您需要配置模型提供商和 API 密钥（此步骤在本课程中已预先设置好）：

1. 点击顶部菜单栏中的 Settings \(设置\)。

2. 从下拉菜单中选择 AI Settings \(AI 设置\)（在最新版本中，它被称为 Jupyternaut Settings）。

3. 在 Chat model \(聊天模型\) 下，选择您偏好的模型（本课程使用 `openai/gpt-5-chat-latest`），然后点击 Update Chat Model \(更新聊天模型\)。

4. 在 Secrets and API keys \(密钥和 API 密钥\) 下，输入您的 API 密钥。
