# -*- coding: utf-8 -*-
import  re
from download import download
import urlparse


def link_crawler(seed_url, link_regex):
    """
        抓取匹配link_regex的url(seed_url+links)
    :param seed_url:
    :param link_regex:
    :return:
    """
    crawl_queue = [seed_url]
    seen = set(crawl_queue)  # 去除重复链接
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # 过滤匹配link_regex的链接
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)  #绝对地址
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    """
        从html源码返回link的列表
    :param html:
    :return:
    """
    # 利用正则提取链接 匹配单|双引号包含的内容
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com', '/(index|view)/')