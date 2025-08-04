name = [['一点水', '131456780001'], ['两点水', '131456780002'], ['三点水', '131456780003'], ['四点水', '131456780004'], ['五点水', '131456780005']]

print('姓名列表:', name)
print('姓名列表长度:', len(name)) 
print(name[0][1])


dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
print('字典1:', dict1)
print('字典1的长度:', len(dict1))
print('字典1的键:', dict1.keys()) 
print('字典1的值:',dict1.values())
print('字典1的项:', dict1.items())
print(dict1["liangdianshui"])
dict1["xqs666"]="444444"
print('更新后的字典1:', dict1)
# dict1.clear()  # 清空字典
# print('清空后的字典1:', dict1)
vars=dict1.values()
print()

dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}

for key in dict1:
    print(key,dict1[key])

for key,value in dict1.items():
    print(key,value)


data={x:x**2 for x in range(4)}
print(data)