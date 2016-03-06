# -*- coding: utf-8 -*-
import csv, re, lxml.html
from day1.link_crawler import link_crawler


class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country',
                        'capital', 'continent', 'tld', 'currency_code',
                        'currency_name', 'phone', 'postal_code_format',
                        'postal_code_regex', 'languages',
                        'neighbours')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        if re.search('/index/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
                # print tree.cssselect('table > tr#places_{}__row > td.w2p_fw' % field)[0].text_content()
                # print row
            self.writer.writerow(row)

link_crawler('http://example.webscraping.com/', '/index', scrape_callback=ScrapeCallback())
