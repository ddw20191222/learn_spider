# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class Test1Pipeline:
	def __init__(self):
		self.file = open("douban.md", "w")
	def process_item(self, item, spider):
		line = str(item)
		self.file.write(line)
		self.file.write('\n')
		return item
		
		return item
	def close_spider(self, spider):
		self.file.close()