# python--oop
class Animal():
    shengao = "gao"
    tizhong = "zhong"
    __chiren = "nicai"
    _suibian = "suibian"
    def elpx(self):
        print("awuawuawu~")

class Dog(Animal):
    shengao = "hengao"
    tizhong = "henzhong"
    _suibian = "jiuhensuibian"
    def elpx(self):
        Animal.elpx(self)
        print("wangwangwang")

d = Dog()
d.elpx()
print(d._suibian)