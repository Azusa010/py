# list1 = [1,2,3]
# # list2 = list1[:]
# # list2 = list1.copy()
# list2 = list(list1)


# import copy
# # list1 = [1,2,3,[100,200,300]]
# # print(id(list1),id(list1[0]),id(list1[3]))
# # list2 = copy.copy(list1)
# # print(id(list2),id(list2[0]),id(list2[3]))

# num1 = 1
# num2 = copy.copy(num1)
# print(num2)


# import os

# for element in [1,2,3]:
#     print(element)

# for element in (1,2,3):
#     print(element)

# for key in {"one":1,"tow":2}:
#     print(key)

# for char in "123":
#     print(char)

# with open("test.txt",'w') as f:
#     f.write("H\ne\n")
# for line in open('test.txt'):
#     print(line,end="")
# os.remove("test.txt")

# from collections.abc import Iterable
# print(isinstance([],Iterable))


# from collections.abc import Iterator
# print(isinstance([],Iterator))
# print(isinstance((i for i in range(2)),Iterator))

# list1 = [1,2,3]
# #返回迭代器对象
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# from collections.abc import Iterator


# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]


# l1 = [1, 2, 3]
# it = Reverse(l1)
# print(isinstance(l1, Iterator))
# print(isinstance(it, Iterator))


