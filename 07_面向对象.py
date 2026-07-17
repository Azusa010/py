class Person:
    '''人类'''
    home = 'earth'

    def __init__(self,name,age):
        #实例属性
        self.name = name
        self.age = age
    
    def eat(self):
        print('eating')
    def drink(self):
        print('drinking')
        
# 成员引用
home = Person.home
eat_func = Person.eat
drink_fun = Person.drink
doc = Person.__doc__
print(home,'\n',eat_func,'\n',drink_fun,'\n',doc)


# 实例化
p1 = Person('paul',19)
p1.drink()
p1.eat()