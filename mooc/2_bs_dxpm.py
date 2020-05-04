#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 2_bs_dxpm.py
# date: 2020.05.04
# website: https://www.bilibili.com/video/BV1kx411S7Fh?from=search&seid=17694479333795138682

__author__="ddw20191222"


import bs4
import requests
from bs4 import BeautifulSoup
# 测试BeautifulSoup库的基本用法
def test(): 
	html = '<tr class="alt"><td>459</td><td><div align="left">黄山学院</div></td><td>安徽</td>\
<td>26.3</td><td class="hidden-xs need-hidden indicator5">26.3</td><td class="hidden-xs need-hidden indicator6"\
style="display: none;">96.72%</td><td class="hidden-xs need-hidden indicator7"\
style="display: none;">125</td>\
<td class="hidden-xs need-hidden indicator8"\
style="display: none;">0.576</td>\
<td class="hidden-xs need-hidden indicator9"\
style="display: none;">0</td>\
<td class="hidden-xs need-hidden indicator10"\
style="display: none;">0</td>\
<td class="hidden-xs need-hidden indicator11"\
style="display: none;">1341</td>\
<td class="hidden-xs need-hidden indicator12"\
style="display: none;">0</td>\
<td class="hidden-xs need-hidden indicator13"\
style="display: none;">0.05%</td></tr>'
	soup = BeautifulSoup(html, "html.parser")
	print(soup.prettify())

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
		print("there are somethin wrong")
		return ""

def fill_univ_list(html, ulist):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find("tbody").children: # 此处应该是find， 而非findall
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')					# 表示取出tr中的所有td标签
			ulist.append([tds[0].string, tds[1].string, tds[2].string])
	# tr标签中的内容，第一个td表示排名，第二个表示学校名称，第三个表示地址
	# <!-- <tr class="alt">
	# 	<td>459</td>
	# 	<td><div align="left">黄山学院</div></td>
	# 	<td>安徽</td>
	# 	<td>26.3</td>
	# 	<td class="hidden-xs need-hidden indicator5">26.3</td>
	# 	<td class="hidden-xs need-hidden indicator6"
	# 		style="display: none;">96.72%</td>
	# 	<td class="hidden-xs need-hidden indicator7"
	# 		style="display: none;">125</td>
	# 	<td class="hidden-xs need-hidden indicator8"
	# 		style="display: none;">0.576</td>
	# 	<td class="hidden-xs need-hidden indicator9"
	# 		style="display: none;">0</td>
	# 	<td class="hidden-xs need-hidden indicator10"
	# 		style="display: none;">0</td>
	# 	<td class="hidden-xs need-hidden indicator11"
	# 		style="display: none;">1341</td>
	# 	<td class="hidden-xs need-hidden indicator12"
	# 		style="display: none;">0</td>
	# 	<td class="hidden-xs need-hidden indicator13"
	# 		style="display: none;">0.05%</td>
	# </tr> -->

def print_univ_list(ulist, num):
	tplt = "{0:^10}{1:{3}^10}{2:^10}"
	print(tplt.format("排名", "大学", "地址", chr(12288)))
	for i in range(num):
		u = ulist[i] 
		print(tplt.format(u[0], u[1], u[2], chr(12288)))
	pass
def main():
	uinfo = []
	url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
	html_text = get_html_text(url)
	fill_univ_list(html_text, uinfo)
	print_univ_list(uinfo, 20)

if __name__=="__main__":
	# test()
	main()