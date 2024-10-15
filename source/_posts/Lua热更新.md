---
title: Lua运行时热更新的实现
date: 2024-07-31 23:12:18
tags: 热更新
catagories : 秋招
---
### 前言

常见的Lua热更新都是在客户端下载所有Lua代码之后重启游戏，以实现重载所有数据和函数的目的。但在实际开发过程中，如果每次都要改完Lua代码重启游戏，正常人都不能接受。
除这种热更方式之外，其实还可以实现运行时热更，或者叫无感知热更。可以做到在玩家运行游戏的时候偷偷更新一部分代码。

很多项目会将只负责处理界面的View层Lua代码在每次调用时重新读取，以此实现不重启地更新代码。但这样依然有局限性——如果需要在数据层等其他模块修改函数，这些修改都无法生效。因为如果直接require，旧的数据都会丢失。

要实现比较合理的运行时热更新，除了设计热更的逻辑之外，前提是遵循一些约定。在规定热更新约定之前，先了解一下Lua热更新涉及的原理。

### 热更新原理
#### require机制
从 Lua 5.1 开始，Lua 加入了标准的模块管理机制，可以把一些公用的代码放在一个文件里，以 API 接口的形式在其他地方调用，有利于代码的重用和降低代码耦合度。

Lua 的模块是由变量、函数等已知元素组成的 table，因此创建一个模块很简单，就是创建一个 table，然后把需要导出的常量、函数放入其中，最后返回这个 table 就行。

以下为创建自定义模块 exmaple.lua，文件代码格式如下：
```lua
exmaple = {}

exmaple.constant = "constant variable"

function exmaple.func1()
    print("public func")
end

local function func2()
    print("private func")
end

function exmaple.func3()
    func2() 
end

return exmaple
```

在其他模块中，需要调用exmaple.lua模块的函数，则需要require
```lua
require("exmaple")
```
或者
```lua
require "exmaple"
```
require之后，Lua的package.loaded中就会有exmaple.lua模块的数据，并且只有第一次require会执行exmaple.lua中的内容，之后再次require就会直接返回package.loaded["exmaple"]。

这样的话，如果想要更新exmaple.lua的内容，就需要先清空package.loaded["exmaple"]再require。
```lua
package.loaded["example"] = nil
require("example")
```
似乎这样就实现了简单的热更，但这远远不够。因为清空package.loaded["exmaple"]会导致丢失原有的数据，下面是一个简单的例子：
```lua
local t = {}
t.data = 0
function t.func()
    print(t.data)
end
return t
```
如果按照上面的方式热更，每次t.data都会被重置为0，显然这不是我们想要的。

这种情况下，t.data作为函数t.func的upvalue（外部局部变量）会被重置。

upvalue
上面讲到的就是upvalue的例子，在游戏运行时，我们不会希望数据被覆盖或清空，应该尽量在保留原有数据的情况下替换函数的逻辑。

1
2
3
4
5
6
local count = 0
local function func()
	count = count + 1
	print(count)
end
return func
在上面这个例子中，如果使用require机制热更代码，我们需要保存旧函数的count值。Lua中提供了获取并设置upvalue的方法debug.getupvalue和debug.setupvalue。

遍历一个函数的所有upvalue并设置upvalue：

1
2
3
4
5
6
7
8
9
local oldfunc = require "example"
package.loaded["example"] = nil
local newfunc = require "example"

for i = 1, math.huge do
	local name, value = debug.getupvalue(oldfunc, i)
	if not name then break end
	debug.setupvalue(newfunc, i, value)
end
要注意的是，函数同样可以作为upvalue，而我们希望使用新的函数、旧的数据。所以在遍历upvalue的时候需要判断是否为函数，如果是则要用新的覆盖。

全局语句
在require一个模块时，会重新执行其中的全局语句，这会破坏已有的代码逻辑。解决办法有两种，都比较复杂。一种是语法分析，将全局语句变成local i = {}这种，保留住这个变量，然后把旧的数据复制过来；另一种是使用临时环境表执行新模块，执行完切换成旧模块使用的环境表。

这两种方法都比较麻烦，一般需要热更的主要都是各个系统的数据层，这些数据层基本不会包含全局语句的修改，所以我们可以忽略这种情况，只进行数据层的热更新。在多数情况下可以满足需求。

热更新的约定
了解了上面的原理之后，我们要想实现简单的Lua运行时热更新，需要满足以下的约定。

不破坏原有数据
游戏运行时许多Lua系统中都保存了服务器发来的数据，或者是计算产生的一些数据，我们不希望这些数据被清空或改变。热更新的基础就是更新服务的逻辑，通常只是逻辑发生变化，但原有的值并不能被改变。

不为热更多写代码
程序员都比较懒，如果热更需要现在原有的逻辑中加入热更前后进行的操作的话，没人能接受。就像为了热更C#而改变原有的代码结构，应该尽量避免额外的负担。

只修改逻辑，而非增加
一般来说需要运行时热更的都是改动比较小的更新或者修复一些bug，这种情况下只要修改函数就可以达到目的，而没有必要新增函数。而且，新增的函数如果使用了upvalue，新增之后没法给它赋值，因为在旧的模块中不存在这个upvalue。

可以热更嵌套结构中的函数
比如table中的函数、table的metatable中的函数等。

不改变所有数据和函数的命名
显然，如果改变命名，那谁知道要更新啥呢~

实现思路
下面简单介绍实现思路。

热更模块
一般来说需要热更的话，是你修改了某个XXXModel.lua文件，这个文件在package.loaded中名为XXXSystem.XXXModel。其中XXXSystem是这个Lua模块存放的文件夹名称。

热更之前要先保存旧模块的全部数据：

1
2
3
4
5
local oldModule
if package.loaded[packageName] then
    oldModule = package.loaded[packageName]
    package.loaded[packageName] = nil
end
之后直接require新的模块，然后把新模块记录下来，遍历新模块的所有数据。总体来说，遍历的过程中，元素如果是table就保留就模块的，如果是function就用新模块的。

当然要注意，table会嵌套table和function，因此这是一个递归的过程。

还有，function要用新的，但是function的的upvalue要用旧的。

table中的metatable同样作为table处理，使用debug.getmetatable获取一个table的metatable然后进行与table一样的操作。

对于可能出现循环引用的情况，可以在更新表的时候记录已更新的table，避免重复处理死循环。

监听模块
热更可以用在编辑器下，同样可以在线上环境使用（当然要有更严格的限制）。在编辑器下热更的话，要监听本地lua文件的变化，

Unity编辑器中可以使用FileSystemWatcher来实现监听，可以把这个功能封装到一个DirectoryWatcher类里，方便监听指定的多个文件夹。

1
2
3
4
5
6
7
8
9
10
if (!Directory.Exists(dirPath)) 
	return;
var watcher = new FileSystemWatcher();
watcher.IncludeSubdirectories = true;
watcher.Path = dirPath;
watcher.NotifyFilter = NotifyFilters.LastWrite;
watcher.Filter = "*.lua";
watcher.Changed += handler;
watcher.EnableRaisingEvents = true;
watcher.InternalBufferSize = 10240;
编辑器下游戏启动时创建DirectoryWatcher监听指定文件夹，并写处理函数LuaFileOnChanged

1
var luaDirWatcher = new DirectoryWatcher(LuaConst.luaDir, new FileSystemEventHandler(LuaFileOnChanged));//监听lua文件
触发LuaFileOnChanged的时候调用对应的Lua方法重载该文件模块即可。