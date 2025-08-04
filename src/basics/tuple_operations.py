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