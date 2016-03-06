# -*- coding: utf-8 -*-
from day1.delay_download import Throttle
import random
import urllib2, urlparse


class Downloader:
    def __init__(self, delay=0, user_agent='wswp', proxies=None, num_retries=1, cache=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
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
                if self.num_retries >0 and 500 <= result['code'] < 600:
                    # 服务器错误 忽略缓存
                    result = None

        if result is None:
            self.throttle.wait(url)
            proxy = random(self.proxies) if self.proxies else None
            headers = {'user_agent': self.user_agent}
            result = self.download(url, headers, proxy, self.num_retries)
            if self.cache:
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxy, num_retries=0, data=None):
        request = urllib2.Request(url, headers=headers)
        # 支持代理的爬虫
        opener = urllib2.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme: proxy}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            html = urllib2.urlopen(request).read()
            code = urllib2.urlopen(request).code
        except urllib2.URLError as e:
            print 'Download error:', e.reason
            # html = None
            # if num_retries > 0:
            #     if hasattr(e, 'code') and 500 <= e.code < 600:
            #         return download(url, user_agent, num_retries-1)
        return {'html': html, 'code': code}

