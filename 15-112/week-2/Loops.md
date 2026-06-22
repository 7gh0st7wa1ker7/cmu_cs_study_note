# Loops

Loops 解决的是**如何重复处理数据**。这一章真正训练的是：
- 数据遍历
- 状态更新
- 终止条件
- 算法复杂度

## for & while

`for` & `while` 都是常用的循环方法，该使用哪个方法：
- 如果不确定需要重复的次数的情况下，选择 `while`
- 其他情况下都选择 `for`

## 项目中常见的循环方式

### 累加器

```python
total = 0
for x:
    total += x
```

### 查找

```python
for x:
    if x == 'x':
        continue
```

### 映射

```python
result = []
for x:
    result.append(transform(x))
```

### 统计

```python
count = 0
for x:
    if condition:
        count += 1
```

### 最大值

```python
max_val = int
for x:
    if x > max_val:
        max_val = x
```

### Guess & Check

```python
guess = 0
while not success:
    guess += 1
```

## 实际开发中最容易踩的坑

### 修改正在遍历的 list

修改正在遍历的 list ，会导致 list 中的元素序号变化，导致元素误操作。应该 `for x in nums[:]` 或直接创建一个新 list，所有操作都在新的 list中操作。

### while 死循环

`while x < 0:`，而后续的逻辑中没有持续的更新 `x` 的值。

### break 只退出一层

`break` 只影响当前的循环。

### range 不包含右边界

`range(5) -> 0,1,2,3,4` 默认从0开始，不包含5.

### float循环需要考虑精度

`while x < 1: x += 0.1`，需要考虑到0.999999999997的情况，最好别用float做判断条件。
