#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 2_youdao.py
# date: 2020.05.03


__author__="ddw20191222"

from urllib import request
import urllib
import re
# 反爬虫机制一，模拟登陆
header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
key = "狗狗"
formdata = {
	"1": key,
	"from":	"AUTO",
	"to":	"AUTO",
	"smartresult":	"dict",
	"client":	"fanyideskweb",
	"salt":	"15885202997456",
	"sign":	"961b98045910ed52eaf9681804d3bffb",
	"ts":	"1588520299745",
	"bv":	"e2a78ed30c66e16a857c5b6486a1d326",
	"doctype":	"json",
	"version":	"2.1",
	"keyfrom":	"fanyi.web",
	"action":	"FY_BY_REALTlME"
}

# data = urllib.parse.urlencode(fromdata).encode(encoding='utf-8')

# req = request.Request(url, data=data, headers=header)
# res = request.urlopen(req).read().decode()
data=urllib.parse.urlencode(formdata).encode(encoding='utf-8')

req=request.Request(url,data=data,headers=header)

resp=request.urlopen(req).read().decode()

# pat = r'"tgt":"(.*?)"}]]'


# print(re.findall(pat, res))
print(resp)


# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
