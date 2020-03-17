from urllib import request

if __name__ == "__main__":
    rst = request.urlopen("https://music.163.com/")
    html = rst.read()
    html = html.decode()
    print(html)