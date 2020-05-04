#!/d:\\awesome-python-webapp/www python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 2_get.py
# date: 2020.05.03


__author__="ddw20191222"

from urllib import request
import urllib

url = "http://www.baidu.com/s?"
wd = {"wd":"北京"}
wdd = urllib.parse.urlencode(wd)
# print(wdd)
url = url+wdd

req = request.Request(url)
res = request.urlopen(req).read().decode()

print(res)