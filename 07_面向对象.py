# class Person:
#     '''人类'''
#     home = 'earth'

#     @staticmethod
#     def m4():
#         print('人类')

# Person.m4() # 人类


# def m5(self,x,y):
#     print(x+y)

# class Person:
#     f1=m5

# Person().f1(1,2) # 3


# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __getattribute__(self, item):
#         print(item+'获取属性')
#         return object.__getattribute__(self, item)
# p = Person('Alice')
# p.name


# class Engine:
#     def __init__(self,cylinders,horsepower):
#         self.cylinders = cylinders
#         self.horsepower = horsepower

#     def start(self):
#         print('汽车启动')
#     def stop(self):
#         print('汽车停止')

# class Car:
#     def __init__(self,make,model,year,engine):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.engine = engine
#         self.speed = 0

#     def start(self):
#         self.engine.start()

#     def stop(self):
#         self.engine.stop()

#     def accelerate(self,amount):
#         self.speed += amount
#         return f'汽车加速，当前速度为{self.speed} km/h'

#     def brake(self,amount):
#         self.speed -= amount
#         return f'car is braking, current speed is {self.speed} km/h'


# file1 = open('output.txt','w+')
# file1.write('This is a test')
# file1.seek(0)
# print(file1.read())
# file1.close()

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bake(self):
#         print(f'Woof! My name is {self.name} and i am {self.age} years old')

# doggy = Dog('旺财',5)
# doggy.bake()
# doggy.age = 10
# doggy.bake()

# def reverseNum(n:int):
#     if n == 0:
#         return 0
#     s = str(n)
#     if s.startswith('-'):
#         reversed_str = '-' + s[1:][::-1]
#     else:
#         reversed_str = s[::-1]
#     return int(reversed_str)

# num = input('请输入一个整数 ')
# print(reverseNum(num))


# def rev(num):
#     s = str(num)
#     if num < 0:
#         res = -int(s[1:][::-1])
#     elif num==0:
#         res = 0
#     else:
#         res = int(s[1:][::-1])
#     return res
# print(rev(-12))
# students = {
#     "Alice": {"Math": 85, "English": 90, "Science": 78},
#     "Bob": {"Math": 92, "English": 88, "Science": 95},
#     "Charlie": {"Math": 70, "English": 75, "Science": 80},
# }


# def avg(arg):
#     return sum(arg)/len(arg)

# res = {}
# for k,v in students.items():
#     res[k] = round(avg(v.values()),2)

# print(res)
import types



# def eat(self):
#     print('eating')
# p = Person('zs')
# p.eat = types.MethodType(eat,p)
# p.eat()
class Person:
    __slots__ = ('name','age','drink')
    home = 'earth'

    def __init__(self,name):
        self.name = name

p1 = Person('zs')
p1.age=19
print(p1.age)