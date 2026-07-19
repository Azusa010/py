# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def __private_method(self):
#         print('这是一个私有方法')

# p1 = Person('张三',20)
# p1._Person__private_method()  # 调用私有方法


# class Person:
#     @property
#     def eat(self):
#         print('吃饭')

# p = Person()
# p.eat


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     @property
#     def age(self):
#         if self.__age > 18:
#             return 18
#         return self.__age
#     @age.setter
#     def age(self,age):
#         self.__age = age
# p1 = Person('张三',20)
# print(p1.age)  # 20
# p1.age = 15
# print(p1.age)  # 15


# class Person:
#     home = "earth"
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print("吃饭")

# class YellowRace(Person):
#     color = "yellow"

# class Student(Person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade = grade

#     def study(self):
#         print("学习")


# class CNStudent(Student, YellowRace):
#     country = "China"


# zs = CNStudent("张三", 1)
# print(zs.name,zs.grade,zs.country,zs.home,zs.color)  # 张三
# zs.study()
# zs.eat()


# class Person:
#     """人类"""
#     home = 'earth'
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print('吃饭')

# class YellowRace(Person):
#     skin = 'yellow'

#     def run(self):
#         print('跑步')

# class Student(Person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade = grade

#     def study(self):
#         # Person.eat(self)
#         super().eat()
#         print('学习')

# print(Student.__mro__)


# class Person:
#     def eat(self,a):
#         print('person eat')

# class Student(Person):
#     def eat(self,a,b):
#         super().eat(a)
#         print('student eat')

# s= Student()
# s.eat(10,20)


# class A:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

# class B:
#     def __init__(self,d,e,f):
#         self.d = d
#         self.e = e
#         self.f = f

# class C(A,B):
#     def __init__(self,a,b,c,d,e,f):
#         # A.__init__(self,a,b,c)
#         # B.__init__(self,d,e,f)
#         # super().__init__(a,b,c)
#         # super(A,self).__init__(d,e,f)
#         super().__init__(a=a,b=b,c=c,d=d,e=e,f=f)

# print(C(1,2,3,4,5,6).d)


# class Parent1:
#     def __init__(self,value1,**kwargs):
#         print('Parent1')
#         super().__init__(**kwargs)
#         self.value1 = value1

# class Paren2:
#     def __init__(self,value2,**kwargs):
#         print('parent2')
#         super().__init__(**kwargs)
#         self.value2 = value2
# class Child(Paren2,Parent1):
#     def __init__(self, value2, value1):
#         super().__init__(value2=value2,value1=value1)

# c = Child(1,2)
# print(c.value1)
# print(c.value2)


# 多态
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f'{self.age}岁的{self.name}去吃饭')

# class Teacher(Person):
#     pass


# class Student(Person):
#     pass

# def  eating(Person):
#     Person.eat()

# # zs = Teacher('zs',20)
# # ls = Student('ls',18)
# # eating(zs)
# # eating(ls)

# def new_obj(num):
#     if num==1:
#         obj = Teacher('zs',20)
#     else:
#         obj = Student('ls',20)
#     return obj
# obj=new_obj(1)
# print(obj.name)


# class Person:
#     pass


# Person.hobby = "reading"
# print(Person.hobby)
# from types import MethodType

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius


# def calculate_area(self):
#     return 3.14*self.radius**2

# c = Circle(5)
# c.calculate = MethodType(calculate_area,c)
# print(c.calculate())


# class BankAccount:
#     def __init__(self,balance=0):
#         self.__balance = balance
#     @property
#     def balance(self):
#         return self.__balance
#     @balance.setter
#     def balance(self,m):
#         self.__balance +=m 
    
#     def withdraw(self,m):
#         if self.__balance > m:
#             self.__balance -= m
#         else:
#             print('余额不足')

# b = BankAccount(0)
# print(b.balance)
# b.balance = 19
# b.withdraw(20)


# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,h,w):
#         self.h = h
#         self.w = w
#     def area(self):
#         return self.h * self.w
# class Circle(Shape):
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return 3.14 * self.r**2

# r= Rectangle(2,2)
# c = Circle(5)
# l1 = [r,c]
# for item in l1:
#     print(item.area())