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


class Person:
    """人类"""
    home = 'earth'
    def __init__(self,name):
        self.name=name
    def eat(self):
        print('吃饭')
        
class YellowRace(Person):
    skin = 'yellow'

    def run(self):
        print('跑步')

class Student(Person):
    def __init__(self, name,grade):
        super().__init__(name)
        self.grade = grade

    def study(self):
        # Person.eat(self)
        super().eat()
        print('学习')

print(Student.__mro__)