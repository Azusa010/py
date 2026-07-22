# from math_operations import add,multiply

# print(add(3,5))
# print(multiply(3,5))


# def func():
#     for i in range(1,11):
#         yield i

# y = func()
# for i in y:
#     if i % 2==0:
#         print(i)



class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.data[self.index]
        
t1 = MyIterator([10,20,30])
for i in t1:
    print(i)