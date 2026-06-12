---
title: "Docker 常用命令"
subtitle: ""
date: 2026-05-13
draft: false
author: "Xiaopeng Xu"
description: "Docker 常用命令速查：镜像、容器与常见操作。"
tags: ["Docker", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 镜像使用

### docker pull 获取镜像

```PowerShell
docker pull informaticsmatters/rdock
```

### docker run 从镜像创建容器

```PowerShell
docker run -it --rm -u $(id -u):$(id -g) -v $PWD:$PWD:Z -w $PWD informaticsmatters/rdock bash # 启动 bash
```

### 在 docker 中运行命令

#### 在启动容器时运行

```PowerShell
docker run -it --rm ubuntu:18.04 bash
```

#### 在 bash 中直接运行

```PowerShell
docker run -it --rm ubuntu:18.04 bash
rbdock
```

#### 在 DockerFile 中使用 CMD 命令运行

```Dockerfile
FROM frolvlad/alpine-oraclejre8
ARG JAR_FILE_NAME
ADD target/${JAR_FILE_NAME} app.jar
 
CMD java -jar /app.jar
```

### 外部访问容器

## 入门介绍

### 用 apt 安装：

[https://yeasy\.gitbook\.io/docker\_practice/install/ubuntu](https://yeasy.gitbook.io/docker_practice/install/ubuntu)

#### 安装依赖组件：

```Python
sudo apt-get install apt-transport-https ca-certificates curl gnupg  lsb-release
```

#### 添加源

```Python
# 官方源， 其他源流程类似
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

#### 安装 docker

更新 apt 软件包缓存，并安装 docker\-ce

```Python
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# 用脚本自动安装
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun

# 修改运行权限
sudo chmod 666 /var/run/docker.sock
```

#### 启动 docker

```Python
sudo systemctl enable docker
sudo systemctl start docker
```

#### 建立 docker 用户组

```Python
sudo groupadd docker
sudo usermod -aG docker $USER
```

#### 测试是否正确安装

```Python
 docker run --rm hello-world
```

## 运行 Dockerfile 容器

#### 从 Dockerfile 构建镜像 

假设 Dockerfile 在当前目录下，通过如下命令build docker 镜像。其中，react\-coord\-conf\-md 是镜像名称。

```Python
docker build -t react-coord-conf-md .
```

#### 运行 docker镜像 

对于常见程序，需要打开 docker 的命令行，所以需要打开其 bash。使用如下命令。

```Python
docker run -it --entrypoint /bin/bash  react-coord-conf-md
```

#### 展示正在运行的 docker （docker ps）

```Python
docker ps                                                                                                      [11:23:29]
CONTAINER ID   IMAGE                 COMMAND       CREATED          STATUS          PORTS     NAMES
67131e98199c   react-coord-conf-md   "/bin/bash"   33 seconds ago   Up 33 seconds             epic_easley
```

#### 加载本地目录到 doker 容器

```Python
docker run -it  -v /home/xux/Desktop/Enzyme_MD/:/app --entrypoint /bin/bash  react-coord-conf-md
```

#### 连接 shell 到 docker 容器

```Python
$ sudo docker exec -it  67131e98199c bash                           [11:40:11]
root@67131e98199c:/# 
```
