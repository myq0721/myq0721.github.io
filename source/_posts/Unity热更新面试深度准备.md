---
title: Unity热更新面试深度准备
date: 2026-05-28 12:00:00
categories: 秋招
tags:
  - Unity
---

# Unity热更新面试深度准备

## 一、AssetBundle打包策略

### 你的回答框架(结合《疯狂蹦床》项目):

**开场白:**
"在《疯狂蹦床》项目中,我们采用了混合打包策略,核心原则是**按更新频率和依赖关系分组**。"

### 具体策略(选2-3个详细说):

#### 1. 按功能模块划分(主策略)
```
UI模块
├── Common UI (通用按钮、弹窗) → common_ui.ab
├── Main UI (主界面) → main_ui.ab
└── Battle UI (战斗界面) → battle_ui.ab

角色模块
├── Player (玩家) → player.ab
├── NPC → npc.ab

场景模块
├── Scene_Level1 → level1.ab
├── Scene_Level2 → level2.ab
```

**为什么这样分?**
- **独立更新**: 修复UI bug不需要重新下载角色资源
- **按需加载**: 进入关卡才下载对应场景包
- **减少冗余**: 共享资源单独打包(见下一条)

#### 2. 共享资源单独打包(重要!)
```
Shared
├── common_textures.ab (UI通用图集)
├── common_materials.ab (共享材质)
├── common_prefabs.ab (通用特效、音效)
└── shaders.ab (所有Shader)
```

**核心逻辑:**
"我们用AssetDatabase.GetDependencies分析依赖,如果一个资源被3个以上Bundle引用,就提取到Shared包中,避免重复打包。"

**数据支撑(重要):**
"这个优化让首包体积从500MB降到350MB,因为同一个粒子特效之前在5个场景包里各有一份。"

#### 3. 按更新频率分级(进阶)
```
热更新频率:
├── Hot (1-2周更新) - 活动资源、临时玩法
├── Normal (1-2月更新) - 常规关卡、角色
└── Stable (基本不变) - 核心框架、Shader
```

**实际案例:**
"节日活动的UI和特效打成hot_event.ab,活动结束后可以单独删除,不影响其他资源。"

### 避坑指南(加分项):

**问题1: 循环依赖**
"遇到过A场景引用B预制体,B预制体又引用A的材质,导致打包失败。解决办法是建立AssetImporter后处理脚本,自动检测循环依赖并警告。"

**问题2: 图集打包**
"UI Sprite如果单独打包会炸成几百个小文件,我们用Unity的SpriteAtlas,一个图集对应一个ab包,减少了80%的Bundle数量。"

---

## 二、资源依赖关系管理

### 核心问题: 如何保证加载顺序?

#### 你的方案(准备画图):

```
依赖链示例:
battle_ui.ab
    ↓ 依赖
common_ui.ab
    ↓ 依赖
common_textures.ab
```

### 实现方式:

#### 1. 依赖清单生成(打包时)
```csharp
// 打包时生成依赖配置
public class BundleBuildPipeline
{
    [MenuItem("Tools/Build AssetBundles")]
    static void BuildBundles()
    {
        // 打包
        AssetBundleManifest manifest = BuildPipeline.BuildAssetBundles(
            outputPath, 
            BuildAssetBundleOptions.None, 
            BuildTarget.Android
        );
        
        // 解析依赖关系
        Dictionary<string, string[]> dependencies = new Dictionary<string, string[]>();
        foreach (string bundleName in manifest.GetAllAssetBundles())
        {
            dependencies[bundleName] = manifest.GetAllDependencies(bundleName);
        }
        
        // 序列化成JSON
        File.WriteAllText("DependencyConfig.json", JsonUtility.ToJson(dependencies));
    }
}
```

#### 2. 运行时加载管理
```csharp
// 递归加载依赖
public class AssetBundleManager
{
    private Dictionary<string, AssetBundle> loadedBundles = new Dictionary<string, AssetBundle>();
    private DependencyConfig config; // 从JSON读取
    
    public IEnumerator LoadAssetBundleAsync(string bundleName)
    {
        // 先加载依赖
        string[] dependencies = config.GetDependencies(bundleName);
        foreach (string dep in dependencies)
        {
            if (!loadedBundles.ContainsKey(dep))
            {
                yield return LoadAssetBundleAsync(dep); // 递归加载
            }
        }
        
        // 再加载自己
        if (!loadedBundles.ContainsKey(bundleName))
        {
            AssetBundleCreateRequest request = AssetBundle.LoadFromFileAsync(bundleName);
            yield return request;
            loadedBundles[bundleName] = request.assetBundle;
        }
    }
}
```

### 关键优化点(面试官会问):

**Q: 依赖链太深怎么办?**
"设置依赖深度限制为3层,超过的通过重构资源结构解决。比如把多层嵌套的Prefab拍平,直接引用底层资源。"

**Q: 卸载时如何处理依赖?**
"用引用计数,每个Bundle记录被几个其他Bundle依赖,计数为0才真正Unload。"

```csharp
class BundleReference
{
    public AssetBundle bundle;
    public int refCount;
    
    public void AddRef() => refCount++;
    public void Release()
    {
        if (--refCount <= 0)
        {
            bundle.Unload(false); // 卸载Bundle但保留已加载的Asset
        }
    }
}
```

---

## 三、热更新版本控制方案

### 你的方案(结合实际项目):

#### 1. 版本号体系
```
版本格式: Major.Minor.Patch.Hotfix
示例: 1.2.3.005

Major: 大版本(需要重新下载完整包)
Minor: 功能更新(热更新资源+代码)
Patch: Bug修复(热更新代码)
Hotfix: 紧急修复(单个资源替换)
```

#### 2. 服务器文件结构
```
CDN目录:
/AssetBundles/
    /1.2.3/
        ├── version.json (版本清单)
        ├── battle_ui.ab (MD5: abc123)
        ├── player.ab (MD5: def456)
        └── ...
    /1.2.4/
        └── ... (增量文件)
```

#### 3. 版本清单(version.json)
```json
{
    "version": "1.2.4.001",
    "minSupportVersion": "1.2.0.000",
    "files": [
        {
            "name": "battle_ui.ab",
            "size": 2048576,
            "md5": "a1b2c3d4e5f6",
            "url": "http://cdn.com/1.2.4/battle_ui.ab"
        },
        {
            "name": "player.ab",
            "size": 5242880,
            "md5": "f6e5d4c3b2a1",
            "url": "http://cdn.com/1.2.4/player.ab"
        }
    ]
}
```

#### 4. 更新流程(画流程图)
```
启动游戏
    ↓
请求version.json
    ↓
对比本地版本
    ↓
计算需要下载的文件(MD5对比)
    ↓
下载增量包
    ↓
校验MD5
    ↓
替换旧文件
    ↓
重启游戏/热加载
```

### 核心代码思路:
```csharp
public class HotfixManager
{
    private string localVersion;
    private VersionManifest serverManifest;
    
    public IEnumerator CheckUpdate()
    {
        // 1. 获取服务器版本信息
        UnityWebRequest request = UnityWebRequest.Get(serverUrl + "/version.json");
        yield return request.SendWebRequest();
        serverManifest = JsonUtility.FromJson<VersionManifest>(request.downloadHandler.text);
        
        // 2. 对比版本
        if (CompareVersion(serverManifest.version, localVersion) > 0)
        {
            // 3. 计算差异文件
            List<FileInfo> needDownload = new List<FileInfo>();
            foreach (var file in serverManifest.files)
            {
                string localMD5 = GetLocalFileMD5(file.name);
                if (localMD5 != file.md5)
                {
                    needDownload.Add(file);
                }
            }
            
            // 4. 下载并校验
            foreach (var file in needDownload)
            {
                yield return DownloadFile(file);
                if (!VerifyMD5(file))
                {
                    Debug.LogError($"文件校验失败: {file.name}");
                    yield break;
                }
            }
            
            // 5. 更新本地版本号
            SaveLocalVersion(serverManifest.version);
        }
    }
}
```

### 异常处理(加分):
"实际项目中还做了:
- **断点续传**: 大文件分片下载,失败后从断点继续
- **重试机制**: 下载失败自动重试3次
- **回滚方案**: 保留上一版本文件,更新失败可回滚
- **灰度发布**: version.json支持A/B测试,部分用户先更新"

---

## 四、Lua与C#通信及性能瓶颈

### 通信方式(xLua框架):

#### 1. C#调用Lua(常用)
```csharp
// C# 端
LuaEnv luaEnv = new LuaEnv();
luaEnv.DoString("require 'main'"); // 加载Lua脚本

// 调用Lua全局函数
LuaFunction func = luaEnv.Global.Get<LuaFunction>("OnPlayerAttack");
func.Call(playerID, damage);

// 获取Lua Table
LuaTable config = luaEnv.Global.Get<LuaTable>("WeaponConfig");
int attackPower = config.Get<int>("attackPower");
```

#### 2. Lua调用C#(常用)
```lua
-- Lua 端
CS.UnityEngine.Debug.Log("Hello from Lua")

-- 调用自定义C#类
local player = CS.GameLogic.Player.GetInstance()
player:Attack(100)

-- 访问C#静态方法
local time = CS.UnityEngine.Time.time
```

#### 3. 委托/事件绑定(重要)
```csharp
// C# 定义事件
public class GameEventManager
{
    [CSharpCallLua] // xLua标记
    public delegate void OnEnemyDeadDelegate(int enemyID);
    public static OnEnemyDeadDelegate OnEnemyDead;
}

// Lua 监听事件
CS.GameEventManager.OnEnemyDead = function(enemyID)
    print("Enemy died: " .. enemyID)
    -- 更新UI、播放音效等
end
```

### 性能瓶颈分