from urllib import request
import chardet

if __name__ == "__main__":
    url = "https://music.163.com/"
    rsp = request.urlopen(url)

    print(rsp.info())
    print(rsp.geturl())
    print(rsp.getcode())
    html = rsp.read()

    cs = chardet.detect(html)
    print(cs)

    # html = html.decode()
    # print(html)
