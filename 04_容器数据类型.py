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

list1=[1,2,3,1]
list2=[4,5,6]
list3=[5,1,2]
# list1.extend(list2)
# print(list1)
print(list1.index(1,2))
