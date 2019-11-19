# odoo

@api.multi
def newRefresh(self):  # 定义方法
    url = "http://www.baidu.com"
    date = {'xxx': xxx}  # 接口请求参数
    url_res = requests.post(url, date=date)
    if url_res.status_code == 200:  # 连接成功
        result = (json.loads(url_res.text)).get('data')  # 获取数据
        if result:
            for r in result:
                member = {
                    'userId': r.get('userId'),  # 员工id
                    'field1': r.get('field1'),  # 请假类型
                    'field2': r.get('field2'),  # 请假时间
                    'field4': r.get('field4'),  # 请假事由
                }
