# Python高级语法

## 浅拷贝与深拷贝

- 浅拷贝:拷贝父对象,不会拷贝父对象内部的子对象,拷贝后只有第一层是独立的,子对象指向同一块内存地址,修改子对象会影响原对象,性能开销小

- 深拷贝:完全拷贝父对象及其子对象,拷贝后所有层都是独立的,性能开销大

### 浅拷贝

- 切片( 如[:] )

- 使用工厂函数( 如list() / set() )

- 使用copy()

#### 例

```py
list1 = [1,2,3]
# list2 = list1[:]
# list2 = list1.copy()
list2 = list(list1)
```

### 深拷贝

- 使用copy.deeepcopy( )

```py
import copy
list1 = [1,2,3]
list2 = copy.deepcopy(list1)
```

### 拷贝的特殊情况

- 非容器类型(如数字、字符串、和其他"原子"类型对象)无法拷贝

- 元组变量如果只包含原子类型对象，则不能对其深拷贝

## 迭代器

迭代是遍历容器的一种方式

迭代器是一个可以记住遍历的位置的对象

迭代器只能往前，不会后退

`字符串,列表或者元组`都可用于创建迭代器

### 可迭代对象

- 可以直接作用与 `for` 循环的数据类型有:
  
  - 容器,如`list`,`tuple`,`dict`,`set`,`str`等
  
  - `generator`包括生成器和带`yield`的`generator funciton`

```py
import os

for element in [1,2,3]:  #列表可迭代
    print(element)

for element in (1,2,3):  #元组可迭代
    print(element)

for key in {"one":1,"tow":2}: #字典可迭代
    print(key)

for char in "123": #字符串可迭代
    print(char)

with open("test.txt",'w') as f:
    f.write("H\ne\n")
for line in open('test.txt'): #可迭代
    print(line,end="")
os.remove("test.txt")
```

- 判断是否是可迭代对象(Iterable)    

```py
from collections.abc import Iterable
print(isinstance([],Iterable)) #True
```

- 判断是否是迭代器(Iterator)

```py
from collections.abc import Iterator
print(isinstance([],Iterator)) #False
print(isinstance((i for i in range(2)),Iterator)) #True
```

### 使用迭代器

迭代器有两个基本方法:`iter()和next()`

`iter()`获得一个可迭代对象的迭代器

`next()`获得可迭代对象的下一个元素

使用`iter()获得一个可迭代对象的迭代器`

```py
list1 = [1,2,3]
#返回迭代器对象
it = iter(list1)
print(next(it)) #1
print(next(it)) #2
print(next(it)) #3
print(next(it)) #StopIteration
```

### 创建迭代器对象

实现`__iter__`和`__next__`方法

```py
class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]
```

```py
l1 = [1, 2, 3]
it = Reverse(l1)
print(isinstance(l1, Iterator)) #False
print(isinstance(it, Iterator)) #True
```

## 生成器

### 什么是生成器

是一个**用于创建迭代器**的简单而强大的工具

生成器可以按需生成值,避免一次性生成大量数据并占用大量内存

生成器可以与其他迭代工具( 如for )配合使用

### 创建生成器

1. 使用推导式创建生成器

```py
gen = (i for i in range(10))
print(type(gen)) #<class 'generator'>
```

2. 通过类似标准函数的形式创建生成器
- 通过`yield`进行值的返回

```py
def fibo():
    a,b,count=0,1,0
    while count<10:
        yield b
        a,b,count=b,a+b,count+1
    return "abcd" #返回异常的描述信息
f=fibo()
try:
    while True:
        print(next(f))
except StopIteration as e:
    print(e)
```

### send( )

1. 向生成器发送值

2. send函数发送的函数会作为yield表达式的返回值，赋值给task_id

3. **生成器刚创建时，处于“未启动（还未执行到第一个 `yield`）”状态，此时只能用 `None` 启动，不能直接发送非空值。**用`g.send(None)或next(g)`

```py
def gen():
    task_id=0
    int_value=0
    char_value='A'
    while True:
        match task_id:
            case 0:
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield char_value
                char_value = chr(ord(char_value)+1)
            case _:
                yield
```

```py
g=gen()
print(next(g)) 
print(g.send(0))
print(g.send(0))
print(g.send(1))
print(g.send(1))
```

## 命名空间

是从名称到对象的映射,大多数命名空间使用Python字典实现

各个命名空间是独立的，没有任何关系，一个命名空间中不能有重名



一般有三种不同的命名空间,在不同时刻创建,并且有不同的生命周期

### (1)内置命名

内置命名的命名空间是在Python解释器启动时创建的，永远不会被删除

### (2)一个模块的全局名称

### (3)一个函数调用中的局部名称



## 闭包

```py
def outer(a,b):
    def inner(x):
        return a * x+b
    return inner

outer = outer(1,2)
cells = outer.__closure__
print(cells[0].cell_contents)  #1
print(cells[1].cell_contents)  #2
```

所有函数对象都有一个`__closure__`属性，如果他是一个闭包函数，则该属性返回单元格对象元组，每个单元格对象都对应着闭包所引用的外部函数作用域中的一个变量

普通函数的`__closure__`一般为`None`

## 装饰器

装饰器允许在不修改原有函数的基础上，动态的添加或修改函数的功能

本质上是一个接收函数作为输入并且返回一个新的函数的对象

```py
from math import sqrt

def func(x):
    return sqrt(x)


def decorator(func):
    def inner(x):
        x = abs(x)
        return func(x)

    return inner

inn = decorator(func)
print(inn(-4))
```

### 装饰器和普通函数的区别

装饰器返回的是函数,普通函数直接返回结果

装饰器更符合Python装饰器模式,可以方便的复用和组合



### 装饰器语法糖

在函数前使用`@decorator`( decorator要和定义的装饰器名字相同 )

Python会将func作为参数传递给decorator,然后将返回的inner函数替换掉原来的func

```py
from math import sqrt


def decorator(func):
    def inner(x):
        x = abs(x)
        return func(x)

    return inner

@decorator
def func(x):
    return sqrt(x)


print(func(-4))
```

### 多层装饰器

多层装饰器的装饰过程，离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰 

先装饰，后执行

想要哪个装饰器先执行，就离函数远一点

```py
def get_abs(func):
    def inner(x):
        x = abs(x)
        return func(x)
    return inner

def get_int(func):
    def inner(x):
        x = int(x)
        return func(x)
    return inner

@get_int
@get_abs
def func(x):
    return sqrt(x)


print(func("-4"))
```

### 带参数的装饰器

```py
from math import sqrt

def times(n):
    def get_absolute(f):
        def inner(x):
            x=abs(x)
            for i in range(n):
                x = f(x)
            return x
        return inner
    return get_absolute

@times(2)
def func(x):
    return sqrt(x)

print(func(-16))
```



### 类装饰器

类装饰器是包含`__call__()`方法的类，他接受函数作为参数，并返回新的函数



如果有`__call__()`可以通过 类的`实例()`直接调用

```py
d = DecoratorClass(func)
print(d(-4))
```

```python
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
```


