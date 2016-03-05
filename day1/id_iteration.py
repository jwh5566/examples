# -*- coding: utf-8 -*-
import itertools
from download import download

# for page in itertools.count(1):  #id 从1开始
#     url = 'http://example.webscraping.com/view/-%d' %page
#     html = download(url)
#     if html is None:
#         break
#     else:
#         pass  #sucess
#

# 最多忽略5次连续id 出错
max_errors = 5
# 当前错误数
num_errors = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' %page
    html = download(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        # success
        num_errors = 0