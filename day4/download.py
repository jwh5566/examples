# -*- coding: utf-8 -*-
from day1.delay_download import Throttle
import urllib2, urlparse, random
import json


class Downloader:
    def __init__(self, delay=0, user_agent='wswp', proxy=None, num_retries=1, cache=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxy = proxy
        self.num_retries = num_retries
        self.cache = cache

    def __call__(self, url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries > 0 and 500 < result['code'] < 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            proxy = random.choice(self.proxy) if self.proxy else None
            headers = {'User-agent': self.user_agent}
            result = self.download(url, headers, proxy, self.num_retries)
            if self.cache:
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxy, num_retries, data=None):
        print 'Downloading:', url
        request = urllib2.Request(url, headers=headers)
        # 支持代理的爬虫
        opener = urllib2.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme: proxy}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            response = urllib2.urlopen(request)
            html = response.read()
            code = response.code
        except urllib2.URLError as e:
            print 'Download error:', str(e)
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= e.code < 600:
                    print '服务器内部错误'
                    # return download(url,  num_retries-1)
        return {'html': html, 'code': code}


# D = Downloader()
# html = D('http://example.webscraping.com/ajax/search.json?&search_term=B&page_size=10&page=0')  #返回一个json对象
# # print html
# print json.loads(html)
# print json.loads(html)['num_pages']


# http://example.webscraping.com/ajax/search.json?&search_term=B&page_size=10&page=0

# import csv
#
# FIELDS = ('pretty_link', 'country', 'id')
# writer = csv.writer(open('countries.csv', 'w'))
# writer.writerow(FIELDS)
# D = Downloader()
# html = D('http://example.webscraping.com/ajax/search.json?page=0&page_size=1000&search_term=.')
# ajax = json.loads(html)
# for record in ajax['records']:
#     row = [record[field] for field in FIELDS]
#     print row
#     writer.writerow(row)

# {u'pretty_link': u'<div><a href="/view/Afghanistan-1"><img src="/places/static/images/flags/af.png" /> Afghanistan</a></div>', u'country': u'Afghanistan', u'id': 636553}


