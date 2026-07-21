# list1 = [1,2,3]
# # list2 = list1[:]
# # list2 = list1.copy()
# list2 = list(list1)


# import copy
# # list1 = [1,2,3,[100,200,300]]
# # print(id(list1),id(list1[0]),id(list1[3]))
# # list2 = copy.copy(list1)
# # print(id(list2),id(list2[0]),id(list2[3]))

# num1 = 1
# num2 = copy.copy(num1)
# print(num2)


# import os

# for element in [1,2,3]:
#     print(element)

# for element in (1,2,3):
#     print(element)

# for key in {"one":1,"tow":2}:
#     print(key)

# for char in "123":
#     print(char)

# with open("test.txt",'w') as f:
#     f.write("H\ne\n")
# for line in open('test.txt'):
#     print(line,end="")
# os.remove("test.txt")

# from collections.abc import Iterable
# print(isinstance([],Iterable))


# from collections.abc import Iterator
# print(isinstance([],Iterator))
# print(isinstance((i for i in range(2)),Iterator))

# list1 = [1,2,3]
# #返回迭代器对象
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# from collections.abc import Iterator


# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]


# l1 = [1, 2, 3]
# it = Reverse(l1)
# print(isinstance(l1, Iterator))
# print(isinstance(it, Iterator))


# gen = (i for i in range(10))
# print(type(gen))


# def fibo():
#     a,b,count=0,1,0
#     while count<10:
#         yield b
#         a,b,count=b,a+b,count+1
#     return "abcd"
# f=fibo()
# try:
#     while True:
#         print(next(f))
# except StopIteration as e:
#     print(e)

# def gen():
#     task_id=0
#     int_value=0
#     char_value='A'
#     while True:
#         match task_id:
#             case 0:
#                 task_id = yield int_value
#                 int_value += 1
#             case 1:
#                 task_id = yield char_value
#                 char_value = chr(ord(char_value)+1)
#             case _:
#                 task_id= yield


# g=gen()
# print(next(g))
# print(g.send(0))
# print(g.send(0))
# print(g.send(1))
# print(g.send(1))


# def outer(a,b):
#     def inner(x):
#         return a * x+b
#     return inner

# outer = outer(1,2)
# cells = outer.__closure__
# print(cells[0].cell_contents)
# print(cells[1].cell_contents)

# def decorator(func):
#     def inner(x):
#         x = abs(x)
#         return func(x)

#     return inner

# from math import sqrt


# def get_abs(func):
#     def inner(x):
#         x = abs(x)
#         return func(x)
#     return inner

# def get_int(func):
#     def inner(x):
#         x = int(x)
#         return func(x)
#     return inner


# @get_int
# @get_abs
# def func(x):
#     return sqrt(x)


# print(func("-4"))


# from math import sqrt

# def times(n):
#     def get_absolute(f):
#         def inner(x):
#             x=abs(x)
#             for i in range(n):
#                 x = f(x)
#             return x
#         return inner
#     return get_absolute

# @times(2)
# def func(x):
#     return sqrt(x)

# print(func(-16))


from math import sqrt

class DecortatorClass:
    def __init__(self,func):
        self.func = func
        
    def __call__(self, x):
        x = abs(x)
        return self.func(x)

@DecortatorClass
def func(x):
    return sqrt(x)


print(func(-4))