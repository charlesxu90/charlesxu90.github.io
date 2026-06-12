---
title: "PyTorch 常用命令"
subtitle: ""
date: 2023-12-05
draft: false
author: "Xiaopeng Xu"
description: "PyTorch 常用命令与张量操作速查笔记。"
tags: ["PyTorch", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Tensor 操作

文档：[https://pytorch\.org/docs/stable/index\.html](https://pytorch.org/docs/stable/index.html)

### Tensor 相关属性

#### 查看 device

```Python
example_tensor.device
```

#### 查看 shape

```Python
example_tensor.shape
example_tensor.size(1)
```

#### 查看元素个数

```Python
example_tensor.numel()
```

### Tensor 元素索引

```Python
example_scalar = example_tensor[1, 1, 0]
example_scalar.item()
example_tensor[:, 0, 0]
```

### Tensor 初始化

#### 0, 1 或随机数

```Python
torch.ones_like(example_tensor)
torch.zeros_like(example_tensor)
torch.randn_like(example_tensor)
torch.randn(2, 2, device='cpu') # Alternatively, for a GPU tensor, you'd use device='cuda'
torch.arange(4 * 5 * 6).view(4, 5, 6) # shape [4,5,6]
```

#### `torch.clone` 复制 tensor

```Python
real_clone = real.clone()
```

#### `F.one_hot` 生成多分类 tensor

```Python
F.one_hot(labels % n_classes)
```

#### `nn.init.*` 填充 tensor

```Python
nn.init.xavier_uniform_(tensor) # fill with uniform distribution, values scaled by 'gain'
nn.init.constant_(bias, 0) # fill with constant
nn.init.orthogonal_(param) # with a (semi) orthogonal matrix
```

### 基础函数

#### 逐元素加减乘 mul, \*

```Python
(example_tensor - 5) * 2 # 顺序有影响
torch.mul(tensor_x, tensor_x) # 逐元素积
tensor_x * tensor_y # 逐元素积 = torch.mul(x, y)
```

#### Tensor 乘法 matmul, @, bmm, dot

[https://blog\.csdn\.net/foneone/article/details/103876519](https://blog.csdn.net/foneone/article/details/103876519)

```Python
torch.matmul(tensor_x, tensor_x)  # 张量乘法，类似矩阵乘法, 支持维度的 broadcast， 当输入均为 3 维时，和 bmm 一样 
tensor_x @ tensor_y # 和 torch.matmul(A, B) 一样

torch.bmm(tensor_x, tensor_y)  # 和 torch.matmul(A, B) 一样, 但只支持三维 tensor，常用于 Attention 计算，其中, tensor_x 是 weight_matrix， tensor_y 是 hidden_matrix

torch.dot(tensor_vec_x, tensor_vec_y)  # 和 torch.matmul(A, B) 类似, 但只支持一维 tensor
```

#### 求 mean 和 std

```Python
example_tensor.mean()
example_tensor.std()

# mean over one dimension
example_tensor.mean(0)
example_tensor.mean(dim=0) # or axis=0
torch.mean(example_tensor, dim=0) # or axis=0
```

#### 返回所有元素的乘积

```Python
a = torch.randn(1, 3)  # [0.3618 1.2095 -0.3403]
torch.prod(a)  # -0.14892165020372308
```

### 高级计算

#### torch\.isclose 查看两个 tensor 是否相近

```Python
torch.isclose(tensorA, tensorB)
```

#### torch\.norm 计算模

```Python
torch.norm(torch.ones(4, 2), dim=1)
# tensor([2., 2.])
torch.norm(torch.ones(4, 2), dim=1)
# tensor([1.4142, 1.4142, 1.4142, 1.4142])
```

#### torch\.lerp 两个 tensor 的线性插值

linear interpolation of two tensors `start` \(given by `input`\) and `end` based on a scalar or tensor `weight` and returns the resulting `out` tensor\.

out*i*=start*i*\+ weight*i*×\(end*i*− start*i*\)

```Python
start = torch.arange(1., 5.)
end = torch.empty(4).fill_(10)
torch.lerp(start, end, 0.5)
```

### 维度变换

#### `torch.transpose` 转置

对两个维度进行转置

```Python
tensor_A.transpose(0, 1)
tensor_A.transpose(-2, -1)
```

#### `torch.expand` 增加维度

增加 dimension 并复制值

```Python
tensor_A = torch.ones(4)
tensor_A.expand([2,3,4])
```

#### torch\.unsqueeze  拓展维度

返回一个新的张量，对输入的既定位置插入维度 1。

```Python
a = torch.randn(2, 3)  # shape= [2, 3]
torch.unsqueeze(a, dim=0)  # shape = [1, 2, 3]
a.unsqueeze(dim=-1) # shape = [2, 3, 1]
# dim range [-a.dim() -1, a.dim()]
```

注意： 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。

##### unsqueeze\_ 和 unsqueeze 的区别

unsqueeze\_ 和 unsqueeze 实现一样的功能,区别在于 unsqueeze\_ 是 in\_place 操作,即 unsqueeze 不会对使用 unsqueeze 的 tensor 进行改变,想要获取 unsqueeze 后的值必须赋予个新值, unsqueeze\_ 则会对自己改变。

#### torch\.squeeze 缩减空维度

多维张量本质上就是一个变换，如果维度是 1 ，那么，1 仅仅起到扩充维度的作用，而没有其他用途，因而，在进行降维操作时，为了加快计算，是可以去掉这些 1 的维度。

```Python
m = torch.zeros(2, 1, 2, 1, 2) # shape = [2, 1, 2, 1, 2]
n = torch.squeeze(m)  # shape = [2， 2， 2]
```

#### permute 维度换位

将 tensor 的维度换位。后面为各个维度的 index。

```Python
a = torch.tensor([[[1,2,3],[4,5,6]]]) # shape = [1, 2, 3]
a_p =a.permute(2,0,1)  # shape = [3, 1, 2]
# tensor([[[ 1,  4]], [[ 2,  5]], [[ 3,  6]]])
```

#### view 重构维度

重构张量的维度。

```Python
a = torch.tensor([[[1,2,3],[4,5,6]]]) # shape = [1, 2, 3]
a_v =a.view(1,3,2)  # shape = [3, 1, 2]
# tensor([[[ 1,  2], [ 3,  4], [ 5,  6]]])
```

### 数据转换

#### tensor 与 list 相互转换

```Python
# list to tensor(cpu)
l0 = [1, 2, 3]
t = torch.Tensor(l0)

# tensor(cpu) to list
l1 = t.numpy().tolist()
```

#### tensor 与 numpy 相互转换

```Python
# Tensor(cpu) to numpy
t = torch.ones(5)
a = t.numpy()
print(a) #  [1. 1. 1. 1. 1.]
# 注意，转换后的tensor与numpy指向同一地址，所以，对一方的值改变另一方也随之改变

# Numpy to tensor(cpu)
t1 = torch.from_numpy(a)
```

### 其他

#### `nn.Identity`

恒等函数

```Python
m = nn.Identity()
m(torch.ones(2, 2))
# tensor([[1., 1.], [1., 1.]]) 
```

## 基础模型模块

通常在`torch.nn` 模块中。

### `nn` 类结构

需要定义两个函数 **init** 和 forward。其他参数可以通过 nn\.Module 自动继承。

```Python
class ExampleModule(nn.Module):
    def __init__(self, input_dims, output_dims):
        super(ExampleModule, self).__init__()
        self.linear = nn.Linear(input_dims, output_dims)
        self.exponent = nn.Parameter(torch.tensor(1.))
        self._init_params()

    def forward(self, x): # What to return after pass x to model
        x = self.linear(x)
        x = x ** self.exponent 
        return x
    
    def _init_params(self):  # For special cases
        # init parameters here
```

#### 查看 nn 参数

```Python
example_model = ExampleModule(10, 2)
list(example_model.parameters()) # Parameters without name
list(example_model.named_parameters()) # Parameters & names
```

#### 使用示例

```Python
input = torch.randn(2, 10)
example_model(input)
```

#### 保存模型

```Python
def get_path(base_dir, base_name, suffix):
    return os.path.join(base_dir, base_name + suffix)

def save_gpt_model(model, base_dir, base_name):
    raw_model = model.module if hasattr(model, "module") else model
    torch.save(raw_model.state_dict(), get_path(base_dir, base_name, '.pt'))
```

#### 加载模型

```Python
def get_path(base_dir, base_name, suffix):
    return os.path.join(base_dir, base_name + suffix)

# Need config and checkpoint file
def load_model(model, model_weights_path, device, copy_to_cpu=True):
    raw_model = model.module if hasattr(model, "module") else model
    map_location = lambda storage, loc: storage if copy_to_cpu else None
    raw_model.load_state_dict(torch.load(model_weights_path, map_location))
    return raw_model.to(device)
```

### 模型层

#### `nn.Linear`

Initialize a linear layer which performs the operation Ax\+b, where A and 𝑏 are initialized randomly when you generate the `nn.Linear()` object\.

```Python
linear = nn.Linear(10, 2)
example_input = torch.randn(3, 10)
example_output = linear(example_input)
```

#### nn\.Sequential

简单方便的创建模型。Creates a single operation that performs a sequence of operations\.

```Python
mlp_layer = nn.Sequential(
    nn.Linear(5, 2),
    nn.BatchNorm1d(2),
    nn.ReLU()
)
test_example = torch.randn(5,5) + 1

print(mlp_layer(test_example))
```

#### `nn.Embedding`

A simple lookup table that stores embeddings of a fixed dictionary and size\.

Often used to store word embeddings and retrieve them using indices\. The input to the module is a list of indices, and the output is the corresponding word embeddings\.

```Python
embedding = nn.Embedding(10, 3)
input = torch.LongTensor([[1,2,4,5],[4,3,2,9]])
embedding(input)
```

#### `nn.BatchNorm1d`

A normalization technique that will rescale a batch of 𝑛 inputs to have a consistent mean and standard deviation between batches\.

`nn.BatchNorm1d` takes an argument of the number of input dimensions of each object in the batch \(the size of each example vector\)\.

```Python
batchnorm = nn.BatchNorm1d(2)
batchnorm_output = batchnorm(relu_output)
```

### 激活函数

#### `nn.ReLU`

Create an object that, when receiving a tensor, will perform a ReLU activation function\.

```Python
relu = nn.ReLU()
relu_output = relu(example_output)
```

#### `nn.LeakyReLU`

```Python
nn.LeakyReLU(0.2)
```

## 自然语言处理模型 NLP model

### 数据预处理

通常自然语言处理模型是按 batch 来进行计算的。所以需要对一个batch 的数据做一些预处理。包括两块，一个是拓展到同一长度，给较短的文本增加 pad。使用 pack\_padded\_sequence 和 pad\_packed\_sequence 可以提升这一步骤的效率。

#### pad\_sequence

对序列进行填充，默认填充值是0\.

```Python
def collate_fn(data):
    data.sort(key=lambda x: len(x), reverse=True)
    data = pad_sequence(data, batch_first=True, padding_value=0)
    return data

data_loader = DataLoader(data, batch_size=2, shuffle=True, collate_fn=collate_fn)
```

#### pack\_padded\_sequence

对填充后的序列作 pack，提升计算效率。

```Python
def collate_fn(data):
    data.sort(key=lambda x: len(x), reverse=True)
    seq_len = [s.size(0) for s in data] # 获取数据真实的长度
    data = pad_sequence(data, batch_first=True)    
    data = pack_padded_sequence(data, seq_len, batch_first=True)
    return data

data_loader = DataLoader(data, batch_size=2, shuffle=True, collate_fn=collate_fn)
```

需要注意的是，默认条件下，我们必须把输入数据按照序列长度从大到小排列后才能送入 pack\_padded\_sequence ，否则会报错。

#### pack\_sequence

实际上就是对 pad\_sequence 和 pack\_padded\_sequence 操作的一个封装。通过一个函数完成了两步才能完成的工作。

```Python
def collate_fn(data):
    data.sort(key=lambda x: len(x), reverse=True)
    data = pack_sequence(data)
    return data

data_loader = DataLoader(data, batch_size=2, shuffle=True, collate_fn=collate_fn)
```

#### pad\_packed\_sequence

实际上是 pack\_padded\_sequence 函数的逆向操作。就是把压紧的序列再填充回来。

```Python
def collate_fn(data):
    data.sort(key=lambda x: len(x), reverse=True)
    seq_len = [s.size(0) for s in data]
    data = pad_sequence(data, batch_first=True).float()    
    data = data.unsqueeze(-1)
    data = pack_padded_sequence(data, seq_len, batch_first=True)
    return data
   
data_loader = DataLoader(data, batch_size=2, shuffle=True, collate_fn=collate_fn)
```

### 模型层

#### `nn.LSTM`

## 图像模型 Image model

### 二维操作 2D Operations

#### `nn.Conv2d`

2D卷积，需要输入 I/O 的 channel 和 kernel 大小

```Python
nn.Conv2d(input_channels, output_channels, kernel_size, stride)
```

#### `nn.ConvTranspose2d`

转置后的卷积，也需要输入 I/O 的 channel 和 kernel 大小

```Python
nn.ConvTranspose2d(input_channels, output_channels, kernel_size, stride)
```

#### `nn.BatchNorm2d`

需要输入的 dimension

```Python
nn.BatchNorm2d(output_channels)
```

#### `nn.Upsample`

需要最终大小 final size 和一个因子值 scale factor。

```Python
nn.Upsample((starting_size, starting_size), mode='bilinear')
```

#### `nn.functional.interpolate`

和 `nn.Upsample` 的输入一样。需要最终大小 final size 和一个因子值 scale factor。

```Python
nn.functional.interpolate((starting_size, starting_size), mode='bilinear')
```

## 损失函数 Loss

Loss 见：[https://pytorch\.org/docs/stable/nn\.html\#loss\-functions](https://pytorch.org/docs/stable/nn.html#loss-functions)

### 回归问题

最常用的是 MSELoss。

### NLP 问题

最常用的是 CrossEntropyLoss。

### 图像问题

#### `nn.BCEWithLogitsLoss`

This loss combines a Sigmoid layer and the BCELoss in one single class\. This version is more numerically stable\. Popular in GAN\.

```Python
criterion = nn.BCEWithLogitsLoss()
```

## 模型训练 Train

### 训练类 Trainer

```Python
import logging
from tqdm import tqdm
import numpy as np
import torch
from torch.utils.data.dataloader import DataLoader
from torch.utils.tensorboard import SummaryWriter
from model import save_model

logger = logging.getLogger(__name__)

class Trainer:
    def __init__(self, model, output_dir='./', learning_rate=3e-4, betas=(0.9, 0.95), grad_norm_clip=1.0, multi_gpu=False):
        ...

    def _save_checkpoint(self, base_dir, info, valid_loss):
        ...
.        
    def train(self, train_dataset, test_dataset=None, n_epochs=10, batch_size=64, num_workers=0):
        ...
```

#### Trainer init

```Python
class Trainer:
    def __init__(self, model, output_dir='./', learning_rate=3e-4, betas=(0.9, 0.95), grad_norm_clip=1.0, multi_gpu=False):
        self.model = model

        self.learning_rate = learning_rate
        self.betas = betas
        self.grad_norm_clip = grad_norm_clip
        self.lr_decay = lr_decay

        self.output_dir = output_dir
        self.writer = SummaryWriter(self.output_dir)

        self.device = 'cpu'
        if torch.cuda.is_available():
            self.device = torch.cuda.current_device()
            if multi_gpu:
                self.model = torch.nn.DataParallel(self.model).to(self.device)
```

#### Trainer save checkpoint

Save checkpoint during training

```Python
class Trainer:
    def _save_checkpoint(self, base_dir, info, valid_loss):
        """save checkpoint during training. Format: model_{info}_{valid_loss}"""
        base_name = f'model_{info}_{valid_loss:.3f}'
        logger.info(f'Save model {base_name}')
        save_model(self.model, base_dir, base_name)
```

#### Trainer train

Save checkpoint during training

```Python
class Trainer:
    def train(self, train_dataset, test_dataset=None, n_epochs=10, batch_size=64, num_workers=0):
        model = self.model
        raw_model = model.module if hasattr(self.model, "module") else model
        optimizer = raw_model.configure_optimizers(self.learning_rate, self.betas)

        def run_epoch(split):
            ...
            return loss

        train_loss, test_loss, best_loss = float('inf'), float('inf'), float('inf')
        for epoch in range(n_epochs):
            train_loss = run_epoch('train')

            if test_dataset is not None:
                test_loss = run_epoch('test')
                if test_loss < best_loss:
                    self._save_model(self.output_dir, str(epoch + 1), test_loss)
                    best_loss = test_loss

            if test_dataset is None:  # save every step if no test dataset
                self._save_model(self.output_dir, str(epoch + 1), train_loss)

        final_loss = test_loss if test_dataset is not None else train_loss
        self._save_model(self.output_dir, 'final', final_loss)
```

#### Trainer run\_epoch

Run a epoch during training

```Python
class Trainer:
    def train(self, train_dataset, test_dataset=None, n_epochs=10, batch_size=64, num_workers=0):
        ...
        def run_epoch(split):
            is_train = True if split == 'train' else False
            model.train(is_train)
            data = train_dataset if is_train else test_dataset
            loader = DataLoader(data, shuffle=True, pin_memory=True, batch_size=batch_size, num_workers=num_workers)

            losses = []
            pbar = tqdm(enumerate(loader), total=len(loader)) if is_train else enumerate(loader)
            for it, (x, y) in pbar:
                x = x.to(self.device)
                y = y.to(self.device)

                with torch.set_grad_enabled(is_train):
                    logits, loss = model(x, y)
                    loss = loss.mean()  # collapse all losses if they are scattered on multiple gpus
                    losses.append(loss.item())

                if is_train:
                    model.zero_grad()
                    loss.backward()
                    torch.nn.utils.clip_grad_norm_(model.parameters(), self.grad_norm_clip)
                    optimizer.step()
                    pbar.set_description(f"epoch {epoch + 1} iter {it}: train loss {loss.item():.5f}")

            loss = float(np.mean(losses))
            logger.info(f'{split}, epoch: {epoch + 1}/{n_epochs}, loss: {loss:.4f}')
            self.writer.add_scalar('loss', loss, epoch + 1)  # rewrite if having test dataset
            return loss
         ...
```

### 优化方法 Optimizers

通常导入为 `optim`。 Adam optimizer 最为常用，对应的是`optim.Adam` 。通过 `nn` 对象的`parameters()` 方法来获取模型的参数。

```Python
import torch.optim as optim
adam_opt = optim.Adam(model.parameters(), lr=1e-1)
```

Pytorch 目前支持的 optimizer 包括 Adadelta, Adagrad, Adam, AdamW, SparseAdam, Adamax, ASGD, LBFGS, NAdam, RAdam, RMSprop, Rprop, SGD。
其中，随机梯度下降法 SGD、Adagrad、Adam、都是属于梯度下降法的变式。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGQ1NjVlMmRmODU4YTdmYjg4NmNlYzY4YmJhNjQ0MzBfMTY3ZGZlMGE1NzUxOTJmN2Q1ZmE2M2IwNzYxZDU5ZDRfSUQ6NzM0MDc1ODc0NjU1NDk1NzgyN18xNzgxMjk0MDEwOjE3ODEzODA0MTBfVjM)

另一类牛顿法，是一种二阶收敛算法，能够以较远的目光全局的逼近目标函数。

#### 如何选择 optimizer

如果数据是稀疏的，就用自适用方法，即 Adagrad, Adadelta, RMSprop, Adam。**整体来讲，Adam 是最好的选择**。RMSprop, Adadelta, Adam 在很多情况下的效果是相似的。Adam 就是在 RMSprop 的基础上加了 bias\-correction 和 momentum，随着梯度变的稀疏，Adam 比 RMSprop 效果会好。很多论文里都会用 SGD，没有 momentum 等。SGD 虽然能达到极小值，但是比其它算法用的时间长，而且可能会被困在鞍点。

如果需要更快的收敛，或者是训练更深更复杂的神经网络，需要用一种自适应的算法。

[https://www\.cnblogs\.com/guoyaohua/p/8542554\.html](https://www.cnblogs.com/guoyaohua/p/8542554.html)

Adam 训练速度快，但是 generalize 不如 SGD with momentum。所以用 AdamW 在这种问题中效果会好一些。AdamW 准确性可以与 SGD 匹敌。

[https://towardsdatascience\.com/why\-adamw\-matters\-736223f31b5d](https://towardsdatascience.com/why-adamw-matters-736223f31b5d)

Review:

[https://ruder\.io/optimizing\-gradient\-descent/](https://ruder.io/optimizing-gradient-descent/)

### 模型训练 training

PyTorch 基础的 training 过程包括 4 个部分:

1. 使用`opt.zero_grad()`将所有的 gradients 设为 0；

2. 计算`loss`；

3. 使用`loss.backward()`根据 loss 计算 gradients；

4. 使用 `opt.step()`更新优化后的参数。

```Python
train_example = torch.randn(100,5) + 1
adam_opt.zero_grad() # 1
cur_loss = torch.abs(1 - mlp_layer(train_example)).mean() # 2
cur_loss.backward() # 3
adam_opt.step() # 4
print(cur_loss) 
```

其他优化相关内容

1. 通过 requires\_grad\_\(\) 函数告诉 PyTorch 需要对某个 tensor 计算 gradient。

2. PyTorch 会默认计算 tensor 的 gradient，通常比较耗时。如果在某段代码中不需要计算，可将其包在 with torch\.no\_grad\(\) 里面。

3. 有时可以通过 B\.detach\(\) 来将 B 的值赋予 A，同时不计算 gradient。

### 模型评估 eval

在模型训练过程中，需要对模型进行评估，以确定模型的好坏。评估过程通常是使用 evaluation 的 dataset。针对这个数据集，模型计算过程中不应计算 gradient。因此需要对模型进行特殊的处理。

```Python
for epoch in range(N_EPOCH):
    # train model
    ...    
    # evaluate model:
    net.eval() # changing the behavior of the nn.Module
    with torch.no_grad():  # changing the behavior of the autograd to disable gradient
        y_pred = net(x.float())
        mseLoss = torch.nn.MSELoss(reduction='sum')(y_pred, y.float())
        loss_values.append(loss_v)

    # enable training
    net.train()
```

即将支持（或已经支持）的功能：

```Python
@torch.no_grad()
def eval(model, data):
  model.eval()
  # Rest of eval code
```

### LR 衰减 （lr\_scheduler）

在深度学习模型中，最重要的两个部分，一个是 loss，一个是 optimizer。optimizer 中最重要的参数是 learning rate，对结果的影响极大。

通常，为了使得模型学习更快、且学习过程中不局限在最小值，需要比较大的 lr。但是为了让模型更精准，在模型最后的几个步骤，希望模型的 lr 更小，这个可以更逼近最优点。这个时候使用 lr decay 可以同时实现这两个目标。

Pytorch中已经提供了几个 LR decay 的方案，叫 lr\_scheduler。共有 14 中 lr decay 的方案。比较常用的是 ExponentialLR。

参考：[https://www\.kaggle\.com/isbhargav/guide\-to\-pytorch\-learning\-rate\-scheduling](https://www.kaggle.com/isbhargav/guide-to-pytorch-learning-rate-scheduling)

#### ExponentialLR

通过在 epoch 循环中调研 step\(\) 来更新 lr。

```Python
model = [Parameter(torch.randn(2, 2, requires_grad=True))]
optimizer = SGD(model, 0.1)
scheduler = ExponentialLR(optimizer, gamma=0.9)

for epoch in range(20):
    for input, target in dataset:
        optimizer.zero_grad()
        output = model(input)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
    scheduler.step()
```

## 数据预处理 Dataset \& Dataloader

### Dataset

创建 dataset，用于 Dataloader 的输入。

### Dataloader

作为每个 batch 需要加载的数据集合。

## 迁移学习操作 Transfer learning

### 获取特征向量

需要去掉最后一个全链接 \(fully\-connected, fc\) 层。有三种方式。

```Python
Model.fc = nn.Identity() # method 1
Model.fc = nn.Sequential() # method 2
newmodel = torch.nn.Sequential(*(list(Model.children())[:-1])) # method 2
```

## torchrun 并行计算

torchrun 是 python \-m torch\.distributed\.launch 的一个简化版本，可以便捷的支持多 GPU 计算和分布式计算。

有人测算，在单机上用 Distributed Data\-Parallel 甚至比 Data\-Parallel 效率还快，参见 [https://theaisummer\.com/distributed\-training\-pytorch](https://theaisummer.com/distributed-training-pytorch)。个人实测单机 Distributed Data\-Parallel 速度和 Data\-Parallel 相近，但 batch size 显著减小。原因是模型会在每个 GPU 上都有一个版本，因此导致模型占用的内存增大。

### 分布式计算初始化

```Python
from utils.dist import init_distributed

init_distributed()
```

实际执行的代码：

```Python
def init_distributed():
    dist_url = "env://" # default

    # only works with torch.distributed.launch // torch.run
    rank = int(os.environ["RANK"])
    world_size = int(os.environ['WORLD_SIZE'])
    local_rank = int(os.environ['LOCAL_RANK'])
    dist.init_process_group(
            backend="nccl",
            init_method=dist_url,
            world_size=world_size,
            rank=rank)
    
    torch.cuda.set_device(local_rank)
    dist.barrier()
```

### 定义分布式计算数据集

#### 设置随机 seed

```Python
from torch.utils.data.distributed import DistributedSampler
from utils.dist import get_rank

seed = args.seed + global_rank
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)
```

get\_rank 代码：

```Python
import torch.distributed as dist

def is_dist_avail_and_initialized():
    if not dist.is_available():
        return False
    if not dist.is_initialized():
        return False
    return True

def get_rank():
    if not is_dist_avail_and_initialized():
        return 0
    return dist.get_rank()
```

#### 定义数据集

核心是增加了sampler，做数据抽样，这时需要注意 rank。

```Python
from torch.utils.data.distributed import DistributedSampler

train_data, valid_data = load_data(config.data.input_path, col_name=config.data.col_name,)
train_set, test_set = CrossDataset(train_data), CrossDataset(valid_data)



train_sampler = DistributedSampler(dataset=train_set, shuffle=True, rank=global_rank)
train_dataloader = DataLoader(train_set, batch_size=config.data.batch_size, sampler=train_sampler, num_workers=10, pin_memory=True)

test_sampler = DistributedSampler(dataset=test_set, shuffle=False, rank=global_rank)
test_dataloader = DataLoader(test_set, batch_size=config.data.batch_size, sampler=test_sampler, shuffle=False, num_workers=10, pin_memory=True)
```

### Trainer 设置

#### 模型并行化

需要注意并行化需要 在 apex fp16 混合计算之后。

```Python
if torch.cuda.is_available():  # for distributed parallel
    self.model = torch.nn.SyncBatchNorm.convert_sync_batchnorm(self.model.cuda())
    local_rank = int(os.environ['LOCAL_RANK'])
    self.model = torch.nn.parallel.DistributedDataParallel(self.model, device_ids=[local_rank])
```

#### epoch 运行设置

每个 epoch 需要调用 sampler 的 set\_epoch\(\) 函数。这是为了确保数据 shuffle 正常工作，否则，每个 epoch 中数据调用都会使用相同的顺序。

```Python
loader.sampler.set_epoch(epoch)  # for distributed parallel
```

#### 模型保存

为确保模型只在主程序中做 save 操作，需要增加一个判断

```Python
if not is_dist_avail_and_initialized() or is_main_process():  # for distributed parallel
    save_model(self.model, base_dir, base_name)
```

对应函数

```Python
def is_main_process():
    return get_rank() == 0
```

### 运行 torchrun

```PowerShell
# 单击双卡运行
torchrun --nproc_per_node=2 train_bert.py # ...
```

位数。用 FP16 计算，效率高而且省内存。

Apex 是 Navidia 开发的一个机器学习模型并行计算方法。通过简单的命令，可以实现 FP32/FP16 混合精度或 FP16 计算。

### 安装 apex

不能直接通过 pip 安装，需要从 github 库安装。

```PowerShell
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" ./
```

### 使用 apex

Apex 支持三种模式 O1 for mixed, O2 for almost fp16, O3 for fp16。默认 O1 即可。

```Python
# Allow Amp to perform casts as required by the opt_level
model, optimizer = amp.initialize(model, optimizer, opt_level="O1")
self.model = nn.parallel.DistributedDataParallel(self.model, device_ids=[local_rank]) # 分布式计算，model parallel 需要在 apex.initialize 之后
...
# loss.backward() becomes:
with amp.scale_loss(loss, optimizer) as scaled_loss:
    scaled_loss.backward()
...
```

## Pytorch AMP 混合精度计算

AMP 是 Apex 的一个替代方案。在 Pytorch 1\.6 后已经支持，后续 Apex 将被取消，只支持 amp。

通常是通过两个函数 autocast 和 GradScaler 的调用实现 AMP。

### autocast

torch\.autocast 的实例可以为选定的区域启用自动转换精度，会自动选择 GPU 运算的精度，以在保持准确性的同时提高性能。

```Python
with torch.autocast(device_type=self.device, dtype=torch.float16, enabled=self.use_amp):
    loss = model.forward(x, y)
```

### GradScaler

torch\.cuda\.amp\.GradScaler 帮助方便地执行梯度缩放的步骤，通过 minimize gradient underflow 来提高 float16 梯度下网络的收敛性。

```Python
model.zero_grad()

with torch.autocast(device_type=self.device, dtype=torch.float16, enabled=self.use_amp):
  ...
  scaler.scale(loss).backward(retain_graph=True)

scaler.unscale_(optimizer)
torch.nn.utils.clip_grad_norm_(model.parameters(), self.grad_norm_clip)
scaler.step(optimizer)
scaler.update()
scheduler.step()
optimizer.zero_grad(set_to_none=True)
```

注意：

1. 在多个 loss 组合作为最终 loss 时，对每一个 loss 需要单独做 backward\(\)。否则会出发bug。

2. scaler\.scale\(loss\)\.backward\(\) 必须在 with torch\.autocast 内操作，否则会导致loss计算出问题。

## Pytorch lightning

Lightning 实现可以比较便捷的实现 Pytorch 的并行计算，包括分布计算和多 GPU 计算。其优势在这里有描述。[https://www\.ithome\.com/0/578/800\.htm](https://www.ithome.com/0/578/800.htm)

典型功能：

1. 优化机器学习 pipeline

2. 并行数据加载

3. 使用分布式数据并行的多 GPU 训练

4. 混合精度

5. 早停法

6. Sharded Training
缺点：

7. pl 的 trainer 对 memory 使用效率不高，自己写 batch\_size 会更大；

8. 如果做复杂项目，pl 的一些限制，不适合很多复杂模型场景，如 RL\+DNN，CL等。

使用中，核心是 创建 LightningModule 和 使用 pl\.Trainer\(\)。优势是不用自己写 trainer 了，它已经将常用的 trainer 功能写好。劣势是默认 trainer 的训练，其 memory 优化有限，单机跑不见得比纯 pytorch 快。

### 创建 LightningModule

新建一个模型，将原有功能包进来即可。注意：需要将模型参数暴露在 init 函数中。

```Python
class LitGPT(pl.LightningModule):
    """ Use Pytorch Lightning wrapping to enable distributed parallel. """

    def __init__(self, vocab_size, n_embd, block_size, n_layer=8, n_head=8,
                 attn_pdrop=0.1, resid_pdrop=0.1, embd_pdrop=0.1,
                 learning_rate=3e-4, weight_decay=0.1, betas=(0.9, 0.95),  # used to config optimizer
                 warmup_tokens=375e6, final_tokens=260e9):
        super().__init__()
        self.save_hyperparameters()
        self.model = GPT(vocab_size, n_embd, block_size, n_layer=n_layer, n_head=n_head,
                         attn_pdrop=attn_pdrop, resid_pdrop=resid_pdrop, embd_pdrop=embd_pdrop)

    def forward(self, batch_x, targets=None):
        # Forward function that is run when visualizing the graph
        return self.model(batch_x, targets)

    def configure_optimizers(self):
        optimizer = self.model.configure_optimizers(learning_rate=self.hparams.learning_rate,
                                                    weight_decay=self.hparams.weight_decay,
                                                    betas=self.hparams.betas)

        t_mult = self.hparams.final_tokens - self.hparams.warmup_tokens
        scheduler = CosineAnnealingWarmRestarts(optimizer, int(self.hparams.warmup_tokens), T_mult=int(t_mult))

        return [optimizer], [scheduler]

    def _calculate_loss(self, batch, mode="train"):
        inp_x, labels = batch
        logits, loss = self.forward(inp_x, labels)
        acc = (logits.argmax(dim=-1) == labels).float().mean()

        self.log(f"{mode}_loss", loss)
        self.log(f"{mode}_acc", acc)

        return loss

    def training_step(self, batch, batch_idx):
        loss = self._calculate_loss(batch, mode="train")
        return loss

    @torch.no_grad()
    def validation_step(self, batch, batch_idx):
        _ = self._calculate_loss(batch, mode="val")

    @torch.no_grad()
    def test_step(self, batch, batch_idx):
        _ = self._calculate_loss(batch, mode="test")
```

### 调用 pl\.Trainer\(\)

新建 trainer 函数，调用 pl\.Trainer\(\) 即可。注意：pl\.Trainer\(\) 的参数是核心参数。需要仔细调整。

```Python
def train(training_set: List[str], validation_set: List[str], output_dir,
          max_len=100, batch_size=64, n_layer=8, n_head=8, n_embd=512, attn_pdrop=0.1, resid_pdrop=0.1, embd_pdrop=0.1,
          n_epochs=10, lr=1e-3, weight_decay=0.1, betas=(0.9, 0.95), grad_clip_val=1.0, warmup_tokens=375e6,
          final_tokens=260e9, device='cuda', n_nodes=1, n_gpus=-1, ckpt_path=None, tf_train=True):

    prot_dm = ProtDataModule(training_set, validation_set, batch_size, max_len, num_workers=100)
    logger.info(f"Train dataloader length {len(prot_dm.train_dataloader().dataset)}, test dataloader length {len(prot_dm.val_dataloader().dataset)}")

    # Init trainer
    trainer = pl.Trainer(strategy=DDPStrategy(find_unused_parameters=False),
                         default_root_dir=output_dir,
                         callbacks=[ModelCheckpoint(save_weights_only=True, mode="max", monitor="train_acc"),
                                    TQDMProgressBar(refresh_rate=1), LearningRateMonitor("epoch")],  # to update
                         num_nodes=n_nodes, gpus=n_gpus if str(device).startswith("cuda") else 0, auto_select_gpus=True,
                         max_epochs=n_epochs, gradient_clip_val=grad_clip_val, log_every_n_steps=10)
    trainer.logger._default_hp_metric = None  # Optional logging argument that we don't need

    # Train model if no pretrained model exist
    if ckpt_path:
        print("Found pretrained model, loading...")
        model = LitGPT.load_from_checkpoint(ckpt_path)
    else:
        sd = AASeqDictionary()
        vocab_size = sd.get_char_num()
        block_size = max_len + 2  # add start & end

        model = LitGPT(vocab_size, n_embd, block_size, n_layer=n_layer, n_head=n_head,
                       attn_pdrop=attn_pdrop, resid_pdrop=resid_pdrop, embd_pdrop=embd_pdrop,
                       learning_rate=lr, weight_decay=weight_decay, betas=betas,
                       warmup_tokens=warmup_tokens, final_tokens=final_tokens)
    if tf_train:
        logger.info("check if model is training...")
        trainer.fit(model, prot_dm.train_dataloader())

    test_result = trainer.test(model, prot_dm.test_dataloader(), verbose=False)
    print(f"Test accuracy:  {(100.0 * test_result[0]['test_acc']):4.2f}%")

    return model.to(device)
```

### 创建 LightningDataModule

这是可选项目，可以用 LightningDataModule 来直接设定 train, test, 和 validation 的 dataloader。

```Python
class ProtDataModule(pl.LightningDataModule):
    def __init__(self, training_set: List[str], validation_set: List[str], batch_size=64, max_len=100, num_workers=100):
        super().__init__()
        self.batch_size = batch_size
        self.max_len = max_len
        self.num_workers = num_workers
        # load data
        train_seqs, _ = load_seqs_from_list(training_set, max_len=max_len, rm_duplicates=False)
        valid_seqs, _ = load_seqs_from_list(validation_set, max_len=max_len, rm_duplicates=False)
        logger.info(len(train_seqs))
        logger.info(f"Total GPU memory: {torch.cuda.get_device_properties(0).total_memory // 1024 ** 3} G")

        self.train_set = get_tensor_dataset(train_seqs)
        self.test_set = get_tensor_dataset(valid_seqs)
        logger.info(f"Train set length {len(self.train_set)}, test set length {len(self.test_set)}")

    def train_dataloader(self):
        return data.DataLoader(self.train_set, batch_size=self.batch_size, shuffle=True, drop_last=True, pin_memory=False,
                               num_workers=self.num_workers)

    def val_dataloader(self):
        return data.DataLoader(self.test_set, batch_size=self.batch_size, num_workers=self.num_workers, pin_memory=False)

    def test_dataloader(self):
        return data.DataLoader(self.test_set, batch_size=self.batch_size, num_workers=self.num_workers, pin_memory=False)
```

## 其他

### 模型在 CPU 和 GPU 之间训练和加载

我们在使用pytorch的过程，经常会需要加载模型参数，不管是别人提供给我们的模型参数，还是我们自己训练的模型参数，那么加载模型参数就会碰到一些情况，即GPU模型和CPU模型，这两种模型是不能混为一谈的，下面分情况进行操作说明。

#### 情况一：模型是GPU模型，预加载的训练参数也是GPU；模型是CPU模型，预加载的训练参数也是CPU

这种情况下我们都只用直接用下面的语句即可：

```Python
torch.load('model_dict.pkl')
```

#### 情况二：GPU\-\>CPU 模型是 CPU，预加载的训练参数却是 GPU

```Python
torch.load('model_dict.pkl', map_location=lambda storage, loc: storage)
```

#### 情况三：CPU\-\>GPU 模型是 GPU，预加载的训练参数却是 CPU

```Python
torch.load('model_dic.pkl', map_location=lambda storage, loc: storage.cuda)

#CPU->GPU1   模型是GPU1，预加载的训练参数却是CPU：
torch.load('model_dic.pkl', map_location=lambda storage, loc: storage.cuda(1))
```

### 降低显存使用的方法

1. 减小 batch\_size

2. 缩小模型大小

3. 使用 自动混合精度： [https://zhuanlan\.zhihu\.com/p/165152789](https://zhuanlan.zhihu.com/p/165152789)

### 使用 tqdm 展示 batch 中的 loss

tqdm 核心是一个进度条。用它可以方便的显示当前训练的进度，并显示一些参数。

见：[https://blog\.csdn\.net/qq\_33472765/article/details/82940843](https://blog.csdn.net/qq_33472765/article/details/82940843)

```Python
from tqdm import tqdm

# Set tqdm
pbar = tqdm(enumerate(loader), total=len(loader)) if is_train else enumerate(loader)            

# Report progress
for epoch in range(n_epochs):
  for it, (x, y) in pbar:
    ...
    pbar.set_description(f"epoch {epoch + 1} iter {it}: train loss {loss.item():.5f}. lr {lr:e}")
  
# Result
# epoch 1 iter 11252: train loss 0.30460. lr 8.118256e-04:  57%|xxxx     | 11251/19893 
```

### 使用 tensorboard 查看模型训练情况

见：[https://zhuanlan\.zhihu\.com/p/103630393](https://zhuanlan.zhihu.com/p/103630393)

```Python
from torch.utils.tensorboard import SummaryWriter

# Set writer, usually in trainer
writer = SummaryWriter(self.config.output_dir + 'logs')          

# Report progress
for epoch in range(n_epochs):
  writer.add_scalar('loss', loss, epoch + 1)
  
# View results
tensorboard --logdir=./path/to/the/folder --port 8123 # 默认 30s 刷新一次
```

### 快速关闭使用 GPU 的进程

```PowerShell
lsof /dev/nvidia1 | awk '{print $2}' | xargs -I {} kill -KILL {}
# show process using GPU card | show PID | kill process
# only need to kill the ones using the nvidia1
```

## Loss 异常

### Loss 中出现负数

#### 场景一: label 特殊处理导致 loss 为负数

正常情况下 loss 都是大于 0 得正数，但是在某些代码修改中，可能会意外出现 loss 为负数的情况。

典型的是在一些 graph 分类算法中，他们会对 label 做一些特殊处理，输入中 将0， 1 转换为 \-1，\+1，计算 loss 前又做 \(y\+1\)/2 得运算。理论上，这个技巧可以放大目标信号，提升图算法对输入值的敏感性，有助于学习过程。实用的取巧技术，但不值得鼓吹。

#### 场景二: loss 公式与任务数据不符合,导致 loss 为负数

例如, 在对比学习中, 错误使用了 triplet loss,而非 InfoNCE loss\.导致用同 batch 样本作为负例,对应样本做正例的情况下,出现loss 为特别大的负数\.这种情况,主要也是 label 和 loss 不匹配导致。

### Loss 中出现 nan

#### 场景一: 对比学习中，loss 为nan

1. \*\*没有在 loss\.backward\(\)中增加 retrain\_graph=True。\*\*对比学习中，需要将两组样本分别在同一模型上做一次 back propagation。但如果未加注意，没有在 loss\.backward\(\)中增加 retrain\_graph=True，会导致模型 loss 不收敛，在计算过程中崩溃。但增加 retrain\_graph=True，会显著增大内存消耗，尤其是在 CNN中，可能会需要将 batch\_size 缩小到原来的 1/4，这是一个不小的成本。

2. 对比loss 权重过高。通常对比学习中，会有多个对比 loss，如果对比 loss 的权重过高，会导致 loss 出现 nan。这时候可以考虑随着模型的训练 epoch增大，逐步增加 loss 的权重。但需要注意：单个 epoch 内模型收敛可以比较，跨 epoch 比较意义就不大了。

#### 场景二: 多模态学习中，loss 为nan

多模态对比学习中，会常出现 loss 为 nan 的情况。尤其是模态差异很大的时候，更容易出现 nan。

解决的方法有：

1. 不要冻结单模态的 encoder 模型，而是支持其训练。但这会增加模型训练的成本。

2. 增加各单模态中对齐层的层数，让模型有更多可调整的参数来收敛。

3. 调整loss 函数，让想办法 loss 函数更加平滑。

4. 减小任务的 learning rate，增加 warmup，可以增加 loss 收敛的可能性。

5. 增加 loss 异常检测的模块，将异常 loss 提前删除。但这种技巧实战中不是很常用，loss 异常时候，删除再多的样本，最后 loss 还会是 nan。

## Milvus 向量数据库使用

安装可以参考：[https://milvus\.io/docs/install\_standalone\-docker\.md](https://milvus.io/docs/install_standalone-docker.md)

```PowerShell
# Start
sudo docker compose ps

# Connect to Milvus
docker port milvus-standalone 19530/tcp

# Stop Milvus
sudo docker compose down

# Delete data after stop Milvus
sudo rm -rf  volumes
```

#### collection 操作

```PowerShell
from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection

# Connect to Milvus server
connections.connect("default", host="localhost", port="19530")

# Creates a collection
fields = [
    FieldSchema(name="read_id", dtype=DataType.VARCHAR, max_length=40, is_primary=True, auto_id=False),
    FieldSchema(name="gene_id", dtype=DataType.VARCHAR, max_length=40, auto_id=False),
    FieldSchema(name="gene_name", dtype=DataType.VARCHAR, max_length=40, auto_id=False),
    FieldSchema(name="gene_type", dtype=DataType.VARCHAR, max_length=40, auto_id=False),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=512, description="vector"),
]
schema = CollectionSchema(fields, "Signal annotation library")
collection = Collection("signal_annotation_library", schema)

# connect to collection
collection = Collection("signal_annotation_library")

# drop a collection
utility.drop_collection("signal_annotation_library")
```

#### entity 操作

```PowerShell
# write to a collection
entities = [read_ids, gene_ids, gene_names, gene_types, sig_embds]

collection.insert(entities)
collection.flush()

# Deletes entities by their primary keys
expr = f"pk in [{entities[0][0]}, {entities[0][1]}]"
collection.delete(expr)
```

#### index操作

```PowerShell
from pymilvus import Collection

# Builds indexes on the entities
index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 512},
}
collection.create_index("embedding", index)

# Drop collection index
collection = Collection("signal_annotation_library")
collection.release()  # Release the collection.
collection.drop_index()
```

#### search和 query 操作

```PowerShell
# Load the collection to memory
collection.load()

# Perform a vector similarity search
vectors_to_search = entities[-1][-2:]
search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}

result = collection.search(vectors_to_search, "embeddings", search_params, limit=3, output_fields=["random"])
```
