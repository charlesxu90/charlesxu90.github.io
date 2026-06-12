---
title: "Tensorflow 常用命令"
subtitle: ""
date: 2021-06-13
draft: false
author: "Xiaopeng Xu"
description: "TensorFlow 常用命令与张量操作速查笔记。"
tags: ["TensorFlow", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## Tensor 操作

### 元素逐个乘积

```Python
tf.multiply(x, x)
```

### 各元素值求和

```Python
tf.reduce_sum(x)
```

### 

## Keras 操作

### 新建模型

#### 使用 Sequential

```Python
model = tf.keras.Sequential([
        tf.keras.layers.ZeroPadding2D(padding=3, input_shape=(64, 64, 3)),
        tf.keras.layers.Conv2D(32, 7),
        tf.keras.layers.BatchNormalization(axis=3),
        tf.keras.layers.ReLU(),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])       
```

#### 使用 API

```Python
def convolutional_model(input_shape):

    input_img = tf.keras.Input(shape=input_shape)
    Z1 = tf.keras.layers.Conv2D(8, 4, strides=1, padding='same')(input_img)
    A1 = tf.keras.layers.ReLU()(Z1)
    P1 = tf.keras.layers.MaxPool2D(pool_size=(8, 8), strides=8, padding='same')(A1)
    Z2 = tf.keras.layers.Conv2D(16, 2, strides=1, padding='same')(P1)
    A2 = tf.keras.layers.ReLU()(Z2)
    P2 = tf.keras.layers.MaxPool2D(pool_size=(4, 4), strides=4, padding='same')(A2)
    F = tf.keras.layers.Flatten()(P2)
    outputs = tf.keras.layers.Dense(6, activation='softmax')(F)
    model = tf.keras.Model(inputs=input_img, outputs=outputs)
    
    return model     
```

### 通用模型

#### Dense

```Python
outputs = tf.keras.layers.Dense(6, activation='softmax')(F)
```

#### ReLU

```Python
A1 = tf.keras.layers.ReLU()(Z1)
```

#### Flatten

```Python
F = tf.keras.layers.Flatten()(P2)
```

#### Dropout

```Python
F = tf.keras.layers.Dropout(.2, input_shape=(2,))(P2)
```

### Image 模型

#### CONV2D

```Python
Z1 = tf.keras.layers.Conv2D(8, 4, strides=1, padding='same')(input_img)
```

#### MaxPool2D

```Python
P1 = tf.keras.layers.MaxPool2D(pool_size=(8, 8), strides=8, padding='same')(A1)
```

#### Conv2DTranspose

```Python
P1 = tf.keras.layers.MaxPool2D(pool_size=(8, 8), strides=8, padding='same')(A1)
```
