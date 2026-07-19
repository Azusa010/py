# try:
#     res = 10/1
# except  ZeroDivisionError:
#     print('除数不能为零')
# else:
#     print('没有异常发生')
# finally:
#     print('无论是否发生异常都会执行')

# def add(num1,num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         return num1 + num2
#     else:
#         raise TypeError('参数类型错误')  # 手动抛出异常
# print(add(1, 2))
# try:
#     add(1, '2')
# except TypeError as e:
#     print(e)

# class MyError(Exception):
#     def __init__(self, message):
#         self.message = message
#     def __str__(self):
#         return super().__str__()

# def add(num1,num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         return num1 + num2
#     else:
#         raise MyError('参数类型错误')  # 手动抛出异常
# try:
#     add(1, '2')
# except MyError as e:
#     print(e)
# try:
#     try:
#         try:
#             res = 10/1
#         except ZeroDivisionError as e:
#             print('第三层', e)
#     except TypeError as e:
#         print('第二层', e)
# except Exception as e:
#     print('第一层', e)

# def m3():
#     print(1/0)
# def m2():
#     m3()
# def m1():
#     m2()


# try:
#     with open("test.txt", "w") as f:
#         f.write('str1')
# finally:
#     print(f.closed)


# try:
#     int('abc123')
# except ValueError as e:
#     with open('error.log','a') as f:
#         f.write(str(e))

class InvalidAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return super().__str__()
        
class UnrealisticAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return super().__str__()
def check_age(age):
    if age<0:
        raise InvalidAgeError('小于0')
    elif age>120:
        raise UnrealisticAgeError('不真实的年龄')
    
try:
    check_age(122)
except Exception as e:
    print(e)