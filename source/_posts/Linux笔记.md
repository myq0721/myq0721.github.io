---
title: Linux入门学习笔记
date: 2022-12-15 19:02:25
categories: 操作系统与软件
img: https://i.postimg.cc/MZgFsVkF/image.png
---

### 常用指令[命令](https://www.runoob.com/linux/linux-command-manual.html)

## 杂记

- su 登录root用户 exit 退出
- sudo /etc/init.d/ssh start 启动ssh服务

> - ifconfig 未找到命令</br>
yum install ifconfig发现输出了如下错误信息：没有可用软件包 ifconfig。</br>
通过命令：yum search ifconfig，来搜索可用或者匹配的安装包程序。</br>
搜索结果匹配ifconfig的安装包是net-tools.x86_64</br>
我们安装ifconfig输入：yum install net-tools</br>

## 二、实操篇

### 1.远程登录Linux系统

- Xshell5 远程登录linux，完美解决中文乱码问题、但是只能发指令

- XFep5 上传和下载文件，需要linux开启sshd服务22

- Xshell连接成功~
```c
Connecting to 192.168.232.3:22...
Connection established.
To escape to local shell, press 'Ctrl+Alt+]'.

Last login: Wed Mar  8 19:44:55 2023
[ayanami@master ~]$
```


MySQL安装文件



</br>

---
## 一、基础篇

### 1.Linux学习方向

- linux运维工程师

- linux嵌入式工程师

- linux下开发项目{ JavaEE，大数据，Python，PHP，c/c++}

### 2.Linux的应用领域

- 个人桌面领域应用、相对薄弱
- 服务器领域、Linux主要用途
- 嵌入式领域、可以根据需要进行软件裁剪

### 3.学习路线

- 基本操作命令，包括文件操作命令、编辑工具使用、linux用户管理等

- linux的各种配置：环境变量配置、网络配置、服务配置等

- linux下搭建对应语言的开发环境：大数据、JavaEE、Python等

- 能编写shell脚本，对Linux服务器进行维护

- 能进行安全设置，防止攻击，保障服务器正常运行，能对系统调优

- 深入理解Linux系统，对内核有研究，数据掌握大型网站应用架构组成、并熟悉各个环节的部署和维护方法

>先学整体到框架再到细节。
>一定要实操！

### 4.Linux基础介绍

- linux 免费、开源、安全、高效、稳定、处理高并发非常强

- 主要发行版：CentOSE、Redhat、Ubuntu、Suse、

### 5.Linux和Unix的关系

- Linux 和 Unix 之间的其他差异主要与许可模式有关:开源与专有许可软件。

- 由内而外分别是：Hardware、Linux Kernal、GNU Shell、FTP DBMS 等，称为GNU计划

### 6.Linux与Windows的比较

- Linux比Windows更安全

- Linux更多的是命令行操作

- Linux因为开源，所以可定制

### 7.VM和Linux(CentOS)和vmtools安装

- 确保BIOS中虚拟化设备支持启用
- 省略

### 8.文件系统目录

- linux只有一个根目录，下有多个子目录，bin，homo，root等，但根目录只有一个

- *在linux的世界里，一切皆文件*

{
- bin 存放二进制可执行文件(ls,cat,mkdir等)

- boot 存放用于系统引导时使用的各种文件

- dev 用于存放设备文件

- etc 存放系统配置文件

- home 存放所有用户文件的根目录

- lib 存放跟文件系统中的程序运行所需要的共享库及内核模块

- mnt 系统管理员安装临时文件系统的安装点

- opt 额外安装的可选应用程序包所放置的位置

- proc 虚拟文件系统，存放当前内存的映射

- root 超级用户目录

- sbin 存放二进制可执行文件，只有root才能访问

- tmp 用于存放各种临时文件

- usr 用于存放系统应用程序，比较重要的目录/usr/local 本地管理员软件安装目录

- var 用于存放运行时需要改变数据的文件

}



