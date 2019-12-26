# a = '1.7'
# b = round(float(a), 2)
# c = str(b)
# print(c, type(c))

# a = [1,2,3,4]
# b = [5,6,7,8]
# print(a+b)
# a.extend(b)
# c = a
# print(c)

import datetime
lday = datetime.datetime.strptime("2019-07-19","%Y-%m-%d")
today = datetime.datetime.today()
print((today-lday).days)