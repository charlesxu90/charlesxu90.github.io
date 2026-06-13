---
title: "Google Sites 网站开发"
subtitle: ""
date: 2024-10-16
draft: false
author: "Xiaopeng Xu"
description: "Google Sites 网站开发相关笔记。"
tags: ["Google Sites", "Web"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Google Sites Web 开发

## Google Sites 域名配置

在 https://sites\.google\.com/ 上开发个人主页．在腾讯云上购买域名．

购买域名后，在 https://sites\.google\.com/ 网站下的设置功能中，输入自己的域名，点击下一步获得域名解析的配置信息．

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031629979.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031626000.png)

将相应的信息输入到腾讯云域名解析服务中，即可通过域名访问网站．

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031622846.png)

https://www\.xu\-xp\.com/

## 修改域名配置为 Github Pages

通常在国内没法访问谷歌的域名，为了解决这个问题 Github pages 就是一个比较好的方案。首先，在Github 个人帐号下开发个人页面，参考我的个人页面 https://charlesxu90\.github\.io/，这块因人而异，不想细讲，后面打算写一个《Agent 开发个人主页》来单独讲讲。接下来，我主要描述下，如何配置 Github和域名解析服务，来支持这个域名的解析。

首先，需要在 Google Sites 取消这个域名的关联。1）在Google Pages 的操作如下，点开发布设置，在自定义网域里面删除这个域名。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031619662.png)

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031616192.png)

其次，需要在域名解析服务中，需要指向 GitHub，而非 Google Sites。

原有 Google Sites 的配置如下：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031612859.png)

需要修改为如下信息：

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031609390.png)

其中，185\.199\.109\.153 和 185\.199\.108\.153 是 GitHub 的 IP 地址，charlesxu90\.github\.io 是 GitHub 对应网域的地址。 



最后，在 Github 项目的设置中，支持域名的配置。比较直接，在 Settings 页面添加这个域名，并 check 即可，这样 GitHub 就能将这个网域转到这个项目的网站上。

![Image](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613031606420.png)

配置完后，等 TLS certificate，授权后增加 HTTPS即可。
