# -*- coding: utf-8 -*-
import urlparse
import datetime, time


class Throttle:
    """
        添加延迟在同一个域名中下载
    """
    def __init__(self, delay):
        self.delay = delay
        # 域名最后访问的时间戳
        self.domains = {}

    def wait(self, url):
        doamin = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(doamin)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        # 更新最后访问的时间
        self.domains[doamin] = datetime.datetime.now()