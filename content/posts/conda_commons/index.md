---
title: "Conda 常用命令"
subtitle: ""
date: 2020-09-25
draft: false
author: "Xiaopeng Xu"
description: "Conda 环境与包管理常用命令速查。"
tags: ["Conda", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 简介

通常在项目开发中，不同项目有不同的环境要求，配置这些环境会花大量的时间。Conda就是为了解决这一问题而生。其他解决方案还有 docker，虚拟化程度更高，但使用成本也会提升。

Conda是一个开源软件包管理和环境管理系统。 Conda可快速安装、运行和升级软件包及其依赖包。 Conda可在本地计算机上轻松地进行创建、保存、加载和切换环境。

> 注：Conda 在创建环境时候较慢，用mamba可以更快创建环境。
> 
> 

## 安装 conda

通常安装 miniconda 即可。参考 https://docs\.anaconda\.com/free/miniconda/miniconda\-install/。

## 环境操作

### mamba 从文件创建环境

```PowerShell
mamba env create --prefix flame-dsr-env --file environment.yml # crete a local environment
mamba env create -n flame-dsr-env --file environment.yml # crete a global environment 
```

### 创建环境

```Plaintext
$ conda create --name python36-env python=3.6 pip=20.0
```

### 激活环境

```Plaintext
$ conda activate basic-scipy-env
```

### 关闭环境

```Plaintext
(basic-scipy-env) $ conda deactivate
```

### 在当前目录下创建并激活环境

```Plaintext
$ conda create --prefix ./env ipython=7.13 matplotlib=3.1 pandas=1.0 python=3.6
$ conda activate ./env
```

### 列出已有环境

```Plaintext
$ conda env list
```

### 删除环境

```Plaintext
$ conda remove --name my-first-conda-env --all
$ conda remove --prefix /path/to/conda-env/ --all
```

## 包操作

### 搜索包/检查包版本

```Plaintext
$ conda search scikit-learn
$ conda search -f libgcc
```

### 安装包

```Plaintext
(basic-scipy-env) $ conda install scikit-learn=0.22
```

### 使用 pip 在 conda 环境中安装包

```Plaintext
(basic-scipy-env) $ pip install pandas
```

### 列出环境中的包

```Plaintext
$ conda list --name basic-conda-env
$ conda list --prefix /path/to/conda-env
```

## 分享环境

### 创建 environment\.yml 文件

#### 示例 environment\.yml 文件：

```Plaintext
name: machine-learning-env

dependencies:
  - ipython
  - matplotlib
  - pandas
  - pip
  - python
  - scikit-learn
```

- 如果要用于在当前目录下创建\./env 文件夹，需要将 name 的值设为 null。

### 使用 environment\.yml 文件

- 通过 environment\.yml 文件来对环境做版本控制，如将其添加到 git 中。

```Plaintext
$ cd project-dir
$ conda env create --prefix ./env --file environment.yml
$ conda activate ./env
```

### 导出当前环境

```Plaintext
$ conda env export --name machine-learning-env --no-builds
```

### 更新环境：

```Plaintext
$ conda env update --prefix ./env --file environment.yml  --prune
```

### 重新创建环境：

```Plaintext
$ conda env create --prefix ./env --file environment.yml --force
```

### Jupyter 与 Conda 环境的同步

JupyterLab 和 Jupyter Notebooks 会默认确保 IPython kernel 可用。但如果有使用某一版本的 IPython kernel，则需要在 environment\.yml 文件中添加相应的信息。

```Plaintext
name: xgboost-env

dependencies:
  - ipykernel=5.3
  - ipython=7.13
  - matplotlib=3.1
  - pandas=1.0
  - pip=20.0
  - python=3.6
  - scikit-learn=0.22
  - xgboost=1.0
```

## Conda 安装源 \(channels\)

### 命令行中使用

```Plaintext
$ conda install scipy=1.3 --channel conda-forge --name my-first-conda-env
```

### 添加其他 channel

#### 命令行添加

```Plaintext
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
$ conda config --set show_channel_urls yes
```

#### environment\.yml 文件中添加

```Plaintext
dependencies:
- chanelname::modulename=X.Y.Z
```

### 无法找到源，使用 pip 安装

在 channel 中都没找到时，可以使用 pip 安装。

```Plaintext
name: null

dependencies:
 - jupyterlab=1.0
 - matplotlib=3.1
 - pandas=0.24
 - scikit-learn=0.21
 - pip=19.1
 - pip:
   - kaggle=1.5
   - yellowbrick=0.9
```

其他：[使用 conda 管理 GPU 依赖包](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/05-managing-cuda-dependencies/index.html); [Conda常用操作记录（for Mac）](https://zhuanlan.zhihu.com/p/81611615)。

### 
