---
title: "Cloud 常用命令"
subtitle: ""
date: 2024-02-08
draft: false
author: "Xiaopeng Xu"
description: "云服务 / 云平台常用命令速查。"
tags: ["Cloud", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Google cloud 操作

### 增加 ssh key

```PowerShell
ssh-keygen # -t rsa -b 4096 -C account_name
# copy the content in *.pub to google cloud user keys.
```

### VM 相关

#### 创建和删除 VM

在 web 界面中按步骤操作即可。

注意：

1. 在高级选项中的 availability policies，课选择 spot。可大幅减少计算成本。
使用 Admin 创建的 image，可以使用 NFS，已有 environment。

#### 登录 VM

使用 gcloud 登录较为方便，命令如下

```PowerShell
gcloud compute ssh --zone "us-central1-c" "xux-a100-test"  --project "pi-xin"
```

#### 关闭 VM

有时候 A100 80G 的 GPU 无法在界面中关闭，这时候需要在命令行中关闭。

```PowerShell
sudo shutdown now
```

### NFS 相关

#### 加载 NFS

使用 Saif 的 image，可自动加载 NFS

使用 Saif 创建的 NFS，可以长期保存计算数据和环境

1. 需要使用 Saif 的 image 来创建 instance

2. 创建 instance 后，需要运行 shell 命令来加载 instance

```PowerShell
sudo /scratch/ADMIN/enviornment.sh
# then type the current username
```

#### 上传和下载文件

```PowerShell
rsync -a -e “ssh -i path_private_key” path_or_dic_local username@address:path_or_dic_remote  
```

### Buckets 相关

#### 创建和删除 Buckets

在 web 界面按步骤操作即可。

#### 上传数据到 buckets

使用 gsutil 操作较为方便，命令如下

```PowerShell
gsutil -m cp -r Petase-gen gs://xux-bucket
```

#### 在 VM 中加载（mount） bucket

```PowerShell
gcsfuse xux-bucket mount-empty-dir/
```

#### 卸载（unmount） bucket

```PowerShell
fusermount -u mount-empty-dir/
```

#### 向 bucket 中写入文件

```PowerShell
是的说法
```

#### 删除 bucket 中的文件

```PowerShell
是的说法
```

### 布置Conda 环境

#### 安装 Mambaforge

mamba 远远快于 conda。mambaforge 是 miniconda 的替代品。

```PowerShell
# wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh

bash Mambaforge-Linux-x86_64.sh
```

#### 创建 conda 环境

```PowerShell
mamba env create -f environment.yml
```

## Google Colab 使用

Google Colab 是谷歌提供的免费计算资源，使用 Google Cloud 来进行计算。

它会有默认的部署环境，通常是 python 3\.10。常用的机器学习依赖包都已经安装好。

线下部署 Google Colab 环境，需要有一个相似的环境，会比较容易实现。

### 链接 Google Drive

```SQL
from google.colab import drive
drive.mount('/content/drive')
```

## AWS 操作

### 从 AWS 下载数据

```PowerShell
# example
aws s3 cp s3://BUCKET/ folder --exclude "*" --include "2018-02-06*" --recursive

# folder download
aws s3 cp --recursive s3://nanopore-human-wgs/rna/Multi_Fast5/  ./

# single document download
aws s3 cp s3://nanopore-human-wgs/rna/fastq/NA12878-cDNA_All_Guppy_4.2.2.fastq.gz ./
```
