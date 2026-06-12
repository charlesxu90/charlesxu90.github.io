---
title: "Nanopore 信号分析"
subtitle: ""
date: 2024-02-07
draft: false
author: "Xiaopeng Xu"
description: "Nanopore 原始电信号数据格式与信号分析笔记。"
tags: ["Nanopore", "Bioinformatics", "Signal Processing"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## 原始测序电信号数据格式

### FAST5 数据格式

[https://github.com/nanoporetech/fast5_research](https://github.com/nanoporetech/fast5_research)

[https://blog.csdn.net/Emmett_Bioinfo/article/details/113847543](https://blog.csdn.net/Emmett_Bioinfo/article/details/113847543)

[https://zhuanlan.zhihu.com/p/137069950](https://zhuanlan.zhihu.com/p/137069950)


FAST5格式（.fast5）实际上是在HDF5格式上的一种变体。HDF是Hierarchical Data Format的首字母缩写，从名字上就可以看出来这种文件格式储存信息的方式是层级嵌套的（hierarchical, nested）。它采用chunking（分解）的方式来存储多维数据，它内部表现出来的是类似于文件夹（树）的结构。由于这种文件层级分解的特性，想要获取某一部分信息，只需要获得该部分信息所在的chunk即可，这样就让这种文件格式非常的flexible，也非常适合用于多种编程语言来处理。FAST5格式是Oxford推出Nanopore测序之后在HDF5格式的基础上设计用于存储Nanopore测序信息的文件。


#### 使用`h5ls`命令查看

```powershell
$ h5ls -r /home/pengxi/2021nanopore_data/F5_data/20210205-BNL0526-PAG41930/fast5_pass/barcode01/PAG41930_pass_barcode01_80f14244_0.fast5
```
结果：
```powershell
/read_fff14025-a57b-45de-9a84-426435575674 Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Basecall_1D_000 Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Basecall_1D_000/BaseCalled_template Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Basecall_1D_000/BaseCalled_template/Fastq Dataset {SCALAR}
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Basecall_1D_000/Summary Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Basecall_1D_000/Summary/basecall_1d_template Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Segmentation_000 Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Segmentation_000/Summary Group
/read_fff14025-a57b-45de-9a84-426435575674/Analyses/Segmentation_000/Summary/segmentation Group
/read_fff14025-a57b-45de-9a84-426435575674/Raw Group
/read_fff14025-a57b-45de-9a84-426435575674/Raw/Signal Dataset {4837/Inf}
/read_fff14025-a57b-45de-9a84-426435575674/channel_id Group
/read_fff14025-a57b-45de-9a84-426435575674/context_tags Group, same as /read_00083fc0-0f1f-4bac-ac95-f55c944b6a6d/context_tags
/read_fff14025-a57b-45de-9a84-426435575674/tracking_id Group, same as /read_00083fc0-0f1f-4bac-ac95-f55c944b6a6d/tracking_id
```
可以看一下这个fast5文件的结构，每一条（图中这条可以认为它的“根目录”是 /read_fff14025-a57b-45de-9a84-426435575674）下都分为了几个层级（像文件归档路径一样），主要的是Analyses和Raw这两个层级，前者里面放的好像是Basecalling信息，也就是判断碱基的结果，还有segmentation划分信息，而后者里面放的是原始电信号的信息，也就是basecalling的依据

#### 用h5dump命令查看

```powershell
$ h5dump -A -g '/Raw' abf2bulkfast5.fast5  # view /Raw
$ h5dump abf2bulkfast5.fast5  # view all
```
结果：
```powershell
HDF5 "abf2bulkfast5.fast5" {
GROUP "/Raw" {
   GROUP "Channel_1" {
      ATTRIBUTE "description" {
         DATATYPE  H5T_STRING {
            STRSIZE H5T_VARIABLE;
            STRPAD H5T_STR_NULLTERM;
            CSET H5T_CSET_ASCII;
            CTYPE H5T_C_S1;
         }
         DATASPACE  SCALAR
         DATA {
         (0): "ABF"
         }
      }
      ATTRIBUTE "digitisation" {
         DATATYPE  H5T_STD_I64LE
         DATASPACE  SCALAR
         DATA {
         (0): 65536
         }
      }
      ATTRIBUTE "offset" {
         DATATYPE  H5T_IEEE_F64LE
         DATASPACE  SCALAR
         DATA {
         (0): 0
         }
      }
      ATTRIBUTE "range" {
         DATATYPE  H5T_IEEE_F64LE
         DATASPACE  SCALAR
         DATA {
         (0): 40000
         }
      }
      ATTRIBUTE "sample_rate" {
         DATATYPE  H5T_STD_I64LE
         DATASPACE  SCALAR
         DATA {
         (0): 10000
         }
      }
      DATASET "Signal" {
         DATATYPE  H5T_STD_I16LE
         DATASPACE  SIMPLE { ( 10000 ) / ( 10000 ) }
      }
   }
}
}
```
这里面大概放的就是一些Raw data所具有的属性（Attribute）了，具体的数据应该存储在最后一个DATASET "Signal"里面。

### POD5 数据格式

[https://github.com/nanoporetech/pod5-file-format](https://github.com/nanoporetech/pod5-file-format)

POD5  是 Nanopore 推出的最新的电信号存储格式。目前 Nanopore 的 MinKNOW 系统默认的输出格式是 POD5, 因为相比广泛使用的 FAST5格式， POD5 格式读写快且压缩比高。


```powershell
pod5 convert to_fast5  pod5_pass/*.pod5 -r -o fast5_pass
```
#### 查看 POD5

##### 查看 summary 信息

```powershell
pod5 view PAU73183_pass_15caf1a1_68646c47_2571.pod5 | less
```
会展示类似 samtools view 的一个概要表格。
##### 查看单条 read信息

```powershell
pod5 inspect read PAU73183_pass_15caf1a1_68646c47_2571.pod5 e3213511-fbb8-4d67-9e68-80ffa6cf0333
```
#### 将 FAST5 转为 POD5

FAST5 和 POD5 之间可以很方便的相互转换。可以使用 POD5 工具转换[https://github.com/nanoporetech/pod5-file-format](https://github.com/nanoporetech/pod5-file-format)

#### 将 POD5 转为 FAST5

```powershell
pod5 convert to_fast5  pod5_pass/*.pod5 -r -o fast5_pass
```




## ReadUtil API

[https://github.com/nanoporetech/read_until_api](https://github.com/nanoporetech/read_until_api)

### 简介

ReadUtil API 是 Nanopore 提供得一个支持自适应采样的API。这使得支持复杂生物实验预处理过程，能够由测序仪本身执行。 

自适应采样可以实现以下功能：

* **富集Enrichment**：可以富集包含感兴趣的 reads，如编码基因的 reads

* **滤除Depletion**：可以拒绝来自不感兴趣的 reads，例如宏基因组中，滤除宿主相关的序列

* **平衡Balancing**：用户可以使用自适应采样来平衡标记序列，确保实现每个标记序列的目标深度，并通过拒绝已经达到目标深度的基因组区域的链而均匀覆盖整个基因组，从而获得覆盖率较低的区域的序列。


目前这一功能还只是为科研提供，并不是商用服务。只支持 MinION 20.06 以后得 MinKNOW 版本 (MinKNOW-Core 4.04)。


### 客户端 (Client) 介绍

Read Until 包为 MinKNOW 的 gRPC 接口的必要部分提供了一个高级接口。 开发人员可以专注于创建丰富的分析，而不是处理 MinKNOW 提供的数据的较低级别细节。 

Read Util 功能的目的是基于任何可想象的分析选择性地“解锁（unblock）”测序通道（channel）以增加对感兴趣的分析物进行测序所花费的时间。可以请求 MinKNOW 发送连续的“read chunks”流（具有可配置的最小大小），通过客户端 (client) 可以对其进行分析。


客户端核心代码在 read_until.base.ReadUntilClient 类中，可以简单地导入该类：

```python
from read_until import ReadUntilClient
```
这个类的接口已详细记录，同时开发人员可以从 gRPC stream 开发自己的自定义客户端提供了额外的注释。 鼓励开发人员阅读代码和内联文档（可以使用 docs make 目标构建 HTML 版本）。

客户端管理的 gRPC stream 是双向的：它既可以向客户端传送原始数据“read chunks”，又可以向 MinKNOW 传送“action responses”。 客户端实现两个队列，操作队列 .action_queue 和 reads 读取对列 read_until.base.ReadCache。 

1. 操作队列 **.action_queue**相当简单：对 MinKNOW 解锁(unblock) channel 的请求将暂时存储在这里，捆绑在一起进行分发。

2. Reads 读取队列**read_until.base.ReadCache**相对复杂。 Client 将读取的块（block）存储在这里以准备分析。 该队列还以通道为 key，因此它只存储来自每个测序通道（channel）的一个块； 从而保护 Client 的 consumer 免受已结束的读取的影响。 这种方法的一个限制是 consumer 无法组合来自同一 read 的多个块的数据。 如果需要此读取同一 read 的多个块的数据，可以使用 ReadCache 来实现一个自定义的客户端，作为参数传递给 ReadUntilClient 实例即可。但由于延迟对于基于 ReadUtil 开发的应用十分重要，因此建议尽可能少的数据来分析，设置接收的 **chunk size**就好了。


#### Client 类

##### **函数 .run(kwargs**)**

指示 client 类开始从 MinKNOW 检索 read chunk

**kwargs参数:

* first_channel, last_channel, raw_data_type, 和 sample_minimum_chunk_size

##### **函数 .get_read_chunks(**batch_size=1, last=True**)**

获取从 MinKNOW 检索到的最新数据， 将它们从队列中删除

参数:

* batch_size – 最大读取次数

* last – 获取最新的（或者最旧的）

##### **函数 .unblock_read(**read_channel, read_number, duration=0.1**)** 

请求从通道 channel 中弹出 reads

参数:

* read_channel – read 的 channel 号

* read_number – read 的编号（通道的第 n 个 read）

* duration – 施加解锁电压的时间（以秒为单位）

##### **函数 .stop_reciving_read(**read_channel, read_number**)** 

请求 MinKNOW 不再向 client 发送更多读取数据 

参数:

* read_channel – read 的 channel 号

* read_number – read 的编号（通道的第 n 个 read）

##### 函数 reset(timeout=5)

队列中没有数据或请求时，将客户端的状态重置为初始（未运行）状态

##### 属性 is_running

Client/gRPC 流的处理状态

##### 属性 missed_chunks

队列中同一 read 得块替换（read chunk replace）的此数（单个 read 得块可能会被多次替换）

##### 属性 missed_reads

从队列中弹出的 read 数量（即，read 有一个或多个 chunk 进入分析队列，但在被从队列中推出之前被另一个 read 替换

##### 属性queue_length

读取队列的长度


#### Client 的使用示例

```python
from read_until import ReadUntilClient

client = ReadUntilClient(filter_strands=True, one_chunk=False)
client.run(first_channel=1, last_channel=512)

while client.is_running is False:
    time.sleep(0.1)

duration=0.1
throttle=0.4
batch_size=512

while client.is_running:
    t0 = timer()
    unblock_batch_reads = []
    stop_receiving_reads = []

    for i, (channel, read) in enumerate(client.get_read_chunks(batch_size=batch_size, last=True), start=1):
        raw_data = np.fromstring(read.raw_data, client.signal_dtype)
        unblock_batch_reads.append((channel, read.number))
        stop_receiving_reads.append((channel, read.number))

    if len(unblock_batch_reads) > 0:
        client.unblock_read_batch(unblock_batch_reads, duration=duration)
        client.stop_receiving_batch(stop_receiving_reads)

    t1 = timer()
    if t0 + throttle > t1:
        time.sleep(throttle + t0 - t1)
else:
    logger.info("Client stopped, finished analysis.")
```


### Client 和 MinKNOW 通讯消息

#### Client 发送给 MinKNOW 的消息

```json
message GetLiveReadsRequest {
    enum RawDataType {
        // Don't change the previously specified setting for raw data sent
        // with live reads note: If sent when there is no last setting, NONE
        // is assumed.
        KEEP_LAST = 0;
        // No raw data required for live reads
        NONE = 1;
        // Calibrated raw data should be sent to the user with each read
        CALIBRATED = 2;
        // Uncalibrated data should be sent to the user with each read
        UNCALIBRATED = 3;
    }

    message UnblockAction {
        // Duration of unblock in seconds.
        double duration = 1;
    }

    message StopFurtherData {}

    message Action {
        string action_id = 1;

        // Channel name to unblock
        uint32 channel = 2;

        // Identifier for the read to act on. If the read requested is no
        // longer in progress, the action fails.
        oneof read { string id = 3; uint32 number = 4; }

        oneof action {
            // Unblock a read and skip further data from this read.
            UnblockAction unblock = 5;

            // Skip further data from this read, doesn't affect the read
            // data.
            StopFurtherData stop_further_data = 6;
        }
    }

    message StreamSetup {
        // The first channel (inclusive) for which to return data. Note
        // that channel numbering starts at 1.
        uint32 first_channel = 1;

        // The last channel (inclusive) for which to return data.
        uint32 last_channel = 2;

        // Specify the type of raw data to retrieve
        RawDataType raw_data_type = 3;

        // Minimum chunk size read data is returned in.
        uint64 sample_minimum_chunk_size = 4;
    }

    message Actions { repeated Action actions = 2; }

    oneof request {
        // Read setup request, initialises channel numbers and type of data
        // returned. Must be specified in the first message sent to MinKNOW.
        // Once MinKNOW has the first setup message reads are sent to the
        // caller as requested. The user can then resend a setup message as
        // frequently as they need to in order to reconfigure live reads -
        // for example by changing if raw data is sent with reads or not.
        StreamSetup setup = 1;

        // Actions to take given data returned to the user - can only be
        // sent once the setup message above has been sent.
        Actions actions = 2;
    }
}
```


#### Client 从 MinKNOW 收到的消息

```json
message GetLiveReadsResponse {
    message ReadData {
        // The id of this read, this id is unique for every read ever
        // produced.
        string id = 1;

        // The MinKNOW assigned number of this read. Read numbers always
        // increment throughout the experiment, and are unique per channel,
        // however they are not necessarily contiguous.
        uint32 number = 2;
        
        // Absolute start point of this read
        uint64 start_sample = 3;
        
        // Absolute start point through the experiment of this chunk
        uint64 chunk_start_sample = 4;
        
        // Length of the chunk in samples
        uint64 chunk_length = 5;
        
        // All Classifications given to intermediate chunks by analysis
        repeated int32 chunk_classifications = 6;
        
        // Any raw data selected by the request. The type of the elements
        // will depend on whether calibrated data was chosen. The
        // get_data_types() RPC call should be used to determine the
        // precise format of the data, but in general terms, uncalibrated
        // data will be signed integers and calibrated data will be
        // floating-point numbers.
        bytes raw_data = 7;
        
        // The median of the read previous to this read. intended to allow
        // querying of the approximate level of this read, comapred to the
        // last. For example, a user could try to verify this is a strand be
        // ensuring the median of the current read is lower than the
        // median_before level.
        float median_before = 8;
        
        // The media pA level of this read from all aggregated read chunks
        // so far.
        float median = 9;
    };
    
    message ActionResponse {
        string action_id = 1;
        enum Response { SUCCESS = 0; FAILED_READ_FINISHED = 1; }
        Response response = 2;
    }
    
    // The number of samples collected before the first sample included is
    // this response. This gives the position of the first data point on
    // each channel in the overall stream of data being acquired from the
    // device (since this period of data acquisition was started).
    uint64 samples_since_start = 1;
    
    // The number of seconds elapsed since data acquisition started.
    // This is the same as ``samples_since_start``, but expressed in
    // seconds.
    double seconds_since_start = 2;
    
    // In progress reads for the requested channels. Sparsely populated as
    // not all channels have new/incomplete reads.
    map<uint32, ReadData> channels = 4;
    
    // List of responses to requested actions, informing the caller of
    // results to requested unblocks or discards of data.
    repeated ActionResponse action_reponses = 5;
}
```
