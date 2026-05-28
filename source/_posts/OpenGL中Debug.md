---
title: OpenGL中Debug
date: 2023-02-14 23:12:18
categories: 图形与渲染
---
### glGetError

兼容所有版本，使用方法简单

调用后只返回一个任意的错误标志，所以要循环调用，而且使用麻烦，要在所有要检查的前后分别打上下面两段代码ww

```cpp
static void GLClearError()//查错
{
	while (glGetError() != GL_NO_ERROR);
}

static void GLCheckError()//输出错误信息
{
	while (GLenum error =  glGetError())
	{
		std::cout << "[OpenGL Error!](" << error << ")" << std::endl;
	}
}
```
且OpenGl用十六进制定义了他所有的错误码，需要把拿到的错误码转换成十六进制，然后去glew头文件里搜



</br>
断言改进版
</br>

```cpp
#define ASSERT(x) if(!(x)) __debugbreak();

static void GLClearError()//查错
{
	while (glGetError() != GL_NO_ERROR);
}

static bool GLLogCall()
{
	while (GLenum error =  glGetError())
	{
		std::cout << "[OpenGL Error!](" << error << ")" << std::endl;
		return false;
	}
	return true;
}
```

### 4.3之后，glMessageCallback

允许我们指定一个指向OpenGL的函数指针，OpenGL会调用我们的那个函数

比glGetError好用多了awa~，不需要一直问（

错误信息也比glGetError详细