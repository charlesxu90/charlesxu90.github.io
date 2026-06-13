---
title: "TTS 语音合成"
subtitle: ""
date: 2023-11-01
draft: false
author: "Xiaopeng Xu"
description: "TTS 语音合成相关笔记。"
tags: ["TTS", "Speech"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

原文参考：[https://zhuanlan.zhihu.com/p/622980527](https://zhuanlan.zhihu.com/p/622980527)


## 1. 语音合成任务简介

### 1.1. 语音与文本

对比语音来说，NLP技术在深度学习中更为普及。在介绍语音合成任务前，我们先来了解语音这一模态的特点，并将其与文本模态对比。

#### 文本模态：

1. 表示为离散的token序列；

2. 短序列，例如每个句子10-20词；

3. 高度抽象，几乎每个词都包含语义信息，因此信息密度较高。

#### 语音模态：

1. 表示为连续值的序列；

2. 极长序列，如每句话3s，16k采样率，则每句话由48000个连续值的序列表示；

3. 信息密度极低，因此有短时不变性，可以从一个片段推测相邻片段的信号。

#### 语音vs文本：

1. 语音是自然语言的超集，理想中的语音既包含自然语言中完整的文本内容（语义信息），也包含语音特有的音色、语气、韵律、情感等声学信息；

2. 观察二者对比可以发现，语音中的总体信息多于文本，但信息密度极低，序列过长；

3. 此外，语音用连续值表示，因此语音合成是回归任务，而非语言模型的分类任务。


2-3两个特点，使得NLP中的常用方法难以用于语音合成：

1. 对于极长序列，难以使用自回归策略以及seq2seq的生成方案（并非不行，但效率低）；

2. 由于语音合成是回归任务，语言模型中许多常用的技术无法应用，而回归任务也比分类任务的稳定性更低。

### 1.2. 语音合成任务

在语音合成的相关任务中，我们主要关注文本语音合成（Text-to-Speech Synthesis, TTS），该任务旨在给定一段文本，合成与文本对应的语音。根据上文中的分析可以发现，从文本到语音的合成会面对三个问题：

1. 长度差异大，语音信号长度是文本序列的上千倍，难以跨越这么大的长度差异，直接从文本合成语音；

2. 模态差异大，主要是信息含量不同，文本中只包含语义信息，而语音包含语义信息和丰富的声学信息；

3. 生成任务困难，基于回归任务的生成通常难于分类任务。


基于1和2两个问题，TTS任务难以实现端到端的合成，因此**主流的TTS方法通常使用pipeline框架**，使用声学特征作为中间表征，将模型分为三部分。具体地，常见的TTS模型分为**文本分析（Text Analysis）, 声学模型（Acoustic Model）和声码器（Vocoder）**：

#### 1. 文本分析模块：

* 1) 该模块主要负责将输入文本从字素(Grapheme)转为音素(Phoneme)，音素是发音的最小单元，类似拼音或音标，是比文字本身更适合语音合成的输入形式；

* 2) 此外，该模块还经常负责韵律、音调以及中文的分词等任务；

* 3) 该模块被称作TTS的前端，并不是TTS pipeline的重点。

#### 2. 声学模型(Acoustic Model, AM)：

* 1) 该模块主要负责通过音素预测TTS的中间表征，中间表征一般是某种手工声学特征，例如最常用的梅尔频谱(Mel-Spectrogram, 后称Mels) ；

* 2) 以Mels为例，如果每秒语音所对应的音素长度为10，Mels长度通常为100-200，长度差异约为1+个数量级，在可接受范围内；

* 3) 声学模型主要对合成语音的语义质量负责，即决定合成出的语音是否符合输入文本，此外，语音中的情感、韵律等也现象也主要与声学模型有关。

#### 3. 声码器：

* 1) 该模块主要负责将Mels等中间表征还原为音频，该模块主要决定合成语音的音质；

* 2) 例如，在16k采样率下，声码器会将100+长度的Mels还原为16k长度的语音，跨越约2个数量级；

* 3) Vocoder的训练不需要文本作为输入，因此可以使用audio-only的训练数据；但是，由于声学模型的预测Mels通常与真实Mels的特征空间存在差异，实际使用中需要将vocoder在AM的输出上finetune一遍效果才比较好，此时依然需要利用成对的文本-语音数据。


## 1.3. 主流声学模型简介

接下来简单介绍一下当前主流的声学模型，不展开讲，只用来分析当前存在的问题

### 1.3.1. Tacotron (2017)

Tacotron是比较早期的深度TTS模型了，介绍它主要是介绍一下自回归的AM思路，模型结构如下：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032142902.webp)
* 1. Tacotron直接从文本生成Mels，省去了前端转音素的步骤，而且使用了基于传统方法的声码器，在这个角度上算是end-to-end的语音合成；不过为了保证效果，需要使用更好的声码器，此时仍然是pipeline；

* 2. tacotron的主体结构是一个seq2seq的模型，中间有一个attention模块负责对齐mels和文本，生成部分由一个RNN负责，RNN每次同时生成mels中的若干帧，直到预测出全0向量停止；

* 3. tacotron的生成质量并不差，但问题是自回归太慢了，即使一次生成若干帧也很慢。

### 1.3.2. FastSpeech2 (2020)

FS2是近两年很常见的声学模型，FastSpeech主要针对之前模型速度太慢的问题，抛弃了自回归策略，完全并行，整体结构如下：

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032144362.webp)

* 1. FastSpeech的Encoder和Decoder都改为了非自回归的Transformer encoder结构，非自回归的结构如何决定序列长度呢？作者引入了Duration Predictor，在Decoder前预测每个音素对应的Mels帧数，随后把每个音素的特征复制对应次数，预先确定了序列长度再生成；

* 2. 非自回归的策略降低了模型精度，换来的是整体速度大幅度提升；

* 3. FastSpeech2额外引入了对语音energy和pitch的预测，对应响度和音高，大幅度提高了精度；

* 4. 此外，FastSpeech 2还尝试了end-to-end的生成，实验证明end-to-end的性能略微降低，训练速度大幅度降低，end-to-end的声学模型都有这些问题，因此pipeline依然是TTS的主流思路。

## 1.4. TTS的主要问题与优化思路

### 1.4.1. 主要问题

基于上述讨论以及AM中存在的问题，我们将TTS中存在的主要问题分为以下几点：

* 1. 文本和语音之间存在长度、模态差异，难以端到端生成

   * 1) 解决方案： 使用pipeline策略，用声学特征（Mels等）作为中间表征

   * 2) 存在问题：

      * 1. Pipeline中存在误差累积、训练流程麻烦等问题（vocoder需要finetune）；

      * 2. Mels等传统特征作为中间表征，效率和稳定性较低。

* 2. TTS的生成信号与中间表征是连续的，因此是回归任务，不能做分类任务

   * 1) 回归任务难度较大，稳定性比分类任务低；

   * 2) 回归任务难以利用NLP、语言模型（Language Model, LM）中的seq2seq相关技术和经验

* 3. 干净的文本-语音平行语料需要人工标注，成本较高、数据较少

   * 1) 单模态文本 / 语音语料都很多，但平行语料较少

   * 2) TTS任务对较高质量的文本语料有需求，难以利用ASR的粗糙数据

* 4. 其他问题：TTS本身是一对多任务，一条文本能生成多种语音，如何生成更多样的语音，例如更多说话人的音色、更多情感等，是尚未完全解决的问题。


### 1.4.2. 优化思路

* 1. 基于问题1，最优解是找到合适的end-to-end生成方式，但当前的end-to-end策略都存在各种问题，尚待优化；退而求其次，可以放弃Mels这种传统特征，优化中间表征；

* 2. 结合问题1和2，不难想到，可以考虑将TTS的中间表征离散化：

   * 1) 将中间表征离散化，AM的任务变为预测中间表征tokens，此时是分类任务，任务难度更低、更稳定，且可以利用现有的NLP技术经验；

   * 2) 中间表征离散化后，可以保证AM的预测结果不会出现特征空间上的偏差，减小了pipeline的传播误差，vocoder finetune的必要性降低，一方面简化工作量，另一方面也让vocoder可以利用更多audio-only数据；

   * 3) 作为习得的中间表征，效率和稳定性高于Mels等传统特征。

* 3. 针对问题3，一方面需要加强TTS的鲁棒性，使系统可以利用粗糙数据；另一方面借用预训练思路，让系统能够利用更多单模态数据

## 2. 语音表征离散化相关工作

基于上一节的讨论，我们可以认为，离散化的语音表征对于TTS来说是不错的中间表征。因此，在本节中，我们将讨论两种类型的离散语音表征， 考虑它们的特点以及是否可以应用到TTS中。

### 2.1. 语音预训练中的离散化

提起语音的离散化表征，不难想到HuBERT等语音预训练工作。

语音预训练中的离散化表征，整体思路应该来自NLP中的MLM任务以及BERT等模型，NLP已经证明MLM任务可以学到很强的语义特征提取器；语音本身是连续、无清晰分界、无文本标注的，想要借用MLM等预训练思路，有必要对语音进行离散化，作为语音 / 语义的中间表征：

* 1. 离散化后，任务可以从生成任务改为判别任务，更关注语义信息、效率更高；

* 2. 离散化后，语音表征更为稳定。

当然，语音预训练相关工作通常仅仅将离散化特征作为中间表征，用于优化训练任务，而非最后提取的特征。接下来，我们简单介绍一下这些语音预训练工作。

#### 2.1.1. Wav2vec2.0

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032145914.webp)

耳熟能详的语音预训练技术，这里也不过多介绍了。

* 1. Wav2vec2.0的训练任务是mask帧的特征预测，训练目标基于对比学习，mask帧的真实特征为正例，相邻帧的特征为负例；

* 2. 作者将预测过程中，目标帧的特征离散化，通过实验发现，基于离散化的语音表征进行预训练，模型的性能超过了原本基于连续表征的策略。

#### 2.1.2. HuBERT

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032147117.webp)

HuBERT大家也比较熟悉，基本思路融合了wav2vec2.0和BERT，既然BERT做MLM任务得到的特征质量如此高，语音是否也能利用这种思路，离散化后做MLM？

HuBERT和Wav2vec2.0主要区别有二：

* 1. 预训练任务是离散后的MLM，而不是对比学习；

* 2. 离散表征不是端到端获得的，而是离线通过k-means对特征进行聚类获得。

实验证明，HuBERT在ASR等任务上的性能超过Wav2vec2.0。

#### 2.1.3. W2v-BERT

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032148575.webp)
Wav2vec2.0和HuBERT的结合体，事实上是把对比学习和MLM任务都做了一遍，前若干层做对比学习，并且通过对比学习过程把离散表征学出来（对比HuBERT，可以端到端地获得离散表征，不需要k-means处理），后若干层做MLM训练。

实验证明，该方法比Wav2vec2.0和HuBERT在ASR任务性能上高了5%-10%，说明两个任务都有作用。


### 2.2. 音频编码解码器(Audio Codec)

上述几个模型利用离散化的语音表征，作为模型预训练过程的一部分，虽然没有直接将这些离散化的表征作为最终的特征， 但利用这些表征增加了预训练的效率和稳定性。

那么，这些表征能否直接用于TTS呢？个人认为是不能的：

* 1. 上述模型只做了基于上下文预测的预训练任务，因此，表征中主要是与上下文相关的**语义信息**；

* 2. 相应地，这些表征中**缺乏**足够支持将特征还原为原始语音信号的**声学信息**。


接下来，我们将介绍另一种离散化的音频表征，这些表征来自音频编码解码器(Audio Codec)：

* 1. Audio Codec的基本任务是将一段音频压缩为向量或其他表征，并且根据这些表征可以还原音频——该任务本身类似Auto Encoder, 但有两个重点，一是需要尽可能节约中间表征的比特数，达到低资源应用的目的，二是需要尽可能忠实地还原出原本的音频；

* 2. 当前主流方法：

   * 1) 同样利用离散化的codebook获得离散tokens，离散tokens对应的中间表征作为压缩后的表征；

   * 2) 对于每个离散token，可以用一个整数(或one-hot向量，等价)表示，此时对于N大小的codebook，只需要logN的比特数即可记录，压缩效率较高。

#### 2.2.1. SoundStream

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032150025.webp)
SoundStream是目前性能较好的主流Audio Codec之一，其结构分为Encoder、Vector Quantizer、Decoder三部分：

* 1. Encoder / Decoder使用常规的卷积层和反卷积层，不详细介绍；

* 2. Vector Quantizer是该模型重点，作者提出了一种**Residual Vector Quantitation**, 性能提升较大：

   * 1) 先考虑传统的Vector Quantitation：

      * a) 假设一段音频可以被压缩为S个中间编码，codebook中有N个向量，则音频可以表示为S * N个one-hot向量，消耗比特数为S * log N ;

      * b) 假设音频采样率24k, 每个中间表征编码320帧，则每秒有S = 24000 / 320 = 75个中间编码；

      * c) 假设编码后的比特率为6kbps, 对于75个中间编码，每个编码可用6000 / 75 = 80 bits;

      * d) 参照上面的公式，若充分利用比特率，需要N = 2^80大小的codebook，不可接受，而更小的codebook在高比特率场景又会损失性能。

   * 2) 此时需要考虑多个codebook的设置，但多个codebook如何编码、如何高效利用资源也是一个问题

   * 3) 为此，作者提出**Residual Vector Quantitation (RVQ)**：

      * a) 为平衡codebook大小和比特利用率，本文提出使用多个quantitation block对应多个codebook，它们之间有残差连接，重要性不同；若使用8个codebook，则每个codebook可利用10 bits, 大小为2^8=1024, 可接受；

      * b) 具体地，每个Block在量化时，其量化与真实表征之间的差值会传给下一个block，相当于每个block只会量化前一个block的误差；

      * c) 这样做的好处，一方面区分出不同block的分工和重要性，第一个block中蕴含最重要的信息（偏语义），后续block则负责精确还原语音时的细节信息；另一方面，在训练时我们可以随机sample前k个block进行训练，保证在丢弃后若干个不重要的block时，模型仍然能保持一定精度，此时**模型可以在低比特率时选择性地丢弃后面的blocks，实现了对比特率的动态适应**。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032151107.webp)
* 3. 除此之外，作者还引入了对抗学习，让辨别器判断还原语音与原本语音之间的区别，这里存在一个perception-distortion trade-off，即感知度和保真度的取舍：保真度越高的还原，越可能因为信息丢失而显得过度锐化，从而听起来与原始音频不同；反过来，听感相似的音频，其还原的客观相似度可能并不高。

* 4. 为了同时保证感知度和保真度，作者使用 对抗学习loss 和 Mels/特征重建loss，前者用于保证听感相似，后者则用于保证客观指标相似。

#### 2.2.2. Encodec

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032152147.webp)
一笔带过，框架很类似SoundStream，加入了之前忽略的Waveform重建loss;

值得注意的是，作者为了提高语音解码的实时性，引入了一个小的语言模型，该语言模型根据t时刻的RVQ向量，预测t+1时刻的RVQ向量，用于提前解码下一刻的语音；实验证明该模块在性能没有明显降低的情况下，提高了解码的速度，这意味着RVQ向量中也编码了一定的语音语义信息（实际上我没有看到作者对于该模块性能的实验分析，可能我或作者有所遗漏）

## 3. 语音合成新技术

在上一章节中，我们介绍了语音信号的两种离散化特征，分别是预训练语音模型中用到的离散化特征——基于预训练语音模型任务的特点，这些特征主要编码了上下文相关的信息，也就是语义信息；第二种离散化特征是Audio Codec中用到的RVQ特征，这种特征能以较高的精度还原语音信号，因此其中包含着丰富的声学信息。

理想状态下的TTS，既需要理解文本中的语义，表现为语音中的情感、韵律，又需要在中间表征中编码足够的声学信息，足以还原为高质量的语音；当然，实际上声学信息是必须品，而如果不编码语义信息对单纯的TTS任务影响不大，但可能会影响模型后续的扩展能力。

当前语音合成的新技术注意到了这两种离散化的语音表征，我们可以分别将其称为**语义表示（Semantic Tokens）**和**声学表示（Acoustic Tokens）**，首先将它们应用于语音合成的工作，实际上做的是语音到语音的合成（Speech-to-Speech Synthesis）, 我们将先介绍这篇工作，随后介绍后续的TTS新技术。

### 3.1. AudioLM - 基于Semantic tokens 和 Acoustic tokens, 实现语音层面的语言模型

Speech-to-Speech Synthesis (后称STS) 任务的初衷是**实现语音层面的“语言模型”**，其基本任务与LM类似，给定一段语音，STS需要据此预测后续的语音，该任务有两个特点：

* 1. STS不会经历ASR+LM+TTS的pipeline，而是直接从语音中隐式地推理语义信息，这是更符合人类自然状态的真正“自然语言处理”；

* 2. STS在理解语义信息的同时，还需要有生成高质量语音的能力。

这两点恰好对应了上文提到的**semantic tokens和acoustic tokens**拥有的能力，因此，AudioLM选择利**用这两种tokens作为中介**，此时的STS任务变为了常规的seq2seq序列生成任务，而不再是困难的回归任务。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032153403.webp)
具体地，AudioLM使用**SoundStream**提取语音的Acoustic tokens, 使用**w2v-BERT**提取Semantic tokens（对于w2v-BERT，作者没有使用模型中习得的表征，而是类似HuBERT使用k-means获得表征，可能是实践更优）。随后，Audio LM的主体是一个Decoder-only的LM, 词表包括两种所有tokens，AudioLM将STS划分为三个步骤：

* 1. Semantic Modeling, 也就是根据上文的semantic tokens预测下文；

* 2. Coarse acoustic modeling, 也就是根据整句所有semantic tokens, 预测下文的acoustic tokens, 由于RVQ中不同层的token重要性不同，此处仅预测最重要的前Q'层tokens；

* 3. Fine acoustic modeling, 也就是根据前Q'层acoustic tokens，预测后Q-Q'层acoustic tokens，这些层的重要性降低，并且编码的是更加精细的特征（按照SoundStream的经验，这些层的特征可以选择性丢弃，AudioLM作者在后续工作中讨论了将2和3合并为同一个阶段的影响）

最后，AudioLM根据预测得到的所有acoustic tokens, 使用SoundStream解码得到语音。

#### AudioLM的语音demos

[https://](https://link.zhihu.com/?target=https%3A//google-research.github.io/seanet/audiolm/examples)[google-research.github.io](https://link.zhihu.com/?target=https%3A//google-research.github.io/seanet/audiolm/examples)[/seanet/audiolm/examples](https://link.zhihu.com/?target=https%3A//google-research.github.io/seanet/audiolm/examples)，简单总结一下：

* 1. 给定一段上文语音，AudioLM能够生成听起来合理的下文语音（但表达内容可能不合理）；

* 2. 如果将一段语音的semantic tokens输入，仅生成acoustic tokens, 则模型会生成内容相同但音色、语气和环境均不同的语音，展示了semantic tokens编码语义内容的功能；

* 3. 作者尝试只基于acoustic tokens训练LM，随后生成语音，模型能够生成连贯的语音，但完全是babble，并不是人类语言，再次展示了semantic和acoustic tokens的区别；

* 4. 作者尝试在音乐数据上训练，并且只基于acoustic tokens, 发现能够接上较为连贯的音乐（感觉质量一般）。


### 3.2. VALL-E - 基于Acoustic tokens，实现大规模粗糙语料进行预训练

同样的，基于**语音离散tokens + LM**的思路也可以用在TTS上；相比之下，TTS的问题在于对语料的要求更高，同时要求干净的语音-文本对；VALL-E参考了AudioLM的思路，但仅仅利用了acoustic tokens在TTS任务上，并取得了惊人的效果。

VALL-E的贡献：

* 1. 借助acoustic tokens + LM，使模型在利用大规模粗糙语料（未必清晰的音频+ASR获得的粗糙文本）预训练的基础上，依然能合成清晰的语音，训练语料达到了 60k hours（约是主流模型的百倍以上）；

* 2. LM结构使模型有强大的in-context learning能力：

   * 1) 使用phoneme作为prompt，实现标准的TTS

   * 2) 使用音频做prompt，可以做到zero-shot的新说话人语音合成，以及情感 / 环境等信息的保留， 3s音频即可复刻音色

#### VALL-E的整体框架

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032154649.png)

上图是VALL-E的整体框架：

* 1. 使用Encodec提取离散tokens, 同样以LM形式做语音合成；

* 2. 分别使用文本 / 音频prompt，分别控制语音合成的内容与风格；

* 3. 由于只用了phoneme和acoustic tokens，没有语义信息引入，猜想缺乏语义相关的生成能力，这种能力对TTS并不重要，但或许会影响后续的扩展空间。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032156378.webp)

上图是VALL-E的模型细节，依旧是LM的结构，词表包括所有phoneme以及RVQ向量（此处的RVQ向量来自Encodec）；具体地，模型由多层（或者说多个）decoder组成，每个decoder对应RVQ中的一层，对于对重要的第一层RVQ，VALL-E使用一个自回归的结构进行解码预测；随后，后续每层RVQ的tokens基于上一层的RVQ tokens，使用非自回归的transformer encoder进行解码预测(加快运行)。

最终，将acoustic tokens输回Encodec，生成语音。

#### VALL-E的demos

[https://](https://link.zhihu.com/?target=https%3A//aka.ms/valle)[aka.ms/valle](https://link.zhihu.com/?target=https%3A//aka.ms/valle)，整体效果很好，简单总结一下：

* 1. 给定文本和一段语音prompt，能够合成音色非常接近的语音（3s prompt即可，能做到zero-shot的音色复刻）

* 2. 使用不同的随机数，可以生成韵律不同的语音；

* 3. 能够很大程度地保留语音prompt中说话人所处的噪音环境、说话人语气与情感。

### 3.3. 

### - VALLE的双语言版本，实现跨语言的音色复刻

跨语言场景下，有两类较为重要的语音合成任务：

* 1. 跨语言TTS: 给定A语言说话人的语音、B语言的文字，合成该说话人B语言的语音

   * 1) 任务难点：跨语言的音色迁移、说话人口音问题

* 2. 语音翻译：将一种语言的语音翻译为另一种语言的语音

   * 1) 任务难点：pipeline简单一些，end-to-end难做；如何保持说话人音色


VALL-E的团队使用相同的架构，推出跨语言版本的VALL-E，并主要基于上述两个任务做出了改进。


#### VALLE-X的贡献

* 1. 实现zero-shot的跨语言TTS和zero-shot的语音翻译（都针对说话人而言）——语音翻译并没有做到end-to-end，而是使用了外接的翻译插口，利用phoneme-level的SpeechUT进行翻译；

* 2. 同样用了大规模语料预训练（70k hours）, 同样做到in-context learning；

* 3. 在跨语言复刻音色时，高度保持说话人特点，同时没有外语口音（跨语言的说话人adaption本身是比较难的任务，VALLE-X带来的效果比较惊人）

#### VALL-X的整体架构

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032157825.webp)
上图是VALL-X的整体架构，与VALL-E比较类似；实际上，VALL-X只做了中英双语言，并且在训练时每个sample只包含一种语言，而不会同时输入两种语言，因此VALLE-X的跨语言音色复刻能力实际来自in-context learning.

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032159231.webp)
![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032200713.webp)
上两图分别是VALLE-X的训练过程和inference过程。

#### VALLE-X的demos

[https://](https://link.zhihu.com/?target=https%3A//vallex-demo.github.io/)[vallex-demo.github.io/](https://link.zhihu.com/?target=https%3A//vallex-demo.github.io/) 跨语言的表现实际比单语言还要惊艳一些，总结一下：

* 1. 实现了zero-shot的跨语言音色复刻，并且没有外国口音；

* 2. 对于speech-to-speech translation，由于外接了翻译模型，因此实现类似跨语言TTS，音色复刻效果同样很好；

* 3. 外国口音控制，如果在跨语言TTS过程中，目标language ID填入真实的语言ID，展现的就是目标语言的口音，如果填入另一种语言的ID，展示的则是外语口音，利用language ID能够生成native或者foreign的口音；

* 4. 情感、语气的保持，同样出色；

* 5. 语言编码切换：面对中英夹杂的场景，转换较为自然。

### 3.4. Spear-TTS - AudioLM的后继者，超越VALL-E的TTS方法

#### VALL-E的问题：

* 1. 用了大量粗糙数据做伪标注，实现半监督的预训练，但一方面数据量太大，训练流程较长，另一方面说明该方法仍然需要大量的平行语料才能实现（虽然是粗糙的）；

* 2. VALL-E只考虑了音素和声学信息，缺少语义理解能力，未来扩展可能有问题。

#### Spear-TTS的贡献：

* 1. 使用600h audio-only的数据做预训练，15min平行语料训练，即可超越VALL-E ;

* 2. 使用3s音频，做到zero-shot的复刻音色（与VALL-E同量级）

* 3. TTS本身不涉及语义，但个人认为如果扩展到语义相关的生成任务，Spear-TTS考虑了语义信息的框架会有优势

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032202303.webp)

Spear-TTS的思路与AudioLM一脉相承，同时考虑semantics和acoustics的重要性，因此使用semantic tokens和acoustic tokens分别作为中间表征，构建Text-Semantics-Acousitcs-Speech的层级。

#### Spear-TTS的框架

Spear-TTS的框架主体分为两个大阶段，第一阶段是Text到Semantics，被称为Reading，这个阶段需要使用文本-语音平行语料；第二个阶段是Semantics到Acoustics，被称为Speaking, 可以使用audio-only数据训练。

![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032203507.webp)
上面是阶段1的细节：

* 1. 对于第一个阶段(Text - Semantic), 使用一个类似BART的encoder-decoder结构（后简称BART）;

* 2. 首先，使用audio only的大规模语料预训练一个BART， 任务是semantic tokens的mask prediction;

* 3. 随后微调2中BART用于数据增广，fix encoder， 只训练decoder， 目标是semantic tokens到text的预测；

* 4. 使用3中得到的数据增广BART，从audio-only数据生成文本的伪标注；

* 5. 最终训练 text–semantic tokens的BART， 使用小平行数据和增广数据，finetune 2中预训练BART的底层。


![图片](https://xux-zotero-img.oss-cn-beijing.aliyuncs.com/img/20260613032204554.webp)
上图是阶段2的细节：

* 1. 结构基本是AudioLM，根据AudioLM中的发现，如果在prompt中给了acoustic tokens，则生成语音会follow prompt的音色；否则，会随机生成音色；

* 2. 根据这一现象，训练时统一使用有prompt的版本;

* 3. 放弃了AudioLM中的三阶段，在semantics预测acoustics时，直接预测所有层的RVQ tokens；

* 4. 训练时，阶段1和阶段2是分开训练的。

#### Spear-TTS的demos：

[https://](https://link.zhihu.com/?target=https%3A//google-research.github.io/seanet/speartts/examples/)[google-research.github.io](https://link.zhihu.com/?target=https%3A//google-research.github.io/seanet/speartts/examples/)[/seanet/speartts/examples/](https://link.zhihu.com/?target=https%3A//google-research.github.io/seanet/speartts/examples/)

由于Spear-TTS的模型能力整体对标了VALL-E，因此这里不再详细总结了；根据论文里的MOS指标，Spear-TTS宣称用15min平行数据即可显著超过VALL-E，不过个人听下来没有很显著的差距，或许Speaker-TTS的音质以及韵律多样性是超过VALL-E的。


## 4. 总结

本文主要是为了介绍两种TTS新技术，**VALL-E**和**Spear-TTS**，并且将这些工作的前因后果一并介绍出来。现在，我们可以简单总结这两篇工作，并展望TTS的未来发展。

### 4.1. 对比VALL-E和Spear-TTS

#### VALL-E

* 1. 结构简单，方法暴力，能利用大规模语料，有LLM的感觉；

* 2. 仅考虑了声学信息，仅适用TTS，难以扩展到其他文本 / 语音生成类任务；

* 3. 能利用大规模语料，换句话说依赖大规模语料，对语料利用率似乎不高；

* 4. 做了跨语言实验，效果惊人。

#### Spear-TTS

* 1. 结构和训练流程较为复杂，同样可以利用较大规模的音频语料；

* 2. 综合考虑了声学信息和语义信息，更为合理，易于扩展到相关任务；

* 3. 对语料利用率较高，更适合较低资源的复现，毕竟60k hours语料有些过分了；

* 4. 没做跨语言，本身麻烦的框架看起来迁移到跨语言就更麻烦了。

可以看到两者都存在一定的扩展空间，如果能结合两者优点一定是最好的。

### 4.2. TTS将何去何从

#### 1. TTS面对的问题：

* 1) 文本和语音模态差异大，长度差距明显，因此需要中间表征做pipeline; Mel-spectrogram等传统中间表征效率低、稳定性低，需要优化；

* 2) 干净的文本-语音平行语料珍惜，需要利用单模态或粗糙数据的能力；

* 3) 一对多能力：如何合成多说话人、多情感的语音，即使对应数据很少

#### 2. 研究中的发现：

* 1) 语音预训练模型、语音编码解码器都走上了离散化的道路，二者分别编码了语音中重要的语义信息和声学信息，可以用于TTS乃至STS任务；

* 2) 离散化tokens是优秀的中间表征，稳定性强的同时，提供了利用大规模语料的机会；

* 3) 多样性问题：力大砖飞，预训练后单语言乃至跨语言的说话人迁移都解决了

#### 3. 未来的研究趋势：

* 1) 既然TTS都可以做LLM，针对STS或更general场景下的文本-语音LLM会越来越多；

* 2) 作为中间表征，期望能设计任务获取同时编码语义和声学信息的表征;

* 3) 无论如何，基于离散tokens的TTS范式必将成为TTS研究的新趋势，逐步取代旧有的技术框架。


## References：

### 音频预训练模型

wav2vec 2.0: A framework for self-supervised learning of speech representations

[https://](https://link.zhihu.com/?target=https%3A//proceedings.neurips.cc/paper/2020/file/92d1e1eb1cd6f9fba3227870bb6d7f07-Paper.pdf)[proceedings.neurips.cc/](https://link.zhihu.com/?target=https%3A//proceedings.neurips.cc/paper/2020/file/92d1e1eb1cd6f9fba3227870bb6d7f07-Paper.pdf)[paper/2020/file/92d1e1eb1cd6f9fba3227870bb6d7f07-Paper.pdf](https://link.zhihu.com/?target=https%3A//proceedings.neurips.cc/paper/2020/file/92d1e1eb1cd6f9fba3227870bb6d7f07-Paper.pdf)

HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2106.07447.pdf%3Ffbclid%3DIwAR3hI4uGqc4mV5j-ob8R5yLu-BaamVoe9ncxUoVmgFLjJXsE1IevP0rdNYY)[arxiv.org/pdf/2106.0744](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2106.07447.pdf%3Ffbclid%3DIwAR3hI4uGqc4mV5j-ob8R5yLu-BaamVoe9ncxUoVmgFLjJXsE1IevP0rdNYY)[7.pdf?fbclid=IwAR3hI4uGqc4mV5j-ob8R5yLu-BaamVoe9ncxUoVmgFLjJXsE1IevP0rdNYY](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2106.07447.pdf%3Ffbclid%3DIwAR3hI4uGqc4mV5j-ob8R5yLu-BaamVoe9ncxUoVmgFLjJXsE1IevP0rdNYY)

W2v-bert: Combining contrastive learning and masked language modeling for self-supervised speech pre-training

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2108.06209)[arxiv.org/pdf/2108.0620](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2108.06209)[9](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2108.06209)

### 音频编码解码器

High Fidelity Neural Audio Compression (Encodec)

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2210.13438)[arxiv.org/pdf/2210.1343](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2210.13438)[8](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2210.13438)

SoundStream: An End-to-End Neural Audio Codec

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2107.03312)[arxiv.org/pdf/2107.0331](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2107.03312)[2](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2107.03312)

### 语音合成新技术

AudioLM: a Language Modeling Approach to Audio Generation

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2209.03143)[arxiv.org/pdf/2209.0314](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2209.03143)[3](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2209.03143)

Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers (VALL-E)

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2301.02111)[arxiv.org/pdf/2301.0211](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2301.02111)[1](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2301.02111)

Speak Foreign Languages with Your Own Voice: Cross-Lingual Neural Codec Language Modeling (VALLE-X)

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2303.03926)[arxiv.org/pdf/2303.0392](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2303.03926)[6](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2303.03926)

Speak, Read and Prompt: High-Fidelity Text-to-Speech with Minimal Supervision (Spear-TTS)

[https://](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2302.03540)[arxiv.org/pdf/2302.0354](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2302.03540)
