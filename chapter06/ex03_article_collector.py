import os, codecs, re, datetime, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir('./target')
url = 'https://news.daum.net'
f = open(str(datetime.date.today()) + 'articles.txt', 'w')
soup = bs(ur.urlopen(url).read(), 'html.parser')

for i in soup.find_all('div', {'class': 'thumb_relate'}):
    try:
        f.write(i.text)
        article = i.find_all('a')[0].get('href')
        f.write(article + '\n')

        soup2 = bs(ur.urlopen(article).read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
        f.write('\n\n')
    except:
        pass

f.close()
