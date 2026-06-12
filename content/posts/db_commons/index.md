---
title: "数据库常用命令"
subtitle: ""
date: 2026-05-12
draft: false
author: "Xiaopeng Xu"
description: "数据库常用命令速查：查询、表操作与管理。"
tags: ["Database", "SQL", "Cheatsheet"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

## MySQL 使用

### 安装 MySQL

```PowerShell
sudo apt install mysql-server  # install
sudo systemctl start mysql.service  # start
```

### 修改 root 密码

```PowerShell
sudo mysql # start mysql with root user
```

Change root password in mysql, set root password as: Xp@KAUST2023

```SQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Xp@KAUST2023';
exit;
```

Go back to using the default authentication method

```SQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
```

Run the security script using sudo

```PowerShell
sudo mysql_secure_installation
```

### 登录 mysql 服务器

Login with sql root user

```PowerShell
mysql -u root -p
```

### 创建用户

```SQL
CREATE USER 'charlesxu90'@'localhost' IDENTIFIED BY 'Xxp1990320';

/* grant access */
GRANT PRIVILEGE ON database.table TO 'charlesxu90'@'localhost'; 
GRANT ALL PRIVILEGES ON *.* TO 'charlesxu90'@'localhost' WITH GRANT OPTION;
```

### 导入 MySQL dump文件到数据库

创建数据库

```SQL
8 DEFAULT COLLATE utf8_general_ci;
```

导入数据库

```PowerShell
mysql -uroot -pXp@KAUST2023 chembl_32 < chembl_32_mysql.dmp
```

## PostgreSQL 使用

### 安装 PostgreSQL

```PowerShell
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql.service
```

### 使用 PostgreSQL

#### 登录 PostgreSQL

```PowerShell
sudo -i -u postgres # 安装时候会创建 postgre 帐号，可以用此直接访问数据库
psql # psql 后，可以进入数据库命令行

# 或者
sudo -u postgres psql
```

#### 退出 PostgreSQL 命令行

```SQL
\q
```

#### DB 操作

```SQL
/*: list all databases*/
\list
\l 
\c <db name> /* connect to a certain database */
\dt  /* list tables in the current db using your search_path */
\dt *. /*list tables in the current db regardless your search_path */
```

#### Table 操作

```SQL
\dt /* list all tables */
\dt schema_name.* /* list all table under schema */

/* create table */
CREATE TABLE leads2 (id INTEGER PRIMARY KEY, name VARCHAR); CREATE TABLE

/* query table */
SELECT * FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
schemaname != 'information_schema';

/* drop table */
DROP TABLE tblname;
DROP TABLE table1, table2, ...;
```

#### 从 SQL 文件中导入 DB

```SQL
psql splice_vault <misspl_events_ -v ON_ERROR_STOP=1
```

#### 导出 table 到 csv 文件

```SQL
/* Format */
\copy (SELECT ...) TO '/some/local/file' WITH (FORMAT CSV, HEADER)

/* example */
\copy (select * from misspl_app.misspl_events_300k_hg38_events) to '/tmp/misspl_app.misspl_events_300k_hg38_events.csv' with (FORMAT CSV, HEADER);
```

## DuckDB 使用

DuckDB 是一个高效便捷的 SQL 数据库可以用来直接查询 csv 文件\.非常方便\.而且支持 Java, Python 和 R语言\.

#### 安装 DuckDB

```PowerShell
wget [https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip](https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip)

unzip duckdb_cli-linux-amd64.zip
```

#### 创建数据库

```PowerShell
./duckdb learn2thermo.db # learn2thermo.db is the filename of the new database
```

#### 导入 csv 数据

```SQL
CREATE TABLE protein_pairs as SELECT * FROM 'csvs/protein_pairs.csv';
CREATE TABLE proteins as SELECT * FROM 'csvs/proteins.csv';
CREATE TABLE taxa_pairs as SELECT * FROM 'csvs/taxa_pairs.csv';
CREATE TABLE taxa as SELECT * FROM 'csvs/taxa.csv';
```

#### Summarize 表格

```SQL
SUMMARIZE proteins;
```

## Redis内存数据库

Redis 是一个内存数据库．当有很多文件的读写操作时候，直接读取文件会非常慢．自己写个 dict 读取速度不够快．最好的办法，就是调用 Redis 数据库来加速这个读写过程．

### 安装Redis内存数据库

```PowerShell
# whole system
sudo apt install redis-server redis-tools
# install redis-py
pip install redis
```

### 启动Redis服务

```PowerShell
sudo service redis-server start
```

### Redis命令行读写

```PowerShell
# Write
redis-cli set key1 "value1"
# OK

# Read
redis-cli get key1
# "value1"

# Delete
redis-cli del key1
```

### Redis Python读写 

```PowerShell
import redis
import numpy as np

r = redis.Redis()  # Connect to the default Redis instance

# Example usage
sequence = "your_sequence"
embedding = generate_embedding(sequence)

# Cache the embedding in Redis
r.set(sequence, np.array_repr(embedding))

# Retrieve the cached embedding
cached_embedding_str = r.get(sequence)

# Convert the string back to a NumPy array
cached_embedding = np.fromstring(cached_embedding_str[1:-1], dtype=float, sep=',')
```
