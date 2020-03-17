from urllib import request,parse

import json

if __name__ == "__main__":
    url = "https://fanyi.baidu.com/sug"
    kw = input("INPUT:")
    data = {
        "kw": kw
    }
    data = parse.urlencode(data).encode()
    rsp = request.urlopen(url, data=data)
    print(rsp)
    json_data = rsp.read().decode()
    print(json_data)
    rst = json.loads(json_data)
    for i in rst['data']:
        print(i['k'] + "--" + i["v"])

