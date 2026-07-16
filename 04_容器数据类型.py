list1 = [10, "hello", 20.5, True, 100]
# #取全部列表
# print(list1)
# #复制整个列表
# print(list1[:])
# #取索引从2开始到4(不包括)的元素
# print(list1[2:4])
# #取索从2到末尾的元素
# print(list1[2:])
# #从0到2
# print(list1[:2])
# #从2到-1
# print(list1[2:-1])
# #倒取元素
# print(list1[::-1])

# list1.append(150)
# list1.insert(1,200)
# print(list1)

# list2=['a',False,'b']
# print(list1+list2)

# list1 = [100, 200, 300,400,500]
# print(len(list1),max(list1),min(list1),sum(list1))
# for item in list1:
#     print(item,end='\t')

# for i in range(len(list1)):
#     print(list1[i])

# for index,item in enumerate(list1):
#     print(index,item)

# newlist = [item for item in list1 if item != 200]
# print(newlist)
# list2 = [item for item in list1 if item!=200]
# print(list2)


# list3 = [(i,j) for i in list1 for j in list2]
# print(list3)

# list1=[1,2,3,4,5]
# list2=['a','b','c','d','e']
# zipped = zip(list1,list2)
# print(list(zipped))

# list1=[1,2,3,1]
# list2=[4,5,6]
# list3=[5,1,2]
# # list1.extend(list2)
# # print(list1)
# print(list1.index(1,2))


# for x in range(2,10):
#     for y in range(2,x):
#         if(x%y==0):
#             break
#     else:
#         print(f'{x}是一个质数')


# for i in range(1,6):
#     print('*'*i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num2 = [num for num in numbers if num%2!=0]
# print(num2)

# fuits=[]
# fuits[:4] = ['apple','banana','cherry','data']
# fuits.insert(0,'elderberry')
# fuits.insert(3,'fig')
# print(fuits)

# prices = [10.5, 20.0, 15.75, 8.2, 12.0]
# pri = [round(p*1.1,2) for p in prices]
# print(pri)

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# combine_list = list1+list2
# combine_list.sort()
# print(combine_list)

# strings = ["hello", "world", "python", "is", "fun"]
# str1 = ''
# for item in strings:
#     str1 = str1 + item + ' '
# print(str1)

# for i in range(0,6):
#     print(' '*(6-i),'*'* (2*i + 1))

# str1='abcdef'
# print(str1[3])

# str1 = 'abcdefcccc'
# print(str1.replace('c','a'))
# str1='a,b,c,d,e,f,g,h,i'
# print(str1.split(','))

# str1 = "a,b,c,d,e,f,g,h,i"
# print(str1.rsplit(",", 2))
# print('_'.join(["a","b","c"]))
# str2='hello'
# print(str2.removeprefix('he'))


# str1='hElloh'
# str2 =str1.isidentifier()
# print(str2)


# 5）给定一个列表 strings = ["hello", "world", "python", "is", "fun"]，编写一个程序，将列表中的元素拼接成一个字符串，元素之间用空格分隔。
# strings = ["hello", "world", "python", "is", "fun"]
# new_str=' '.join(strings)
# print(new_str)


#6）给定一个字符串 sentence = "Hello, World!"，编写一个程序，将字符串中的所有小写字母转换为大写字母，并输出结果。
# sentence = "Hello, World!"
# print(sentence.upper())

#7）给定一个字符串 text = "Python is fun and powerful."，统计字符串中字母 n 出现的次数。
# text = "Python is fun and powerful."
# print(text.count('n'))

#8）给定一个字符串 str1 = "apple,banana,cherry,date"，将该字符串按照 , 分隔，存储在一个列表中，并将列表中的元素首字母大写，最后将修改后的列表元素用 - 连接成一个新的字符串。
# str1 = "apple,banana,cherry,date"
# str2 = '-'.join(str1.capitalize().split(','))
# print(str2)

# tuple2=(1,2,3)
# for i,item in enumerate(tuple2):
#     print(i,item) 

# fruits = ("apple", "banana", "cherry", "date", "elderberry")

# print(max(fruits))

# longest = ''
# for item in fruits:
#     if len(item) > len(longest):
#         longest = item
# print(longest)


