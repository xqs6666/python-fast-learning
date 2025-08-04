# python基础

## python数据类型

## python变量和常量

### 变量
变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：

在内存中创建了一个`'ABC'`的字符串；
在内存中创建了一个名为a的变量，并把它指向`'ABC'`。
也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

```python
a = 'ABC'
b = a
a = 'XYZ'
print(b)
```

### 常量
所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你

```python
PI = 3.14159265359
print(PI)
```

1. /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
2. 还有一种除法是//，称为地板除，两个整数的除法仍然是整数

```python
print(3/3)
# 1.0
print(3//3)
# 1
```

Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。
注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

## python字符串格式化

f-string
格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

```python
r = 2.5
s = 3.14 * r ** 2  # 3.14xr^2
print(f'nihao {r}，，{s}，{s:.2f}') #:后面的.2f指定了格式化参数（即保留两位小数）
```

`{r}`被变量r的值替换，`{s:.2f}`被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数），因此，`{s:.2f}`的替换结果是19.62。

## List列表和元组tuple

### 有序可变List
```python
# 列表的基本操作示例

# 1. 创建列表
fruits = ['苹果', '香蕉', '橙子']
print('原始列表:', fruits)

# 2. 访问列表元素
print('\n访问列表元素:')
print('第一个水果:', fruits[0])  # 通过索引访问
print('最后一个水果:', fruits[-1])  # 负索引访问

# 3. 添加元素
print('\n添加元素:')
fruits.append('葡萄')  # 在末尾添加
print('append 后:', fruits)

fruits.insert(1, '草莓')  # 在指定位置插入
print('insert 后:', fruits)

# 4. 删除元素
print('\n删除元素:')
popped_fruit = fruits.pop()  # 删除并返回最后一个元素
print('pop 删除的元素:', popped_fruit)
print('pop 后:', fruits)

fruits.remove('香蕉')  # 删除指定元素
print('remove 后:', fruits)

# 5. 修改元素
print('\n修改元素:')
fruits[0] = '红苹果'  # 通过索引修改
print('修改后:', fruits)

# 6. 列表操作
print('\n列表操作:')
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print('原始数字列表:', numbers)

# 排序
numbers.sort()
print('排序后:', numbers)

# 反转
numbers.reverse()
print('反转后:', numbers)


# 列表长度
print('列表长度:', len(numbers))

# 统计元素出现次数
print('数字5出现的次数:', numbers.count(5))

# 查找元素索引
print('数字9的索引:', numbers.index(9))

# 7. 列表切片
print('\n列表切片:')
print('前3个元素:', numbers[:3])
print('中间3个元素:', numbers[3:6])
print('最后3个元素:', numbers[-3:])
```

### 有序不可变元组
```python
# 元组的基本操作示例

# 1. 创建元组
print('创建元组:')
tuple1 = (1, 2, 3)  # 使用圆括号创建
tuple2 = 'a', 'b', 'c'  # 不使用圆括号
tuple3 = ('python',)  # 单元素元组，注意逗号不能省略

print('tuple1:', tuple1)
print('tuple2:', tuple2)
print('tuple3:', tuple3)

# 2. 访问元组元素
print('\n访问元组元素:')
print('第一个元素:', tuple1[0])
print('最后一个元素:', tuple1[-1])

# 3. 元组的不可变性
print('\n元组的不可变性:')
try:
    tuple1[0] = 10  # 这会引发TypeError
except TypeError as e:
    print('无法修改元组元素:', e)

# 4. 元组的切片
print('\n元组切片:')
numbers = (0, 1, 2, 3, 4, 5)
print('原始元组:', numbers)
print('前三个元素:', numbers[:3])
print('中间元素:', numbers[2:4])
print(numbers[1:3])
print('最后两个元素:', numbers[-2:])

# 5. 元组的运算
print('\n元组运算:')
tuple4 = (1, 2) + (3, 4)  # 连接
print('连接后:', tuple4)
tuple5 = (1, 2) * 3  # 重复
print('重复后:', tuple5)

# 6. 元组方法
print('\n元组方法:')
tuple6 = (1, 2, 2, 3, 2)
print('元组中2出现的次数:', tuple6.count(2))
print('元素2第一次出现的索引:', tuple6.index(2))

# 7. 元组解包
print('\n元组解包:')
x, y, z = (1, 2, 3)
print(f'x={x}, y={y}, z={z}')

# 8. 元组与列表的转换
print('\n元组与列表的转换:')
my_list = list(tuple1)  # 元组转换为列表
print('元组转换为列表:', my_list)
my_tuple = tuple(my_list)  # 列表转换为元组
print('列表转换为元组:', my_tuple)

# 9. 元组的应用场景
print('\n元组的应用场景:')
# 作为函数的返回值
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(f'坐标: ({x}, {y})')

# 作为字典的键
point_data = {(0, 0): '原点', (1, 1): '点1'}
print('使用元组作为字典键:', point_data)
```

## dict和set

### dict

Python 字典（dict）是一种可变、无序的键值对（key-value）集合，是 Python 中非常常用的数据结构之一。字典的键必须是不可变类型（如字符串、数字、元组等），而值可以是任意类型。

1. 字典的常用方法
​
```python
方法	说明
keys()	返回所有键的视图
values()	返回所有值的视图
items()	返回所有键值对的视图
update()	合并另一个字典
popitem()	删除并返回最后一个键值对
setdefault()	如果键不存在，设置默认值
```
2. 遍历

```python
 遍历键
for key in d:
    print(key, d[key])
```

```python
 遍历键值对
for key, value in d.items():
    print(key, value)
```

### set

```python
a = {1, 2, 3}
b = {3, 4, 5}

# 并集
print(a | b)  # {1, 2, 3, 4, 5}

# 交集
print(a & b)  # {3}

# 差集
print(a - b)  # {1, 2}

# 对称差集
print(a ^ b)  # {1, 2, 4, 5}

# 添加元素
a.add(4)
print(a)  # {1, 2, 3, 4}

# 删除元素
a.discard(2)
print(a)  # {1, 3, 4}

a.clean()
a.remove(3)
```

## 条件语句 循环语句

> 非零数值、非空字符串、非空 list 等，判断为 True，否则为 False

```python
num=""

if num:
    print("字符串 not null")

bool=None

if bool:
    print("None not null")

data=0

if data:
    print("data not null")

results = 59

if results>=90:
    print("优秀")
elif results>=80:
    print("良好")
elif results>=60:
    print("及格")
else:
    print("不及格")

java = 86
python = 68

if ( java >= 80  and java < 90 )  or ( python >= 80 and python < 90):
    print('良好')
```


