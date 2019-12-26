# def study(name,age,what=None):
#     print("{0}今年{1}岁了，{2}".format(name,age,what))
#
# study(name = "liu",age = 18,what = None)

# class people():
#     def fget(self):
#         return self._age
#
#     def fset(self, age):
#         age22 = str(age)
#         self._age = age22.split(".")[0]
#
#     def fdel(self):
#         self._age = "....."
#
#     age = property(fget, fset, fdel, "adsada")
#
# p = people()
# p.age = 18.2
# print(p.age)

import sys
print(sys.path)
