import os, re, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'http://quotes.toscrape.com'
soup = bs(ur.urlopen(url).read(), 'html.parser')
