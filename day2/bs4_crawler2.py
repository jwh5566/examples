# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from day1.download import download


url = 'http://example.webscraping.com/places/view/United-Kingdom-239'
html = download(url)
soup = BeautifulSoup(html)
# 找到tr
tr = soup.find(attrs={'id': 'places_area__row'})
td = tr.find(attrs={'class': 'w2p_fw'})
area = td.text
print area