# Ayanami 的部落格

> 只要微笑就好了……

这是我自己写着玩、记一记、偶尔吐槽的 **个人部落格** 仓库。  
线上地址：**https://myq0721.github.io**

不是什么正式项目文档，更像一个 **随手的笔记本 + 公开日记本**：  
学东西的时候记一笔，踩坑了写一笔，想唠两句也能发一笔。

---

## 这里大概有什么

文章多半是我自己写的 **技术向笔记**，想到哪写到哪，不追求体系完整，只求当时能看懂、以后还能翻出来。
不过入职某游戏公司之后大概率这个博客不会更新什么很有含金量的东西了，本来游戏开发者也不怎么用github不是吗（笑

常见主题包括（但不限于）：

- **图形学 / OpenGL / Shader** —— 画三角形、读外部 shader、Debug 之类
- **引擎与游戏开发** —— mini 引擎开发日志、比赛、杂谈
- **C++ / STL** —— vector、tuple、一些用法小结
- **其它零碎** —— Linux、Lua 热更新、408、日语语法、随笔牢骚……

也会混进一点 **完全不硬核** 的内容，所以别把它当成教程站；  
写对了是笔记，写偏了是当时的自己。

---

## 关于这个仓库

- 用 [Hexo](https://hexo.io/) 搭的静态站，主题是 [Matery](https://github.com/blinkfox/hexo-theme-matery)（好看、花里胡哨，我挺喜欢）。
- 源码推上 GitHub 后，由 **GitHub Actions** 自动构建并发布到 Pages。
- 首页可以挂音乐、换 banner、樱花飘一飘——纯属个人审美，和「专业博客」无关。

---

## 我自己平时怎么用（备忘）

**本地看一眼效果：**

```bash
npm install
npm run server
```

浏览器打开提示的地址（一般是 `http://localhost:4000`）。

**改完文章或配置，更新线上：**

```bash
git add .
git commit -m "随便写一句提交说明"
git push origin master
```

然后去仓库的 **Actions** 等绿色勾，过一两分钟刷新网站即可。

**新建一篇文章：**

```bash
hexo new "文章标题"
```

会在 `source/_posts/` 里生成一篇新的 Markdown，改完再按上面的流程推送。

> 小提示：首页大图在 `themes/matery/source/medias/banner/`（默认是 `0.jpg`）；  
> 站点标题、副标题等在根目录 `_config.yml`；主题里各种花活在 `themes/matery/_config.yml`。

---

## 随便看看

- 博客首页：[myq0721.github.io](https://myq0721.github.io)
- 关于我：[/about](https://myq0721.github.io/about/)
- 友链：[/friends](https://myq0721.github.io/friends/)

---

## 最后

如果你是从 GitHub 逛到这里：欢迎翻翻文章，留言随缘（评论系统我时常关着或懒得折腾）。  
祝你天天开心！

—— Ayanami / Engine Team
