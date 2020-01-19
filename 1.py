import datetime
import time

# 时间戳转成str
# timeStamp = 1563148800000//1000         # 时间戳
# timeArray = time.localtime(timeStamp)       # 时间元组
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)      # str
# print(otherStyleTime)
#
# now = int(time.time())  # 获取系统当前时间的时间戳
# timeStamp = 1546272000
# dateArray = datetime.datetime.utcfromtimestamp(timeStamp) + datetime.timedelta(hours=8)     # 时间戳转换成datetime格式，加上时区
# otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M")       # datetime转化成 str
# print(type(otherStyleTime))
# print(str(datetime.datetime.today())>'2015-01-01')
d1 = datetime.datetime.strptime('2017-12-12',"%Y-%m-%d")       # str转化成 datetime格式   取年； 时间元组格式取年：.tm_year
otherStyleTime = d1.strftime("%Y-%m")
print(otherStyleTime)
# # d2 = datetime.datetime.today().year
# d2 = datetime.datetime.strptime(datetime.date.today(),"%Y-%m-%d")
# #
# print((d2-d1))
#
# d3 = 42886.0
# delta = datetime.timedelta(days=d3)
# today = datetime.datetime.strptime('2019-01-01', '%Y-%m-%d')        # str转成datetime
# print(today)
# otherStyleTime = datetime.datetime.strftime(today, '%Y-%m-%d')      # 转成str
# d = datetime.timedelta(days=365)
# newdate = datetime.datetime.strptime('1899-12-30', '%Y-%m-%d')+delta+d    # excel 导入数据时间戳转换格式
# otherStyleTime2 = datetime.datetime.strftime(newdate, '%Y-%m-%d')
# print(otherStyleTime,otherStyleTime2)
#
# d2 = str(datetime.datetime.today().year)+'-01-01'
# print(d2)
# a = '2000-01-01'
# b = '2000-12-31'
# dd = datetime.datetime.strptime(a, '%Y-%m-%d')
# dt = datetime.datetime.strptime(b, '%Y-%m-%d')
# print((dd - dt).days)
# d3 = datetime.datetime.strftime(dd, '%Y-%m-%d')
# print(type(d3))


# tss1 = str(datetime.datetime.today().year) + '-01-01'
# timeArray = time.strptime(tss1, "%Y-%m-%d")
# timeStamp = int(time.mktime(timeArray))     # 时间元组转成float时间戳，强转int
# print(type(timeArray))
