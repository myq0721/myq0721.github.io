---
title: Unity客户端面试准备
date: 2026-05-28 12:00:00
categories: 秋招
tags:
  - Unity
---

## 简历

>重点掌握课程： 几何与线性代数 、C++程序设计、数字图像处理、算法与数据结构 、网络安全 等。
>所获荣誉：CUSGA决赛入围、网易雷火游戏开发大赛优秀奖、CMA 银奖、江苏省领航杯省奖、第四届金创翼大学生创新创业大赛三等奖、第九届互联网+校级、挑战杯校级、河海大学网络安全竞赛第三名，程序设计二等奖及第一届 GameJam 程序组评委。

### 2022.11-2023.09 南京微掣视觉有限公司 次元射击
1. 任引擎部部长并于河海大学开展过两次 Unity 游戏开发训练营，并于实习期间完成了 3D 塔防《次元射击》；
2. 《次元射击》通过 GameManager 管理游戏状态和流程，使游戏代码更加模块化，灵活和可扩展，方便添加
新的功能或修改现有的功能；
3. 通过 unity 内设置 Quality、使用 LOD、遮挡剔除等减少 Tris 数量以及批处理优化等方式，优化性能；
4. 与策划交流明确需求再开工、与美术通过 ProBuilder 合并网格等、动画机的 Conditions 与过渡时间使效果
自然、根据需求不断调整、优化逻辑；

### 2023.02-2023.06 CUSGA 第三届中国大学生游戏开发创作大赛 思觉失调(Dyskinesia)
1. 使用接口去统一管理场景中的可交互对象，将在 Player 脚本中的对象中的逻辑移至其他对象的逻辑中，提高
拓展性；
2. 使用异步接口进行 load，同步 load 会导致卡顿。通过异步加载场景，减少卡顿的时间；
3. 热更新模块使用 0 AssetBundle 实现资源的完全自主控制，使用 xLua 来实现整个游戏的逻辑部分。
4. Android 设置相对较低的 Quality 后打包选择 ASTC 压缩方式，输入方式采用 EasyTouch 插件

### 个人技能
1. 熟练使用 C++，C#，Lua 等编程语言；熟练使用 Unity 引擎进行游戏开发；
2. 熟悉 OpenGL 等图形 API，使用过 UE5、Godot 等引擎; 有着丰富的游戏开发实践经验，
3. 理解渲染管线，Unity Shader 等相关技术，对引擎架构有一定学习；
4. 了解各主流操作系统的跨平台差异，有相关的性能优化经验

### 自我评价
1. 热爱游戏开发，享受创造的快乐，看过 Games101,104 等课程，最喜欢的博主是 YouTube 的 Cherno 大佬。
2. 读过《游戏引擎架构》《STL 源码剖析》“虎书”等书籍；对游戏引擎的前沿技术感兴趣… 
3. 永劫无间双排修罗，赛博朋克 2077，rdr2，幽灵行者，Warframe，文明六，双人成行，雀魂麻将，柚子社 ciallo~ 课余爱好做菜和烘焙，喜欢淮扬菜系和巧克力类甜品，拍好看的照片，另外和朋友 @Paper 朱 运营了一个 Vup@溪冉 hira。 
4. 自学能力强、抗压能力强，工作认真负责，日常诙谐幽默，具有良好的团队合作意识。

- 附[溪冉hira来自河海大学的虚拟主播，还请多多指教⌯>ᴗ o⌯. 粉丝群号：916521635](https://space.bilibili.com/3546692106324064?spm_id_from=333.337.search-card.all.click)
---

- 附扫雷：
创建HTML结构
打开你的文本编辑器，创建一个新的HTML文件，并输入以下代码：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>myq721扫大雷</title>
    <style>
        /* 在这里添加CSS样式 */
    </style>
</head>
<body>
    <div class="bigBox">
        <div id="controls">
            <form>
                <label for="level">难度级别：</label>
                <select id="level">
                    <option value="easy">简单</option>
                    <option value="medium">中等</option>
                    <option value="hard">困难</option>
                </select>
                <button id="reset">重新开始</button>
            </form>
        </div>

        <table id="board"></table>
    </div>
    <script>
        // 在这里添加JavaScript代码
    </script>
</body>
</html>
```
这是我们游戏的基本结构。<head>部分包含了页面的元数据和样式定义，<body>部分则是游戏的主要内容。

添加CSS样式
在<style>标签内，我们将添加一些CSS样式来美化我们的扫雷游戏。这包括游戏布局、控制面板和表格样式。
```css
/* 游戏布局样式 */
.bigBox {
    background-color: rgb(163, 159, 159);
    width: 40%;
    margin: 5% auto;
    text-align: center;
    padding: 20px;
}

#reset {
    width: 100px;
    font-size: 15px;
}

table {
    border-collapse: collapse;
    margin: 30px auto;
}

td {
    width: 30px;
    height: 30px;
    text-align: center;
    vertical-align: middle;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    font-size: 16px;
    font-weight: bold;
    color: #fff;
    background-color: #333;
    border: none;
}
```
编写JavaScript逻辑
现在，我们将在<script>标签内添加JavaScript代码，这是游戏的核心部分。我们将创建游戏参数配置、初始化游戏、处理用户点击事件、检查游戏胜利条件等。
```js
// 游戏参数配置
const config = {
    easy: {
        rows: 8,
        cols: 8,
        mines: 10,
    },
    medium: {
        rows: 10,
        cols: 10,
        mines: 20,
    },
    hard: {
        rows: 12,
        cols: 12,
        mines: 30,
    },
};
// 初始化游戏
function init() {
    // ...（省略代码以节省空间，详见原代码）
}

// 用户点击格子的处理函数
function clickCell(row, col) {
    // ...（省略代码以节省空间，详见原代码）
}

// 更新地雷数目显示
function updateMinesCount() {
    // ...（省略代码以节省空间，详见原代码）
}

// 显示游戏结束
function showGameOver(win) {
    // ...（省略代码以节省空间，详见原代码）
}

// 检查游戏是否胜利
function checkWin() {
    // ...（省略代码以节省空间，详见原代码）
}

// 初始化游戏
init();
```
在这个脚本中，首先定义了游戏的难度级别配置，然后创建了初始化游戏的函数init。我们还定义了处理用户点击事件的函数clickCell，更新地雷数目的函数updateMinesCount，显示游戏结束的函数showGameOver，以及检查游戏胜利条件的函数checkWin。最后，我们调用init函数来初始化游戏。
测试游戏
保存HTML文件，并在浏览器中打开。

---

## 个人技能


### C++（misc，内存，对象，STL，新特性）

> https://www.nowcoder.com/issue/tutorial?tutorialId=93&uuid=b36a4e16637540b48edebbe29a405eb8

C++更加安全，增加了const常量、引用、四类cast转换（static_cast、dynamic_cast、const_cast、reinterpret_cast）、智能指针、try—catch等等；

### C#

>https://docs.unity.cn/cn/2021.3/Manual/JobSystem.html

编写多线程代码可以带来高性能优势，包括显著提高帧率。将 Burst 编译器与 C# 作业配合使用可以提高代码生成质量，还可以大大降低移动设备的电池消耗。

C# 作业系统的一个重要特点是它与 Unity 内部使用的系统（Unity 的原生作业系统）相集成。用户编写的代码与 Unity 共享工作线程。此协作避免了创建超过 CPU 核心数的线程（这种情况会导致争用 CPU 资源）。

### Lua与热更新

1. 什么是热更新？
热更新 是一种App软件开发者常用的更新方式。简单来说，就是在用户通过下载安装APP之后，打开App时遇到的即时更新。

在安卓、iOS平台，热更新表示在更新游戏资源或逻辑的时候不需要开发者将游戏再打包、上传、审核、发布、玩家重新下载安装包更新游戏，仅需要开发者打出新的ab（AssetBundle）资源文件放到网上，然后游戏程序下载新的ab资源文件替换本地的资源文件来实现游戏更新的流程。

热更代码可以理解成是特殊的资源。

Unity热更新详细文章可参考文章：[Unity 热更新技术 | （一） 热更新的基本概念原理及主流热更新方案介绍](https://cloud.tencent.com/developer/article/2239496?from_column=20421&from=20421)

2. 主流的代码热更方案有哪些？
- LUA热更(xLua/toLua等)（LUA与C#绑定，方案成熟）
- ILRuntime热更
- puerts
- HyBridCLR（原huatuo）

- iOS：IL2CPP，AOT（Ahead of Time，运行前编译）
- 安卓：Mono，JIT（Just in Time，动态(即时)编译）

DLL基于动态即时编译，只能在JIT模式下使用，即无法在iOS平台使用

 lua有自己的虚拟机和运行时解释器，不受限于编译方式（IL2CPP、Mono）

 ILRuntime和LSharp也有自己的虚拟机和运行时解译引擎，也不受限于编译方式

3. AssetBundle介绍
AssetBundle是将资源使用Unity提供的一种用于存储资源的压缩格式打包后的集合，它可以存储任何一种Unity可以识别的资源，如模型，纹理图，音频，场景等资源。也可以加载开发者自定义的二进制文件。

用途：
制作DLC （动态的可下载内容）
减少初始包大小
加载为用户平台优化的资源
减少运行时的内存压力

4. AssetBundle的具体开发流程

- 创建Asset bundle，开发者在unity编辑器中通过脚本将所需要的资源打包成AssetBundle文件。
- 上传服务器。开发者将打包好的AssetBundle文件上传至服务器中。使得游戏客户端能够获取当前的资源，进行游戏的更新。
- 下载AssetBundle，首先将其下载到本地设备中，然后再通过AsstBundle的加载模块将资源加到游戏之中。
- 加载，通过Unity提供的API可以加载资源里面包含的模型、纹理图、音频、动画、场景等来更新游戏客户端。
- 卸载AssetBundle，卸载之后可以节省内存资源，并且要保证资源的正常更新。

5. AssetBundle的压缩格式
- LZMA格式： 使用LZMA格式压缩的AssetBundle的包体积最小（高压缩比），但是相应的会增加解压缩时的时间。
- LZ4格式：压缩后的AssetBundle包体的体积较大（该算法基于chunk）。但是使用LZ4格式的好处在于解压缩的时间相对要短。
不压缩：没有经过压缩的包体积最大，但是访问速度最快。

6. AssetBundle对象的加载方式
Unity提供了三个不同的API从AssetBundles加载UnityEngine.Objects，这些API都绑定到AssetBundle对象上，并且这些API具有同步（和异步变体）:
- LoadAsset(LoadAssetAsync)：从资源包中加载指定的资源
- LoadAllAssets (LoadAllAssetsAsync)：加载当前资源包中所有的资源
- LoadAssetWithSubAssets (LoadAssetWithSubAssetsAsync)

并且这些API的同步版本总是比异步版本快至少一个帧(其实是因为异步版本为了确保异步，都至少延迟了1帧)，异步加载每帧会加载多个对象，直到它们的时间切片切出。

7. AssetBundle资源卸载

- AssetBundle.Unload(false):内存中的AssetBundle对象包含的资源会被销毁。
- AssetBundle.Unload(true):不仅仅内存中的AssetBundle对象包含的资源会被销毁。根据这些资源实例化而来的游戏内的对象也会销毁。
- Reources.UnloadAsset(Object):显式的卸载已加载的Asset对象，只能卸载磁盘文件加载的Asset对象Resources。
- UnloadUnusedAssets:用于释放所有没有引用的Asset对象
- Destroy：主要用于销毁克隆对象，也可以用于场景内的静态物体，不会自动释放该对象的所有引用。虽然也可以用于Asset,但是概念不一样要小心，如果用于销毁从文件加载的Asset对象会销毁相应的资源文件!但是如果销毁的Asset是Copy的或者用脚本动态生成的，只会销毁内存对象。

8. 资源如何打包？依赖项列表如何生成？

查找指定文件夹ABResource里的资源文件    
Directory.GetFile(资源路径)
新建AssetBundleBuild对象
获取资源名称，并赋值对应AB名称
获取各个资源的依赖项：通过UnityEditor.AssetDataBase类获取各个资源的依赖项
使用Unity自带的BuildPipeline进行构建AB包    
BuildPipeLine.BuildAssetBundles(输出AB包路径)
File.WriteAllLines(将依赖项写入文件里)

9. 如何解析版本文件？如何加载AB包资源？具体流程是怎么样的？

解析版本文件列表    
File.ReadAllLines(读取文件列表资源路径URL)
获取资源名称，获取AB包名称，获取依赖项，字典容器存储
获取Lua文件
加载资源    
异步加载资源AB包，AssetBundleRequest请求，AssetBundle.LoadFromFileAsync
先检查依赖项，再异步加载AB包依赖项
加载成功后都有对应的回调方法，将资源作为参数传入

10. 热更新打包方案有哪些？

整包：将完整更新资源放在Application.StreamAssets目录下，首次进入游戏将资源释放到Application.persistentDataPath下。

- 优点：首次更新少
- 缺点：安装包下载时间长，首次安装久

- 优点：安装包小，安装时间短，下载快
- 缺点：首次更新下载解压缩包时间旧

- 海外游戏大部分是使用分包策略，平台规定
- 国内游戏大部分是使用整包策略

11. 热更新的流程

(1) 导出热更流程

打包热更资源的对应的md5信息（涉及到增量打包）
上传热更 ab 到热更服务器
上传版本信息到版本服务器

(2) 游戏热更流程

启动游戏。
根据当前版本号，和平台号去版本服务器上检查是否有热更。
从热更服务器上下载 MD5 文件，比对需要热更的具体文件列表。
从热更服务器上下载需要热更的资源，解压到热更资源目录。
游戏运行加载资源，优先到热更目录中加载，再到母包资源目录加载
。
12. 简述Lua实现面向对象的原理

表table就是一个对象，对象具有了标识self，状态等相关操作
使用参数self表示方法的该接受者是对象本身，是面向对象的核心点,冒号操作符可以隐藏该self参数

- 类（Class）：每个对象都有一个原型，原型(lua类体系)可以组织多个对象间共享行为
setmetatable(A,{__index=B}) 把B设为A的原型

- 继承（Inheritance）：Lua中类也是对象，可以从其他类（对象）中获取方法和没有的字段

- 继承特性：可以重新定义（修改实现）在基类继承的任意方法

- 多重继承：一个函数function用作__Index元方法，实现多重继承，还需要对父类列表进行查找方法，但多继承复杂性，性能不如单继承，优化，将继承的方法赋值到子类当中

- 私有性（很少用）基本思想：两个表表示一个对象，第一个表保存对象的状态在方法的闭包中，第二个表用来保存对象的操作（或接口），用来访问对象本身。使第一个表完成内容私有性。

13. 简述Lua有哪8个类型?简述用途

nil 空——可以表示无效值，全局变量（默认赋值为nil），赋值nil ，使其被删除。
number 整数
table 表
string 字符
userdata 自定义
function 函数
bool 布尔
thread线程

14. C#与Lua的交互原理简述

想要理解Lua语言与其它语言交互的实质，我们首先就要理解Lua堆栈。

 简单来说，Lua语言之所以能和C/C++进行交互，主要是因为存在这样一个无处不在的虚拟栈。栈的特点是先进后出，在Lua语言中，Lua堆栈是一种索引可以是正数或者负数的结构，并规定正数1永远表示栈底，负数-1永远表示栈顶。

 换句话说，在不知道栈大小的情况下，我们可以通过索引-1取得栈底元素、通过索引1取得栈顶元素。

Lua是一种嵌入式脚本语言，可以方便的与c/c++进行相互调用。但是Unity中主要是用c#进行开发的，因此在Unity中使用Lua通常有以下两种方案:

- 使用c#实现一个lua虚拟机
- 基于原生的c lua api做一个封装，让c#调用

从性能上考虑，当前主流方案都是第二种。

基于第二种方案实现的框架目前主要有xLua,sLua,uLua,NLua(+KeraLua)。在这些方案中，都能找到一个相关的类，封装了c#对lua c api的调用。例如在xlua中是XLua.LuaDLL.Lua这个类，在slua中是SLua.LuaDll这个类。

所以在Unity里执行Lua是以c作为中间媒介的:

```js
C# <=> C <=> Lua
```

Lua与宿主语言(这里以c#为例)最基础的两种交互模式即:

c#执行lua代码
lua执行c#静态/成员函数
这种交互是通过一个栈结构进行的。

15. Lua中 pairs与ipairs区别

pairs会遍历所有key，对于key的类型没有要求，遇到nil时可以跳过，不会影响后面的遍历，既可以遍历数组部分，又能遍历哈希部分。
ipairs只会从1开始，步进1，只能遍历数组部分， 中间不是数字的key忽略, 到第一个不连续的数字为止（不含），遍历时只能取key为整数值，遇到nil时终止遍历。

16. Lua中 点和冒号区别

点 ：无法传递自身，需要显示传递
冒号 ：隐式传递自身

17. Lua深拷贝和浅拷贝

- 如何实现浅拷贝
 使用 = 运算符进行浅拷贝
拷贝对象是string、number、bool基本类型。拷贝的过程就是复制黏贴！修改新拷贝出来的对象，不会影响原先对象的值，两者互不干涉。
拷贝对象是table表，拷贝出来的对象和原先对象时同一个对象，占用同一个对象，只是一个人两个名字，类似C#引用地址，指向同一个堆里的数据~，两者任意改变都会影响对方。

- 如何实现深拷贝
 复制对象的基本类型，也复制源对象中的对象
 常常需用对Table表进行深拷贝，赋值一个全新的一模一样的对象，但不是同一个表。

Lua没有实现，封装一个函数，递归拷贝table中所有元素，以及设置metetable元表。

如果key和value都不包含table属性，那么每次在泛型for内调用的Func就直接由if判断返回具体的key和value。

如果有包含多重table属性，那么这段if判断就是用来解开下一层table的，最后层层递归返回。

18. Lua中的闭包简述

> 闭包 = 函数 + 引用环境

子函数可以使用父函数中的局部变量，这种行为可以理解为闭包！

闭包的数据隔离
不同实例上的两个不同闭包，闭包中的upvalue变量各自独立，从而实现数据隔离
闭包的数据共享
两个闭包共享一份变量upvalue，引用的是更外部函数的局部变量（即Upvlaue）,变量是同一个，引用也指向同一个地方，从而实现对共享数据进行访问和修改。
利用闭包实现简单的迭代器
迭代器只是一个生成器，他自己本身不带循环。我们还需要在循环里面去调用它才行。
1）while…do循环，每次调用迭代器都会产生一个新的闭包，闭包内部包括了upvalue(t,i,n)，闭包根据上一次的记录，返回下一个元素，实现迭代
2）for…in循环，只会产生一个闭包函数，后面每一次迭代都是使用该闭包函数。内部保存迭代函数、状态常量、控制变量。

19. __index和__newindex元方法的区别

__newindex用于表的更新，__index用于表的查询。

如果访问不存在的数据，由__index提供最终结果
如果对不存在的数据赋值，由__newindex对数据进行赋值

__index元方法可以是一个函数，Lua语言就会以【表】和【不存在键】为参数调用该函数

__index元方法也可以是一个表，Lua语言就访问这个元表

对表中不存在的值进行赋值的时候，解释器会查找__newindex

 __newindex元方法如果是一个表，Lua语言就对这个元表的字段进行赋值

20. table的一些知识点

table 是 Lua 的一种数据结构，用于帮助我们创建不同的数据类型，如：数组、字典等；

table 是一个关联型数组，你可以用任意类型的值来作数组的索引，*但这个值不能是 nil*，所有索引值都需要用 ““和”” 括起来；如果是字符串，还可以去掉引号和中括号； 即如果没有[]括起，则认为是字符串索引，Lua table 是不固定大小的，你可以根据自己需要进行扩容；

table 的默认初始索引一般以 1 开始，如果不写索引，则索引就会被认为是数字，并按顺序自动从1往后编；

table 的变量只是一个地址引用，对 table 的操作不会产生数据影响；

table 不会固定长度大小，有新数据插入时长度会自动增长；

table 里保存数据可以是任何类型，包括function和table；

table所有元素之间，总是用逗号 “，” 隔开；

21. Lua是如何实现热更新的

Lua的模块加载机制，*热更的核心就是替换Package.loaded表中的模块。*

导出函数require（mode_name）
查询全局缓存表package.loaded
通过package.searchers查找加载器
package.loaded
存储已经被加载的模块：当require一个mode_name模块得到的结果不为假时，require返回这个存储的值。require从package.loader中获得的值仅仅是对那张表（模块）的引用，改变这个值并不会改变require使用的表（模块）。
package.preload
保存一些特殊模块的加载器：这里面的值仅仅是对那张表（模块）的引用，改变这个值并不会改变require使用的表（模块）。
package.searchers
require查找加载器的表：这个表内的每一项都是一个查找器函数。当加载一个模块时，require按次序调用这些查找器，传入modname作为唯一参数。此方法会返回一个函数（模块的加载器）和一个传给这个加载器的参数。或返回一个描述为什么没有找到这个模块的字符串或者nil。


### Unity相关技术
Unity中的网络知识包括TCP和UDP，帧同步和状态同步，如何处理网络波动等问题
1. LOD技术
层次细节（LOD），它是根据物体在游戏画面中所占视图的百分比来调用不同复杂度的模型的。简单而言，就是当一个物体距离摄像机比较远的时候使用低模，当物体距离摄像机比较近的时候使用高模。这是一种优化游戏渲染效率的常用方法。使用这个技术，一般是在解决运行时流畅度的问题，采用的是空间换时间的方式。

2. 遮挡剔除技术
在场景空间中创建一个遮挡区域，该遮挡区域是有单元格（Cell）组成；每个单元格是构成整个场景遮挡区域的一部分，这些单元格会把整个场景拆分成多个部分，当摄像机能够看到该单元格时，表示该单元格的物体会被渲染出来，其他的不去渲染。当场景中包含大量模型时，造成渲染效率的降低（即帧速率FPS的降低），采用遮挡剔除技术，可以使得那些被阻挡的物体不被渲染提高渲染效率。

3. 对象池技术
对象池就是我们将对象存储在一个池子中，当需要时在再次使用，而不是每次都实例化一个新的对象。池的最重要的特性，也就是对象池设计模式的本质是允许我们获取一个“新的”对象而不管它真的是一个新的对象还是循环使用的对象。在FPS中常用作需要被发射的子弹、粒子，等优点在于优化内存资源，提高系统性能。

4. 场景异步加载技术
在切换场景的时候，使用异步接口进行load，还是之前说的，同步load会导致卡顿而影响渲染。通过异步加载场景，尽量减少阻塞的时间，因为场景加载完毕运行的时候，初始化相关例如awake和start还是会导致一定的卡顿，这个就要通过后面的方式来解决。

5. 静态批处理技术
只在运行开始阶段，把需要进行静态批处理的模型合并到一个新的网格中，这意味着这些模型数据不可以在运行时刻被移动。它只需要进行一次合并操作，因此比动态批处理更加高效。将Inspector面板右上角的Static勾选(实际上只需要勾选Batching Static即可)。

6. 动态批处理技术
每一帧把可以进行批处理的模型网格进行合并，再把合并后模型数据传递给GPU，然后使用同一个材质对其渲染。动态批处理条件相当苛刻。有时Unity动态批处理会自动完成，不需要我们操作。程序进行动态批处理后，物体们会合并成为一个物体的子物体。DrawCall会下降很多，减少了那些被合并模型原来的DC值，效果立杆见影。

7. 合并网格技术
　加载，关联各个已有的SkinnedMeshRenderer，保持可以获取到对其的指向，这些SkinnedMeshRenderer并不显示。 对应部分共用一个SkinnedMeshRenderer展示，确保坐标和旋转角度的正确。 从关联的SkinnedMeshRenderer中获取需要的信息复制到展示用的SkinnedMeshRenderer。合并网格，将所有网格的信息合并到使用一个SkinnedMeshRenderer来渲染，降低CPU负担

8. 单例模式技术
在我们的整个游戏生命周期当中，有很多对象从始至终有且只有一个。这个唯一的实例只需要生成一次，并且直到游戏结束才需要销毁。 单例模式一般应用于管理器类，或者是一些需要持久化存在的对象。意味着在内存中，只存在一个实例，减少了内存开销。适用于资源管理器，资源对象数据的加载和卸载（无状态不需要实例化的对象）；单一客户端连接服务器等；生命周期在游戏中永不消毁的对象。

9. 组合模式技术
组合模式可以清楚地定义分层次的复杂对象，表示对象的全部或部分层次，使得增加新部件也更容易，因为它让客户忽略了层次的不同性，而它的结构又是动态的，提供了对象管理的灵活接口。组合模式对于树结构的控制有着神奇的功效，例如在人力资源系统的组织架构及ERP系统的BOM设计中，组合模式得到重点应用。
组合模式的缺陷是使得设计变得更加抽象。对象的商业规则如果很复杂，则实现组合模式具有很大挑战性，并且，不是所有的方法都与叶部件子类有关联。

10. 装饰模式技术
装饰模式提供了比静态继承更好的柔韧性，它允许开发一系列的功能类用来代替增加对象的行为，这既不会污染原来对象的源码，还能使代码更容易编写，使类更具扩展性，因为变化都是由新的装饰类来完成。还可以建立连接的装饰对象关系链。
需要注意的是，装饰链不宜过长。装饰链太长会使系统花费较长时间用于初始化对象，同时信息在链中的传递也会浪费太多的时间。这个情况好比物品包装，包了一层又一层，大包套小包。另外，如果原来的对象接口发生变化，它所以的装饰类都要修改以匹配它的变化。派生子类会影响对象的内部，而一个Decorator只会影响对象的外表。

11. Lightmapping光照贴图技术
Lightmapping光照贴图技术是一种增强静态场景光照效果的技术，其优点是可以通过较少的性能消耗使静态场景看上去更加真实，丰富，更加具有立体感；缺点是不能用来实时地处理动态光照。当游戏场景包含了大量的多边形时，实时光源和阴影对游戏的性能的影响会很大。这时使用Lightmapping技术，将光线效果预渲染成贴图使用到多边形上模拟光影效果。

12. Dynamic Bone插件
为了增加角色运动的真实代入感，我们常常需要某些主体的附属物能跟随主体的运动自然地发生变化，如头发、衣服的运动等，这时候Dynamic Bone就能满足我们的需求，从而避免了美术设计师费时费力地重复工作，并且性能表现非常高效。该插件是源码开放的，适合移动设备。该插件的使用非常简单，开发者只需要在此设置一些根节点等相关参数。原理也不难理解：对于每个附属物体，获取骨骼根节点和控制节点的Transform信息。根据这两个结点信息，根据设定参数将运动传播出去。

13. Vectrosity插件
Unity3D中可以用Vectrosity插件画直线、画点、画曲线、画方框，这个插件可以说是Unity3D目前发现的一个画线最好的工具插件。

14. NGUI插件
NGUI是一款严格遵循KISS原则并用C#编写的插件，提供强大的UI系统和事件通知框架，主要用在界面设计之中。支持Flash，支持语言本地化即多语言，支持图像高低清配置，还会随着unity一直更新。

15. Itween插件
iTween是一个动画库,用它可以轻松实现各种动画,晃动,旋转,移动,褪色,上色,控制音频等等，核心功能就是对位移，缩放，颜色等数值进行插值。
16. Bitmap2Material插件
Bitmap2Material是一个强大的工具帮助您从位图中生成无缝材质(法线、高度、高光等),也可以帮助你直接在Unity中从任意位图产生完整的、高质量的、无缝的瓦片状材质(法线、高度、高光、环境遮挡等贴图)，主要用于画面增强。

17. Playmaker插件
可视化脚本语言，具有高度有好的界面、整合性高、功能强大、修改容易等特点。开发者只需将集成的功能模块用连线的方式，通过逻辑关系将其连接，即可快速创建所需功能，非常适合非编程人员与项目制作使用。

18. BIG Environment Pack Vol.2插件
一款环境开发插件，有很多场景模型环境包。灌木丛拥有8个不同种类，一共超过80种变种。草拥有5个不同种类，一共超过21种变种。植物拥有8个不同种类，一共22种变种。树木拥有8个不同种类，一共240种变种。草丛拥有超过40种的预制

19. ProBuilder插件
ProBuilder 2.0允许用户进行快速、高度优化，编辑器水平的建设。从环境细节，到结构体，到整体水平生成自定义的几何形状并将其贴上文理。利用即时反馈和零中断创作过程的特性来进行创作和测试

20. DoTween插件
做动画非常的方便，直接链式结构写代码也非常的快。避免代码里面控制物体还需要写协程或者再Update里面循环。

21. Litjson插件
对Json数据处理非常的简洁方便,比如我们要去读取一个json的数据换成游戏里面的脚本类，只用 JsonMapper.ToObject的函数就搞定了

**法线贴图** (Normal Map) 是一种凹凸贴图 (Bump Map)。它们是一种特殊的纹理，可让您将表面细节（如凹凸、凹槽和划痕）添加到模型，从而捕捉光线，就像由真实几何体表示一样。
例如，您可能希望显示一个表面，在表面上有凹槽和螺钉或铆钉，比如飞机机身。为实现此目的，一种方法是将这些细节建模为几何体，
为什么呈现紫蓝色？
了解这一点对于使用法线贴图并不重要！跳过这一段是可以的。但是，如果真的想知道，请参考以下信息：RGB 颜色值用于存储矢量的 X、Y、Z 方向，其中的 Z 为“向上”（与 Unity 通常使用 Y 作为“向上”的惯例相反）。此外，纹理中的值视为经过减半处理，即添加了 0.5 的系数。这样就能存储所有方向的矢量。因此，为了将 RGB 颜色转换为矢量方向，必须乘以 2，然后减去 1。例如，RGB 值 (0.5, 0.5, 1) 或十六进制的 #8080FF 将得到矢量 (0,0,1)，这便是用于法线贴图的“向上”，并表示模型表面没有变化。这就是您在此页面前面的法线贴图“示例”的平面区域中看到的颜色。

### Shader&渲染管线&图形学&OpenGL

1. 什么是LightMap？
LightMap：就是指在三维软件⾥实现打好光，然后渲染把场景各表⾯的光照输出到贴图上，最后⼜通过引擎贴到场景上，这样就使物体有了光照的感觉。

2. MipMap是什么，作用？
MipMapping：在三维计算机图形的贴图渲染中有常⽤的技术，为加快渲染进度和减少图像锯⻮，贴图被处理成由⼀系列被预先计算和优化过的图⽚组成的⽂件，这样的贴图被称为MipMap。

优点：优化显存带宽，用来减少渲染。因为可以根据距离摄像机远近，选择适合的贴图来渲染。所以UI不适用MipMap。
缺点：运行时占用更多内存，且增加包的容量。
【使用 Mip maps 需要使用 33%以上的内存，但不使用它会导致巨大的性能损失】

3. 请问alpha test在何时使用？能达到什么效果？
Alpha Test，中文就是透明度测试。
简而言之就是V&F shader中最后fragment函数输出的该点颜色值（即上一讲frag的输出half4）的alpha值与固定值进行比较。Alpha Test语句通常于Pass{}中的起始位置。Alpha Test产生的效果也很极端，要么完全透明，即看不到，要么完全不透明。

4. 一个Terrain，分别贴3张，4张，5张地表贴图，渲染速度有什么区别？为什么？
没有区别，因为不管几张贴图只渲染一次。

5. 实时点光源的优缺点是什么？
可以有cookies – 带有 alpha通道的立方图(Cubemap )纹理。点光源是最耗费资源的。

6. 简述水面倒影的渲染原理？
原理就是对水面的贴图纹理进行扰动，以产生波光玲玲的效果。用shader可以通过GPU在像素级别作扰动，效果细腻，需要的顶点少，速度快

7. MeshRender中material和 sharedmaterial的区别?
修改sharedMaterial将改变所有物体使用这个材质 的外观，并且也改变储存在工程里的材质设置。
不推荐修改由sharedMaterial返回的材质。如果你 想修改渲染器的材质，使用material替代。

8. 什么是渲染管道?
是指在显示器上为了显示出图像⽽经过的⼀系列必要 操作。 渲染管道中的很多步骤，都要将⼏何物体从⼀个坐标系中变换到另⼀个坐标系中去。

**主要步骤有： 本地坐标->视图坐标->背⾯裁剪->光照->裁剪->投影-> 视图变换->光栅化。**

GPU工作流程：顶点处理、光栅化、纹理贴图、像素处理

顶点处理：这阶段GPU读取描述3D图形外观的顶点数 据并根据顶点数据确定3D图形的形状及位置关系，建 ⽴起3D图形的⻣架。
光栅化：把⼀个⽮ᰁ图形转换为 ⼀系列像素点的过程就称为光栅化
纹理贴图：就是将多边形的表⾯贴 上相应的图⽚，从⽽⽣成“真实”的图形。
像素处理：这阶段（在对每个像素进⾏光栅化处理期 间）GPU完成对像素的计算和处理，从⽽确定每个像 素的最终属性。
最终输出：由ROP（光栅化引擎）最终完成像素的输 出，1帧渲染完毕后，被送到显存帧缓冲区。
总结：GPU的⼯作通俗的来说就是完成3D图形的⽣成，将图形映射到相应的像素点上，对每个像素进⾏ 计算确定最终颜⾊并完成输出。

9. 如何在Unity3D中查看场景的面数，顶点数和DrawCall数？如何降低DrawCall数？
在Game视图右上⻆点击Stats。降低Draw Call 的技术是Draw Call Batching

10. 写出光照计算中的diffuse的计算公式
diffuse = Kd x colorLight x max(N*L,0)；
Kd 漫反射系数、colorLight 光的颜⾊、N 单位法线向量、L 由点指向光源的单位向量、其中N与L点乘，如果结果⼩于等于0，则漫反射为0。

11. 两种阴影判断的方法、工作原理。

本影：景物表⾯上那些没有被光源直接照射的区域
（全⿊的轮廓分明的区域）。

半影：景物表⾯上那些被某些特定光源直接照射但并⾮被所有特定光源直接照射的区域（半明半暗区域）

⼯作原理：从光源处向物体的所有可⻅⾯投射光线，将这些⾯投影到场景中得到投影⾯，再将这些投影⾯与场景中的其他平⾯求交得出阴影多边形，保存这些阴影多边形信息，然后再按视点位置对场景进⾏相应处理得到所要求的视图（利⽤空间换时间，每次只需依据视点位置进⾏⼀次阴影计算即可，省去了⼀次消隐过程）

12. 有A和B两组物体，有什么办法能够保证A组物体永远比B组物体先渲染？
在Unity中，为了确保A组物体永远比B组物体先渲染，可以通过调整物体的渲染队列（Render Queue）来实现。下面将具体探讨如何操作以及相关的一些技术细节：
调整渲染队列
修改材质的Render Queue：在Unity中，每个物体的渲染顺序是通过分配给它们的材质决定的。每种材质都有一个默认的渲染队列值。要更改物体的渲染顺序，您可以直接修改其材质的渲染队列值。这通过在材质的属性面板中查找"Render Queue"字段来完成。您可以为A组物体分配一个较小的渲染队列值，而给B组物体分配一个较大的值[9]。
使用Shader更改渲染队列：如果您对Unity的Shader编程有一定了解，可以在Shader中直接指定"Tags { “Queue”=“…” }"来改变使用该Shader的物体的渲染队列。例如，可以设置"Queue"标签值为"Geometry"或"Transparent"等，根据需要将A组物体放在B组物体之前渲染。
使用脚本动态控制

编写脚本调整Render Queue：如果场景中的物体经常变动，或者您希望根据特定条件动态改变物体的渲染顺序，可以编写一个Unity脚本来动态修改物体的Render Queue值。使用Material类的renderQueue属性，可以方便地在脚本中设置材质的渲染队列值。
示例脚本：一个简单的示例是创建一个脚本，遍历A组和B组的所有物体，然后分别设置它们的Render Queue值。例如，对于A组物体设置为1000，而B组物体设置为2000，以确保A组物体总是先渲染。
理解Unity的渲染顺序

渲染队列工作原理：Unity的渲染顺序基本上是按照渲染队列值从小到大进行的。较小的数值将被先渲染，而较大的数值则后渲染。这一点在不同的Shader类型间也成立，例如，通常“Opaque”类型的物体会在“Transparent”类型之前渲染。
注意透明材质：值得注意的是，当处理带有透明材质的物体时，渲染顺序可能会更加复杂，因为透明物体常常需要按照深度排序来正确渲染。在这种情况下，除了调整渲染队列外，可能还需要特别注意场景设置和Shader配置。
总的来说，通过上述方法，您可以有效地控制Unity中不同物体组的渲染顺序，确保A组物体始终在B组物体之前渲染。这不仅有助于实现特定的视觉效果，也可能对性能优化有积极影响。在进行这些调整时，建议密切关注场景的渲染表现和性能，以确保达到预期的效果。

13. Unity的Shader中，Blend SrcAlpha OneMinusSrcAlpha这句话是什么意思？
作用就是Alpha混合。公式：最终颜色 = 源颜色源透明值 + 目标颜色（1 - 源透明值）

14. Vertex Shader是什么，怎么计算？
顶点着⾊器是⼀段执⾏在GPU上的程序，⽤来取代fixed pipeline中的transformation和lighting，Vertex Shader主要操作顶点。
Vertex Shader对输⼊顶点完成了从local space到homogeneous space（⻬次空间）的变换过程，homogeneous space即projection space的下⼀个space。
在这其间共有world transformation, view transformation和projection transformation及lighting⼏个过程

15. Unity3D Shader分哪⼏种，有什么区别？
表⾯着⾊器 的抽象层次⽐较⾼，它可以轻松地以简洁⽅式实现复杂着⾊。表⾯着⾊器可同时在前向渲染及延迟渲染模式下正常⼯作。

顶点⽚段着⾊器可以⾮常灵活地实现需要的效果，但是需要编写更多的代码，并且很难与Unity的渲染管线完美集成。

固定功能管线着⾊器可以作为前两种着⾊器的备⽤选择，当硬件⽆法运⾏那些酷炫Shader的时，还可以通过固定功能管线着⾊器来绘制出⼀些基本的内容。

16. Unity提供了几种光源，分别是什么？
四种。

平行光：Directional Light
点光源：Point Light
聚光灯：Spot Light
区域光源：Area Light
17. 分别解释顶点着色器和像素着色器是什么
顶点着⾊器是⼀段执⾏在GPU上的程序，⽤来取代 fixed pipeline中的transformation和lighting，Vertex Shader主要操作顶点。‘’

像素着色器实际上就是对每一个像素进行光栅化的处理期间，在GPU上运算的一段程序。

不同与顶点着色器，像素着色器不会以软件的形式来模拟像素着色器。

像素着色器实质上是取代了固定功能流水线中多重纹理的环节，而且赋予了我们访问单个像素以及访问每一个像素纹理坐标的能力

18. 简述SkinnedMesh的实现原理
根据骨骼，动态整体实现表层Mesh，相对普通mesh由不同面片堆砌，根据骨骼结构，对顶点的变换计算出不同的蒙皮，最终进行模型的渲染

19. MeshRender中material和sharedmaterial的区别？
答：修改sharedMaterial将改变所有物体使用这个材质的外观，并且也改变储存在工程里的材质设置。 不推荐修改由sharedMaterial返回的材质。如果你想修改渲染器的材质，使用material替代。

### 主流操作系统的跨平台差异

### 408

---

## 项目经历

客户端是用的什么框架、热更技术，如何和后端交互的，用的是什么设计模式等等

### 次元射击

#### GameManager

GameManager是一个用于管理游戏状态和流程的工具，可以让游戏的流程更加清晰和有序，也更容易调试和组织。比如，在回合制游戏中，GameManager可以跟踪当前回合，让玩家和敌人轮流行动。使用GameManager可以使游戏更加灵活和可扩展，方便添加新的功能或修改现有的功能。此外，GameManager让游戏代码更加模块化，更易于维护和扩展。

在游戏开发的早期阶段，可以考虑使用GameManager来规划游戏的状态和流程。在游戏的后期阶段，可以使用GameManager来实现游戏的状态转换和流程控制。GameManager可以帮助游戏开发人员更好地管理游戏的状态和流程。

举个栗子, GameManager可以通过以下步骤来使用：

创建一个名为GameManager的空对象，并添加一个名为GameManager的脚本组件。
在GameManager脚本中，定义一个名为GameState的枚举类型，用于表示游戏的不同状态。
在GameManager脚本中，定义一个名为gameState的变量，用于存储当前游戏状态。
在GameManager脚本中，定义一个名为UpdateGameState的方法，用于更新游戏状态，并触发OnGameStateChanged事件。
在GameManager脚本中，定义一个名为OnGameStateChanged的公共静态事件，用于通知其他脚本游戏状态的更改。
在其他脚本中，订阅OnGameStateChanged事件，以响应游戏状态的更改。
在其他脚本中，使用GameManager实例的静态引用来获取当前游戏状态，并根据需要执行相应的操作。
例如，在回合制游戏中，可以使用GameManager来跟踪当前回合，让玩家和敌人轮流行动。下面是一个简单的例子：
```cs
public class TurnManager : MonoBehaviour
{
    void Start()
    {
        // 订阅OnGameStateChanged事件
        GameManager.OnGameStateChanged += OnGameStateChanged;
    }

    void OnDestroy()
    {
        // 取消订阅OnGameStateChanged事件
        GameManager.OnGameStateChanged -= OnGameStateChanged;
    }

    void OnGameStateChanged(GameState newState)
    {
        // 根据新状态执行相应的操作
        switch (newState)
        {
            case GameState.PlayerTurn:
            // 玩家回合，允许玩家行动
            break;
            case GameState.EnemyTurn:
            // 敌人回合，执行敌人的行动
            break;
            case GameState.GameOver:
            // 游戏结束，显示游戏结束画面
            break;
        }
    }
}
```
使用GameManager可以使游戏更加灵活和可扩展，方便添加新的功能或修改现有的功能。此外，GameManager让游戏代码更加模块化，更易于维护和扩展。

#### 优化画面效果：

##### 1、指标介绍:
FPS（Frames per Second）：显示当前游戏帧率。帧率越高，游戏画面越流畅。为提高帧率，可减少游戏对象数量、优化渲染方式等。

Draw Calls：显示当前帧需要渲染的次数。过多的Draw Calls会导致游戏运行缓慢。降低此指标可通过优化场景、材质或使用批处理技术等方式。

Tris：显示当前帧需要渲染的三角形数量。过多的三角形数量同样会导致游戏运行缓慢。减少此指标可采取降低模型细节、使用LOD技术等方法。

Memory：显示当前游戏所使用的内存大小。过高的内存占用会导致游戏运行缓慢或崩溃。降低此指标可通过优化资源加载和释放方式等方法。

Audio：显示当前游戏音频的播放情况，包括音频资源的大小和播放时间。优化音频资源的加载和播放方式可减少CPU占用率，提高游戏性能。

通过实时监控这些性能指标，开发者可以及时发现问题并采取相应的优化措施，提高游戏性能和流畅度。

##### 2、如何优化Tris:
在Unity中，Tris是指场景中所有三角形的数量，也称为三角形数或面数。Tris是影响游戏性能的重要指标，它直接影响游戏的帧率和渲染性能。

Tris数量过多会导致游戏的帧率下降，因为GPU需要处理更多的三角形，在性能较差的设备上可能会出现卡顿现象。因此，在制作游戏时，需要尽可能减少Tris的数量，以提高游戏的运行效率。

以下是一些常用的减少Tris数量的方法：

使用简单的几何形状：在制作游戏时，尽量使用简单的几何形状，例如球体、立方体、圆柱等。这些几何形状的Tris数量较少，可以有效地减少三角形数量。

使用LOD（Level Of Detail）：在场景中使用不同级别的模型或材质，以适应不同距离的观察者。在近距离观察时，使用高级别的模型或材质；远距离观察时，使用低级别的模型或材质。这样可以有效减少Tris数量，提高游戏性能。

合并网格：将多个网格合并为一个网格，以减少Tris数量。可以使用Unity自带的网格合并工具或第三方插件，例如ProBuilder。

使用遮挡剔除（Occlusion Culling）：根据场景中物体的可见性，只渲染可见的物体，从而减少不必要的渲染操作。这样可以减少渲染的Tris数量，提高游戏性能。

通过使用这些技术，开发者可以有效减少Tris数量，优化游戏性能，提高游戏的帧率和流畅度。

##### 3、批处理优化方法：
合并相同材质球的多个网格：将多个使用相同材质球的网格合并成一个网格，减少批次的数量。在使用Mesh Combine工具时，设置CombineInstances数组的材质球为相同的材质球即可。

使用材质球批次合并：使用相同的材质球对多个物体应用相同的材质，或者使用批处理材质球，将多个物体合并到同一个批处理中。

使用 GPU Instance（GPU 实例化）：通过使用 GPU 实例化技术，可以将多个相同的网格实例化为一个批次进行渲染。这样可以减少不必要的绘制调用和渲染开销，提高游戏性能。

使用静态批处理：将不会进行移动或变化的物体合并为一个静态批次。静态批处理只需要进行一次渲染调用，减少了渲染开销。

减少动态批处理中的顶点数：动态批处理会对每个物体的每帧顶点进行重新计算，因此顶点数越多开销越大。可以通过优化模型或使用低多边形模型来减少顶点数。

使用 GPU Skinning：GPU Skinning 是一种在 GPU 上执行的骨骼动画渲染技术，可以大幅度提高骨骼动画的性能。它通过将计算部分放到 GPU 上，减轻了 CPU 的负载。

##### 4、Unity设置优化画面
ColorSpace，选择设置为Linear线性空间而不是Gamma非线性空间，因为线性空间在计算渲染时可以更真实的还原物理世界的光强度，实现更好的预期。需要注意的是，Linear不支持一些低端的移动安卓平台，目前只支持OpenGl SE3.0 Android4.3及以上，IOS只有Metal才支持。虽然Linear渲染的效果更好，但是Gamma的渲染开销更低，效率高，开发时根据情况选择。

PixelLightCount，根据情况设置像素灯数量，数量越多可渲染的灯数量也就越多，渲染开销也越高，有时候场景中有多个灯光但是只有几个是正常显示，原因就是灯光数量超过了PixelLightCount设置的数量。

TextureQuality，根据情况选择纹理质量大小，最好的是FullRes完整分辨率，往下有HalfRes QuarterRes EightRes，分辨率越高处理开销也越大。

AnisotropicTextures，一般都选择ForcedOn一直开启各向异性纹理，个别情况选择PerTexture逐纹理或者Disabled关闭。

AntiAliasing，根据情况选择抗锯齿级别，有2x 4x 8x，采样倍数越高抗锯齿效果越好同时处理开销也越大。

SoftParticles，根据情况选择软粒子是否开启，开启软粒子可以让粒子特效与场景有一个过渡，提升效果质量，不过开启后会增加处理开销，尤其手机移动端开启后掉帧明显。

RealtimeReflectionProbes，根据情况选择实时更新反射探针是否开启，开启实时反射对于场景画面的质量有很大提升，可以模拟物理世界的反射，但是开启后其处理开销也是大大增加，开发时酌情选择。

BillboardsFaceCameraPosition，开启后可以产生更好更逼真的图像，但是处理开销会增加根据情况选择。

ResolutionScalingFixedDPIFactor，基于当前的分辨率设置缩放，默认设置1，一般不动它，如果场景画面运行帧数不够可以降低设置，比如场景分辨率为1920*1080然后设置为0.5，则分辨率减半为960*540，可以优化性能。

Shadows，根据情况选择开启阴影或者阴影的类型，选择HardAndSoftShadows硬和软阴影都会被渲染，都渲染可以提升场景画面效果，但是会增加处理开销，选择HardShadowsOnly仅渲染硬阴影，仅渲染硬阴影会使的场景中的阴影看起来比较生硬没有过度，相对于硬软都开处理开销会低一些，DisableShadows不渲染阴影，则场景中没有阴影。

ShadowResolution，根据情况选择阴影的分辨率，有LowResolution MediumResolution HighResolution VeryHighResolution，分辨率越高处理开销越大。

ShadowProjection，根据情况选择阴影投射的方式，CloseFit渲染较高分辨率的阴影，但是当相机移动时，有时阴影会有轻微摆动，StableFit渲染的阴影分辨率较低，但是相机移动时阴影不会发生摆动。

ShadowDistance，相机的最大阴影可见距离，超过设置的距离则不会被渲染，默认设置150，根据情况设置。

ShadowmaskMode，根据情况设置阴影遮罩的质量，DistanceShadowmask以更高的性能成本提供更高保真度的阴影，Shadowmask以更低的性能成本提供更低保真度的阴影，配合lighting设置mode为Shadowmask，Shadowmask光照模式在所有光照模式中提供最高保真度的阴影，但是所需的性能成本和内存要求也是最高的，此模式适用于在高端或者中档硬件上渲染远处游戏对象可见时的真实场景，如空旷的空间世界。

ShadowNearPlaneOffset，根据情况输入阴影近平面偏移，默认设置3，用于解决大三角形由于阴影平坠而扭曲的问题。

ShadowCascades，根据情况选择阴影的级联数量，有NoCascades TwoCascades FourCascades， 级联数量越高，提供的质量越高，但代价是处理开销增加。

CascadesSplits，根据ShadowCascades设置的值可以看见两种或者四种不同的颜色，通过向左或者向右移动每个级联之间的垂直线来调整级联阴影分割，如果ShadowCascades设置为NoCascades则看不见CascadesSplits。

BlendWeights，选择在动画期间可以影响给定顶点的骨骼数量，有1Bone 2Bones 4Bones，根据情况选择。

VSyncCount，根据情况选择将渲染与垂直空白同步还是根本不同步，可将渲染与显示设备的刷新率同步来避免撕裂瑕疵，一般选择设置EveryVBlank。

LodBias，根据情况设置细节级别偏差，默认设置2，越高倾向于更多细节。

MaximumLODLevel，根据情况设置游戏使用的最高LOD，默认设置0，在构建中不会使用 LOD 低于 MaximumLOD 级别的模型，而是将其忽略（这样可以节省存储和内存空间）。Unity 将使用与目标平台质量设置相关联的所有 MaximumLOD 值中的最小 LOD 值。如果包含 LOD 级别，则该 LODGroup 中的模型将包含在构建中，并始终在运行时为该 LODGroup 加载，无论使用何种质量设置。例如，如果在任何质量设置中使用 LOD 级别 0，则所有 LOD 级别都将包含在构建中，并且所有引用的模型都将在运行时加载。

ParticleRaycastBudget，设置用于模拟粒子系统碰撞的最大射线投射数，默认设置4096，根据情况设置。

AsyncUploadTimeSlice，设置将缓冲的纹理和网格数据上传到GPU时花费的CPU时间量，默认设置2，单位为毫秒/帧，根据情况设置。

AsyncUploadBufferSize，设置用于将纹理和网格数据串流到GPU的异步上传缓冲区大小，默认设置4，单位为MB，根据情况设置。

### 思觉失调(Dyskinesia)

#### 使用统一接口
使用接口去统一管理场景中的可交互对象，我们声明一个交互对象接口。
```cs
public interface IInteractiveItem
{
    void Trigger();
}
```
交互对象接口

让我们需要与玩家进行交互的场景物品对象继承这个接口 并实现接口方法。我们拿一个门的游戏物体来举例 我们希望 玩家在碰到门时 进行场景切换 
```cs
public class PassDoor : MonoBehaviour, IInteractiveItem
{
    [SerializeField] private int NextLevelID;

    void IInteractiveItem.Triger()
    {
        //切换到通关场景
    }
}
```
可以发现已经可以将本该在玩家脚本中的对象中的逻辑 移动到了门的逻辑中，这是比较符合设计原则的，那么玩家脚本中又出现了什么变化呢？我们在Unity编辑器中定义一个标签叫 Interactive 并将需要交互的对象设置成当前的Tag

这是是为了跟其他的类型逻辑区分，我们来看一下玩家脚本部分
```cs
private void OnTriggerEnter2D(Collider2D coll)
{
    if(coll.CompareTag("Interactive"))
    {
        coll.GetComponent<IInteractiveItem>().Trigger();
    }
}
```
玩家碰撞逻辑

可以发现 玩家逻辑中 所有 Interactive 标签的交互对象都被统一成了一个接口，通过这个接口，就能调用到对应的逻辑，而且这套方案的扩展性非常高 直接让新的对象继承 IInteractiveItem 接口 并标识为 Interactive 标签即可

####  跨平台

通常在进行不同平台的设置时会基于以下几点：

1：创建、开发、打包时我们通常针对Player和Quality设置进行质量的设定

2：在不同平台上运行时，有不同的平台包体大小，加载方式的限定，测试、打包上的区别，帧率稳定60

3：代码封装上的区别，特别针对单一项目转为不同不同平台的问题

4：输入系统的不同

##### Android

1：针对PlayerSetting、Quality

Android Player 设置 - Unity 手册

这里面的设置基本和我上面介绍的没有什么差异，基本差别在于

ColorSpace、LightmapEncoding(硬性要求)、Texture Compression

安卓多了Minimum API Level、Target API Level，需要适配不同机型，基本上最低我会选择到Android5.1，最高是Autimatic

2：包体大小限定，加载方式，测试
安卓项目对于包体大小有严格的限定，我一般选择ASTC压缩方式，包体大小会小很多

测试使用Development Build，Build and Run，Android Studio这三种进行测试

3：输入方式
我采用了EasyTouch插件，一般移动端有比如单击，双击，滑动屏幕等操作，使用的代码也不是很复杂

双击/长按
```cs
 if (Input.GetMouseButton(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
 
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit))
            {
                #region 双击
                if (Input.touchCount == 1 && Input.GetTouch(0).phase == TouchPhase.Began)//判断几个点击位置而且是最开始点击的屏幕，而不是滑动屏幕
                {
                    if (Input.GetTouch(0).tapCount == 2)//tapcount是点击次数
                    {
                        Destroy(hit.collider.gameObject);
                    }
                }
                #endregion
 
 
                #region 长按
                if (Input.touchCount == 1)
                {
                    Touch touch = Input.GetTouch(0);
                    if (touch.phase == TouchPhase.Began)
                    {
                        newTouch = true;
                        touchTime = Time.time;
                    }
                    else if (touch.phase == TouchPhase.Stationary)//点击没有滑动的时候会触发Stationary
                    {
                        if (newTouch == true && Time.time - touchTime > 1f)
                        {
                            newTouch = false;
 
                            Destroy(hit.collider.gameObject);
                        }
                    }
                    else
                    {
                        newTouch = false;
                    }
 
                }
                #endregion
 
            }
        }
```

滑动屏幕
```cs

        if (Input.GetMouseButton(0))
        {
            if (Input.touchCount==1)
            {
                if (Input.GetTouch(0).phase==TouchPhase.Moved)//滑动状态
                {
                   transform.Rotate(Vector3.up * Input.GetAxis("Mouse X") * -xSpeed * Time.deltaTime,Space.World);
                }
            }
        }
```

双指缩放等
```cs
    /// <summary>
    /// 判断手势
    /// </summary>
    /// <param name="op1">开始的第一个点</param>
    /// <param name="op2">开始的第二个点</param>
    /// <param name="np1">结束的第一个点</param>
    /// <param name="np2">结束的第二个点</param>
    /// <returns></returns>
    bool isEnlarge(Vector2 op1, Vector2 op2, Vector2 np1, Vector2 np2)
    {
        float startLength = Mathf.Sqrt((op1.x - op2.x) * (op1.x - op2.x)+ (op1.y - op2.y) * (op1.y - op2.y));
 
        float endLength = Mathf.Sqrt((np1.x - np2.x) * (np1.x - np2.x) + (np1.y - np2.y) * (np1.y - np2.y));
 
        if (startLength<endLength)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    Vector2 oldPos1;
    Vector2 oldPos2;
    void Update () {
 
        if (Input.touchCount==2)
        {
            if (Input.GetTouch(0).phase==TouchPhase.Moved||Input.GetTouch(1).phase==TouchPhase.Moved)
            {
                Vector2 temPosl = Input.GetTouch(0).position;
                Vector2 temPos2 = Input.GetTouch(1).position;
                if (isEnlarge(oldPos1,oldPos2,temPosl,temPos2))
                {
                    float oldScale = transform.localScale.x;
                    float newScale= oldScale*1.025f;
                    transform.localScale = new Vector3(newScale, newScale, newScale);
                }
                else
                {
                    float oldScale = transform.localScale.x;
                    float newScale = oldScale / 1.025f;
                    transform.localScale = new Vector3(newScale, newScale, newScale);
                }
                oldPos1 = temPosl;
                oldPos2 = temPos2;
            }
        }
    }
```

#### 异步接口进行 load

Unity中的异步加载（Asynchronous Loading）和分帧平滑加载（Load Smoothing Across Frames）虽然都是为了减轻游戏运行时的性能压力，但它们的原理和用途有所不同。

异步加载（Asynchronous Loading）：

原理：异步加载允许游戏在后台加载资源，而不会阻塞主线程。这意味着游戏可以在加载新场景或资源的同时继续运行，从而不会造成明显的停顿或冻结。

实现：Unity 提供了AsyncOperation类和SceneManager.LoadSceneAsync方法，用于异步加载场景。这些操作通常涉及以下步骤：

开始加载操作，通常是通过调用LoadSceneAsync。

在后台线程中加载资源。

通过AsyncOperation的progress属性来监控加载进度。

加载完成后，通常会有一个回调函数来处理后续逻辑。

分帧平滑加载（Load Smoothing Across Frames）：

原理：分帧加载是一种优化手段，它通过将加载工作分散到多个帧中来减少单帧的性能开销。这种方法并不一定是异步的，但它确保了每帧的处理时间保持在一个合理的范围内，从而避免帧率下降。

实现：分帧加载通常是通过以下步骤手动实现的：

评估每帧可以处理的加载量。

在每帧的开始或结束时，加载一定量的资源。

通过检查加载进度或剩余工作来决定是否继续在下一帧加载。

对比：

目的：异步加载主要是为了不阻塞主线程，而分帧加载主要是为了平衡每帧的工作量。

线程：异步加载可能涉及后台线程，而分帧加载通常在主线程上进行，但是将工作分散到多个帧中。

使用场景：异步加载适用于大型资源的加载，如整个场景或大量的数据，而分帧加载适用于可以在多个帧中逐步加载的资源，以避免帧率下降。

总的来说，虽然两者都是为了优化加载性能，但它们的实现方式和应用场景是不同的。开发者会根据具体需求选择最合适的加载策略。

下面是一个异步加载场景的例子.主要使用UnityEngine.SceneManagement;中的异步加载的形式.
```cs
SceneManager.LoadSceneAsync((int)SceneIndex.Main, LoadSceneMode.Additive);
```
下面是一个分帧加载的范例
```cs
public class SmoothLoader : MonoBehaviour
{
    public GameObject[] prefabs; // 预制体列表
    public int objectsPerFrame = 1; // 每帧加载的物体数量
    //读取频率
    public int frameInterval = 15;
    private Queue<GameObject> prefabQueue = new Queue<GameObject>();


    [Button("Load")]

    void LoadTest()
    {
        // 将所有预制体加入队列
        foreach (GameObject prefab in prefabs)
        {
            prefabQueue.Enqueue(prefab);
        }

        // 开始分帧加载物体
        StartCoroutine(LoadObjects());

    }


    IEnumerator LoadObjects()
    {
        while (prefabQueue.Count > 0)
        {
            //显示加载的进度
            Debug.Log("加载进度" + prefabQueue.Count);
            // 加载指定数量的物体
            for (int i = 0; i < objectsPerFrame; i++)
            {
                if (prefabQueue.Count > 0)
                {
                    GameObject spawned;
                    GameObject prefab = prefabQueue.Dequeue();
                    spawned = Instantiate(prefab, transform);
                    spawned.SetActive(true);
                    spawned.SetActive(false);
                    //实例化之后可以,setActive,然后再SetInActive.
                }
                else
                {
                    //如果队列已经为空，结束协程
                    yield break;
                }
            }


            for (int i = 0; i < frameInterval; i++)
            {
                // 等待下一帧
                yield return null;
            }
        }
    }
} 
```
#### 热更新模块

---

## 自我评价
1. 《游戏引擎架构》《STL 源码剖析》“虎书”
2. 永劫无间双排修罗，雀魂麻将
3. 课余爱好做菜和烘焙，喜欢淮扬菜系和巧克力类甜品，拍好看的照片，
4. 另外和朋友 @Paper 朱 运营了一个 Vup@溪冉 hira

- 附淮扬菜
淮扬菜的选料尤为注意鲜活、鲜嫩；
制作精细，注意刀工；
口味清淡，强调本味，重视调汤，风味清鲜，略带甜味；
做过的：文思豆腐、清炖蟹粉狮子头、醋溜鳜鱼、芙蓉鸡片、盐水鹅、清蒸鲥鱼、大煮干丝

### 《游戏引擎架构》《STL 源码剖析》“虎书” 游戏引擎的前沿技术
https://myq0721.github.io/2023/02/07/mini-yin-qing-kai-fa-ri-zhi/#%E4%B8%89%E3%80%81%E6%A0%B8%E5%BF%83%E7%B3%BB%E7%BB%9F
##### 《游戏引擎架构》

##### 《STL源码剖析》

##### 游戏引擎的核心技术：

图形渲染技术：图形渲染技术决定了游戏画面的质量和流畅度。现代游戏引擎普遍支持高级的图形渲染技术，如实时渲染、光线追踪、全局光照等。

物理模拟技术：物理模拟技术用于模拟游戏世界中的物体行为，包括碰撞检测、动力学模拟等。物理引擎如Havok、Bullet等，为游戏提供了逼真的物理效果。

音效处理技术：音效处理技术包括音效的生成、播放、空间化处理等。现代游戏引擎通常提供完整的音效处理解决方案，以提升游戏的沉浸感。

人工智能技术：人工智能技术在游戏中用于控制非玩家角色（NPC）的行为。游戏引擎中的人工智能系统通常包括寻路、决策树、行为树等组件。

###### 一、游戏引擎的高级特性

1. 高级图形渲染技术

光线追踪：光线追踪是一种能够模拟光线在场景中传播的渲染技术，它可以产生非常逼真的光照和阴影效果。随着硬件技术的发展，实时光线追踪已经成为现代游戏引擎的一个重要特性。

全局光照：全局光照是一种考虑光线在场景中多次反射和折射的渲染技术，它可以产生更加自然和真实的光照效果。全局光照技术包括预计算的光照和实时的全局光照。

2. 多线程编程

多线程编程是提高游戏性能的关键技术之一。利用多线程可以提高游戏的性能，尤其是在处理计算密集型任务时。开发者可以利用多线程进行图形渲染、物理模拟、音效处理等。
动态加载与卸载资源

为了减少内存占用，开发者应该实现资源的动态加载和卸载。这包括纹理、网格、音频和动画等。动态加载资源可以减少游戏启动时间，而卸载不再使用的资源可以释放内存，提高游戏的性能。

###### 二、游戏性能优化技巧

1. 代码优化

高效的算法和数据结构：选择合适的数据结构和算法可以显著提高游戏的性能。开发者应该避免使用低效的循环和递归，尽量减少内存分配和释放的次数。

内存管理：优化内存使用，避免内存泄漏和内存溢出。使用智能指针、内存池等技术可以提高内存管理的效率。

2. 资源管理

资源压缩和优化：压缩资源可以减少内存和存储空间的占用。开发者应该使用合适的压缩格式，并对资源进行优化，如减少纹理的大小和分辨率。

资源预加载：在游戏启动时预加载关键资源，减少游戏启动时间。同时，在游戏运行过程中动态加载资源，以提高游戏性能。

3. 渲染优化

合并绘制调用：减少绘制调用可以提高渲染性能。开发者应该尽量合并相同的材质和网格，使用批处理技术。

LOD（细节层次距离）系统：为了优化性能，开发者应该实现LOD系统，根据距离摄像机的距离来显示不同细节级别的模型。

###### 三、游戏引擎的调试与测试

性能分析工具

游戏引擎通常提供性能分析工具，如Unity Profiler、Unreal Engine的Inspector等。这些工具可以帮助开发者诊断和优化游戏性能问题。
单元测试和集成测试

开发者应该编写单元测试和集成测试，以确保游戏逻辑的正确性和稳定性。这些测试可以帮助发现和修复游戏中的bug和性能问题。
用户反馈和社区支持

开发者应该积极收集用户反馈，了解游戏性能问题和用户体验问题。同时，可以利用社区支持，如Unity Forums、Unreal Engine Forums等，获取更多优化建议和技术支持。

---

##### UE5的新技术
###### NANITE虚拟几何体系统

###### LUMEN全局光照解决方案

###### 时序超级分辨率

###### 世界分区

---

## 秋招流程


---

- 上海莉莉丝 校园大使 投递简历 
【2025秋招】客户端开发工程师- Gameplay（生活派对）
https://lilithgames.jobs.feishu.cn/campus/position/application?spread=DQSEHSG

- 北京完美世界 游戏客户端开发工程师 简历收集 
https://app.mokahr.com/campus-recruitment/pwrd/140155#/candidateHome/applications

- 杭州游卡 游戏客户端开发 申请成功 
https://app.mokahr.com/campus-recruitment/yokagames/41940#/candidateHome/applications

- 搜狐畅游 【2025届秋招】U3D开发工程师 初筛 
https://app.mokahr.com/campus-recruitment/cyou-inc/42233#/candidateHome/applications

- 上海友塔 游戏客户端开发工程师 笔试
https://www.yotta-hr.com/zh/job

- 阿里灵犀互娱 游戏客户端开发工程师-上海 新投递
https://talent.lingxigames.com/personal/campus-application?lang=zh

- 吉比特 游戏研发工程师(厦门)  初筛过等笔试
https://hr.g-bits.com/web/index.html#/center-web/recruit-query

- 广州三七互娱 客户端开发工程师 简历筛选
https://app.mokahr.com/campus-recruitment/37/25238?sourceToken=974e7eba170b288bb00457f03863d9bf#/candidateHome/applications

- 北京博乐  游戏客户端开发工程师 初筛
https://app.mokahr.com/campus-recruitment/bolegames/37643?sourceToken=30bcc43e5b67961b7117ab03d500927f#/candidateHome/applications

- 柠檬微趣 Unity3D客户端开发工程师研发中心客户端北京市·西城区
https://app.mokahr.com/apply/microfunhr/75944#/jobs?zhineng=69016

- 广州火羽 U3D开发工程师
https://campus.huoyugame.com/job_detail/job_detail5.html

- 北京乐元素 【校招】游戏客户端开发工程师（北京） 初筛
https://app.mokahr.com/campus_apply/leyuansu/2357#/candidateHome/applications

- 上海沐瞳 【2025届秋招】Unity客户端开发工程师  
https://moonton.jobs.feishu.cn/campus/position/application
JD：
1.精通C#开发语言，有Python,Lua,C++开发经验者优先
2.精通Unity3D开发，精通编辑器和各组件库开发和扩展
3.有技能编辑器，UGC编辑器等相关开发经验者优先
4.了解策划的工作流程并有效能优化经验者优先
5.具有各种工具链的开发经验，并在在实际项目中实现效率和效果提升
6.有较强的产品意识和团队协作能力，有较强的沟通能力

- 牛客https://www.nowcoder.com/users/791488934/deliver
> 没开的： 无端，炎魂，电魂

---

- 哔哩哔哩 Unity图形程序员【2025届】 初筛阶段不匹配