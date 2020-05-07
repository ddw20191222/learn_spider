#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 6_糗事百科.py
# date: 2020.05.05
# website: www.51zxw.com

__author__ = "ddw20191222"

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

def get_article_code(url_first_part, start, end):
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
	start, end = 1, 3
	print("{:^10}{:^20}{:^10}".format('-----', 'Start', '-----'))
	url_first_part = "https://www.qiushibaike.com/8hr/page/"
	url_first_part_article = "https://www.qiushibaike.com/article/"
	article_code = get_article_code(url_first_part, start, end)
	print(article_code)
	count = 0
	for i in article_code:
		count += 1
		url_article = url_first_part_article + str(i)
		article_text = get_article_text(url_article)
		# print(article_text)
		with open("E:\\learn_spider\\product\\qiushibaike.md", "a", encoding = "utf-8") as f:
			f.write(str(article_text) + '\n')
	print("{:^10}{:^20}{:^10}".format('-----', 'End', '-----'))


if __name__=="__main__":
	qsbk_spider()

'''
补充
1. 分析网页url
	第一页： https://www.qiushibaike.com/
	第二页： https://www.qiushibaike.com/8hr/page/2/
	第三页： https://www.qiushibaike.com/8hr/page/3/

	最后确认url的地址为
	第n页： https://www.qiushibaike.com/text/page/n/
2. 分析网页源代码，
	找到对应的百科的url，直接点击其中一个超链接，得到url
	https://www.qiushibaike.com/article/123074889
	其中有一个确定的参数 "article/123074889"
	按标题进行搜索，得到下面内容

<li class="item typs_video" id='qiushi_tag_123074889'>
<a class="recmd-left video" href="/article/123074889" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">
<img src="//qiubai-video-web.qiushibaike.com/L8FPI216FEVX07BH_hd.jpg?imageView2/1/w/150/h/112" alt="工作之余拯救了一架飞">
<div class="recmd-tag">0:13</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/123074889" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">工作之余拯救了一架飞机</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

	查找数字，发现多次出现，且"www.qiushibaike.com"+href, 即为文章的源代码。故直接得到利用标签的属性attrs的到href

3. 分析article源代码
	发现文章错误了。本来是要下载text的，但是找错了地方。所以现在就下载title了。	

<h1 class="article-title">
萌萌哒逗兔子的糗事：解决了我多年的疑惑</h1>
<div class="stats">
<span class="stats-time">
2020-04-29 17:36
</span>

<span class="stats-vote">好笑数：<i class="number">284</i></span>

'''