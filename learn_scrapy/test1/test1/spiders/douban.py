# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from test1.items import Test1Item

class DoubanSpider(scrapy.Spider):
	name = 'douban'
	print("douban")
	# allowed_domains = ['douban.com']	# 为list
	start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0']
	# items = []							# 亦为list
	def parse(self, response):
		html = response.body.decode()
		with open("mu.html", "w") as f:
			f.write(html)
		pat_rate = re.compile('"rate":"(.*?)","cover_x":.*?,"title":".*?"')
		pat_title = re.compile('"rate":".*?","cover_x":.*?,"title":"(.*?)"')
		rate_list = re.findall(pat_rate, html)
		title_list = re.findall(pat_title, html)
		for i in range(len(rate_list)):
			item = Test1Item()
			item['order'] = i + 1
			item['title'] = title_list[i]
			item['rate'] = rate_list[i]
			yield item	
		# 	items.append(dict(item))
		# for item in items:
		# 	print(items)
		# return items	
# scrapy startproject xx
# scrapy genspider xxxx "http:"

# items.py 写目标
# 编写spiders/xxx.py 处理相应，以及爬取数据（yield items）
# 编写pipeline 处理items
# 更改setting