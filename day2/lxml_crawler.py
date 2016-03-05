# -*- coding: utf-8 -*-
"""
    lxml使用css选择器提取数据
"""
import lxml.html
from day1.download import download

#
# beoken_html = '<ul class=country><li>Area<li>Population</ul>'
# tree = lxml.html.fromstring(beoken_html)
# fixed_html = lxml.html.tostring(tree, pretty_print=True)
# print fixed_html

url = 'http://example.webscraping.com/places/view/United-Kingdom-239'
html = download(url)
tree = lxml.html.fromstring(html)
# css 安装 pip install cssselect
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print area

