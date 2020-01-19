# 打开文件，写
# r表示后面的字符串内容不需要转义
# f = open(r'D:\\testlizi.txt','w')
# f.write('我希望有个如你一般的人\n等待不怕岁月蹉跎\n不怕路途遥远\n只要最后是你就好')
# f.close()
# # 写操作，如果找不到文件，默认创建
#
# # with语句
# with open(r'D:\\testlizi.txt','r') as f:
#     strline = f.readline()      # 按行读取内容
#     while strline:
#         print(strline)
#         strline = f.readline()
# # with语句，自动判断文件的作用域，自动关闭不再使用的打开的文件句柄f
# # 不需要使用close关闭文件f
#
# # list，把一行内容作为一个元素
# with open(r"D:\\testlizi.txt",'r') as f:
#     l = list(f)
#     for line in l:
#         print(line)

# read,读取第一个元素
# with open(r"D:\\testlizi.txt",'r') as f:
#         l = len(f.read())
#         with open(r"D:\\testlizi.txt", 'r') as f:
#             for i in range(l + 1):
#                 strnum = f.read(1)
#                 if strnum != "\n":
#                     print(strnum, end='')
#                 else:
#                     print(strnum)

# with open(r"D:\\testlizi.txt",'r') as f:
#     strnum = f.read(1)
#     while strnum:
#         if strnum != "\n":
#             print(strnum, end='')
#         else:
#             print(strnum)
#         strnum = f.read(1)
# seek(offset, form)
# 移动文件的读取位置，也叫读取针
# form的取值范围：0，从文件开头偏移；1，从文件当前位置偏移；2，从文件末尾偏移
# 移动的单位是字节
# with open(r"D:\\testlizi.txt",'r') as f:
#     f.seek(6, 0)
#     strnum = f.read()
#     print(strnum)

import time

# with open(r"D:\\testlizi.txt",'r') as f:
#     strnum = f.read(2)
#     while strnum:
#         if strnum != "\n":
#             print(strnum, end='')
#         else:
#             print(strnum)
#         # time.sleep(1)
#         strnum = f.read(2)

# write(str):把字符串写入文件--------只能是字符串参数
# writeline(str):把字符串按行写入文件----------可以是字符串，也可以是字符序列

with open('D:\\oooo1.txt','w') as f:
    f.write('黄沛仪臭宝宝')