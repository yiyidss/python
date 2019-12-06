a = "{{first.DATA}}\n患者名称：{{keyword1.DATA}}\n服务类型：{{keyword2.DATA}}\n申请时间：{{keyword3.DATA}}\n"
for o in range(1,4):

    x = a.split("\n")
    member = []
    members = []
    for i in range(1,len(x)-1):
        z = x[i].split("：")
        k = i
        tupp = (i,z[0])
        member.append(tupp)
    a = a + "到期时间：{{keyword4.DATA}}\n{{remark.DATA}}"
    print(member)