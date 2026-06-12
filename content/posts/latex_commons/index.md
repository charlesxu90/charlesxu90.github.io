---
title: "Latex 常用命令"
subtitle: ""
date: 2022-04-25
draft: false
author: "Xiaopeng Xu"
description: "LaTeX 常用命令速查：公式、表格、图片与排版。"
tags: ["LaTeX", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 常用包说明

```LaTeX
\documentclass{proc} % 一个基于 article 的会议文集文件类型
\usepackage[utf8]{inputenc} % 输入编码 utf-8
\usepackage{natbib} % 参考文献引用格式
\usepackage{graphicx} % 插图的标准宏包
\usepackage{authblk} % 自定义作者环境
\usepackage{soul} % 文本强调
\usepackage{xcolor} % 提供了更方便的混色语法
\usepackage{booktabs} % 三线表
\usepackage{adjustbox} % 图片文档对齐
\usepackage{lscape} % 单页面变为横置
\usepackage[margin=.6in, footskip=.75cm]{geometry} % 设置页面各部分尺寸
\usepackage{hyperref} % 超链接与其他 PDF 专有功能
\usepackage{rotating} % 旋转文字，图像，表格等对象
```

LaTex常用包及其功能：[https://blog\.csdn\.net/i1020/article/details/98525978](https://blog.csdn.net/i1020/article/details/98525978)

常用latex宏包：[https://blog\.csdn\.net/u012684062/article/details/78403957](https://blog.csdn.net/u012684062/article/details/78403957)

Latex常用宏包说明： [https://www\.jianshu\.com/p/a2721d47028d](https://www.jianshu.com/p/a2721d47028d)

\[LaTeX 指南\] 功能性宏包推荐： [https://zhuanlan\.zhihu\.com/p/43981639](https://zhuanlan.zhihu.com/p/43981639)

## 文件类型 documentclass

当 latex 处理源文件时， 首先需要知道的就是作者所要创建的文档类型。 文档类型可由\\documentclass 命令来指定。

```PowerShell
\documentclass[option]{class}
```

class 指定想要的文档类型。表1给出了一些用到的文档类型。通过options 参数可以定制文档类的属性。 不同的选项之间须用逗号隔开。标准文档类的最常用选项如表2所示。
例子：

```PowerShell
\documentclass[11pt,twoside,a4paper]{article}
```

这条命令会引导 latex 使用article 格式、 11 磅大小的字体来排版该文档， 并得到在A4 纸上双面打印的效果。 

### Latex 文件类型

|article|排版科学期刊、 演示文档、 短报告、 程序文档、 邀请函……|
|---|---|
|proc|一个基于 article 的会议文集类|
|minimal|非常小的文档类。 只设置了页面尺寸和基本字体。 主要用来查错。|
|report|排版多章节长报告、 短篇书籍、 博士论文……|
|book|排版书籍。|
|slides|排版幻灯片。 该文档类使用大号 sans serif 字体。 也可以选用 FoilTEXa 来得到相同的效果。|

### Latex 文档类选项

|10pt, 11pt, 12pt|设置文档中所使用的字体的大小。 如果该项没有指定， 默认使用10pt 字体。|
|---|---|
|a4paper, letterpaper, \. \. \.|定义纸张的尺寸。 缺省设置为letterpaper。 此外， 还可以使用a5paper, b5paper, executivepaper 以及legalpaper。|
|fleqn|设置行间公式为左对齐， 而不是居中对齐。|
|leqno|设置行间公式的编号为左对齐， 而不是右对齐。|
|titlepage, notitlepage|指定是否在文档标题\(document title\) 后另起一页。 article 文档类缺省设置为不开始新页， report 和book 类则相反。|
|onecolumn, twocolumn|latex 以单栏\(one column\) 或双栏\(two column\) 的方式来排版文档。|
|twoside, oneside|指定文档为双面或单面打印格式。 article 和report 类为单面\(single sided\) 格式， book 类缺省为双面\(double sided\) 格式。 注意该选项只是作用于文档样式， 而不会通知打印机以双面格式打印文档。|
|landscape|将文档的打印输出布局设置为 landscape 模式。|
|openright, openany|决定新的一章仅在奇数页开始还是在下一页开始。 在文档类型为article 时该选项不起作用， 因为该类中没有定义“章” \(chapter\)。 report 类默认在下一页开始新一章而book 类的新一章总是在奇数页开始。|

## 页面样式 pagestyle

LATEX 支持三种预定义的页眉/页脚\(header/footer\) 样式， 称为页面样式\(pagestyle\)。 使用方式：

```LaTeX
\pagestyle{style}
```

其中的 style 参数确定了使用哪一种页面样式 。表4 列出了预定义的页面样式。

### LATEX预定义的页面样式

|plain|在页脚正中显示页码。 这是页面样式的缺省设置。|
|---|---|
|headings|在页眉中显示章节名及页码， 页脚空白。|
|empty|将页眉页脚都设为空白。|

#### 改变当前页面的页面样式

```LaTeX
\thispagestyle{style}
```

## 使用宏包 usepackage

排版文档时， 你可能会发现某些时候基本的LATEX 并不能解决你的问题。 如果想插入图形\(graphics\)、 彩色文本\(coloured text\) 或源代码到你的文档中， 你就需要使用宏包来增强LATEX 的功能。 可使用如下命令调用宏包

```LaTeX
\usepackage[options]{package}
```

这里package 是宏包的名称， options 是用来激活宏包特殊功能的一组关键词。很多宏包随LATEX 基本发行版一起发布\(表3\)

### Latex 默认宏包

|doc|排版LATEX 的说明文档。提供了写 LaTeX 宏包文档需要的一些功能。|
|---|---|
|exscale|提供了按比例伸缩的数学扩展字体。|
|fontenc|指明使用哪种LATEX 字体编码\(font encoding\)。|
|ifthen|提供如下形式的命令‘if \. \. \. then do \. \. \. otherwise do \. \. \. \.’|
|latexsym|提供LATEX 符号字体。|
|makeidx|提供排版索引的命令|
|syntonly|编译文档而不生成 dvi 文件|
|inputenc|指明使用哪种输入编码， 如 ASCII, ISO Latin\-1, ISO Latin\-2, 437/850IBM code pages, Apple Macintosh, Next, ANSI\-Windows 或用户自定义编码。|

### 几乎必用的宏包

- 数学公式 \- amsmath

- 插图 \- graphicx 插图的标准宏包。

- 颜色 \- xcolor 主要提供了更方便的混色语法。此宏包会被许多图形相关的宏包自动调用

- 表格 \- array

- 中文 \- ctex, xecjk

- 西文 otf 字体 \- fontspec

### 样式定制宏包

- 页面布局 \- geometry, typearea（额外支持在文档中途改变纸型）

    - 设置页面各部分尺寸 geometry

    - 页眉页脚 \- fancyhdr 设置页眉页边页脚。

    - fancyhdr 不会自动更新版心宽度，与 geometry 配合使用时可能出现问题。宏包 autofancyhdr 修复了这个问题

- 章节标题 \- ctexheading（ctex 宏集的子包），titlesec

- 目录 \- tocloft, titletoc

- 列表 \- enumitem

- 脚注 \- footmisc

- 抄录环境 \- listings, fancyvrb（及扩展 fvextra）, minted（不分先后）

    - listings 代码抄录并语法高亮。

- 定理环境 \- amsthm, thmtools, 不推荐 ntheorem

- 文本强调（下划线、文字底纹等） \- ulem, soul（均不支持中文）, xeCJKfntef（仅 xetex），lua\-ul（仅 luatex）

### 特定领域宏包

- 更多公式符号 \- amssymb

- 交换图 \- amsmath（amscd 环境），tikzcd（有[在线编辑器](https://link.zhihu.com/?target=https%3A//tikzcd.yichuanshen.de/)）, tikz 功能最强大的绘图宏包之一

- 段落对齐方式 \- ragged2e

- 幻灯片，学术报告向 \- beamer

- 多栏模式 \- multicol 平衡方便的多栏排版

- 允许栏宽不等的多栏模式（不可跨页） \- vwcol

- 数字、单位与量 \- siunitx

- 参考文献引用格式 \- cite, natbib（方便的参考文献格式控制。提供了「人名年份」引用格式）

- 索引 \- makeindex（定制索引样式见 texdoc ind）

- 绘制分子和反应流程，偏有机化学 \- chemfig

- 排版分子和反应式，偏无机化学 \- chemformula, mhchem

- 排版算法和伪代码 \- algorithm2e，另见[知乎回答](https://www.zhihu.com/question/26535085/answer/33144177)

- 排版代码，带语法高亮 \- minted（需安装 Python 库 Pygments）

- 排版示例，「一边是源码，一边是结果」 \- showexpl, tcolorbox 的 listings 等模块

- 插入多页 PDF \- pdfpages

- 自动切边 \- standalone

### 特定需求宏包

- 四则运算 \- calc

- 术语表 \- nomencl

- 自动调整宽度的子段盒子 \- varwidth

- 让长章节拥有自己的子目录 \- minitoc

- 为目录、参考文献和索引添加目录项 \- tocbibind

- 多栏目录 \- multitoc

- 首字下沉 \- lettrine

- 章首名人名言 \- epigraph

- 尾注 \- end­notes

- 多个参考文献列表 \- chapterbib

- 获知文档总页数 \- lastpage

- 获知文档各部分的总页数 \- pageslts

- 插入终端执行命令后返回的结果 \- bashful

- 使用相对于子文件的路径 \- import

- 页面水印 \- watermark, atbegshi

- 自定义作者环境 \- authblk [Link](https://blog.csdn.net/robert_chen1988/article/details/79187224) 定义作者，通讯作者，联系地址

### 浮动体宏包

- 浮动体标题的格式 \- caption

- 双语标题 \- bicaption

- 定义新浮动体系列，让浮动体「不浮动」 \- float

- 定义新浮动体系列，允许一个浮动体环境包含多个标题 \- newfloat

- 提供「算法」浮动体系列，基于 float 宏包 \- algorithm

- 子图的标题 \- subcatpion, subfig

- 在侧边排版标题，及其他 \- floatrow

- 避免浮动体跨章节出现 \- placeins

### 表格宏包

- 在单元格中自由换行 \- makecell

- 纵向合并单元格 \- multirow

- 均分列宽 \- tabularx

- 在小数点处对齐的列 \- dcolumn, siunitx

- 三线表 \- booktabs

- 表头斜线 \- diagbox

- 使横表线避开纵表线 \- hhline

- 彩色的单元格和表线 \- colortbl（常通过`\usepackage[table]{xcolor}` 间接调用）

- 可跨页表格 \- longtable \(跨页的长表格\), supertabular

- 使列按比例分配宽度 \- tabu（缺乏维护，色彩支持部分有 bug）

### PDF 宏包

- 超链接 \- hyperref 超链接与其他 PDF 专有功能（如表单制做）。

- 书签 \- bookmark

- 注释 \- pdfcomment

- 附件 \- embedall, embedfile

### 辅助工具宏包

- 以表格形式输出指定字体前256个符号 \- fonttable

- 输出页面布局示意图，列出页面参数的值 \- layout

- 可视化各文档部件的布局参数，提供调整接口 \- layouts

- 英文测试文本，可用于测试排版效果 \- lipsum

- 中文测试文本 \- zhlipsum

- 输出测试文档，可包含目录、各级标题、列表、公式、文本等 \- blindtext

- 提供示例图片 \- mwe

- 长度的单位转换 \- printlen

- 输出文件加载依赖关系 \- inputtrc

### 命令定义、宏包编写

- 综合工具 \- etoolbox

- 指定命令参数「类型」 \- xparse

- 修改已定义命令 \- xpatch, regexpatch

- 操作「字符串」 \- xstring

### 个人推荐

- 功能类

    - 数学公式辅助 \- mathtools

    - 公式输入便捷命令 \- physics

    - 使用 opentype 数学字体 \- unicode\-math

    - 自动调整引号方向 \- csquote

- 兴趣类

    - 排版微调 \- microtype

    - 为一系列宏包统一配置接口 \- interfaces

    - 高度可配置的彩色盒子 \- tcolorbox

    - 选项形式提供对「盒子」的操作，避免命令嵌套 \- adjustbox

- 其他

    - 数学公式样式配置和小宏包功能汇总 \- voss\-math­mode（TeX Live 未收录，CTAN 标记为「已废弃」）

- 有名但笔者尚不了解

    - 高度可定制的专业文档类 \- koma\-script, memoir

## Latex 转换为 Word

直接用最新的 Office Word 打开 PDF 文件即可！

## 设置引文风格 Citation style 

Latex 使用中，最重要的一个功能是能够比较好的管理引文文献。它支持比较便捷的设置引文的格式，方便管理文献。但在实际投稿中，尤其是投稿 Bioinformatics时，文献页数要求很严格，需要对文章进行压缩，这个对引用文献就提出了很严格的要求。



可以通过如下方式压缩引用文献的长度：

1. 使用 number，而不是 author\-date 来引用，对应的是 unsrt 格式

```LaTeX
\bibliographystyle{unsrt}
```

2. 压缩作者长度，只展示最多两个 author，通常是 一个author, 如 `Xiaopeng Xu, et al. `格式。需要修改unsrt\.bst, 参考https://tex\.stackexchange\.com/questions/26575/bibtex\-how\-to\-reduce\-long\-author\-lists\-to\-firstauthor\-et\-al\.

```LaTeX
\bibliographystyle{unsrt_1name}
```

3. 使用 small 字体，来压缩长度。

```LaTeX
{\small
\bibliography{reference}}
```

使用后，引用格式上会出现一些变更，需要用 setcitestyle 来调整引用格式

```LaTeX
\setcitestyle{square,citesep={,\kern-0.1em}}
```

## 设置图标标题格式 Caption 

```LaTeX
% set to bold format
\usepackage{caption}
\captionsetup{labelfont={bf}}

% Rename name in Caption
\renewcommand{\figurename}{Supplementary Figure}
\renewcommand{\tablename}{Supplementary Table}
```

## 自定义引用格式 citation

Latex 的最重要的功能，是比较便捷的管理引用。常用的包是 natbib 和 Biblatex。两个都是基于 BibTeX 的基础功能。相对而言，natbib 是最常用也较简单的引用方式，但其支持的功能比较有限。对一些特定期刊，用 biblatex 来自定义引用会方便一些。但是最恶心的 bioinformatics，仍然没有办法，只能用 natbib。又要非常高的引用压缩比，这个确实很恶心。

### Natbib 

#### 切换引用类型

```LaTeX
% set to bold format
\usepackage{natbib}

\setcitestyle{authoryear, round, aysep={}}

% \bibliographystyle{unsrt}
% \bibliographystyle{unsrt_1name}
\bibliographystyle{myplainnat} 
% \bibliographystyle{abbrvnat} 
% \bibliographystyle{abbrvnat_1name} 

% set to small fontsize
{\small \bibliography{reference}}
```

#### 使用作者名称简称

说明：

需要将对应的 bst 文件另存，并修改其中 format\.names 的相关内容

```LaTeX
FUNCTION {format.names}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    % { s nameptr "{f.~}{vv~}{ll}{, jj}" format.name$ 't :=
    { s nameptr "{vv~}{ll}{, jj}{, ff}" format.name$ 't :=
      nameptr #1 >
        { nameptr #1
          #1 + =
          numnames #2
          > and
            { "others" 't :=
              #1 'namesleft := }
            'skip$
          if$
          namesleft #1 >
            { ", " * t * }
            {
              s nameptr "{ll}" format.name$ duplicate$ "others" =
                { 't := }
                { pop$ }
              if$
              numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " et~al." * }
                { " and " * t * }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}
```

### biblatex

说明：https://linorg\.usp\.br/CTAN/macros/latex/contrib/biblatex/doc/biblatex\.pdf

#### 切换引用类型

```LaTeX
% set style using biblatex
\usepackage[backend=biber, style=alphabetic,]{biblatex}

\addbibresource{reference.bib}

% set to small fontsize
{\small \printbibliography}
```
