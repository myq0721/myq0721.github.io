---
title: mini引擎(Ayana engine)开发日志
date: 2023-02-07 01:33:22
categories: 游戏/引擎开发
top : true
img : https://i.postimg.cc/zv2WgWR8/85f618385196c7b0ea3cb7bc52c5eb75388411170.png
---

# 第二部分（02/18

##  项目设置

>创建Ayana DLL文件

>完成与Ayana链接的Sandbox启动项

>建立GitHub存储库

github : https://github.com/myq0721/Ayana

c++17,x64,vs2017(v141)

>*SDK版本要改为10.0.19041.0,不然会有无法打开源文件的错*

配置：

输出目录:   \$(SolutionDir)bin\\$(Configuration)-\$(Platform)\\$(ProjectName)\

中间目录: \$(SolutionDir)bin-int\\$(Configuration)-\$(Platform)\\$(ProjectName)\

完成基础配置并链接dl与exe后

测试一:
```cpp
#pragma once

namespace Ayana {

	__declspec(dllexport) void Print();

}
```
```cpp
#include "Test.h"
#include <stdio.h>

namespace Ayana {

	void Print()
	{
		printf("Hello Ayana!");
	}

}
```
```
已启动生成…
1>------ 已启动生成: 项目: Ayana, 配置: Debug x64 ------
1>Test.cpp
1>  正在创建库 G:\VS\Ayana\bin\Debug-x64\Ayana\Ayana.lib 和对象 G:\VS\Ayana\bin\Debug-x64\Ayana\Ayana.exp
1>Ayana.vcxproj -> G:\VS\Ayana\bin\Debug-x64\Ayana\Ayana.dll
========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```
测试二
```cpp

namespace Ayana {

	__declspec(dllimport) void Print();

}


void main()
{
	Ayana::Print();
}
```
```
Hello Ayana!
G:\VS\Ayana\bin\Debug-x64\Sandbox\Sandbox.exe (进程 15832)已退出，代码为 0。
要在调试停止时自动关闭控制台，请启用“工具”->“选项”->“调试”->“调试停止时自动关闭控制台”。
按任意键关闭此窗口. . .
```

好诶，环境准备完毕！~

## 入口点

>创建宏，控制导入和导出

>完成基本的入口点，并且将入口移动到了引擎内部并进行了适当的处理

>推到github上，并通过.gitignore忽略部分文件

```cpp
//根据building的DLL文件决定导入或导出
#ifdef AY_PLATFORM_WINDOWS
	#ifdef AY_BUILD_DLL
		#define AYANA_API __declspec(dllexport)
	#else
		#define AYANA_API __declspec(dllimport)
	#endif // AY_BUILD_DLL
#else
	#error Ayana only support windows!
#endif
```
```c
git reset
git add *
git status
//确认无误后提交设置
git commit -m "Setup basic Application and Entry Point."
//结果
G:\VS\Ayana>git commit -m "Setup basic Application and Entry Point."
[main 43e7b11] Setup basic Application and Entry Point.
 12 files changed, 385 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 Ayana.sln
 create mode 100644 Ayana/Ayana.vcxproj
 create mode 100644 Ayana/Ayana.vcxproj.filters
 create mode 100644 Ayana/src/Ayana.h
 create mode 100644 Ayana/src/Ayana/Application.cpp
 create mode 100644 Ayana/src/Ayana/Application.h
 create mode 100644 Ayana/src/Ayana/Core.h
 create mode 100644 Ayana/src/Ayana/EntryPoint.h
 create mode 100644 Sandbox/Sandbox.vcxproj
 create mode 100644 Sandbox/Sandbox.vcxproj.filters
 create mode 100644 Sandbox/src/SandboxApp.cpp
 //OK，没问题，推过去
 git push origin master
```
>*错误记录1*
>```
>error: src refspec master does not match any.
>error: failed to push some refs to 
>```
>*原因：
1.本地git仓库目录下为空;
2.本地仓库add后未commit;
3.git init错误;
用命令 git add + 文件名，把文件添加到仓库就行 ，然后正常push*

>*错误记录2*
>```
>remote: Invalid username or password. fatal: Authentication failed for 'https://github.com/myq0721/Ayana.git/'
>```
>*原因：长时间未上传过远程仓库或者存在多个远程仓库。
解决方案：
需要获取一个新的 token*

--02/21

## 添加日志功能

>通过SPD log格式化不同的类型

>输出信息，错误（红色，警告（黄色等

>通过宏使得更容易编辑，还可以使代码剥离出来

需要打印文本，数字，字符，对象，指针等，所以调用SPD log支持

https://github.com/gabime/spdlog

```
git submodule add https://github.com/gabime/spdlog.git Ayana/vendor/spdlog
```
然后添加到c++/常规/附加包含目录中即可
>*错误记录1：*
>```
>	s_CoreLogger = spdlog::stdout_color_mt("AYANA");
>```
>错误(活动)	E0135	namespace "spdlog" 没有成员 "stdout_color_mt"	Ayana	G:\VS\Ayana\Ayana\src\Ayana\Log.cpp	11	
>
>*在查阅github上的示例后，发现需添加*
>```
>#include "spdlog/sinks/stdout_color_sinks.h"
>```
> </br>
</br>


>*错误记录2：完成后发现Ayana可以成功编译，Sandbox找不到文件*
>```
>atal error C1083: 无法打开包括文件: “spdlog/spdlog.h”: No such file or directory
>```
>*找了半天，原因是属性中c++的附加包含目录，最后一项不慎加了分号，真是傻呗设计*
></br>
</br>

## Premake

>调用premake

迄今为止构建工具为windows的VisualStudio，当我们需要添加其他平台时，我们需要为我们的引擎实际生成项目文件，与工具集一起使用为我们编译这些应用程序，比如生成Xcode项目文件以便在mac上构建我们的引擎。

不使用过于复杂的Cmake，它在很多事情上使用自己的形式，以至于很难处理而且不必要

所以我们选用这个

https://github.com/premake/premake-core.git

参考premake的wiki，使用 lua 完成 Ayana 和 Sandbox 的结构配置
```lua
workspace "Ayana" --解决方案名称
    architecture "x86_64" --编译平台 只编64位--(x86,x86_64,ARM)

    configurations 
    {
        "Debug",
        "Release",
        "Dist"
    }
--临时变量 定义 输出目录
--详细的所有支持的tokens 可参考 
outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

project "Ayana" --项目名称
    location "Ayana" --相对路径
    kind "SharedLib" --表明该项目是dll动态库
    language "c++"

    targetdir ("bin/" .. outputdir .. "/%{prj.name}")--输出目录
    objdir ("bin-int/" .. outputdir .. "/%{prj.name}")--中间临时文件的目录

    files--该项目的文件
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp"
    }

    includedirs--附加包含目录
    {
        "%{prj.name}/vendor/spdlog/include"
    }

    filter "system:windows"--windows平台的配置
        cppdialect "c++17"
        staticruntime "On"
        systemversion "latest"

        defines --预编译宏
        {
            "AY_BUILD_DLL",
            "AY_PLATFORM_WINDOWS",
            "_WINDLL",
            "_UNICODE",
            "UNICODE",
        }

        postbuildcommands -- build后的自定义命令
        {
            ("{COPY} %{cfg.buildtarget.relpath} ../bin/" .. outputdir .. "/Sandbox") --拷贝引擎dll库到sanbox.exe的同一目录下去
        }

    filter "configurations:Debug"
        defines "AY_DEBUG"
        runtime "Debug"
        symbols "on"

    filter "configurations:Release"
        defines "AY_RELEASE"
        runtime "Release"
        optimize "on"

    filter "configurations:Dist"
        defines "AY_DIST"
        runtime "Release"
        optimize "on"

project "Sandbox"
    location "Sandbox"
    kind "ConsoleApp"
    language "c++"

    targetdir ("bin/" .. outputdir .. "/%{prj.name}")
    objdir ("bin-int/" .. outputdir .. "/%{prj.name}")

    files
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp"
    }

    includedirs
    {
        "Ayana/vendor/spdlog/include",
        "Ayana/src"
    }

    links
    {
        "Ayana"
    }

    filter "system:windows"
        cppdialect "c++17"
        staticruntime "On"
        systemversion "latest"

        defines
        {
            "AY_PLATFORM_WINDOWS",
            "_UNICODE",
            "UNICODE",
        }

    filter "configurations:Debug"
        defines "AY_DEBUG"
        runtime "Debug"
        symbols "on"

    filter "configurations:Release"
        defines "AY_RELEASE"
        runtime "Release"
        optimize "on"

    filter "configurations:Dist"
        defines "AY_DIST"
        runtime "Release"
        optimize "on"

```

完成后删除文件夹中编译的 bin 和 bin-int 文件夹。

然后即可重新生成解决方案
```
G:\VS\Ayana>vendor\bin\premake\premake5.exe vs2017
Building configurations...
Running action 'vs2017'...
Done (11ms).
```
简直又快又好.

通过bat自动执行

```bat
call vendor\bin\premake\premake5.exe vs2017
PAUSE
```
```
G:\VS\Ayana>PAUSE
请按任意键继续. . .
```
OK

>*错误记录*
></br>
>再调试时发生
>```
>无法解析的外部符号 "private: static class std::shared_ptr<class spdlog::logger> Ayana::Log::s_CoreLogger"
>```
>莫名其妙就好了，至今不清楚确切原因(摊手)
>
></br>

</br>

## 事件系统

创建事件系统以处理窗口事件，输入事件等

我们现在有一个应用程序，即我们的Application class，它就像我们游戏引擎的中心。
为了能够接收事件，我们把它分配到一个层上去，应用程序最终会将事件发送给这个层。

我们需要某种事件类，然后需要将数据发送回Application,所以我们给Application提供一个回调窗口。

本质上当我们从应用程序创建一个窗口时，我们还将设置对窗口类的回调，这样每次窗口得到一个事件，它可以检车回调是否正确。如果回调不为空，它将用这个事件的数据调用回调。

然后应用程序会有一个在事件上调用的函数，接收事件引用等，它将从窗口调用这个函数，也就是窗口实际上并不知道应用程序。

事件系统是相当多的代码。。。

---

稍微咕一段时间-0225

</br></br>

# 第一部分（02/08

开了天坑了（悲）

## 架构

### 一、底层与第三方包

#### [openGL](https://www.opengl.org/)

[LearnOpenGL_CN](https://learnopengl-cn.github.io/#_1)

#### [PhysX](https://developer.nvidia.cn/zh-cn/physx-sdk)

[PhysX4.1documentation](PhysX/4.1/documentation)

#### [boost](https://www.boost.org/)

[Boost Library Documentation](https://www.boost.org/doc/libs/)

[速查手册](https://github.com/wuye9036/BoostLibrariesCheetsheetChn)

[中文教程](https://www.cnblogs.com/lidabo/p/9294874.html)

#### [STL/STLPort](https://learn.microsoft.com/zh-cn/cpp/standard-library/cpp-standard-library-reference?view=msvc-170)

[c语言中文网](http://c.biancheng.net/stl/)

#### Kynapse(AI)

#### Euphoria（动画）

#### other

### 二、平台独立层

#### 平台检测
```cpp
#if defined(WIN32)

// Win32 Platform
#include "Win32Window.h"
#include "Win32FileSystem.h"
#include "Win32Timer.h"
```
#### 原子数据类型

数据类型和平台、编译器相关，但基本不涉及平台相关函数，对原子数据类型的确定，主要通过对平台特定数据类型使用typedef进行类型定义。

```cpp
typedef unsigned int uint32;	// 4B
typedef unsigned short uint16;	// 2B
typedef unsigned char uint8;	// 1B
typedef int int32;		// 4B
typedef short int16;		// 2B
typedef char int8;		// 1B

//MSVC
typedef unsigned __int64 uint64;	// 8B
typedef __int64 int64;			// 8B

//其它编译器
typedef unsigned long long uint64;	// 8B
typedef long long int64;		// 8B
```
*此外，与数据相关的问题还包括大小端: 大小端一般与处理器采用的架构相关。 Intel x86, MOS Technology 6502, Z80, VAX, PDP-11都是小端模式(Little Endian)。 Motorola 6800, Motorola 68000, PowerPC 970, System/370, SPARC(除V9外)为大端模式(Big Endian)。 ARM, PowerPC(除PowerPC 970外), DEC Alpha, SPARC V9, MIPS, PA-RISC, IA64的字节序是可配置的。*

#### 高分辨率时钟

时钟作为一个游戏引擎最基本的模块，在很多方面都会使用到，如FPS统计，游戏时间线，物理系统等。 时钟模块的主要作用是获取当前时间。 C语言的time.h库提供了一些基本的时间获取函数，如下。
```cpp
// 从 1970-01-01 00:00:00 GMT 以来消逝的秒数
time_t seconds = time(NULL);

// 获取时分秒结构
struct tm* Current = localtime(&seconds);

// 从程序启动到 clock() 调用，所消耗的CPU时间
clock_t ticks = clock();

// 转换成秒
long ElapsedSecond = ticks / CLOCKS_PER_SEC;
```

上面这些函数只能提供秒级精度，对于一些对时间要求不高的程序，直接使用这些函数就好。 但对游戏引擎而言，秒级精度是不够的，最少需要毫秒级精度。因此就需要使用到与平台相关的一些函数。

```cpp
Win32

// 包含 windows.h
static LARGE_INTEGER m_StartTime;
static LONGLONG m_LastTime;
static DWORD m_StartTick;

void init()
{
    QueryPerformanceFrequency(&m_StartTime);
    m_StartTick = GetTickCount();
    m_LastTime = 0;
}
// 参考 OGRE getMilliseconds， 获取毫秒
unsigned long getMilliseconds()
{
    LARGE_INTEGER frequency;
    QueryPerformanceFrequency(&frequency);

    LARGE_INTEGER endTime;
    QueryPerformanceCounter(&endTime);

    LONGLONG TimeOffset = endTime.QuadPart - m_StartTime.QuadPart;

    // 毫秒：* 1000， 微秒：* 1000000
    unsigned long Ticks = (unsigned long)(1000 * TimeOffset / frequency.QuadPart);

    unsigned long check = GetTickCount() - m_StartTick;
    signed long msecOff = (signed long)(Ticks - check);
    if (msecOff < -100 || msecOff > 100)
    {
        LONGLONG adjust = (std::min)(msecOff * frequency.QuadPart / 1000, TimeOffset - m_LastTime);
        m_StartTime.QuadPart += adjust;
        TimeOffset -= adjust;

        Ticks = (unsigned long)(1000 * TimeOffset / frequency.QuadPart);
    }

    m_LastTime = TimeOffset;

    return Ticks;
}
```
```cpp
Unix/Linux

// 包含 sys/time.h
static struct timeval m_StartTime;

void init()
{
    gettimeofday(&m_StartTime, NULL);
}

unsigned long getMilliseconds()
{
    struct timeval endTime;
    gettimeofday(&endTime, NULL);

    // timeval 由 tv_sec(秒)， tv_usec(微秒) 共同组成
    unsigned long elapsedTime = (endTime.tv_sec - m_StartTime.tv_sec) * 1000;
    elapsedTime += (endTime.tv_usec - m_StartTime.tv_usec) / 1000;

    return elapsedTime;
}
```
#### 文件

游戏引擎的一个重要的功能就是资源管理，而文件系统则是资源管理的基石。 文件系统的主要作用是管理文件、文件夹，必须实现文件的存取，目录的创建、删除、读取等。

1、文件

关于文件的存取，既可以使用C中的FILE相关操作函数，也可以使用C++中的文件流对象。 当然各个操作系统也都提供了对应的用于文件操作的API。
```cpp
Win32

// #include<windows.h>
HANDLE WINAPI CreateFile(
  _In_      LPCTSTR lpFileName,
  _In_      DWORD dwDesiredAccess,
  _In_      DWORD dwShareMode,
  _In_opt_  LPSECURITY_ATTRIBUTES lpSecurityAttributes,
  _In_      DWORD dwCreationDisposition,
  _In_      DWORD dwFlagsAndAttributes,
  _In_opt_  HANDLE hTemplateFile
);
```
```cpp
Unix/Linux

//#include <fcntl.h>
int open(const char *path, int flags, mode_t mode);
```

2、目录(文件夹)

Linux和Windows中都有dirent.h这个头文件，但是里面定义的函数却是不相同的。 Linux中的dirent.h提供的函数能打开目录，关闭目录，遍历目录文件。 而Windows中的dirent.h只提供了创建目录、删除目录、进入目录，已经获取当前路径等功能，并没有提供遍历目录文件的功能。 Windows中遍历目录文件的函数在io.h中。
```cpp
Win32

// dirent.h
int chdir(const char* path);
int mkdir(const char* path);
int rmdir(const char* path);
char* getcwd(char* buf, int buffsize);

// io.h
intptr_t _findfirst(const char *pattern, struct _finddata_t *data);
int _findnext(intptr_t id, struct _finddata_t *data);
int _findclose(intptr_t id);
```
在fileapi.h文件中，定义了Windows关于文件和目录操作的API。
```cpp
Unix/Linux

// dirent.h
DIR * opendir(const char *filename);
struct dirent * readdir(DIR *dirp);
int closedir(DIR *dirp);
```
OGRE的文件系统 在OGRE中，对于Win32平台，使用的是dirent.h和io.h中提供的函数_findfirst、_findnext、_findclose。 对于Unix/Linux平台，则通过dirent.h中的opendir、readdir、closedir实现了上面3个函数。

#### 窗口

应用程序对于窗口的操作，主要集中在创建、删除窗口，查询、设置属性等。除此之外，还要管理绘图上下文。 与窗口相关的还有窗口的事件处理，如何让使用者也能接收到事件也是必须要考虑的问题。
```cpp
Win32

// windows.h

// 注册窗口类
WNDCLASS wndClass;
RegisterClass(&wndclass);

//创建窗口
HWND hwnd = CreateWindow("WndClassName", "WindowName", WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, NULL, NULL, hInstance, NULL);

// 显示（隐藏）窗口
ShowWindow(hwnd, SW_SHOW); // ShowWindow(hwnd, SW_HIDE);

// 获取窗口尺寸
GetWindowRect(hwnd, &rect);

// 获取客户区域尺寸
GetClientRect(hwnd, &rect);
```

Linux 关于Linux上的窗口系统，可以参考《关于X11》这篇文章。
Linux相关*https://juejin.cn/post/7006357005954711588
https://blog.csdn.net/weixin_43833642/article/details/105341872
https://blog.csdn.net/tq384998430/article/details/100707619*

#### 设备IO

对于大部分应用程序而言，其输出设备主要是显示器、音箱（或耳机），输入设备则种类较多：键盘、鼠标、游戏杆、游戏手柄、摄像头、麦克风等。一个典型的跨平台的人机接口函数库如OIS（Object Oriented Input System，面向对象输入系统）。

#### 实现细节

在使用特定语言具体实现一个平台独立层，有很多细节部分需要考虑。

函数返回值

参考Win32的API设计，可以发现大部分函数都用HRESULT作为返回值类型，并且定义了若干个宏来表示函数运行状态。如:

S_OK代表运行正常，

E_FAIL代表未知错误，

E_OUTOFMEMORY代表内存不足，

E_INVALIDARG代表非法参数。 

在winerror.h中有HRESULT与相关错误代码的定义，HRESULT本质上是一个4字节值，所以我们在非Win32平台下，可以定义自己的HRESULT类型。

```cpp
#if !defined(_WIN32) && !defined(PLATFORM_HRESULT_DEFINE) \
    && !defined(_HRESULT_DEFINED) && !defined(__midl)
#define PLATFORM_HRESULT_DEFINE

// 定义4字节整形
typedef long int32;

// 定义 HRESULT 类型
typedef long HRESULT;

/*
  还可以参照winerror.h定义一些工具宏，以及常用错误代码
  如  MAKE_HRESULT
      SUCCEEDED
      FAILED
*/

#endif
```

指针的处理

当一个封装好的库需要向使用者提供指针的时候，必须得考虑指针所指对象的生命周期的管理。 一个简单的办法是使用智能指针，在最新的C++11中，已包括了智能指针，其他也有很多库都提供了智能指针的实现，比如Boost。 另一个办法是定义一套使用规则，保证通过Create返回的指针，使用完之后，必须调用Release，即手动管理生命周期。

### 三、核心系统

断言：gsl::assert

[Guidelines Support Library](https://github.com/Microsoft/GSL)是C++官方的辅助库，有Expects和Ensures分别检测pre-condition和post-condition。是assert的更好替代，推荐使用。

单元测试：boost::test。

内存分配：c++默认分配器

注意我们没有使用高性能的tbb、tcmalloc等分配器。原因有两点：

减少依赖。依赖第三方内存分配器，容易引入更多的bug，使得程序更难调试，我们不太希望有意外的惊喜。性能对我们这种没人用的引擎，没有那么重要，哈哈哈。
内存预分配。我们会尽量预先分配好内存，这样分配器性能就没有那么重要了。

数学库：[eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page)[简单介绍](https://zhuanlan.zhihu.com/p/87598519)

eigen是一款非常好的跨平台数学库，无论是易用性、工程性、性能、功能、扩展能力、跨平台性都是顶尖的。被广泛运用到PCL、OpenCV、Meshlab等优秀的类库中，是久经考验的一款数学库。eigen是我们的核心依赖，会用到Dense、Geometry、Spline等功能。

字符串与散列字符串标识符：

std::string，std::string_view，boost::algorithm::string，boost::flyweight

std::string虽然饱受诟病，不过配合boost::algorithm还是可以一战的。flyweight能方便的制作string的handle，减少内存分配，有跨dll能力，也许会用到。

调试用打印和日志：boost::log

这里的问题是boost::log必须启用rtti，但引擎的runtime又不会开启rtti，所以就暂时就不打log了。这里就体现c++为什么需要zero-overhead abstraction了，功能有传染性的话，那就只有不用了。

本地化服务：std::locale，std::codecvt

c++的locale和codecvt是两朵巨大的奇葩，标准变了又变，我现在已经混乱了。等c++20引入了char8_t再说吧，先不解决locale问题了。

引擎配置：boost::property_tree，boost::program_option

一个读写配置、一个读写控制行命令，很省事。现在用的不多。

随机数生成器：std::random，boost::random

都可以用，速度一般。

曲线与曲面库：unsupported.Eigen.Spline

对象句柄/唯一标识符：boost::uuid

uuid就是一般的guid，我们的资源索引基本会用uuid描述。资源模块之后的章节会介绍。

异步文件io：std::filesystem，std::iostream，boost::asio

这三个加起来，可以解决异步文件io的问题，就是需要一点开发。

场景图/剔除优化

空间剖分：boost::geometry::index::rtree

空间索引，暂时不用开发octree/bvh，不用开发的功能就是好的功能！

以上这些模块，官方文档又全又好。

平台独立层和核心系统是不需要开发的，削减了一小半的工作量。这让我们可以把精力集中到资源和渲染器上。

### *代码编译

#### [vcpkg](https://github.com/Microsoft/vcpkg)

https://zhuanlan.zhihu.com/p/88956340

#### CMake

### 四、资源管理系统

### 五、主要功能系统

#### 低阶渲染器

#### 场景图与剔除优化

#### /后期效果

#### 碰撞与物理

#### 骨骼动画

### 六、前端与工具链

</br></br>

---
*参考资料*

*《游戏引擎架构》*

*《游戏引擎原理与应用》*

*《数字图像处理第四版》*

*[GAMES101-现代计算机图形学入门-闫令琪](https://www.bilibili.com/video/BV1X7411F744/?vd_source=b0edc91d595b72577053303a4da8a361)</br>[GAMEs101笔记](https://www.notion.so/GAMES101-b0e27c856cde429b8672671a54c34817)*

*[GAMES104-现代游戏引擎：从入门到实践](https://www.bilibili.com/video/BV1oU4y1R7Km/)</br>[104笔记](https://www.zhihu.com/people/whys0far/columns)*

*https://www.youtube.com/playlist?list=PLlrATfBNZ98foTJPJ_Ev03o2oq3-GGOS2
https://www.youtube.com/playlist?list=PLlrATfBNZ98dC-V-N3m0Go4deliWHPFwT
https://www.zhihu.com/column/starengine
https://zhuanlan.zhihu.com/p/30538626*

