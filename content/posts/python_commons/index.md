---
title: "Python 常用命令"
subtitle: ""
date: 2026-05-17
draft: false
author: "Xiaopeng Xu"
description: "Python 常用命令与技巧速查。"
tags: ["Python", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Pandas 列过滤

### 用某列对 dataframe 做过滤

```Python
papers_dates[(papers_dates.preprint_test == True) & ~ papers_dates.acptDate.isna()]
# 两列做 or 运算
df_all_norm[(df_all_norm["CO2"] > 0.8) | (df_all_norm["CO"] > 0.8)]
```

### 用日期列对 dataframe 做过滤

```Python
papers_age[papers_age.pubDate >= "2028-03-01"]
```

### 用日期间隔列对 dataframe 做过滤

```Python
papers_dates[papers_dates.preprint_age > pd.Timedelta(30,'D')]
```

### 去除空列

```Python
df.dropna(subset=['name', 'toy'])
```

## Pandas Dataframe 合并

### 同长 dataframe 合并

```Python
pd.concat([papers, CSCoV_scores], axis=1)
```

### 两个 dataframe 做 left outer join

```Python
papers_redup.merge(all_rxiv_redup[['subDate', 'title']], left_on='title', right_on='title',how='left')
```

## Pandas 数据替换

### 值替换

```Python
df.replace([0, 1, 2, 3], [4, 3, 2, 1])
```

## Pandas 数据查看/分析

### 展示长 string

```Python
pd.set_option('display.max_colwidth', None)
```

### 查看 string 是否在某个 string list 中

```Python
X_lxd[X_lxd.title.isin(selected)][['title', 'pub_prob']]
```

### 查看日期列数据分布

```Python
papers_dates[['subDate', 'acptDate', 'pubDate']].describe(datetime_is_numeric=True)
```

### 按某列倒序排列

```Python
X_lxd.sort_values(by='pub_prob', ascending=False)
```

## Numpy 向量计算

### 标量和向量的加减乘除

```Python
x = np.random.rand(3,1)
1 + x # element-wise operation
1 - x
1 * x
1 / x
```

### 初始化向量或者矩阵 np\.zeros, np\.ones

```Python
x = np.zeros((10, 1))
x = np.ones((10, 1))
```

### Mean, std，max，min，median

```Python
x = np.random.rand(3,1)
x.mean()
x.std()
x.max()
x.min()
np.median(x)
```

### 两个向量各对应元素求最大值

```Python
x = np.random.rand(3,1)
y = np.random.rand(3,1)
np.maximum(x, y) # also np.maximum(x, 0) broadcast by default
# Out: array([[0.88240057], [0.38776741], [0.72610557]])
```

### 向量和向量的运算 \*, /, dot

```Python
x = np.random.rand(3,1)
y = np.random.rand(3,1)
x * y # element-wise multiplication, return vector (3,1), or np.multiply()
np.transpose(x).dot(y) # return scalar
x / y # element-wise division, return vector (3,1)
```

### 向量绝对值 absolute

```Python
np.absolute(np.random.rand(3, 2，2)-10)
```

## Numpy 矩阵计算

### 矩阵重新设置大小 reshape

```Python
x = np.random.rand(3, 2，2)
x.shape   # (3, 2，2)
x.reshape(-1, 1) # a column vector, 1 f

# reshape a np.array of images
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
```

## scipy 相关命令

#### **truncnorm 分布区间矫准**

将标准正态分布校准到区间 \[a, b\] 上

```Python
truncnorm.rvs(a, b, size=1000)
```

## multiprocessing 程序并行

### Multiprocessing 函数并行

Python 设计中，只能多进程并行，而不能多线程并行。最简单的实现如下，只是并行 f\(x\) 函数。通过 map 函数向其中增加任务，通过 get 函数获得相应的结果。为了按顺序获得结果，需要按顺序执行 get 函数。

```Python
import multiprocessing

def f(x):
    return x*x

if __name__ == '__main__':
 
    pool = multiprocessing.Pool(processes=2)
    numList = [i for i in range(10)]
    sub_procs = []
 
    for num in numList:
        proc = pool.apply_async(f, (num,))
        sub_procs.append(proc)
    pool.close()
    pool.join()
 
    result = [proc.get() for proc in sub_procs]
    print(result)
```

## Matplotlib 绘图

### 多子图绘制

#### 使用subplot绘制子图

```Python
def plot_kmer_signals(k_mer):
    dup_list = df_read_kmers_not_nan_dup[df_read_kmers_not_nan_dup.kmer == k_mer].index.to_list()
    plt.figure(figsize=(20, 8))
    if len(dup_list) > 4: dup_list = dup_list[:4]
    sig_lens = []
    for i, idx in enumerate(dup_list):
        plt.subplot(len(dup_list), 1, i+1)
        plt.plot(signals[idx])
        plt.xlim(0, 3000)
        plt.ylim(0, 200)
        sig_lens.append(len(signals[idx]))
    plt.show()
    print(sig_lens)
```

#### 使用subplots绘制子图

```Python
def plot_step_curve(ax, prop, ylabel=None, yrefs=[]):
    ylabel = prop if ylabel is None else ylabel
    
    for yc in yrefs:
        ax.axhline(y=yc, ls=':', label=f"y={yc:4.2f}")
    df_r = reinvent_step_n[reinvent_step_n.Validity == True][['step', prop]].groupby('step').mean()
    df_s = sgpt_step_n[sgpt_step_n.Validity == True][['step', prop]].groupby('step').mean()
    
    ax.plot(df_r.index.values, df_r[prop].values, label="Reinvent")
    ax.plot(df_s.index.values, df_s[prop].values, label="SGPT-RL")
    ax.set_xlabel('Step')
    ax.set_ylabel(ylabel)
    ax.legend()
    
fig, axs = plt.subplots(2, 2, figsize=(16, 9))

plot_step_valid_curve(axs[0,0], 'Validity', ylabel='Validity')
axs[0,0].text(-0.1, 1.05, "a", transform=axs[0,0].transAxes, size=16, weight='bold')
plot_step_curve(axs[0,1], 'Activity', ylabel='DRD2 activity')
axs[0,1].text(-0.1, 1.05, "b", transform=axs[0,1].transAxes, size=16, weight='bold')
plot_step_ring_count_curve(axs[1,0], step_lim=1000)
axs[1,0].text(-0.07, 1.05, "c", transform=axs[1,0].transAxes, size=16, weight='bold')
plot_step_new_scaffold_curve(axs[1,1])
axs[1,1].text(-0.1, 1.05, "d", transform=axs[1,1].transAxes, size=16, weight='bold')

fig.savefig("figures/drd2_step.pdf", bbox_inches='tight')
fig.show()
```

### 长 x，y 标签时候，保存全图（含标签）

```Python
plt.savefig(save_path, dpi=300, bbox_inches='tight')
```

## EasyDict 便捷使用 Dict 对象

### 创建 Dict 对象

```Python
from easydict import EasyDict

my_dict = EasyDict()
my_dict.root_path = os.path.dirname(config_file)
```

### 调用 Dict 对象

```Python
my_dict.root_path  # like a property in the object
```
