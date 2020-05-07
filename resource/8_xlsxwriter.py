#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 8_xlsxwriter.py
# date: 2020.05.05
# website: www.51zxw.com

__author__ = "ddw20191222"

import xlsxwriter
def test01():
	# 创建文件（Workbook）并且创建工作表（add_worksheet)
	workbook = xlsxwriter.Workbook("C:\\Users\\ddw\\Desktop\\demo.xlsx")
	worksheet = workbook.add_worksheet()
	
	# 在制定位置写入数据
	worksheet.write("A1", "52zxw.com")
	worksheet.write("A2", "I love work with xlsx")
	
	# close
	workbook.close()

from bs4 import BeautifulSoup
import requests
import os

header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

# 使用request得到网页信息
def get_html_text(url):
	try:
		res = requests.get(url, headers = header, timeout = 10)
		res.raise_for_status()					# 如果返回值不是200，则抛出错误
		res.encoding = res.apparent_encoding	# 将编码固定下来
		return res.text 
	except Exception as e:
		return "解析页面出错哦"

def get_article_code(url_first_part, start, end, worksheet):
	article_code = []
	for i in range(start, end + 1):
		url_full = url_first_part + str(i) + '/'
		html = get_html_text(url_full)
		soup = BeautifulSoup(html, "html.parser")
		# 分析内容见补充内容2	
		IdInfo = soup.find_all("li", attrs = {"class":"item typs_video"})
		# print(IdInfo)
		for i in IdInfo:
			Id = i.attrs["id"].split("_")[2]			# 寻找href会寻找到多个内容，但是 li 标签属性 id="qiushi_tag_123053773"，已经说明了这个数字的唯一性，去id中的参数更加明确
			article_code.append(Id)

	for i in range(len(article_code)):
		# 在制定位置写入数据
		worksheet.write('A'+str(i+1), i+1)
		worksheet.write('B'+str(i+1), article_code[i])
		# worksheet.write('C'+str(i+1), article_text[2])
		# close

	
	return article_code

def get_article_text(url):

	html = get_html_text(url)
	soup = BeautifulSoup(html, "html.parser")
	# 分析article源代码，见补充3
	# print(soup)
	title = soup.html.head.title.text.split(" ")[0]
	# print(title)
	date = soup.find("span", attrs={"class":"stats-time"}).text
	vote = soup.find("span", attrs={"class":"stats-vote"}).i.text
	return [title, date, vote]



def qsbk_spider():
	workbook = xlsxwriter.Workbook("C:\\Users\\ddw\\Desktop\\demo.xlsx")
	worksheet = workbook.add_worksheet()
	start, end = 1, 2
	print("{:^10}{:^20}{:^10}".format('-----', 'Start', '-----'))
	url_first_part = "https://www.qiushibaike.com/8hr/page/"
	url_first_part_article = "https://www.qiushibaike.com/article/"
	article_code = get_article_code(url_first_part, start, end, worksheet)
	print(article_code)
	count = 0
	for i in range(len(article_code)):
		count += 1
		url_article = url_first_part_article + str(article_code[i])
		article_text = get_article_text(url_article)
		worksheet.write('C'+str(i+1), article_text[0])
		worksheet.write('D'+str(i+1), article_text[1])
		worksheet.write('E'+str(i+1), article_text[2])

		print(article_text)

		with open("E:\\learn_spider\\product\\qiushibaike.md", "a", encoding = "utf-8") as f:
			f.write(str(article_text) + '\n')
	print("{:^10}{:^20}{:^10}".format('-----', 'End', '-----'))
	workbook.close()


# if __name__=="__main__":
# 	qsbk_spider()

if __name__ == '__main__':
	print("{:^10}{:^20}{:^10}".format('-----', 'Start', '-----'))
	qsbk_spider()
	print("{:^10}{:^20}{:^10}".format('-----', 'End', '-----'))