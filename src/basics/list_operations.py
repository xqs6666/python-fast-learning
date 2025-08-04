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