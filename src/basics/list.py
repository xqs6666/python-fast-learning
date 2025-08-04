'''
numbers = [1,2,3,4,5,6,7,8,9,10]

for i,number in enumerate(numbers):
    print(i,number)
'''

user=['liangdianshui','twowater','两点水']

print(user)

print(user[1])

print(len(user))

user.append("xqs")
print(user)

user.insert(1,"02hello")
print(user)

user.pop()
print(user)

user.pop(0)
print(user)

user[0]="xqs1"
print(user)

newUser=[['VIP用户',11111],['twowater',22222],['三点水',33333]]
print(newUser)

numbers = [1,2,3,4,5,6,8,9,10,1]
#numbers.sor
print(numbers)
print(max(numbers))
print(numbers.index(3))
numbers.insert(1,1.5)
print(numbers)