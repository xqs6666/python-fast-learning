a = 'ABC'
b = a
a = 'XYZ'
print(b)

PI = 3.14159265359
print(PI)

print(3/3)
print(3//3)

r = 2.5
s = 3.14 * r ** 2  # 3.14xr^2
print(f'nihao {r}，，{s}，{s:.2f}') #:后面的.2f指定了格式化参数（即保留两位小数）

'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点
'''
s1 = 72
s2 = 85
r = ((s2-s1)/s1)*100
print(f'提升的百分点{r:.0f}')

a = b = c = 1

a,b =10,19

class ClassA:

    var1="xqs555"

    @classmethod
    def fun1(cls3,A):
        print(cls3.var1,A)

ClassA.fun1(234)
