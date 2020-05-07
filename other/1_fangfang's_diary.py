#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 1_方方的武汉疫情日记.py
# date: 2020.05.06
# website: 


__author__="ddw20191222"

from bs4 import BeautifulSoup
import requests
import re
import bs4
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

def get_article_href(url):
	article_href = []
	article_title = []
	html = get_html_text(url)
	soup = BeautifulSoup(html, "html.parser")
	# print(soup.prettify())
	for a in soup.find_all('a', attrs= {"target":"_blank"}):
		# print(a.text, a["href"])
		article_title.append(a.text)
		article_href.append(a['href'])
	return [article_title, article_href]




def get_article():
	pass

def article_spider():
	url = "http://www.fbabi.com/bulletin/fangfangriji/"
	filename = "E:\\learn_spider\\product\\方方武汉日记.txt"
	count = 0
	article_href = get_article_href(url)[1]
	article_href = get_article_href(url)[1]
	html_pat = re.compile(r"http://www.fbabi.com/zaker/[0-9]+.html")
	for i in article_href:
		count += 1
		if re.match(html_pat, i) == None:
			break
		print(count, i)

if __name__=="__main__":
	article_spider()