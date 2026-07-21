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


