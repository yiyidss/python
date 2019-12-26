# # 水仙花数
# for i in range(100, 1000):
#     a = (i // 100) ** 3
#     b = ((i-i//100*100)//10) ** 3
#     c = (i-i//100*100-(((i-i//100*100)//10)*10)) ** 3
#     if a+b+c == i:
#         print(i)
#
# n = int(input("请输入数字："))
# if n == 1:
#     print("1不能被分解")
# else:
#     z = ""
#     for i in range(2, n+1):
#         while n != i:
#             if n % i == 0:
#                 n = n / i
#                 z = str(i) + "*" + z
#             else:
#                 break
#     print(z + str(int(n)))


# s = input("请输入：")
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print(letters, space, digit, others)

# 完数
# for i in range(1,1000):
#     z = 0
#     for j in range(1,i):
#         l = []
#         if i % j == 0:
#             z = z + j
#
#     if z == i:
#         print(i)

# h = int(input("掉落的高度："))
# t = int(input("第几次反弹："))
# print("第"+str(t)+"次反弹的高度是："+str(h/2**t))
# z = 0
# for i in range(1, t):
#     z = z + (h/2**i)*2
# print("第"+str(t)+"次落地时共经过多少米："+str(z+h))

#  猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#  以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
x = 1
for i in range(1,10):
    x = (x+1)*2
print(x)