#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 4_douban.py
# date: 2020.05.04
# website: https://www.51zxw.net/list.aspx?cid=732

__author__="ddw20191222"

import requests
import re

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

# 对于没有下一页的网站，使用开发者模式进行浏览，查找对应的url
# 豆瓣电影
# 第一页：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
# 第二页：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20
# 第三页：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=40
# url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=(i-1)*20"
def load_html(url):
	html = requests.get(url, headers = headers).text
	return html
def write_data(html):
	pat_rate = re.compile('"rate":"(.*?)","cover_x":.*?,"title":".*?"')
	pat_name = re.compile('"rate":".*?","cover_x":.*?,"title":"(.*?)"')
	rate_list = re.findall(pat_rate, html)
	name_list = re.findall(pat_name, html)
	for i in range(len(rate_list)):
		print(i+1, name_list[i], rate_list[i])

def douban_spider():
	start = 1
	end = 2
	url_first_part = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="
	print("number", "name", "rate")
	for i in range(start, end+1):
		print("正在查询第{}页".format(i))
		url = url_first_part + str((i - 1) * 20)
		html = load_html(url)
		write_data(html)
if __name__=="__main__":
	douban_spider()
