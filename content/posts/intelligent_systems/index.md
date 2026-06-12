---
title: "智能系统调研"
subtitle: ""
date: 2021-02-21
draft: false
author: "Xiaopeng Xu"
description: "智能系统调研：面向业务流程自动化的 AI 化实践，以及中美等地主流 AI 开放平台与服务概览。"
tags: ["AI Systems", "Survey"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 结论

大部分的 智能系统，主要是面向 “SDAF” 闭环中的 “A” 步骤。针对业务流程的具体任务，实现 AI 化，提升效率。

此外，很多大企业提供了 AI 开放平台，提供通用的 AI 云服务。

## 中国

|公司名称|产品|应用|说明文档|
|:----|:----|:----|:----|
|百度|百度 AI 开发平台[https://ai.baidu.com/](https://ai.baidu.com/)数百项全球领先的人工智能服务助您赋能产品|开放API|[https://ai.baidu.com/ai-doc](https://ai.baidu.com/ai-doc)|
||Apollo 智能交通解决方案[https://apollo.auto/](https://apollo.auto/)通过道路及基础设施的智能化改造，帮助城市实现智能化升级打造安全、高效的城市交通出行体验|智能驾驶|[https://apollo.auto/developer/index_cn.html](https://apollo.auto/developer/index_cn.html)|
||百度智能云[https://cloud.baidu.com/](https://cloud.baidu.com/)云智一体，壮“智”凌云|AI 云|[https://cloud.baidu.com/doc/index.html](https://cloud.baidu.com/doc/index.html)增加人工智能、智能视频、智能大数据、企业智能应用等相关的服务|
||DuerOS一对话式人工智能操作系统[https://dueros.baidu.com/html/dueros/index.html](https://dueros.baidu.com/html/dueros/index.html)|对话机器人||
||百度搜索引擎[https://www.baidu.com/](https://www.baidu.com/)全球最大的中文*搜索引擎*、致力于让网民更便捷地获取信息，找到所求。*百度*超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。|搜索引擎|[https://help.baidu.com/question?prod_id=1](https://help.baidu.com/question?prod_id=1)|
||百度推荐[http://tuijian.baidu.com/rec-web/welcome/login](http://tuijian.baidu.com/rec-web/welcome/login)百度推荐是一款面向站长用户推出的专业网站推荐工具|智能推荐|[http://tuijian.baidu.com/rec-web/introduce/help/product](http://tuijian.baidu.com/rec-web/introduce/help/product)通过为网站的每个访客推荐个性化内容，提高网站内容的点击率，从而大幅提升网站流量。百度推荐依托百度覆盖中国90%以上网民搜索行为的大数据优势，最了解您的访客需求。|
|头条|火山引擎[https://www.volcengine.cn/](https://www.volcengine.cn/)全球领先的企业智能增长引擎，基于前沿的大数据、人工智能以及云基础技术能力，结合独有的增长方法论，为客户提供全链路解决方案，助力企业客户持续快速增长|智能增长|[https://www.volcengine.cn/docs](https://www.volcengine.cn/docs)包括移动中台、数据中台、多媒体中台、AI中台、业务安全套件、智能营销套件、个性化推荐套件、智能体验套件、内容创作套件、智能内容套件、服务支持、存储、研发中台、其他等一整套面向内容营销方向的 to B 服务。|
||巨量引擎[https://www.oceanengine.com/](https://www.oceanengine.com/)巨量引擎是字节跳动旗下综合的数字化营销服务平台，致力于让不分体量、地域的企业及个体，都能通过数字化技术激发创造、驱动生意，实现商业的可持续增长。|广告投放|[https://www.oceanengine.com/help/114](https://www.oceanengine.com/help/114)巨量引擎的营销资源包括了今日头条、抖音、西瓜视频、懂车帝、Faceu激萌、轻颜、皮皮虾、穿山甲等。规模化用户、智能化技术、全内容生态、科学化评估、一站式服务|
||头条搜索（app） - 海量视频热点咨询高质量搜索[https://so.toutiao.com/](https://so.toutiao.com/)|搜索引擎|主要面向“视频、资讯、小视频、图片、音乐、用户、微头条“内容的搜索。尤其是多媒体（视频）搜索，是一个显著的亮点。|
|阿里巴巴|阿里云 AI 云平台[https://ai.aliyun.com/](https://ai.aliyun.com/)阿里云AI依托阿里顶尖的算法技术，结合阿里云可靠和灵活的云计算基础设施和平台服务，帮助企业简化IT框架、实现商业价值、加速数智化转型。阿里云数十项AI能力，稳定、易用、能力突出，是AI技术应用、开发的不二之选。|AI 云|主要包括智能语音、视觉图像、语言技术和场景化方案|
||阿里云 ET 大脑[https://www.alibabacloud.com/zh/solutions/intelligence-brain](https://www.alibabacloud.com/zh/solutions/intelligence-brain)智能大脑是阿里云研发的超级智能，用突破性的技术，解决社会和商业中的棘手问题。|故事|激发行业无限潜能利用智能大脑的革命性技术，快速实现客户的商业目标阿里云智能大脑创新技术能力 – 将这些分散的技术融合成一个有机的整体，实现从单点智能到全局智能的突破计算性能与成本双领先的大数据计算能力海量多源数据规模化处理与实时分析类神经元网络物理架构海量视频规实时分析及自动巡检快速防御多源攻击的安全能力阿里云智能大脑的能力 – 多维感知、全局洞察、实时决策、持续进化在复杂局面下快速做出最优决定，认知多维感知判断实时决策决策全局洞察学习持续进化应用场景 – 智能语音交互、图像识别、印刷文字识别、自然语言处理|
||天猫精灵|智能硬件||
|华为|华为云智能 EI[https://www.huaweicloud.com/ei/index.html](https://www.huaweicloud.com/ei/index.html)企业智能的使能者，多领域智能体，助力各行各业进入人工智能新时代。助力政企智能升级 —— 让智能无所不及。普惠AI，让AI用得起，用得好，用得放心|AI 云|[https://support.huaweicloud.com/help-novice.html](https://support.huaweicloud.com/help-novice.html)华为云智能体以云为基础，以AI为核心，通过统一的平台和架构，将云、大数据、AI等创新技术与行业机理、专家知识融合，提供一体化协同的智能服务，挖掘数据价值，助力政企智能升级，构筑领先优势。|
||服务器 – 智能计算[https://e.huawei.com/cn/products/servers/ascend](https://e.huawei.com/cn/products/servers/ascend)智能计算，将围绕“算、管、AI、存、传”等系列芯片，打造覆盖云、边、端的全栈全场景智能解决方案。|智能计算|昇腾计算，是基于昇腾系列处理器构建的全栈AI计算基础设施及应用，包括昇腾系列芯片、系列硬件、芯片使能、AI框架、应用使能等。华为Atlas人工智能计算解决方案，基于昇腾系列AI处理器，通过模块、板卡、小站、服务器、集群等丰富的产品形态，打造面向“端、边、云”的全场景AI基础设施方案，涵盖数据中心解决方案、智能边缘解决方案，覆盖深度学习领域推理和训练全流程。Atlas 人工智能计算解决方案 – “开放、简单、可信”的AI解决方案 [https://e.huawei.com/cn/products/cloud-computing-dc/atlas](https://e.huawei.com/cn/products/cloud-computing-dc/atlas)|
||智能终端[https://consumer.huawei.com/cn/](https://consumer.huawei.com/cn/)消费者业务致力于将最新的科技带给消费者，让世界各地更多的人享受到技术进步的喜悦，以行践言，实现梦想。|智能硬件智能家居|[https://developer.huawei.com/consumer/cn/doc/development](https://developer.huawei.com/consumer/cn/doc/development)华为AI音箱、手环等可穿戴设备、华为路由器等HUAWEI HiLink 智能硬件生态[https://developer.huawei.com/consumer/cn/smarthome/](https://developer.huawei.com/consumer/cn/smarthome/)HUAWEI HiLink是华为面向消费领域的智能硬件开放生态，开发者可以通过硬件接入和云接入等方式加入到生态中来，成为华为1+8+N全场景生态的重要部分，被华为各种终端通过界面/语音方式查看和控制。平台提供云端边芯的整体解决方案与多种开发、调试工具，为开发者大大提高接入效率。华为愿与生态伙伴一起为华为3亿+用户构建高品质的全场景生活体验。|
||网络人工智能NAIE[https://www.huawei.com/cn/industry-insights/technology/naie](https://www.huawei.com/cn/industry-insights/technology/naie)华为网络人工智能NAIE是将AI技术引入到电信网络中的一站式AI应用开发云平台，提供数据湖、模型训练等云服务。让网络AI开发变得更简单！让网络AI开发更简单、应用更高效，使能自动驾驶网络！|电信网络智能化|[https://www.huawei.com/cn/industry-insights/technology/naie/imaster-naie-whitepaper](https://www.huawei.com/cn/industry-insights/technology/naie/imaster-naie-whitepaper)|
|腾讯|腾讯 AI 开放平台[https://ai.qq.com/](https://ai.qq.com/)一站式机器学习平台 快速构建专业级AI产品|AI 云|[https://cloud.tencent.com/document/product](https://cloud.tencent.com/document/product)包括人脸识别、人脸特效、人体识别、文字识别、AI 行业应用、图像识别、语音技术、AI 平台服务、自然语言处理、智能机器人等服务|
||AI 实验室腾讯 AI LAB – 聚集全球数十位人工智能科学家、70位世界一流AI博士。专注机器学习、计算机视觉、语音识别、自然语言处理等人工智能领域的研究。基于腾讯亿万用户海量数据及在互联网各垂直领域的技术优势，立志打造世界顶尖人工智能团队。优图实验室 – 腾讯旗下顶级的机器学习研发团队，专注于图像处理，模式识别、深度学习。在人脸检测、五官定位、人脸识别、图像理解等领域都积累了完整解决方案和领先技术水平。WeChat AI – 致力于为语音识别、自然语言处理、计算机视觉、数据挖掘和 机器学习等人工智能技术的发展带来革命性进步。|AI 实验室|[https://ai.tencent.com/ailab/zh/index](https://ai.tencent.com/ailab/zh/index)我们的基础研究方向包括计算机视觉、语音识别、自然语言处理和机器学习，应用探索结合了腾讯场景与业务优势，为内容、游戏、社交和平台工具型AI四类，目前已打造出围棋AI“绝艺”，技术也被微信、QQ、天天快报和QQ音乐等上百个腾讯产品使用。|
|科大讯飞|AI + 行业 （教育、城市、工业、生活、儿童、司法、医疗、汽车、办公、营销）[https://www.iflytek.com/index.html](https://www.iflytek.com/index.html)|行业应用|[https://www.iflytek.com/edu](https://www.iflytek.com/edu)|
||AI + 能力平台[https://www.iflytek.com/services/platform](https://www.iflytek.com/services/platform)|AI 云|语音识别、语音合成、自然语言理解、机器翻译、光学字符识别、生物特征识别|
||智能语音相关硬件[http://www.xunfei.cn/help/](http://www.xunfei.cn/help/)|智能硬件|智能翻译机、智能办公本、智能学习、智能录音笔、智能键鼠、电子阅读器、听见录音宝、会议宝S8、智能演示器、智能耳机、扫描词典笔、智能血压计|
|京东|人工智能开放平台[https://neuhub.jd.com/](https://neuhub.jd.com/)|AI 云|文字识别、人脸与人体识别、图像及视频理解、自然语言处理、语音技术、内容审核、商品理解、知识图谱|
||京东智能制造平台[http://c2m.jd.com/](http://c2m.jd.com/)作为京东零售的智能化C2M反向供应链平台，JC2M京东智能制造平台致力于服务京东零售集团及其合作伙伴，通过用户需求反向驱动上游制造业进行数字化升级改造，共建智慧定制、智造生产新时代。|智能制造|反向定制、新品仿真、个性定制、精准试用|
|小米|小米开放平台 - 小米AI[https://dev.mi.com/console/cloud/](https://dev.mi.com/console/cloud/)|AI 云|深度学习、计算机视觉、声学、语音、自然语言处理、知识图谱、智能问答、小爱同学|
||小米智能生活[https://xiaomishare.mi.com/#/](https://xiaomishare.mi.com/#/)|智能硬件智能家居|硬件 – 手环、台灯、扫地机器人、路由器、……米家 APP – 米家APP依托于小米生态链体系，是小米生态链产品的控制中枢和电商平台，集设备操控、电商营销、众筹平台、场景分享于一体，是以智能硬件为主，涵盖硬件及家庭服务产品的用户智能生活整体解决方案。|
|明略数据|知识图谱平台 SCOPA[https://www.mininglamp.com/productdetail/18](https://www.mininglamp.com/productdetail/18)||主要应用于公安方向|
||HAO智能:通过打通感知、认知、行动系统，实现AI闭环落地[https://www.mininglamp.com/column/13](https://www.mininglamp.com/column/13)基于HAO智能理论(Human Intelligence+Artificial Intelligence+ Organizational Intelligence)，打通感知、认知、行动系统，帮助组织进行分析决策|智能理论|五大技术方向：知识工程、信息检索、深度学习、视觉计算、营销智能|
|依图科技|[https://www.yitutech.com/](https://www.yitutech.com/)AI + 行业（城市、医疗、商业）|行业应用|深入行业，真正让AI技术落地专注将人工智能技术深度赋能行业发展，在多领域推出全球领先的创新技术和产品|
|中国平安|AI + 金融|行业应用|营销获客、*风险控制（反欺诈）、客户服务、运营&管理|
||平安云[https://pinganyun.com/](https://pinganyun.com/)|AI 云||
|海康威视|AI 开放平台[https://ai.hikvision.com/](https://ai.hikvision.com/)|AI 云|智能感知平台、大数据智能平台、设备开放平台|
||以视频为核心的*智能*物联网解决方案和大数据服务[https://www.hikvision.com/cn/prlb_936.html](https://www.hikvision.com/cn/prlb_936.html)|智能硬件|各种视频智能终端产品|
|旷视科技|人工智能开放平台[https://www.faceplusplus.com.cn/](https://www.faceplusplus.com.cn/)|AI 云|人脸识别、人体识别、人像处理、文字识别、图像识别|
||智能硬件|智能硬件|智能网络摄像机、智能身份核验终端、人脸识别门禁一体机、智能便携人像比对一体机、智能分析盒、智能存算一体机、机器人及智能装备|
|360|智能硬件|智能硬件|360智能摄像机AP5L、360行车记录仪G300 Pro、360扫地机器人C50、360智能摄像机AW2C、360行车记录仪G600 4G、360家庭防火墙路由器V5P、360家庭防火墙路由器5 pro、360儿童手表9X、360 存储卡64G|
|好未来|AI 开放平台[https://ai.100tal.com/](https://ai.100tal.com/)|AI +教育 云|应用：互动评测、练习批改、内容生产、教学管理能力：教育OCR、智能批改、图像视频分析、人脸分析、人体分析、语音识别、语音合成、语音评测|
|华制智能|华制云工业互联网[http://www.ehz.cn/](http://www.ehz.cn/)|工业互联网|功能：运营管控（数字化驾驶舱）、制造协同（服务、生产、物流、能源、安环）、设备互联（设备数据采集平台）、数据智能（数字孪生、工业大脑）、pass平台（企业中台）行业应用：流程行业、离散制造|

## 美国


|公司名称|产品|应用|说明|
|:----|:----|:----|:----|
|谷歌|Google 搜索[https://www.google.com/](https://www.google.com/)由Google公司推出的一个互联网搜索引擎，它是互联网上最大、影响最广泛的搜索引擎。|搜索引擎|[https://www.google.com/search/about/](https://www.google.com/search/about/)[https://support.google.com/websearch/?hl=zh-Hans#topic=1733202](https://support.google.com/websearch/?hl=zh-Hans#topic=1733202)除了搜索网页外，Google亦提供搜索图像、新聞組、新闻网页、地图、视频的服务。2005年6月，Google已存储超过80亿个网页，1亿3千万张图片，以及超过1亿的新聞組消息 - 总计大概10亿4千万个项目。它也缓存了编入索引中的绝大多数网页的内容。[https://developers.google.com/search/docs/basics/get-started?hl=zh-cn](https://developers.google.com/search/docs/basics/get-started?hl=zh-cn)|
||Google Cloud -  AI[https://cloud.google.com/products/ai?hl=zh-cn](https://cloud.google.com/products/ai?hl=zh-cn)|AI 云|BUILD WITH AI – AI Platform、Cloud AutoML、AI 基础组件 和 AI Infrastructure对话 AI – Speech-to-Text、Text-to-Speech、虚拟代理、客服助手、Natural Language、Dialogflow文档 AI – 自然语言 NL、翻译、视觉 OCR、文档 AI API、账单解析器、基础 OCR工业 AI – 媒体翻译、医疗健康自然语言、推荐 AI|
||Google Knowledge Graph|认知智能|[https://blog.google/products/search/introducing-knowledge-graph-things-not/](https://blog.google/products/search/introducing-knowledge-graph-things-not/)[https://developers.google.com/knowledge-graph](https://developers.google.com/knowledge-graph)|
|IBM|IBM Watson[https://www.ibm.com/watson](https://www.ibm.com/watson)Watson is AI for business. IBM’s portfolio of enterprise-ready pre-built applications, tools and runtimes are designed to reduce the costs and hurdles of AI adoption while maximizing outcomes and responsible use of AI.|AI + 行业|行业：Financial、Travel、Healthcare、Retail、Services、Security、Supply Chain[https://cloud.ibm.com/developer/watson/documentation](https://cloud.ibm.com/developer/watson/documentation)**Watson Assistant**、**Discovery**、Natural Language Understanding、Speech to Text、Text to Speech、Natural Language Classifier、Tone Analyzer、Language Translator、**Watson Studio、Knowledge Studio**、Machine Learning、**Watson Knowledge Catalog**|
|特斯拉|Autopilot[https://www.tesla.com/autopilotAI](https://www.tesla.com/autopilotAI)我们开发和部署了大规模的自主权。 我们相信，基于视觉和计划的高级AI的方法，以及有效使用推理硬件的支持，是实现全面自动驾驶通用解决方案的唯一途径。|自动驾驶|[https://www.tesla.com/support/autopilot](https://www.tesla.com/support/autopilot)|
|亚马逊|AWS AIAI 服务：AWS的人工智能服务提供云端的自然语言理解 (NLU)、自动语音识别 (ASR)、视觉搜索和图像识别、文本转语音 (TTS) 及机器学习 (ML) 托管服务。AI 平台：AWS推荐使用MXNet作为深度学习框架，以获得高度可扩展、灵活且快速的模型训练体验。AWS 可以提供针对 CPU 和 GPU EC2 实例优化过的深度学习 AMI 和 CloudFormation 模板。AI 基础设施：神经网络其中涉及增加大量模型的过程。Amazon EC2 P2 实例提供功能强大的 Nvidia GPU，这大大缩短了完成这些计算所需的时间。[https://aws.amazon.com/cn/events/amazon-ai/#aws-element-modal-96df9910-8361-4427-a724-448c979ded78](https://aws.amazon.com/cn/events/amazon-ai/#aws-element-modal-96df9910-8361-4427-a724-448c979ded78)|AI 平台|<!-- TODO image: re-host on Aliyun OSS, then replace with ![智能系统](OSS_URL "caption"). Original saved at intelligent_systems_images/intelligent_systems_1.png -->[Amazon Rekognition 使用机器学习自动执行图像和视频分析](https://aws.amazon.com/cn/rekognition/?blog-cards.sort-by=item.additionalFields.createdDate&blog-cards.sort-order=desc)[Amazon Polly 使用深度学习将文本转换为逼真的语音](https://aws.amazon.com/cn/polly/)[Amazon Lex 聊天机器人对话 AI](https://aws.amazon.com/cn/lex/)[Amazon SageMaker 面向所有数据科学家和开发人员的机器学习服务](https://aws.amazon.com/cn/sagemaker/)SageMaker Ground Truth 轻松大规模标记用于机器学习的训练数据SageMaker Neo 随处运行 ML 模型，性能提升高达 25 倍SageMaker Studio 是首个用于机器学习的完全集成开发环境，可大规模构建、训练和部署 ML 模型SageMaker Autopilot 是业内首个自动化机器学习功能，可让您完全掌控 ML 模型。[Amazon EMR 轻松运行和扩展 Apache Spark、Hive、Presto 以及其他大数据框架](https://aws.amazon.com/cn/emr/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)ML：[https://aws.amazon.com/cn/machine-learning/](https://aws.amazon.com/cn/machine-learning/)|
|微软|Microsoft Azure 平台[https://azure.microsoft.com/zh-cn/overview/ai-platform/](https://azure.microsoft.com/zh-cn/overview/ai-platform/)|AI 云|Azure 认知搜索：[https://docs.microsoft.com/zh-cn/azure/search/](https://docs.microsoft.com/zh-cn/azure/search/)Azure 认知服务：[https://docs.microsoft.com/zh-cn/azure/cognitive-services/](https://docs.microsoft.com/zh-cn/azure/cognitive-services/)|
|SAP|SAP制造执行 (SAP ME)[https://www.sap.com/products/execution-mes.html](https://www.sap.com/products/execution-mes.html)|智能工业制造|[https://help.sap.com/saphelp_me60/helpdata/en/04/510820335f4e129df327de58689a22/frameset.htm](https://help.sap.com/saphelp_me60/helpdata/en/04/510820335f4e129df327de58689a22/frameset.htm) 核心能力：集中运营 – 使用单个集中式解决方案来管理和控制制造和车间作业。自动数据收集 – 通过自动数据收集，减少了手动输入数据的需求，提高了准确性，并加快了管理流程。缺陷跟踪和解决 – 强制执行流程规则，提供说明并跟踪缺陷，以帮助确保防错制造。|
|Facebook|框架和工具[https://ai.facebook.com/tools#frameworks-and-tools](https://ai.facebook.com/tools#frameworks-and-tools)|工具|PyTorch：是一个开源深度学习框架，旨在灵活，模块化地进行研究，并具有生产部署所需的稳定性和支持。它可以通过基于磁带的autograd系统进行快速，灵活的实验，该系统旨在立即执行和类似python的执行。ONNX：是用于深度学习模型的开放格式，可让AI开发人员轻松在最新工具之间切换。Tensor Comprehensions：通过自动从高级数学运算生成代码来加速开发。Glow：是一种机器学习编译器，可加快深度学习框架在不同硬件平台上的性能。FAISS：使开发人员可以快速搜索彼此相似的多媒体文档的嵌入。StarSpace：是一种通用的神经嵌入模型，可以应用于许多机器学习任务，包括排名，分类，信息检索，相似性学习和推荐。与现有方法都具有很高的竞争力，同时可以很好地推广到新的用例。Visdom：可以生成实时数据的丰富可视化图像，以帮助开发人员掌握科学实验的最前沿。DynaBench：是用于动态数据收集和基准测试的研究平台。COVID-19预测：Facebook AI正在帮助研究人员，公共卫生专家和组织更好地了解COVID-19的传播。|
||库，模型和数据集[https://ai.facebook.com/tools#libraries-models-and-datasets](https://ai.facebook.com/tools#libraries-models-and-datasets)|库，模型和数据集|计算机视觉Detectron2是FAIR的下一代对象检测和分割平台。DensePose旨在将RGB图像的所有人类像素映射到基于3D表面的人体表示。WSL嵌入允许基于在大型数据集上训练的模型进行图像识别功能的实验。语言PyText是基于PyTorch构建的基于深度学习的自然语言处理（NLP）建模框架。FastText是一个轻量级的库，旨在帮助构建可扩展的文本表示和分类解决方案。Translate是基于Facebook的机器翻译系统的开源项目。ParlAI是一个平台，可简化跨多个任务的研究，培训和评估对话模型的过程。Fairseq是一个序列建模工具包，用于训练定制模型以进行翻译，摘要和其他文本生成任务。MUSE是一个Python库，可以更快地开发和评估跨语言单词嵌入和NLP。VizSeq是用于自然语言生成（翻译，字幕，摘要等）的研究工具包。CoVoST是一个大型的多语言语音到文本翻译语料库。KILT是用于培训，评估和分析有关知识密集型语言任务的NLP模型的资源。演讲Wav2letter是用于转录语音的端到端自动语音识别（ASR）系统。Libri-light训练弱监督和无监督语音模型的大型数据集。推理ELF是用于游戏研究的平台，允许开发人员在各种游戏环境中训练和测试其算法。ELF OpenGo是Facebook AI Research（FAIR）的AI机器人，击败了世界冠军的专业围棋选手。House3D是一个丰富的环境，其中包含带有完整标签的数千个视觉逼真的房屋3D场景。PHYRE 物理推理的基准，其中包含2D环境中的一组简单的经典力学难题。TorchCraft是一个库，可用于AI研究实时策略（RTS）游戏，例如《星际争霸：巢穴之战》。ReAgent是用于大型推理系统（强化学习，情境强盗）的平台。多式联运可恶的 Memes：可恶的模因挑战和数据集是一个竞争性开源数据集，旨在衡量多模式视觉和语言分类中的进度。|

## 其他报告

|时间|出品单位|链接|
|:----|:----|:----|
|2019|德勤|链接: [https://pan.baidu.com/s/18NA-8XlY_3CyhYll06KKDg](https://pan.baidu.com/s/18NA-8XlY_3CyhYll06KKDg)  密码: eqeo|
|2019|中国科学院大数据挖掘与知识管理重点实验室|链接: [https://pan.baidu.com/s/1Jysl5a0oosGvYnZ7C5r2eg](https://pan.baidu.com/s/1Jysl5a0oosGvYnZ7C5r2eg)  密码: 1o2p|
|2020|法国里昂商学院|链接: [https://pan.baidu.com/s/175CcNMWmw5u1eXaBKVt2jw](https://pan.baidu.com/s/175CcNMWmw5u1eXaBKVt2jw)  密码: morq|
