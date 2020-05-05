#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 3_stack.py
# date: 2020.05.05
# website: https://www.bilibili.com/video/BV1kx411S7Fh?from=search&seid=17694479333795138682

__author__="ddw20191222"

from bs4 import BeautifulSoup
import requests
import re
import bs4

header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

def get_html_text(url):
	try:
		res = requests.get(url, headers = header, timeout = 10)
		res.raise_for_status()
		res.encoding = res.apparent_encoding
		return res.text
	except Exception as e:
		return "解析页面出租哦"
	

def get_stack_code(url):
	stack_html = get_html_text(url)
	stack_soup = BeautifulSoup(stack_html, "html.parser")
	# print(stack_soup.prettify())
	list_stack_code = []
	for a in stack_soup.find_all("a"):
		try:
			if isinstance(a, bs4.element.Tag):
				href = a.attrs["href"]
				pat_stack_code = re.compile(r'^/stockdata/(.*?).html$')
				stack_code = re.findall(pat_stack_code, href)[0]  # 这个[0]是啥意思，返回匹配列表的第一个？
				# for code in stack_code:
				# 	if re.match(r'\d{6}')
				list_stack_code.append(stack_code)
		except Exception as e:
			continue
	return list_stack_code
def get_stack_info(web, list):
	for i in list:
		url = web + str(i)
		html = get_html_text(url)
		try:
			if html == "":
				continue
			infoDict = {}
			soup = BeautifulSoup(html, "html.parser")
			stack_name = soup.find('h1').text.split(" ")[0]
			print(stack_name)
			infoDict.update({"name": stack_name})
			Stockinfo = soup.find("div", attrs={"class":"detail-data"})
			print(Stockinfo.prettify())
			if isinstance(Stockinfo, bs4.element.Tag):
				keyInfo = Stockinfo.find_all("dt")
				ValueInfo = Stockinfo.find_all("dd")
				for i in range(4):
					key = keyInfo[i].text
					value = ValueInfo[i].text
					infoDict[key] = value
					# print(key, value)			
def main():
	stock_website_url = "http://data.eastmoney.com/bbsj/201912.html"
	stacklist = []
	# 网站： http://www.cninfo.com.cn/new/disclosure/stock?orgId=DR0000021&stockCode=603056
	stock_info_url = "https://www.laohu8.com/stock/"
	# get_stack_code(stock_website_url)
	list_stack_code = get_stack_code(stock_website_url)
	get_stack_info(stock_info_url, list_stack_code)


if __name__=="__main__":
	main()