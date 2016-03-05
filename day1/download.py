# -*- coding: utf-8 -*-
"""
    从站点地图下载
"""
import urllib2
import re
import urlparse


def download(url, user_agent='wswp', proxy=None, num_retries=0):
    print 'Downloading:', url
    # 设置用户代理
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    # 支持代理的爬虫
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html


def crawl_sitemap(url):
    """
    站点地图url
    :param url:
    :return:
    """
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...


# download('http://httpstat.us/500')
if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')