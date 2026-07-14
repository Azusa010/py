# int 整形
## 演示数据类型
```py
num = 10
print(type(num))  # <class 'int'>
```
---
## 书写很大的数字时，可用下划线将数字分组，便于清晰阅读
```py
large_num = 1_000_000_000
print(large_num)  # 1000000000
```
---
## type 与 isinstance 的类型判断
### type() 不会认为子类是一种父类型   isinstance() 会认为子类是一种父类型
- bool是int的子类
```py
num2 = True
print(type(num) == type(num2))  # False
print(isinstance(num, int))  # True
print(isinstance(num2, bool))  # True
```
---
## 小整数池
- Python将[-5,256]的整数维护在小整数池中。这些==整数提前创建好且不会被垃圾回收==，避免了为整数频繁申请和销毁内存空间。不管在程序的什么位置，使用的位于这个范围内的整数都是==同一个对象==
- 在程序中有变量指向这些对象，不需要新创建，直接指向
- id()获得对象的内存地址
- ==注意==：不同编译器的小整数池范围可能不同
Cpython的默认实现[-5,256]
```py
numA = 10
numB = 10
print(id(numA))  # 140736569365912
print(id(numB))  # 140736569365912
```
---
## 大整数池
- 一开始大整数池为空，每创建一个大整数就会往大整数池里面储存一个

- 有时连续赋值的大整数也可能指向同一个对象，这是Python的环境优化机制，但是这个优化不是绝对的，也取决于解释器,交互式,脚本环境


# float 浮点型
```py
f1=0.1
f2=0.2
pritn(type(0.1+0.2))#<class 'float'>
```
- 浮点数计算时可能存在误差，可以通过导入decimal解决
---
# bool 类型
- Ture/False可以与数字相加
---
# 