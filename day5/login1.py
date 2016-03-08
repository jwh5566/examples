# -*- coding: utf-8 -*-
import urllib, urllib2
import lxml.html


def parse_form(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data

LOGIN_URL = 'http://example.webscraping.com/user/login'
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
# data = {'email':LOGIN_EMAIL, 'password':LOGIN_PASSWORD}
# encoded_data = urllib.urlencode(data)
# request = urllib2.Request(LOGIN_URL, encoded_data)
# response = urllib2.urlopen(request)
# print response.geturl()

# import cookielib
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# import pprint
# html = opener.open(LOGIN_URL).read()
# data = parse_form(html)
# # pprint.pprint(form)
# data['email'] = LOGIN_EMAIL
# data['password'] = LOGIN_PASSWORD
# encoded_data = urllib.urlencode(data)
# request = urllib2.Request(LOGIN_URL, encoded_data)
# response = opener.open(request)
# print response.geturl()



import os, glob, json, time


def find_ff_sessions():
    """
    返回session的路径
    :return:
    """
    paths = [
            '~/.mozilla/firefox/*.default',
            '~/Library/Application Support/Firefox/Profiles/*.default',
            '%APPDATA%/Roaming/Mozilla/Firefox/Profiles/*.default'
            ]
    for path in paths:
        filename = os.path.join(path, 'sessionstore.js')
        matches = glob.glob(os.path.expanduser(filename))
        if matches:
            return matches[0]


def load_ff_sessions(session_filename):
    """
    分析sessions到 CookieJar对象
    :param session_filename:
    :return:
    """
    cj = cookielib.CookieJar()
    if os.path.exists(session_filename):
        json_data = json.loads(open(session_filename, 'rb').read())
        for window in json_data.get('windows', []):
            for cookie in window.get('cookies', []):
                c = cookielib.Cookie(0,
                    cookie.get('name', ''),
                    cookie.get('value', ''),
                    cookie.get('host', ''),
                    cookie.get('host', '').startswith('.'),
                    cookie.get('host', '').startswith('.'),
                    cookie.get('path', ''), False, False,
                    str(int(time.time()) + 3600 * 24 * 7),
                    False, None, None, {})
                cj.set_cookie(c)
    else:
        print '文件不存在'
    return cj

# session_filename = find_ff_sessions()
# cj = load_ff_sessions(session_filename)
# processor = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(processor)
# url = 'http://example.webscraping.com'
# html = opener.open(url).read()
# tree = lxml.html.fromstring(html)
# print tree.cssselect('ul#navbar li a')[0].text_content()



import mechanize
#   机械化登录 修改数据

COUNTRY_URL = 'http://example.webscraping.com/edit/United-Kingdom-239'

br = mechanize.Browser()
br.open(LOGIN_URL)
br.select_form(nr=0)   # 选择表单0
br['email'] = LOGIN_EMAIL
br['password'] = LOGIN_PASSWORD
response = br.submit()
br.open(COUNTRY_URL)
br.select_form(nr=0)
print br['population']
br['population'] = str(int(br['population']) + 1)
print br['population']
br.submit()









