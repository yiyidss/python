import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

url = "https://www.runoob.com/python3/python3-tutorial.html"
ua = UserAgent().random

headers = {'User-Agent': ua}

r = requests.get(url, headers=headers)
html = r.text.encode(r.encoding).decode()
soup = BeautifulSoup(html, 'lxml')
la = [i.text for i in soup.findAll('h2')]
df = pd.DataFrame(la, columns=[url])
lt = [x for x in soup.findAll('a') if x.has_attr('href') and x.attrs['href'][0:8] == '/python3']
re_urls = set([i.attrs['href'] for i in lt])
ab_urls = {'https://www.runoob.com/' + i for i in re_urls}
ab_urls.discard(url)
for x in ab_urls:
    r = requests.get(x, headers=headers)
    html = r.text.encode(r.encoding).decode()
    soup = BeautifulSoup(html, 'lxml')
    la = [i.text for i in soup.findAll('h2')]
    dfx = pd.DataFrame(la, columns=[x])
    df = df.join(dfx, how='outer')

df.to_excel('python3.xlsx')
# print([x.keywords for x in soup.findAll('meta')])
