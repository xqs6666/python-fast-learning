def add(a,b):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float))):
        raise TypeError("error")
    return a+b

print(add(1,1))


def  division ( num1, num2 ):
    # 求商与余数
         a = num1 % num2
         b = (num1-a) / num2
         return b , a

print("f ",division(2,4)[0],)
# Python 一次接受多个返回值的数据类型就是元组。


def print_user_info(name,age,userInfo="1870840"):
      print(name,age,userInfo)

print_user_info("xqs",19)
# 只有在形参表末尾的那些参数可以有默认参数值,例如，def func(a, b=1) 是有效的，但是 def func(a=1, b) 是 无效 的。

def print_info(a,b=[]):
      print(b)
      return b

result = print_info(1)
result.append("xqs")

print_info(2)

# 默认参数的值是不可变的对象，比如None、True、False、数字或字符串，如果你像上面的那样操作，当默认值在其他地方被修改后你将会遇到各种麻烦。
no_value=object()

def print_info_2(a,b=no_value):
    if b is no_value:
            print("b is no")
    return

print_info_2(1)


def print_user_info( name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数
print_user_info(name="123",age=13)

def print_user_info( * hobby , name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return

print_user_info(12,12,"x","12",18,"a")