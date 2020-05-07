# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from novel.items import NovelItem

class SyqrlSpider(scrapy.Spider):
	name = 'syqrl'
	# allowed_domains = ['http://www.biquge.info69_69120/']
	start_urls = ['http://www.biquge.info/69_69120/']


	def parse_chapter(self, response):
		html_chapter = response.body
		soup = BeautifulSoup(html_chapter, "html.parser")
		item = NovelItem()

		item['chapter'] = soup.find('div', attrs={"class":"bookname"}).h1.text
		item['content'] = soup.find('div', attrs={"id":"content"}).text.replace("<br>", '')
		yield item
	
	def parse(self, response):
		url_book = "http://www.biquge.info/69_69120/"
		href_chapter_list = response.xpath("//div//dd/a/@href").extract()
		for href in href_chapter_list:
			url = url_book + str(href)
			yield Request(url, callback=self.parse_chapter) 



	# def parse(self, response):
	# 	html_book = response.body
	# 	soup = BeautifulSoup(html_book, "html.parser")
	# 	href_chapter_list = []
	# 	for dd in soup.find("dl").children:
	# 		href_chapter_list.append(dd.a["href"])
	# 	for href in href_chapter_list:
	# 		url = url_book + str(href)
	# 		yield Request(href, callback=parse_chapter) 
	# def parse_chapter(self, response):
	# 	html_chapter = response.body
	# 	soup = BeautifulSoup(html_chapter, "html.parser")
	# 	item = NovelItem()

	# 	item['chapter'] = soup.find('div', attrs={"class":"bookname"}).h1.text
	# 	item['content'] = soup.find('div', attrs={"id":"content"}).text.replace("<br>", '')
	# 	yield item

