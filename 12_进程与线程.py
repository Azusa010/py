# import multiprocessing
# import os
# import time
# def write_file():
#     """像文件中写数据"""
#     with open('test.txt','a') as f:
#         while True:
#             f.write('hello world\n')
#             f.flush() #手动将缓冲区的数据刷写到文件
#             time.sleep(0.5)

# def read_file():
#     """从文件中读数据"""
#     with open('test.txt','r') as f:
#         while True:
#             time.sleep(0.5)
#             print(f.readline())

# if __name__ == '__main__':
#     #避免子进程再创建子进程
#     p1 = multiprocessing.Process(target=write_file)
#     p2 = multiprocessing.Process(target=read_file)

#     p1.start()
#     p2.start()

# import os

# class Worker(multiprocessing.Process):
#     def run(self):
#         print(f"当前进程名:{self.name},进程ID:{os.getpid()}，父进程id:{os.getppid()}")

# if __name__ == '__main__':
#     for i in range(3):
#         p = Worker().start()


# import os
# import multiprocessing
# import time


# def func():
#     for i in range(2):
#         print(os.getpid(), i)
#         time.sleep(0.5)


# if __name__ == "__main__":
#     process_num = 5
#     pool = multiprocessing.Pool(process_num)
#     for p in range(process_num):
#         # pool.apply(func)#同步
#         pool.apply_async(func) #异步
#     pool.close()
#     pool.join()
#     print(f"当前进程名字{multiprocessing.current_process().name}:end")


# import os
# import multiprocessing


# def func(list1):
#     for i in range(10):
#         list1.appen(i)
#         print(os.getpid(), list1)


# if __name__ == "__main__":
#     list1 = []
#     p1 = multiprocessing.Process(func, args=(list1,))
#     p2 = multiprocessing.Process(func, args=(list1,))
#     p1.start()
#     p2.start()

#     p1.close()
#     p2.close()
#     print(f"当前进程名{multiprocessing.current_process().name}", list1)

# from random import randint
# import time
# import multiprocessing
# import os

# def func1(queue):
#     while True:
#         num = randint(1,50)
#         queue.put(num)
#         print(f"进程{os.getpid()}向队列放入{num}")
#         time.sleep(0.5)

# def func2(queue):
#     while True:
#         num = queue.get()
#         print(f"从队列{os.getpid()}中取出了{num}")
#         time.sleep(0.5)


# if __name__ == "__main__":
#     queue = multiprocessing.Manager().Queue()
#     pool = multiprocessing.Pool()
#     pool.apply_async(func1,args=(queue,))
#     pool.apply_async(func2,args=(queue,))
#     pool.close()
#     pool.join()


# import threading
# import time

# def func():
#     flag = 0
#     while True:
#         print(f"线程{threading.current_thread().name}", f"{flag}" * 5)
#         flag = flag ^ 1
#         time.sleep(0.5)

# if __name__ == "__main__":
#     t1 = threading.Thread(target=func)
#     t2 = threading.Thread(target=func)
#     t1.start()
#     t2.start()
# import threading
# import time

# class Worker(threading.Thread):
#     def run(self):
#         flag = 0
#         while True:
#             print(f"线程{threading.current_thread().name}", f"{flag}" * 5)
#             flag = flag ^ 1
#             time.sleep(0.5)


# if __name__ == "__main__":
#     t1 = Worker(name='Thread-1')
#     t2 = Worker(name='Thread-2')
#     t1.start()
#     t2.start()

# import concurrent.futures

# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:


# import time
# import threading


# def sale_ticket():
#     global ticket_num
#     while True:
#         lock.acquire()
#         if ticket_num <= 0:
#             lock.release()
#             break
#         time.sleep(0.01)
#         ticket_num -= 1    
#         print(f"当前{threading.current_thread().name}卖了一张票", f'还剩{ticket_num}')
#         lock.release()


# if __name__ == "__main__":
#     ticket_num = 100
#     lock = threading.Lock()
#     Threads = [threading.Thread(target=sale_ticket, name="窗口" + str(i)) for i in range(1, 4)]
#     [t.start() for t in Threads]
#     [t.join() for t in Threads]


# import multiprocessing

# def print_numbers1():
#     for i in range(1, 6):
#         print(f"进程1: {i}")
# def print_numbers2():
#     for i in range(6, 11):
#         print(f"进程2: {i}")

        
        
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=print_numbers1)
#     p2 = multiprocessing.Process(target=print_numbers2)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

import threading

def printHello():
    for i in range(10):
        print('线程1：Hello')

def printWorld():
    for i in range(10):
        print("线程2: World")

if __name__ == "__main__":
    t1 = threading.Thread(target=printHello)
    t2 = threading.Thread(target=printWorld)
    t1.start()
    t1.join()
    t2.start()
    t2.join()