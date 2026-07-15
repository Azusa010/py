# 基础知识
## int 整形
### 演示数据类型
```py
num = 10
print(type(num))  # <class 'int'>
```
---
### 书写很大的数字时，可用下划线将数字分组，便于清晰阅读
```py
large_num = 1_000_000_000
print(large_num)  # 1000000000
```
---
### type 与 isinstance 的类型判断
#### type() 不会认为子类是一种父类型   isinstance() 会认为子类是一种父类型
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
- ==在程序中有变量指向这些对象，不需要新创建，直接指向==
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


## float 浮点型
```py
f1=0.1
f2=0.2
pritn(type(0.1+0.2))#<class 'float'>
```
- 浮点数计算时可能存在误差，可以通过导入decimal解决
---
## bool 类型
- Ture/False可以与数字相加
---
## str 字符串类型
- 可以用 三个引号 表示多行字符串
```py
print("""hello
world
        """)

```
```console
hello
world
```

<table><tr><th>转义字符<th>说明</tr><tr><td>\<td>在行为作为续行符</tr><tr><td>\\<td>反斜杠符号</tr><tr><td>\n<td>换行符</tr><tr><td>\b <td>退格</tr><tr><td>\t<td>符</tr><tr><td>\r<td>回车，回到行首</tr>
</table>

1. ### intern 机制
- 滞留机制，没有空格或者符号默认开启
```py
str1='hello'
str2='hello'
print(str1 is str2) #True
```
2. 字符串缓冲池
- 单个字母，长度为1的ASCII字符串会被interned，包括空字符

## 数据类型转换
1. 自动类型转换
  - 小类型 → 大类型
  - 两个整数相除结果为float
  - str + 整型 <span style="color:red">报错</span>
2. 强制类型转换
  - <table><tr><th>函数</th><th>说明</th></tr><tr><td>int(x [,base])</td><td>将 x 转换为一个整数，x 若为字符串可用 base 指定进制</td></tr><tr><td>float(x)</td><td>将 x 转换为一个浮点数</td></tr><tr><td>complex(real[,imag])</td><td>创建一个实部为 real，虚部为 imag 的复数</td></tr><tr><td>str(x)</td><td>将对象 x 转换为一个字符串</td></tr><tr><td>repr(x)</td><td>将对象 x 转换为一个字符串，可以转义字符串中的特殊字符</td></tr><tr><td>eval(x)</td><td>执行 x 字符串表达式，并返回表达式的值</td></tr><tr><td>bin(x)</td><td>将一个整数转换为一个二进制字符串</td></tr><tr><td>oct(x)</td><td>将一个整数转换为一个八进制字符串</td></tr><tr><td>hex(x)</td><td>将一个整数转换为一个十六进制字符串</td></tr><tr><td>ord(x)</td><td>将一个字符转换为它的 ASCII 整数值</td></tr><tr><td>chr(x)</td><td>将一个整数转换为一个 Unicode 字符</td></tr><tr><td>tuple(s)</td><td>将序列 s 转换为一个元组</td></tr><tr><td>list(s)</td><td>将序列 s 转换为一个列表</td></tr><tr><td>set(s)</td><td>转换 s 为可变集合</td></tr></table>

## 字符的编码和解码
```py
str1 = '你好'
b1 = str1.encode(encoding='utf-8')
print(b1)  #b'\xe4\xbd\xa0\xe5\xa5\xbd' <class 'bytes'>
print(b1.decode(encoding='utf-8'),type(b1.decode(encoding='utf-8'))) 
#你好 <class 'str'>
```

## 输入与输出
### 1.输入
- 用input()函数，可以让用户输入字符串，并存放到一个字符串变量里
```py
input_str = input('请输入一个字符串: ')
print('你输入的字符串是：', input_str)
```
```
请输入一个字符串: 123
你输入的字符串是：123
```

### 2.输出
1. print()
```python
print('hello world')
```
2. 用逗号分隔
```py
print('hello world','hello python')
```
3. 用end= 来控制用什么结尾
```py
print('hello',end='')
print('world')
```
4. 格式化输出
```py
# %占位
print('int=%d,float=%f,string=%s' %(10, 3.14, 'hello'))
# .format
str = 'int={},string={},float={}'.format(10,'hello',3.14)
str = 'int={0},string={1},float={2}'.format(10,'hello',3.14)
str = 'int={a},string={b},float={c}'.format(a=10,b='hello',c=3.14)
# 数字格式化
float1 = 3.14
# ^ 居中 < 局左 >居右
# 指定输出20字符
# , 表示每三位分割
# .2f保留两位小数
str = "{:*^20,.2f}".format(float1)
print(str)
# f 
float1 = 3.1415926
int1 = 10
str1 = f'float1={float1:.2f},int1={int1}'

# 另一种  使用{}可以转义
float1 = 3.1415
int1 = 10
str1 = f'{float1=},{{int1=}}' #float1=3.1415,{int1=}
```
