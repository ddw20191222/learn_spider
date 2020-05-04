#!/d:\\awesome-python-webapp/www python3
# -*- coding: utf-8 -*-
# software: sublime
# name: spi1.py
# date: 2020.05.03

__author__ = "ddw20191222"

# sample 1
# from urllib import request
# import re
# import random
 

# def request_baidu():
# 	url = r"http://www.baidu.com"
# # 创建自定义对象 对抗反爬虫机制
# # 反爬虫机制
# # 1. 判断是否为浏览器访问 -- 伪装成浏览器 User-agent
# # 2. 

#    # User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko

# #构造request headers信息
# 	agent = [
# 	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
# 	"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
# 	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
# 	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
# 	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
# 	]
# # 自定义 urlopen
# # 代理：用其他的ip地址 cookie的高级功能， http/https(加密)

# 	header={
# 	"User-Agent": random.choice(agent)
# 	}

# 	# User-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
# 	req = request.Request(url, headers=header)
# 	response = request.urlopen(req).read().decode()
# 	pat = r"<title>(.*?)</title>"  # get data from regular expression
# 	# print(len(response), '\r\n', type(response))
# 	# print("-----------------------------------")
# 	# print(response)
# 	data = re.findall(pat, response)
# 	print(data)


# sample2
from urllib import request
# 反爬虫2： 判断请求来源的IP地址 --使用代理ip
# 121.237.148.179 	3000
import random


proxylist = [
	{"http":"121.237.148.179:3000"},
	{"http":"121.237.148.179:3000"},
	{"http":"121.237.148.179:3000"},
	{"http":"121.237.148.179:3000"},
	{"http":"121.237.148.179:3000"}
]


# 构建代理其对象
# proxy = random.choice(proxylist)
# proxy = {"http":"36.248.129.135:9999"}
proxy = {"http":"129.204.189.156:22"}
# 构建代理头
proxyhandler = request.ProxyHandler(proxy)
# 构建代理对象
opener = request.build_opener(proxyhandler)
# 构建访问对象
req = request.Request("https://www.baidu.com")
# res = opener.open(req)
res = opener.open(req)
def proxy():
	print(res.read())
if __name__=="__main__":
	# request_baidu()
	proxy()