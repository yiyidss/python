# 模糊查询时的占位符
# sql = "select * from table_name where name like %s and address like %s"
# env.execute(sql, (('%s'+name+'%s'), ('%s'+address+'%s')))

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
data = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != k and i != j and j != k:
                m = (i,j,k)
                data.append(m)
print(data)
print(len(data))

# 输入某年某月某日，判断这一天是这一年的第几天？
import datetime
# date = input("请输入时间（格式y-m-d）：")
date = "2018-01-05"
date3 = datetime.datetime.strptime(date, "%Y-%m-%d")
date1 = str(date3.year) + "-01-01"
date2 = datetime.datetime.strptime(date1,"%Y-%m-%d")
print((date3-date2).days+1)

# 输入三个整数x,y,z，请把这三个数由小到大输出。
# len = []
# k = int(input("请输入比较的数字数目："))
# for i in range(k):
#     k = int(input("请逐个输入比较的数字："))
#     len.append(k)
# len.sort()
# print("比较后从小到大排序为："+str(len))

# 斐波那契数列
def name(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2 , n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(name(5))
# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a
#
# print(fib(0))
#
# def name(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return name(n-1) + name(n - 2)
# print(name(3))

# 输出 9*9 乘法口诀表。 程序分析：分行与列考虑，共9行9列，i控制行，j控制列
for i in range(1,10):
    for j in range(1,i+1):
        print(i*j,end='   ')
    print("")


# import datetime
# import time
# while True:
#     time.sleep(2)       # 间隔两秒
#     # print(datetime.datetime.now()
#     print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

# 汉诺塔
def hano(n,a,b,c):
    if n == 1:
        print(a, "->", c)
        return None
    if n == 2:
        print(a, "->", b)
        print(a, "->", c)
        print(b, "->", c)
        return None
    hano(n-1,a,c,b)
    print(a, "->", c)
    hano(n-1,b,a,c)


hano(n=4, a="A", b="B", c="C")