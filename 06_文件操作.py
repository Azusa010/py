# test = open('test.txt','w')

# #写入数据
# test.write('hello,python\n')

# # 关闭连接
# test.close()


# test = open('test.txt','rt')

# #读取数据
# #read() 无参数读取全部内容
# #read(size) 读取 size 个字符/字节数
# # print(test.read(3))
# # print(test.read())
# print(test.readlines(211))
# # 关闭连接
# test.close()


# import os

# for root,dirs,files in os.walk(os.getcwd()):
#     print(root,dirs,files)


def copyPic(src, dst):
    pic = open(src, "rb")
    pic_copy = open(dst, "wb")

    while content := pic.read(1024):
        pic_copy.write(content)

    pic.close()
    pic_copy.close()

copyPic("pic.png", "pic_copy.png")
