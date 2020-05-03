#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 2_tieba.py
# date: 2020.05.03

__author__="ddw20191222"

from urllib import request
import urllib
import time

# # 分析url
# 第一页：https://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search
# 第二页：https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
# 第三页：https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
# 第四页：https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150
# 猜测 第一页的内容可以为https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0
# 验证成功
# 所以，第n页的url为：https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=(n-1)*50


# 反爬虫机制一，模拟登陆
header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

# def input_content():
# 	kw = input("请输入查询内容：")
# 	begin = input("请输入起始页：")
# 	end = input("请输入结束页：")
# 	return (kw, begin, end)

def load_html(i, url):
	print("page " + str(i) + " is downloading")
	req = request.Request(url, headers = header)
	html = request.urlopen(req).read()
	return html

def write_html(filename, html):
	print("正在保存: ", filename)
	with open(filename, "wb") as f:
		f.write(html)

def tieba_spider():
	# kw = input("请输入查询内容：")
	# begin = input("请输入起始页：")
	# end = input("请输入结束页：")
	kw = "python"
	begin = 1
	end = 4
	print("----------------start---------------------------")
	website = "https://tieba.baidu.com/f?"
	# input_content = input_content()
	# kw = input_content.[0]
	key = {"kw": kw}
	keyword = urllib.parse.urlencode(key)
	url = website + keyword + "&ie=utf-8"
	# print(url)

	for i in range(begin, end + 1):
		# print("page " + str(start) + " is downloading")
		fullurl = url + "&pn=" + str((i - 1) * 50)
		filename = "E:\\learn_spider\\product\\Page_" + str(i) +".html"
		html = load_html(i, fullurl)
		write_html(filename, html)
		time.sleep(5)
	print("------------------end----------------------------")
	# load_html()
	# write_html()

if __name__=="__main__":
	tieba_spider()