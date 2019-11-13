import datetime

# d1 = datetime.datetime.strptime('2017-12-12',"%Y-%m-%d").year
# d2 = datetime.datetime.today().year
# # d2 = datetime.datetime.strptime(datetime.date.today(),"%Y-%m-%d")
#
# print((d2-d1))
#
# d3 = 42886.0
# delta = datetime.timedelta(days=d3)
# today = datetime.datetime.strptime('1899-12-30', '%Y-%m-%d')+delta
# otherStyleTime = datetime.datetime.strftime(today, '%Y-%m-%d')
# d = datetime.timedelta(days=365)
# newdate = datetime.datetime.strptime('1899-12-30', '%Y-%m-%d')+delta+d    # excel 导入数据时间戳转换格式
# otherStyleTime2 = datetime.datetime.strftime(newdate, '%Y-%m-%d')
# print(otherStyleTime,otherStyleTime2)

d2 = str(datetime.datetime.today().year)+'-01-01'
print(d2)
a = '2000-01-01'
b = '2000-12-31'
dd = datetime.datetime.strptime(a, '%Y-%m-%d')
dt = datetime.datetime.strptime(b, '%Y-%m-%d')
print((dd - dt).days)
# d3 = datetime.datetime.strftime(dd, '%Y-%m-%d')
# print(d3)

