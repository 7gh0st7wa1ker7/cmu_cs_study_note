# Data Types and Operators

## Builtin Types

常见内置类型：

```
int —> 1,100,234
float —> 0.1,4.23
str —> "string”.”22"
bool —> 0,False,1,True
list —> []
tuple —> ()
dict —> {}
set —> set()
NoneType
```

### 边缘情况

#### bool 是 int 的子类

```bash
True == 1 —> True
False == 0 —> True
isinstance(True, int) —> True
```

#### list，tuple ，dict，set 概念

***实际上在真实项目里，数据结构的选择直接影响：***

- 代码可读性
- 查询性能
- 内存占用
- Bug数量
- 并发安全性

#### 先建立一个核心认知

你可以把它们理解成四种完全不同的东西：


| 类型    | 本质       | 类比      | 项目中的定位         | 真实项目中的语义        |
| ----- | -------- | ------- | -------------- | --------------- |
| list  | 有序可修改集合  | 购物清单    | 一串会变化的数据       | 队列、列表、顺序数据      |
| tuple | 有序不可修改记录 | 身份证信息   | 一个固定结构的记录      | 坐标、记录、固定结构      |
| dict  | 键值映射     | 数据库记录   | 一个对象/配置/实体     | 配置、对象、JSON      |
| set   | 唯一值集合    | 白名单/黑名单 | 一个用于快速查找和去重的集合 | 白名单、黑名单、去重、快速查找 |


##### List

从 0 开始计数。

如果需要复制已有list，且与之前的list进行区分，推荐使用 `target_list.copy() or b = list(target_list)`

同一个 `list` 对象可以赋予不同的变量，这些变量最终指向的都是同一个 list 数据，所以修改其中一个变量，就会同步修改指向这个 `list` 的其他变量。

##### tuple

tuple 虽然宣称的是不会变化，但是如果 tuple 引用的对象实际是可修改的，那也是可以修改的，比如：

```
Tuple = ([1,2], [“string”, "mike”])
```

这样我们就能通过改变 list 中的数据来修改 tuple

其次，创建 tuple 的时候不能单元素，就算是单元素也建议使用 tuple = (1,) 的方式创建。

##### dict

- 使用 dict.get(“s“) 来取值和判断是否存在，更安全；
- dict key 必须
  - 可哈希
  - 不可变
  - 同层级 key 不能同名

##### set

其实 set 其实存储了一个所有元素的 hash map，所以才快且元素具有唯一性且无法放 list

### 实际项目里的选择思维

## 我需要顺序吗？

需要：

```
list
tuple
```

不需要：

```
set
dict
```

（虽然 Python 3.7+ 的 dict 保留插入顺序，但本质用途不是顺序容器）

---

## 数据会变化吗？

会：

```
list
dict
set
```

不会：

```
tuple
```

---

## 我需要 Key → Value 映射吗？

需要：

```
dict
```

---

## 我需要快速判断存在吗？

需要：

```
set
```

## Builtin Constants

重要：True，False，None

### 实际运用

None 不建议使用 == 而更建议使用 is ，因为 None 是单例对象。

## Builtin Operators

### 身份运算符

#### is & is not

经常用于 None 判断。判断是否空值。

### 成员运算符

#### in & not in

用于判断 key 是否在 list ，dict 推荐使用 get() ,然后使用上面的 None 判断条件。

## Integer Division

`//` 执行**地板除法（floor division）**，即将除法结果 ***向下取整*** 到最接近的整数（向负无穷方向取整）。

### 实际场景

分页：

```
total = 101
Page_size = 10
pages = total // page_size # —> 10 ,但是真实世界是 11 , 因为还有余数。
# 正确的方式是
import math
pages = math.ceil(total / page_size)
```

## Modulus

% 返回除法的**余数**，满足数学恒等式：`a == (a // b) * b + (a % b)`

```
# 例子 7 % -2
7 = (7 // -2) * 2 + (7 % 2) # 7 // -2 --> -3.5 --> -4
7 = (-4) * 2 + (7 % 2)
7 = -8 + (7 % 2)
7 - 8 = -1 = 7 % 2 
```

## Types Affect Semantics

类型影响语义。

在实际的项目中，对于任何不可信的输入，都应该使用 `isinstance()` 函数对输入进行校验。

## Operator Order

易错点：

```
if user.is_admin or user.is_staff and active:
# 等价于
if user.is_admin or (user.is_staff and active): # 建议使用这种表达，更易读
```

因为 `and` 优先级高于 `or` 

## Floating Point

经典误区：

```
0.1 + 0.2 = 0.3 # 实际结果 0.30000000000000000004
```

因为二进制无法精确表示浮点数。

### 实际场景

在实际场景中，尤其是金融，float 运算需要：

```
from decimal import Decimal 
price = Decimal(“0.1”) + Decimal(“0.2”)
# 但是在实际的编码中，建议使用函数，不建议使用运算符，更易读
price = add(Decimal(“0.1”), Decimal(“0.2"))
```

比较 float 的时候

```
# 不要使用
if x == 0.3:
# 建议使用
import math
math.isclose(x, 0.3)
```

## Short-Circuit Evaluation

```
False and test() # 永远为 False
True or test() # 永远为 True
```

### 实际场景

```
# 防止异常
if user and user.name # 如果 user 为 None，就不会执行后续的操作，不会中断推出
# 默认值
name = input_name or "guest” # 如果用户没有出入，就使用默认值
```

## Type vs isinstance

### 实际开发

推荐使用 isinstance() 来对类型进行判断，因为 type 无法处理继承关系

```
# 比如
isinstance(True, int) —> True
type(True) == int —> False # Bool != int, type 不会将 Bool 转化成 int
```

&nbsp;