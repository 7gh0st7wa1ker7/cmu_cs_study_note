# Variables and Functions

`Variables` & `Functions` 解决的是：代码是如何组织的。

在实际项目中：
- 数据类型决定数据结构
- 函数决定代码结构
- 变量决定状态管理

## Variables

套用 Linux 系统中的理论，变量就是你在内存中创建了一个 `variables name` ，然后将这个 `variables name` 与另一个内存对象做了一个软链接，所以你访问这个 `variables name` 就是访问它绑定的软链接，这个软链接可以随时解除，并和不同类型的数据进行绑定。举例：

```python
config = { "port": 7890 }
a = config
b = config

# a ─┐
#    ├──► dict
# b ─┘
a["port"] = 8888 # 对应的 b、config 也会变
```

### 开发时常见的坑

#### 可变对象共享

```python
def add_user(users):
    users.append("Tom")

user_list = []
add_user(user_list) # user_list 就被改变了
```
这叫副作用（side effect），很多线上 `bug` 都是来自于这里。比如打印和本地文件写入都是副作用的展示。

## Statements vs Expressions

### Expression

`Expression` 最终会返回一个值。

```python
3 + 4 # --> 7
len("abc") # --> 3
```

### Statement

`Statement` 是计算过程的描述，动作本身。

```python
if x > 0:

for i in range(10):

def func():
```

### 为什么重要

```python
x = print("hello") # x --> None
```

显示出来的东西 ≠ 函数返回的东西，`Expression --> value, Statement --> no value`

## Functions

### 函数设计原则

一个函数只做一件事。

所以，前期的需求梳理很重要，尤其考验开发者对问题的拆解能力，类似于拼积木，产品给了你一个原型图，你需要设想构成这个圆形图需要多少块积木，以及积木的形状是什么样的，然后用这些积木拼成最终的产品。

## Built-in Functions

python 有很多内置的库，其中有很多常用的函数，比如 `len(),sum(),max(),min()` 等等，有能用的就直接用，不要自己造轮子。

### 注意

在创建变量的时候，不要覆盖内置函数。

## Module Functions

模块函数。

```python
import os
os.path.exists()
```

项目开发 80% 的代码其实是在调用模块函数。

## Variable Scope

### 局部变量

```python
def test():
    x = 100 # x 只属于 test() 函数内部

print(x) # 报错，无法访问 test() 函数内的变量
```

### 全局变量

```python
count = 0

def add():
    count += 1

add() # Error, 解析器会认为 count 是局部变量，但是在局部变量 add 中又没有找到

# 如果要在函数中修改局部变量的话，需要这样引用：
def add_g():
    global count
    count += 1
```

但是在实际项目中应该避免使用 `global` , 因为如果有多个函数都是用了的话，对于代码阅读和排错是灾难性的。--> 减少共享可变状态。不要多个方法或函数同时修改同一个数据。

## Return Statements

在实际项目中，函数返回的应该是实际的数据（`string/int/float/list/dict/tuple/set`），而不是打印数据 `print`.

`print` 函数最终输出的是 None，打印是函数内置的语句产生的副作用。

## Function Composition

大型项目的核心思想，每个函数职责单一。

```python
def get_user():
    return user

def validate_user():
    return bool

def save_user():
    return save_status

def register():
    user = get_user()
    if validate_user(user):
        save_user(user)
    return bool
```

## Helper Functions

辅助函数。当一个函数里出现多个"因为"（多个职责），你就需要确认下，当前功能的拆解是不是没有做好，是否还能进行拆分。

函数拆分还有一个好处，就是一些工具函数或者叫辅助函数是可以在项目中复用的，比如一些数据处理函数或一些数据库操作的函数，这样也能减少单个函数中的代码量。

## Recommended Functions

### Pure Function

Pure function 的概念：
- 无副作用（不影响外界）；
- 处理逻辑标准，相同的输入参数，一定返回相同的结果，便于测试；

#### 实际开发

```python
# pure function
def calculate_disk_usage(used, total):
    return used / total * 100

calculate_disk_usage(50, 100) # 永远输出 50

# no pure function
def get_disk_usage():
    return psutil.disk_usage("/")

get_disk_usage() # 可能现在 70% ，过一段时间 就是 72%
```

## Test Function

测试函数很多时候能帮助开发者自动的发现函数实现的情况是否符合预期。需要准确的话，测试的样例要尽可能的模拟现实情况。

### 实际项目

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(0.1, 0.2) == 0.3 # 就需要考虑精度和参数数据类型检测了。
    # 对的写法
    assert math.isclose(add(0.1, 02), 0.3)
```
