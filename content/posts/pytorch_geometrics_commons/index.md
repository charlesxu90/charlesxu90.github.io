---
title: "Torch Geometric 常用命令"
subtitle: ""
date: 2022-08-10
draft: false
author: "Xiaopeng Xu"
description: "PyTorch Geometric（PyG）常用命令与图数据处理速查。"
tags: ["PyTorch", "GNN", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

Torch Geometric（PyG）是一个基于PyTorch的用于处理不规则数据（比如图）的库，或者说是一个用于在图等数据上快速实现表征学习的框架。由于速度和方便的优势，PyG 是当前最流行和广泛使用的GNN库。

安装

```Python
 conda install pyg -c pyg 
```

## Data

torch\_geometric\.data这个模块包含了一个叫 Data 的类。这个类允许你非常简单的构建你的图数据对象。你只需要确定两个东西：

1. 节点的属性/特征（the attributes/features associated with each node, node features）

2. 邻接/边连接信息（the connectivity/adjacency of each node, edge index

### 方法一：连接信息要以COO格式进行存储

在COO格式中，COO list 是一个2\*E 维的list。第一个维度的节点是源节点\(source nodes\)，第二个维度中是目标节点\(target nodes\)，连接方式是由源节点指向目标节点。对于无向图来说，存贮的source nodes 和 target node 是成对存在的。

```Python
import torch
from torch_geometric.data import Data

x = torch.tensor([[2,1],[5,6],[3,7],[12,0]],dtype=torch.float)
y = torch.tensor([[0,2,1,0,3],[3,1,0,1,2]],dtype=torch.long)
edge_index = torch.tensor([[0,1,2,0,3], [1,0,1,3,2]],dtype=torch,long)

data = Data(x=x,y=y,edge_index=edge_index)
```

### 方法二：连接信息要以 edge list 格式进行存储

第二种方法在使用时要调用contiguous\(\)方法。

边索引的顺序跟Data对象无关，或者说边的存储顺序并不重要，因为这个edge\_index只是用来计算邻接矩阵（Adjacency Matrix）。

```Python
import torch
from torch_geometric.data import Data

x = torch.tensor([[2,1],[5,6],[3,7],[12,0]],dtype=torch.float)
y = torch.tensor([[0,2,1,0,3],[3,1,0,1,2]],dtype=torch.long)

edge_index = torch.tensor([[0, 1], [1, 0], [2, 1], [0, 3]，[2, 3]], dtype=torch.long)

data = Data(x=x,y=y,edge_index=edge_index.contiguous())
```

## Dataset

PyG提供两种不同的数据集类：

- InMemoryDataset

- Dataset

### InMemoryDataset

要创建一个 InMemoryDataset，必须实现几个函数：

- Raw\_file\_names\(\)：它返回一个包含没有处理的数据的名字的list。如果你只有一个文件，那么它返回的list将只包含一个元素。事实上，你可以返回一个空list，然后确定你的文件在后面的函数process\(\)中。

- Processed\_file\_names\(\)：很像上一个函数，它返回一个包含所有处理过的数据的list。在调用process\(\)这个函数后，通常返回的list只有一个元素，它只保存已经处理过的数据的名字。

- Download\(\)：这个函数下载数据到你正在工作的目录中，你可以在self\.raw\_dir中指定。如果你不需要下载数据，你可以在这函数中简单的写一个 pass 就好。

- Process\(\)：这是Dataset中最重要的函数。你需要整合你的数据成一个包含data的list。然后调用 self\.collate\(\)去计算将用DataLodadr的片段。
下面这个例子来自PyG官方文档。

```Python
import torch
from torch_geometric.data import InMemoryDataset

class MyOwnDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(MyOwnDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return ['some_file_1', 'some_file_2', ...]

    @property
    def processed_file_names(self):
        return ['data.pt']

    def download(self):
        # Download to `self.raw_dir`.

    def process(self):
        # Read data into huge `Data` list.
        data_list = [...]

        if self.pre_filter is not None:
            data_list [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
```

## DataLoader

DataLoader 这个允许通过batch的方式 feed 数据。创建一个DataLoader实例，可以简单的指定数据集和期望的 batch size。

```Python
loader = DataLoader(dataset, batch_size=512, shuffle=True)
```

DataLoader 的每一次迭代都会产生一个Batch对象。它非常像 Data 对象。但是带有一个 ‘batch’ 属性。它指明了了对应图上的节点连接关系。因为 DataLoader 聚合来自不同图的的batch 的 x,y 和 edge\_index，所以 GNN 模型需要 batch 信息去知道那个节点属于哪一图。

```Python
for batch in loader:
    batch
#>>> Batch(x=[1024, 21], edge_index=[2, 1568], y=[512], batch=[1024])
```

## MessagePassing

这个 GNN 的本质，它描述了节点的 embeddings 是怎样被学习到的。

要使用 MessagePassing 这个框架，就要重新定义三个方法：

1. message

2. update

3. aggregation scheme
在实现 message 的时候，节点特征会自动 map 到各自的 source and target nodes。 aggregation scheme 只需要设置参数就好，sum, mean or max。

对于一个简单的GCN来说，我们只需要按照以下步骤，就可以快速实现一个GCN：

1. 添加 self\-loop 到邻接矩阵（Adjacency Matrix）。

2. 节点特征的线性变换。

3. 标准化节点特征。

4. 聚合邻接节点信息。

5. 得到节点新的embeddings
1、2 需要在message passing 前计算好。3\-5 可以用 torch\_geometric\.nn\.MessagePassing 类。

添加 self\-loop 的目的是让 featrue 在聚合的过程中加入当前节点自己的 feature，没有 self\-loop 聚合的就只有邻居节点的信息。

### GCN 例子

Example 1 下面是官方文档的一个GCN例子，其中注释中的Step 1\-5对应上文的步骤1\-5\.

```Python
import torch
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import add_self_loops, degree

class GCNConv(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super(GCNConv, self).__init__(aggr='add')  # "Add" aggregation.
        self.lin = torch.nn.Linear(in_channels, out_channels)

    def forward(self, x, edge_index):
        # x has shape [N, in_channels]
        # edge_index has shape [2, E]

        # Step 1: Add self-loops to the adjacency matrix.
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))

        # Step 2: Linearly transform node feature matrix.
        x = self.lin(x)

        # Step 3-5: Start propagating messages.
        return self.propagate(edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_j, edge_index, size):
        # x_j has shape [E, out_channels]

        # Step 3: Normalize node features.
        row, col = edge_index
        deg = degree(row, size[0], dtype=x_j.dtype)
        deg_inv_sqrt = deg.pow(-0.5)
        norm = deg_inv_sqrt[row] * deg_inv_sqrt[col]

        return norm.view(-1, 1) * x_j

    def update(self, aggr_out):
        # aggr_out has shape [N, out_channels]

        # Step 5: Return new node embeddings.
        return aggr_out
```

所有的逻辑代码都在 forward\(\) 里面，当我们调用 propagate\(\) 函数之后，它将会在内部调用message\(\) 和 update\(\)。

### SAGE 例子

Example 2 下面是一个 SAGE 的例子

```Python
import torch
from torch.nn import Sequential as Seq, Linear, ReLU
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops

class SAGEConv(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super(SAGEConv, self).__init__(aggr='max') #  "Max" aggregation.
        self.lin = torch.nn.Linear(in_channels, out_channels)
        self.act = torch.nn.ReLU()
        self.update_lin = torch.nn.Linear(in_channels + out_channels, in_channels, bias=False)
        self.update_act = torch.nn.ReLU()
        
    def forward(self, x, edge_index):
        # x has shape [N, in_channels]
        # edge_index has shape [2, E]

        edge_index, _ = remove_self_loops(edge_index)
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))
        
        return self.propagate(edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_j):
        # x_j has shape [E, in_channels]
        x_j = self.lin(x_j)
        x_j = self.act(x_j)
        
        return x_j

    def update(self, aggr_out, x):
        # aggr_out has shape [N, out_channels]
        new_embedding = torch.cat([aggr_out, x], dim=1)
        new_embedding = self.update_lin(new_embedding)
        new_embedding = self.update_act(new_embedding)
        
        return new_embedding
```
