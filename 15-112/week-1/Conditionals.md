这整个章节其实是在讲三个核心能力：
1. 程序执行流程（Control Flow）
2. 分支设计（Branch Design）
3. 代码可读性（Code Readability）

很多例子根本不是在教语法，而是在教你：
> 什么样的条件判断更容易维护、更不容易出 Bug。

# 代码执行路径（Execution Path）

训练你脑子里建立下面的模型：
```
程序计数器
  ↓
执行路径
  ↓
条件分支
```

# 能跑不等于好代码

同一个逻辑可以有很多实现方式，一个成熟的开发者思维：代码首先给人看，其次才给机器执行。
代码要清晰明了，并简洁。

# 互斥分支

互斥逻辑用 `if-else` ，要么走 `if` ，要么走 `else` ，绝不可能同时执行。

# 区间判断

`if elif else` ，过滤从上至下，每个区间可能重复，所以要将极端例子或小区间放在上面，然后可能就永远触发不了。

# 根据状态分类

类似 `case` 。

# 简写

简单逻辑可以压缩，复杂逻辑不要压缩，这会牺牲可读性。

# 代码风格

## Negated Condition

课件：
```python
if not b:    
    print("no")
else:    
    print("yes")
```

改成：
```python
if b:    
    print("yes")
else:    
    print("no")
```

### 为什么？

因为人脑处理：`False` 特别慢。

例如：
```python
if not user.is_disabled:
```

读起来就费劲。

更好：
```python
if user.is_active:
```

## Empty if Clause

课件：
```python
if b:    
    pass
else:    
    print("no")
```

这是典型反模式。
因为：
```python
if not b:    
    print("no")
```

更直接。
老师其实是在培养：减少嵌套。

## if 套 if

课件：
```python
if b1:    
    if b2:        
        print("both")
```

改成：
```python
if b1 and b2:
```

实际上是在培养：布尔逻辑表达能力

未来你写：
```python
if user and user.is_admin and user.active:
```

会天天遇到。

# 多个 if 代替 elif

```python
if x < 5:
    print("ok")
if x < 10:
    print("ok")
if x < 15:
    print("ok")
```

实际上每个分支都会执行，这时候应该私用 `elif` ，就能只能命中一个分支。

## Arithmetic Logic

这个例子很多新人看不懂。

```python
y = ((x > 0) and 99)
```

### 为什么不好？

因为 `Python` 的：`and`返回的不是：`True or False`而是：最后计算的对象

例如：`42 and 99` 结果：`99`

虽然能工作。

但读代码的人会懵：你到底想表达什么？

所以：
```python
if x > 0:    
    y = 99
```

更清晰。

# 总结

Conditionals 章节真正不是在学 if。  而是在学：
1. 如何描述业务规则  
2. 如何设计互斥分支  
3. 如何减少嵌套  
4. 如何写出别人能看懂的条件逻辑

因为在真实项目里，绝大多数 Bug 都不是：`if` 语法写错。而是：
- 条件设计错了
- 分支遗漏了
- 边界条件没考虑
- 逻辑表达不清晰

这些才是这个章节真正想训练的能力。