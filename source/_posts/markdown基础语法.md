---
title: markdown基础语法
date: 2023-01-20 21:58:15
categories: 其他
tags: 杂谈
---

## 什么是Markdown?

   Markdown就是一种文档的格式，文件名的末尾是.md，正如我们常用的word文档格式是.doc、.docx，需要对应的软件来打开这一种格式。

## 为什么要用Markdown？

作为一种新的文档格式，我们放着这么好的word文档不用却用Markdown是有一些原因的：

有人发现当他们用Word或者别的文本编辑器写好一篇文章，兴高采烈地发布到博客、论坛、网站上时，发现格式完全乱了，于是需要花费大量的时间来重新排版，处理图片、缩进、字体、加粗、标题等。三番五次之后，开始发现文章写作可能只花了半小时，重新排版就花了十多分钟。更让人不悦的是，当我们要把同一篇文章发布到另一个网页上时，这样的排版还要重新做一次。

并且习惯了非可视化界面后，使用鼠标操作意味着终断打字，是一个显著降低输入速度的行为。一般来说文章的编写必然需要设置一定的格式：标题、加粗、行距、缩进、字体……这些一般都需要用鼠标在可视化界面上选择。


## 1.删除线：

用法：`~~要划删除线的文字~~`

例如：`~~HelloWorld~~`

显示：~~HelloWorld~~

## 2.下划线：

用法：`<u>要添加下划线的文字</u>`

例如：`<u>HelloWorld</u>`

显示：<u>HelloWorld</u>

## 3.分割线：

用法：`---`  *//需要单独的一行！*

例如：`---`

显示：

---

## 4.标题：

用法：`# 标题内容` // 需要单独一行

*如果需要标题下面的小标题可以多加一个“#”符号*

例如：`# 显示效果`

显示：

# 显示效果

## 5.加粗：

用法：`**加粗内容**`

例如：`**HelloWorld**`

显示：**HelloWorld**

## 6.斜体：

用法：`*斜体内容*`

例如：`*HelloWorld*`

显示：*HelloWorld*

## 7.既斜体又加粗：

用法：`***斜体又加粗内容***`

例如：`***HelloWorld***`

显示：***HelloWorld***

## 8.无序列表：

用法：`- 内容` // 需要单独一行

例如：

`- HelloWorld`

`- HelloMarkdown`

显示：

- HelloWorld

- HelloMarkdown

## 9.有序列表：

用法：

`1. 内容`

`2. 内容`

`3. 内容`

// 可以不按数字顺序，但必须从1开始

例如：

`1. HelloWorld`

`2. HelloMarkdown`

`3. Markdown yes`

显示：

1. HelloWorld

2. HelloMarkdown

3. Markdown yes

## 10.引用内容：

## 单行：

用法：`> 引用内容` //  需要单独一行

例如：`> HelloWorld by Markdown`

显示：

> HelloWorld by Markdown

## 空行：

用法：

`> 第一行`

`>`

`> 第二行`

例如：

`> HelloWorld by Markdown 1`

`>`

`> HelloWorld by Markdown 2`

显示：

> HelloWorld by Markdown 1
> 
> HelloWorld by Markdown 2

## 嵌套：

用法：

`> 第一行`

`> 第二行`

`> > 第二行引用的（需要嵌套的）`

例如：

`> HelloWorld by Markdown 1`

`> HelloWorld by Markdown 2`

`> > HelloWorld by Markdown 3`

显示：

> HelloWorld by Markdown 1
> 
> HelloWorld by Markdown 2
> 
> > HelloWorld by Markdown 3

## 带有其他语法的引用：

`> ### HelloWorld`

`>`

`> - HelloWorld`

`> - HelloMarkdown`

`> - Markdown yes`

`>`

`> *Hello* **World**`

显示：

> ### HelloWorld
> 
> - HelloMarkdown
> - Markdown  yes
> 
> *Hello* **World**

## 11.代码块：

用法：三个```符号（要封口） （可以缩减成一个）

例如：```HelloWorld （要封口）

显示：```HelloWorld```

## 12.转义字符：

可以把本来要用来Markdown语法的字符转成正常字符

用法：`\`

例如：`\*HelloWorld\*`

显示：\*HelloWorld\*

## 13.使用HTML标签：

用法：直接写HTML标签

例如：`<u>HelloWorld</u>`

显示：<u>HelloWorld</u>

*（之前的下划线就是用的HTML标签，而不是Markdown语法）*

## 14.表格：

## 正常

用法：
```
| 标题1   | 标题2 |
| -------|------ |
| 内容1   | 内容3 |
| 内容2   | 内容4 |
```

（“|”是分割，"---"是竖着的分割线加粗）

例如：

```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

显示：

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

## 自动对齐

用法：

```
| 标题1      | 标题2 | 标题3     |
| :---:        |    :----:   |          :---: |
| 内容1      | 内容3     | 内容5   |
| 内容2   | 内容4        |内容6      |
```

| 标题1 | 标题2 | 标题3 |
|:---:|:---:|:---:|
| 内容1 | 内容3 | 内容5 |
| 内容2 | 内容4 | 内容6 |

## 15.任务完成表

用法：

`- [x] 打钩的内容`

`- [] 不打钩的内容`

例如：

`- [x] Markdown yes`

`- [] Word Yes`

显示

- [x] Markdown yes

- [ ] Word Yes

更多请看https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/markdown-basics
以及https://markdown.com.cn/basic-syntax/images.html