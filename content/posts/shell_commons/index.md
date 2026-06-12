---
title: "Shell 常用命令"
subtitle: ""
date: 2026-05-30
draft: false
author: "Xiaopeng Xu"
description: "Shell 常用命令速查：日常操作、find/replace、awk、文件与文件夹操作、gutils 与 VSCode 远程开发。"
tags: ["Shell", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 日常操作

### 命令行打开 Rstudio

```plain
open -na Rstudio
```
### 命令行打开 JupyterLab

```plain
jupyter lab # 基础命令
nohup  jupyter-lab --no-browser --ip="0.0.0.0" 2>&1 & # 后台运行命令
```
### 查看系统内存和资源

```plain
htop
top
```
### 查看 GPU 内存使用率

```plain
watch -n 0.5 nvidia-smi
```
### 开启 vncviewer 服务器

```plain
vncserver -rfbport 8888
```
### 更新 DNS 服务器

每次重启 xuxa 后，都需要更新一下

```plain
sudo resolvconf -u
```
### 计算代码行数

计算目录下所有 python 文件的代码行数

```plain
find . -name '*.py' | xargs wc -l
```
### Regex 将字符串转换为单字符列

通常用于比较两个蛋白序列。在 Sublime 中先用如下正则规则来替换，然后可以拷贝到 Excel 中做后续的整理处理。

```plain
# Find
(?<=.)(?!$)

# Replace
\n
```
## Shell 常用操作

### 文件操作

#### 对 TSV 文件按某列倒序排序，并找出最大值

```plain
sort -k 8 -n -r tune_dl_parmas_DeepWalk.4_hid_layers_5.csv | head -1
```
#### 用 for 循环，对类似文件批量处理

```plain
for i in `ls  tune_dl_parmas_*.4_hid_layers_5.csv`; do echo $i; sort -k 6 -n -r $i | head -1; done
```
### awk 操作

#### 打印某列

```plain
awk '{print $1}' filename.txt 
```
#### 按某列做数值过滤

```plain
awk '$4 > 5' NA12878-DirectRNA_All_Guppy_4.2.2.readid.anno.txt | grep -v protein_coding
```


### 文件夹操作

#### cd 打开文件夹

```python
cd ./dir
```
#### pwd 查看当前文件夹位置

```python
pwd
```
#### ls 查看文件夹详情

```python
ls -alh . # 按人可视模式查看
ls -alh * # 按人可视模式查看当前文件夹和其子文件夹内容
```
#### du/df 查看空间大小

```python
du -sh # 查看文件夹大小
df -h # 查看磁盘空间大小
```
### 其他操作

#### ln 增加软连接

```python
ln -s /ibex/scratch/xux data # daΩta 是链接在当前文件夹内的显示名
```
## gutils 操作

### 安装及配置

```plain
conda install -c conda-forge gsutil
gsutil config # 按照提示，输入 auth code 和 project-id
```
### 上传、下载和删除

```plain
gsutil -m cp -r gs://ig_seq-bucket . # 下载
gsutil cp your-file gs://your-bucket/abc/ # 上传
gsutil rm -r gs://my-bucket/dir/ # 删除
```


## VSCode 使用

### 添加远程 SSH 服务器

1. 安装 VS Code 的 Remote-SSH 插件

2. 在服务器端开启 SSH 服务后，在 VS Code 中按 F1，并输入 Remote-SSH： Connect to Host...,  并在其中输入 SSH 服务器信息，链接即可


### 打开远程文件夹

1. 在 VS Code 中点击 Remote Explorer 图标，进入远程文件夹浏览页面

2. 在 Remote Explorer 中点击 SSH Targets 并添加 SSH host，输入 SSH 链接的信息，并点击“Add”添加

3. 在 Remote Exploreer 中可以浏览和添加远程文件夹。


### 添加 Python environment

默认打开远程文件夹后，就会使用远程的 environment。如果是新建的 environment，需要关闭项目，并重新打开下，即可使用新建的 environment。


## GS其他

### Coursera notebook 下载文件到本地

```plain
!tar cvfz allfiles.tar.gz * # 压缩目录下的所有文件
!ls -alh *
!split -b 90m allfiles.tar.gz allfiles.tar.gz.part. # 裁剪为 90m 的小包
!ls -alh .
# 逐个下载小包

!rm allfiles.tar* # 删除服务器上的压缩文件
# 本地
!cat allfiles.tar.gz.part.* > allfiles.tar.gz # 合并为一个大文件
!tar xvf allfiles.tar.gz #解压缩
```
### Google colab 下载文件到本地

使用 chrome 浏览器

```plain
from google.colab import files 
!tar cvfz allfiles.tar.gz sample_data
files.download('allfiles.tar.gz') 
```
## Wget 下载

简单下载 直接 wget <web-url>。有时需要下载所有远程 FTP 文件夹中的资料，可以用如下命令：

```powershell
wget -m ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/ 
```
注意，前面必须是 FTP 格式。

## Parallel 并行运行脚本

当处理数据时候，通常需要批次处理的很多文件。GNU parallel 是一个比较好用的工具。可以用来做此类分析。同时还能嵌入在 python 中使用。

[https://www.gnu.org/software/parallel/](https://www.gnu.org/software/parallel/)

```powershell
parallel < run_obtain_kmer_signals.sh 
```
## 从 SRA 下载数据

通过 SRA-tools 来下载。

```powershell
prefetch SRR21161131
fastq-dump SRR21161131
```


## 安装 Helvetica 字体

Download Helvetica.ttf.gz （[https://laplace.physics.ubc.ca/Doc/rnpletal/Helvetica.ttf.gz](https://laplace.physics.ubc.ca/Doc/rnpletal/Helvetica.ttf.gz)）and install fonts

```powershell
gunzip Helvetica.ttf.gz 
sudo mkdir /usr/share/fonts/truetype/myfonts
sudo mv Helvetica.ttf /usr/share/fonts/truetype/myfonts/.
sudo fc-cache -f -v /usr/share/fonts/truetype/myfonts/

reboot
```
