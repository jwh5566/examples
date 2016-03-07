# -*- coding: utf-8 -*-
import json, string
from day4.download import Downloader


template_url = 'http://example.webscraping.com/ajax/search.json?page={}&page_size=10&search_term={}'
countries = set()
D = Downloader()

for letter in string.uppercase:
    page = 0
    while True:
        html = D(template_url.format(page, letter))
        try:
            ajax = json.loads(html)
        except ValueError as e:
            print e
            ajax = None
        else:
            for record in ajax['records']:
                countries.add(record['country'])
                # print countries
        page += 1
        if ajax is None or page >= ajax['num_pages']:
            break
# print countries


open('countries.txt', 'w').write('\n'.join(sorted(countries)))