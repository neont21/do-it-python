import os, re, usecsv, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

soup = bs(ur.urlopen('https://news.daum.net').read(), 'html.parser')

headline = soup.find_all('div', {'class': 'item_issue'})
for item in headline:
    print(item.text, '\n')

    soup = bs(ur.urlopen(item.find_all('a')[0].get('href')).read(), 'html.parser')
    for para in soup.find_all('p'):
        print(para.text)

