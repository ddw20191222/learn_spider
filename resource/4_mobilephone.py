#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 4_mobilephone.py
# date: 2020.05.04
# website: https://www.51zxw.net/list.aspx?cid=732

__author__="ddw20191222"

import requests
import re

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}
# 从文章的源代码中查找电话号码
url = "http://ww.hao123.com/haoserver/tefudh.htm?tn=94576225_hao_pg"
# 分析源代码结构
          # <td class=f15>兴业银行</td>[\s\S]*?<td class=f15>95561</td>
res = requests.get(url, headers= headers).content.decode('gb2312')
# print(res)

pat1 = re.compile(r"<td class=f15>(.*?)</td>[\s\S]*?<td class=f15>.*?</td>")
pat2 = re.compile(r"<td class=f15>.*?</td>[\s\S]*?<td class=f15>(.*?)</td>")
Name = pat1.findall(res)
Phone = pat2.findall(res)
for i in range(len(Name)):
	print(Name[i], Phone[i])


