import os, re, usecsv, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

soup = bs(ur.urlopen('http://quotes.toscrape.com').read(), 'html.parser')

quote = soup.find_all('div', {'class': 'quote'})

for i in quote:
    print(i.text)
