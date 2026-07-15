from random import randint
# 单分支
# balance = randint(0,100)
# print(f'当前余额为{balance}')
# price = 50
# if balance < price:
#     print(f'余额不足{price},请充值')
# else:
#     print('欢迎下次光临')

# 双分支
# balance = randint(0,100)
# price = 50
# print(f'当前余额为{balance}')
# if balance < price:
#     print(f'余额不足{price},请充值')
# else:
#     balance-=price
#     print(f'消费成功，剩余余额为{balance}')
# print('欢迎下次光临')

# 多分支
# age = randint(0,100)
# print(f'这个人年龄是{age}岁',end='\t')
# if age<2:
#     print('婴儿')
# elif age < 4:
#     print('幼儿')
# elif age < 13:
#     print('儿童')
# elif age < 20:
#     print('青少年')
# elif age < 65:
#     print('成年人')
# else:
#     print('老年人')


# 练习题
# 1）接收控制台输入的薪水值，如果高于15000，就投递简历
# salary = input('请输入您的薪水:')
# if float(salary) > 15000:
#     print('投递简历')

# 2）从键盘上输入3位正整数，判断是否为水仙花数
# num = int(input('请输入一个三位正整数:'))
# a= num//100
# b= num//10%10
# c= num%10
# print(f'百位数为{a},十位数为{b},个位数为{c}')
# if a**3+b**3+c**3 ==num:
#     print(f'{num}是水仙花数')

# 3）从键盘上输入一个年份，判断是否为闰年
# year = int(input("请输入一个年份:"))
# if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")


# 4）从键盘上获取输入的数字，判断奇偶性，分别输出
# num = int(input('请输入一个整数:'))
# if num % 2 == 0:
#     print(f'{num}是偶数')
# else:
#     print(f'{num}是奇数')

# 5）模拟用户登录验证，获取键盘上的输入，如果用户名admin,密码是123，提示登录成功，否则提示登录失败
# username = input('请输入用户名:')
# password = int(input('请输入密码:'))
# if username=='admin' and password==123:
#     print('登陆成功')
# else:
#     print('登陆失败')

# 6）获取键盘上输入的数字，判断整数负数和0
# num = float(input("请输入一个数字:"))
# if num == 0:
#     print(f"{num:.0f}是0")
# elif num > 0:
#     print(f"{num:.0f}是正数")
# else:
#     print(f"{num}是负数")

# 7）从键盘上获取学生成绩，判断成绩等级
# 	>= 90 A
# 	[80~90) B
# 	[70~80) C
# [60~70) D
# <60    E

# score = int(input('请输入成绩:'))
# if score<0 or score >100:
#     print('分数不合法')
#     exit(1)
# if score>90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else:
#     print('E')


# 8）从键盘上输入一个时间，输出它的下一秒时间
# hour = int(input("请输入小时:(0~23)"))
# minute = int(input("请输入分钟:(0~59)"))
# second = int(input("请输入秒钟:(0~59)"))
# print(f'当前时间为{hour}:{minute}:{second}')
# second+=1
# if second>=60 :
#     second-=60
#     minute+=1
#     if minute>=60:
#         minute-=60
#         hour+=1
#         if hour ==24:
#             hour=0

# print(f'1s后时间为:{hour}:{minute}:{hour}')

# 9）遍历出1~100之间所有的数,将能被3整除的数打印出来,每行打印5个
# num = 1
# count = 0
# while num <= 100:
#     if num % 3 == 0:
#         print(num,end=' ')
#         count += 1
#         if count % 5 == 0:
#             print("\n")
#     num += 1


# 10）计算1+2+3+...+100的和
# num=1
# sum=0
# while num<=100:
#     sum+=num
#     num+=1
# print(sum)

# 11）接收用户在键盘上输入的正整数,如果输入-1结束,找出其中输入最大的值
# num = 0
# max=0
# while num!=-1:
#     num = int(input('请输入数字:'))
#     if max<num:
#         max=num

# if(max>0):
#     print(f'最大值为{max}')
# else:
#     print('还没有输入正整数！')


# 12）求出2~10这些数字中的质数


# 嵌套分支
# state = 0b000
# if state & 0b111 == 0b111:
#     print('大写状态')
# else:
#     if state & 0b010 == 0b010:
#         if state & 0b001 == 0b001:
#             print('简体中文-微软拼音')
#         else:
#             print('英文模式')
#     else:
#         print('英语美式键盘')


# match分支
# month = randint(1, 20)
# match month:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(f"{month}有31天")
#     case 4 | 6 | 9 | 11:
#         print(f"{month}有30天")
#     case 2:
#         print(f"{month}有28天")
#     case _:
#         print("输入月份不合理")


# 三目运算符
# num1=10
# num2=20
# max = num1 if num1>num2 else num2


# while循环
# week = 1
# rabbits = 2
# while week<10:
#     rabbits= rabbits+rabbits*2
#     week+=1
# print(f'第{week}周有{rabbits}只兔子')

# import time

# num = 1
# while num < 100:
#     print("=" * num,end='\r')
#     num += 1
#     time.sleep(0.05)

# for i in [2,3,4,5,6,7,8,9,0]:
#     print(i,end=' ')

# for i in 'string':
#     print(i)

# for i in range(10):
#     print(f'第{i+1}')

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i}*{j}={i * j}", end="\t")
#     print()

count = 0
for i in range(10):
    count = count + i**i
    print(count)
    if count > 1_000_0000:
        break