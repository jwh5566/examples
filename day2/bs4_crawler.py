# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

broken_html = '<ul class=country><li>Area<li>Population</ul>'
# 分析html
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()  #补齐有点问题
print fixed_html
ul = soup.find('ul', attrs={'class': 'country'})
result = ul.find_all('li')
print result

#  [<li>Area<li>Population</li></li>, <li>Population</li>]
