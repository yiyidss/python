# # python--oop
# class Animal():
#     shengao = "gao"
#     tizhong = "zhong"
#     __chiren = "nicai"      # 不可以被继承
#     _suibian = "suibian"       # 可以被继承
#     def elpx(self):
#         print("awuawuawu~")
#
# class Dog(Animal):
#     shengao = "hengao"
#     tizhong = "henzhong"
#     # _suibian = "jiuhensuibian"
#     def elpx(self):
#         Animal.elpx(self)
#         print("wangwangwang")
#
# d = Dog()   # 实例化
# d.elpx()
# print(d._suibian)
import calendar

cal = calendar.calendar(2017)
print(cal)

print(calendar.leapdays(2012,2016))