# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import lxml,requests

urls = ['https://zz.fang.anjuke.com/loupan/all/p{}/'.format(str(i)) for i in range(1,30,1)]
userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
headers = {
    'User-Agent':userAgent
}

'''获取单个URL信息
req = requests.get('https://zz.fang.anjuke.com/loupan/all/p1/')
soup = BeautifulSoup(req.text,'lxml')
itom = soup.select('#container > div.list-contents > div.list-results > div.key-list > div > div > a.lp-name > h3 > span.items-name')
for it in itom:
    print(it.get_text())
'''


'''
遍历30页获取信息
'''

for url in urls:
    req = requests.get(url,headers=headers)
    soup=BeautifulSoup(req.text,'lxml')
    itoms = soup.select('#container > div.list-contents > div.list-results > div.key-list > div > div > a.lp-name > h3 > span')
    for itom in itoms:
        data = itom.get_text()
        print(data)


