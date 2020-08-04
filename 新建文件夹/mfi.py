#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: mfi.py
# date: 2020.05.05
# website: https://www.bilibili.com/video/BV1kx411S7Fh?from=search&seid=17694479333795138682

__author__="ddw20191222"

from bs4 import BeautifulSoup
import requests
import re
import bs4

header = {
	"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
	}

# cookies = r'soliao=A5146DC7CE5784E33F8FC0953BE1398D; Hm_lvt_f6c4e4598d33812086dc5e2503768e39=1596555883; Hm_lpvt_f6c4e4598d33812086dc5e2503768e39=1596559409; Qs_lvt_232808=1596555882; Qs_pv_232808=2884464672037185000%2C3359777378782894000%2C374224494645803400%2C4245573366232737000%2C1961411700885247200; Hm_lvt_35a4d1b9d054470bb751f0762ac388c1=1596555887; Hm_lpvt_35a4d1b9d054470bb751f0762ac388c1=1596559410; mediav=%7B%22eid%22%3A%22500307%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22sZ%3F%23Vf%3AYea%3AZz1-n%60%40qU%22%2C%22c…383884e7eb28-4c302273-100200-173ba259320f4; CNZZDATA1260905862=1621239961-1596554171-https%253A%252F%252Flink.zhihu.com%252F%7C1596554171; nb-referrer-hostname=www.soliao.com; nb-start-page-url=https%3A%2F%2Fwww.soliao.com%2Fitem%2F92559-hdpei454404.html; username=15256280211; autoCookie="15256280211:1597160818624:f558440a3de5e01e4d25068c8c9c83a6417a027b"; _jfinal_captcha=4afd521d77158e02aed37e2274b90c9c; PRODUCT_HISTORY=%5B%22HDPE%22%5D; __asc=a038a509173ba26b98a9d341045; __auc=a038a509173ba26b98a9d341045'
cookie = r'15256280211:1597160818624:f558440a3de5e01e4d25068c8c9c83a6417a027b'
cookies = {
	"Cookies": cookie
}
def get_html_text(url):
	try:
		res = requests.get(url, headers = header, timeout = 1)
		res.raise_for_status()
		res.encoding = res.apparent_encoding
		# print(res.encoding, res.raise_for_status())
		return res.text
	except Exception as e:
		return "解析页面出租哦"


# 下面两行函数主要是为了获取产品的超链接

def get_href(url):
	text = get_html_text(url)
	hl = []
	pat_product_href = re.compile(r'href="/item/(.*?)" target="_blank" name="prdTableLink"')
	product_href = re.findall(pat_product_href, text)
	return product_href
	# for href in product_href:
	# 	h1.append(href)
	# return hl

def get_href_list():
	url11 = "https://www.soliao.com/kw?qt=HDPE&currentIndex="
	href_list_all = []
	for i in range(1, 3):
		url1 = url11 + str(i)
		product_href = get_href(url1) 
		for href in product_href:
			href_list_all.append(href)
	for i in href_list_all:
		print(i)
	return href_list_all

# 得到mfi
def get_product_text(url):
	try:
		res = requests.get(url, cookies = cookies, headers = header, timeout = 1) #cookies = cookies,
		res.raise_for_status()
		res.encoding = res.apparent_encoding
		# print(res.encoding, res.raise_for_status())
		return res.text
	except Exception as e:
		return "解析页面出租哦"

def get_mfi(url):
	text = get_product_text(url)

	pat_product_name = re.compile(r'data-type="name">(.*?)</span>')
	pat_product_mfi = re.compile(r'(.*?)</td><td width="20%" align="center">g/cm³</td>')
	# product_name = re.findall(pat_product_name, text)[0]
	product_mfi = re.findall(pat_product_mfi, text)[0]
	
	return product_mfi #, product_mfi


def main():
	url_21 = "https://www.soliao.com/item/"

	href_list_all = get_href_list()
	for href in href_list_all:
		url_2 = url_21 + href
		mfi = get_mfi(url_2)
		print(mfi)


if __name__=="__main__":
	main()
