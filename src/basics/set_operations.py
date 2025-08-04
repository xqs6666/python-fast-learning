list= [1,2,3,45,6,6]

setNum1=set(list)
print(setNum1)

setNum2={1,2,3,4,4}
print(type(setNum2))
setNum2.add(67)
print(setNum2)
setNum2.remove(1)
print(setNum2)

set1=set('hello')
set2=set("python")
print(set1)
print(set2)

n=set1 & set2
print(n)

u=set1 | set2
print(u)

list1 = [111,222,333,444,111,222,333,444,555,666]  
set3=set(list1)
set3.update([1,2,3])
print(set3)

setOne=set1 - set2
print(setOne)