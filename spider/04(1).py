from urllib import request, parse

import json

if __name__ == "__main__":
    url = "https://study.163.com/j/search/suggestions/courses.json?"
    kw = input("INPUT:")
    data = {
        "keyword": kw
    }
    data = parse.urlencode(data).encode()
    rsp = request.urlopen(url, data=data)
    json_data = rsp.read().decode()
    # print(json_data)
    rst = json.loads(json_data)
    # print(rst)
    for i in rst['result']:
        for k,v in i.items():
            print(k+'--'+str(v))