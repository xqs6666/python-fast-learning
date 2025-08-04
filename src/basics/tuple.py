tuplex= (123,"123")
print(type(tuple))

tuple1=(123,)
print(tuple1[0])

tuple2=(123,145)
tuple3=tuple2+tuple1
print(tuple3)

tuple4=(123,"123",145,123,123)
print(tuple4*4)
print(tuple4.count(123))
print(tuple4.index("123"))



tuple5=(2,3,4)
print(len(tuple5))
print(tuple5)

def tuple_func(a,b,c):
    return (a,b,c)



data=tuple_func(2,3,4)
print(data)
print(type(data))

# del data  # 删除元组

if data in tuple5:
    print("data在tuple5中")
else:
    print("data不在tuple5中")