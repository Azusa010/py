# def printStar(row,col):
#     for i in range(row):
#         print('*'*col)

# printStar(2,3)
# printStar(1,4)

# 3）编写一个函数 multiply_list，它接收一个列表 numbers 作为参数，将列表中的元素相乘，并返回结果

# def multiply_list(numbers):
#     result=1
#     for item in numbers:
#         result = result * item
#     return result

# print(multiply_list([1,2,3,2]))

# 4）编写一个函数 is_prime，它接收一个正整数 n，并判断 n 是否为质数，如果是质数返回 True，否则返回 False。
# import math


# def is_prime(n):
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         max = int(math.sqrt(n)) + 1
#         for i in range(3, max):
#             if n % i == 0:
#                 return False
#         return True

# print(is_prime(7))


# my_string ='Hello,Python!'
# print(my_string.upper())
# print(my_string.find('P'))
# print(my_string.split(','))

# my_tuple = (1, 2, 2, 3, 4, 4, 4)
# print(my_tuple.count(4))
# print(len(my_tuple))

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# print(set1 | set2)
# print(set1 & set2)
# set1.discard(3)
# print(set1)


# set1={i for i in range(1,6)}
# dict1 = {i:i**2 for i in set1}
# print(dict1)

# def print_info(a,*args,b=2,c=3):
#     print(a,b,c,args)

# print_info(1,2,3)
# print_info(a=1,b=2,c=3)
# print_info(1,1,2,3,4)


# def prt(a,*args,c):
#     print(a,args,c)

# def pr(a,**args):
#     print(a,args)
# pr(1,b=1,c=2,d=3)

# def func(a,b,c):
#     print(a,b,c)

# tup1=(1,2,3)
# func(*tup1)
# dict1={'a':1,'b':2,'c':3}
# func(**dict1)

# def func(a,b,/,c,*,d,e):
#     print(a,b,c,d,e)
# func(1,2,3,d=1,e=2)


# def adult(age):
#     """判断是否成年"""
#     return "成年" if age > 10 else "未成年"


# 没有return，最后一行隐式添加return,没有返回值，调用者接受到None
# def func():

# print(func())

# def sum(n1,n2):
#     return n1 + n2

# print(sum(1,2))

# def f_a():
#     print('a开始')
#     f_b()
#     print('a结束')

# def f_b():
#     print('b开始')
#     print('b结束')

# f_a()


# def outer():
#     a=10
#     def inner():
#         print(a)
#     return inner

# outer()()


# 作用域
# var1 = 10
# def func():
#     global var1
#     var1 = 20
#     print(var1)
# func()
# print(var1)

# list1 = [1,2,3]
# def func():
#     list1[1]=20
#     print(list1)
# func()
# print(list1)


# def func():
#     var1=10
#     def f():
#         nonlocal var1
#         var1 = 20
#         print(var1)
#     f()
#     print(var1)
# func()

# def get_j(n):
#     if n == 1:
#         return 1
#     return n * get_j(n-1)

# print(get_j(5))


# def calculate(num1,num2,op):
#     return op(num1,num2)

# calculate(10,20,lambda a,b : a+b)

# list1 = [i for i in range(5)]
# print(list(map(lambda item:'py'+str(item),list1)))

# list1 = [i for i in range(10)]
# print(list(filter(lambda i: i % 2 == 0, list1)))
# from functools import reduce
# print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
# def dog(name,age,specices):
#     return (name,age,specices)

# def dog(name:str,age:int,specices:str) -> tuple:
#     return (name,age,specices)

# def add_numbers(a,b,):
#     return a+b
# print(add_numbers(3,5))

# def greet(name,message='Hello'):
#     print(f'{message},{name}')
# greet('张三')

# def sum_all(*args):
#     return sum(args)

# print(sum_all(10,20,30,40))

def square(num):
    return num**2
def cube(num):
    return square(num) * num
print(cube(3))