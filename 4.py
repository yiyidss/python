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