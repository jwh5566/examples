# -*- coding: utf-8 -*-
# def link_crawler(..., max_depth=2):
#     max_depth = 2
#     seen = {}
#     ...
#     depth = seen[url]
#     if depth != max_depth:
#         for link in links:
#             if link not in seen:
#                 seen[link] = depth + 1  #追踪一次就+1
#                 crawl_queue.append(link)
