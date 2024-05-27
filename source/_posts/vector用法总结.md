---
title: vector用法总结
date: 2023-02-01 15:34:29
tags: C++
categories : 编程语言
---
## vector相关的用法总结
因为最近经常用，于是总结在这个地方。

向量（Vector）是一个封装了动态大小数组的顺序容器（Sequence Container）。跟任意其它类型容器一样，它能够存放各种类型的对象。可以简单的认为，向量是一个能够存放任意类型的动态数组。

## 特性
1.顺序序列
顺序容器中的元素按照严格的线性顺序排序。可以通过元素在序列中的位置访问对应的元素。

2.动态数组
支持对序列中的任意元素进行快速直接访问，甚至可以通过指针算述进行该操作。提供了在序列末尾相对快速地添加/删除元素的操作。

3.能够感知内存分配器的（Allocator-aware）
容器使用一个内存分配器对象来动态地处理它的存储需求。

---

## 注意点
使用vector需要注意以下几点：

1.如果你要表示的向量长度较长（需要为向量内部保存很多数），容易导致内存泄漏，而且效率会很低；

2.Vector作为函数的参数或者返回值时，需要注意它的写法：
```cpp
double Distance(vector<int>&a, vector<int>&b); //其中的“&”不能少
```

3.vector的元素不仅仅可以是int,double,string,还，可以是结构体，但是要注意：结构体要定义为全局的.

## 常见使用
使用：
```cpp
#include<vector>

vector<int> vec;///建立一个vector，int为数组元素的数据类型，vec为动态数组名
vector<vector<long int> > vec2; //定义一个二维数组vec2
vec.push_back(1);
vec.push_back(2);//把1和2压入vector，这样vec[0]就是1,vec[1]就是2
cout<<vec[0]<<endl;//使用下标访问元素

//使用迭代器访问元素.
vector<int>::iterator it;
for(it=vec.begin();it!=vec.end();it++)
    cout<<*it<<endl;

vec.insert(vec.begin()+i,a);//插入,在第i+1个元素前面插入a
vec.erase(vec.begin()+2);//删除元素,删除第3个元素
vec.erase(vec.begin()+i,vec.end()+j);//删除区间[i,j-1];区间从0开始
vec.size();//向量大小
vec.clear();//清空
```
一些算法
```cpp
#include<algorithm>

reverse(vec.begin(),vec.end());//将元素翻转，即逆序排列
sort(vec.begin(),vec.end());//默认升序排列

//降序排列需重写
bool Comp(const int &a,const int &b){
    return a>b;
}
sort(vec.begin(),vec.end(),Comp)//降序排序

//交换两个同类型向量的数据
vector<int>vec2;
swap(vec,vec2);
```
先这样，之后用到了再加叭qaq :blush:~