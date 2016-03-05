# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import lxml.html
import time
from day1.download import download


FIELDS = ('area', 'population', 'iso', 'country', 'capital',
'continent', 'tld', 'currency_code', 'currency_name', 'phone',
'postal_code_format', 'postal_code_regex', 'languages',
'neighbours')


def re_scraper(html):
    result = {}
    for field in FIELDS:
        result[field] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
    return result


def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    for field in FIELDS:
        result[field] = soup.find('table').find('tr', id='places_%s__row' % field).find('td', class_='w2p_fw').text
    return result


def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    result = {}
    for field in FIELDS:
        result[field] = tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()
        return result

NUM_ITERATIONS = 1000
html = download('http://example.webscraping.com/places/view/United-Kingdom-239')

for name, scraper in [('re',re_scraper), ('bs',bs_scraper), ('lxml',lxml_scraper)]:
    # 记录开始时间
    start = time.time()
    for i in range(NUM_ITERATIONS):
        if scraper == re_scraper:
            re.purge() # 清除正则缓存
        result = scraper(html)
        assert (result['area'] == '244,820 square kilometres')
    end = time.time()
    print '%s: %.2f seconds' %(name, end-start)

# Downloading: http://example.webscraping.com/places/view/United-Kingdom-239
# re: 8.82 seconds
# bs: 79.15 seconds
# lxml: 2.94 seconds
#
# Process finished with exit code 0

