# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NovelPipeline:
	def __init__(self):
		self.file = open("syqrl.md", "w", encoding = 'utf-8')
	def process_item(self, item, spider):
		line = str(dict(item)) + '\r\n\r\n'
		print(line)
		self.file.write(str(dict(item)))
		return item
	def close_spider(self, spider):
		self.file.close()


