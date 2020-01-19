# def funA(a):
#     if a > 46:
#         return a
#
# L = [1,-5,9,-23,-46,78,-321,654,879]
#
# v = filter(funA,L)      # 过滤
# print([i for i in v])
#
# print(sorted(L))    # 排序
# print(sorted(L, key = abs))     # 绝对值排序
# print(sorted(L, reverse=True))      # 倒序排序
# def count():
#     def fun(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(fun(i))
#     return fs
#
# f1,f2,f3 = count()
# print(f1())
# print(f2())
# print(f3())

l1 = [1,2,3]
l2 = [11,22,33]
z = zip(l1,l2)
l3 = [i for i in z]
print(l3)
for i in z:
    print(i)
help(zip)