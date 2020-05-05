#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 3_stack2.py
# date: 2020.05.05
# website: https://www.bilibili.com/video/BV1kx411S7Fh?from=search&seid=17694479333795138682
# it is modified from 3_stack.py

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
	
# 得到股票的编码
def get_stack_code(url):					
	stack_html = get_html_text(url)									# 直接利用函数得到页面信息
	stack_soup = BeautifulSoup(stack_html, "html.parser")			# 将页面进行解析
	# print(stack_soup.prettify())
	list_stack_code = []											# 设置股票编码存储方式为list
	for a in stack_soup.find_all("a"):								# 发现所有的a标签，并且找到全部内容
		try:
			if isinstance(a, bs4.element.Tag):
				href = a.attrs["href"]								# 注意，此处返回的href的格式为list
				pat_stack_code = re.compile(r'^/stockdata/(.*?).html$')
				stack_code = re.findall(pat_stack_code, href)[0]  	# 如果不加这个0，返回值有很多空格，不知道为什么
				# for code in stack_code:							# 此处推荐学习正则表达式的网址 https://www.bilibili.com/video/BV1N64y1u7Ty?from=search&seid=12587613398178417648
				# 	if re.match(r'\d{6}')
				list_stack_code.append(stack_code)					
		except Exception as e:										# 如果存在异常或错误，继续执行
			continue
	return list_stack_code
def get_stack_info(web, list):
	count = 0							# 用来在最后打印下载进度的
	for i in list:
		count += 1
		url = web + str(i)
		html = get_html_text(url)

		if html == "":
			continue
		infoDict = {}					# 将存放内容的方式设为字典（数据稳定）
		soup = BeautifulSoup(html, "html.parser")
		stack_name = soup.find('h1').text.split(" ")[0]				# 根据下面的补充内容1，选择的公司名字
		# print(stack_name)
		infoDict.update({"name": stack_name})						# 将公司名导入到字典
		Stockinfo = soup.find("div", attrs={"class":"detail-data"})	# 此处查询，来自补充内容2，注意，属性要使用字典
		# print(Stockinfo.prettify())								# 补充内容2的来源
		if isinstance(Stockinfo, bs4.element.Tag):					
			keyInfo = Stockinfo.find_all("dt")						# 补充内容2中，dt存储key，dd存储value
			ValueInfo = Stockinfo.find_all("dd")
			for i in range(4):										# 数据太多，仅选择前面4个
				key = keyInfo[i].text 								# 得到一个标签中的中间部分内容
				value = ValueInfo[i].text
				infoDict[key] = value
			with open("E:\\learn_spider\\product\\stack.md", "a", encoding = "utf-8") as f:
				f.write(str(infoDict) + '\n')						# 上面重新确定一下编码方式，不然可能会乱码的
				
				print("\r当前速度：{:.2f}%".format(count * 100/len(list)), end = '')
				# print(key, value)
		print("number {} has been loaden".format(count))
		
def stack_spider():
	stock_website_url = "http://data.eastmoney.com/bbsj/201912.html"
	stacklist = []
	# 网站： http://www.cninfo.com.cn/new/disclosure/stock?orgId=DR0000021&stockCode=603056
	stock_info_url = "https://www.laohu8.com/stock/"
	# get_stack_code(stock_website_url)
	list_stack_code = get_stack_code(stock_website_url)
	get_stack_info(stock_info_url, list_stack_code)


if __name__=="__main__":
	stack_spider()


补充，
1. 最难点是第三个函数，需要一些补充内容：bf4的使用方式（产生对象，查询，使用相关的参数得到内容，必要时候需要使用字符串分割）
	查询的参数： name，attrs， text， kwargs
	标签的参数：无（所有）， name， content， text，attrs， comment
2. 公司名的来源：公司名是来自于标签 <h1 class="name">德邦股份<!-- --> (SH:603056)</h1>
3. 公司信息，来自于 <div class="detail-data" style="height:80px">...(很多信息)</div>， 因为内容太多，所以仅仅取前面几个参数，并没有取完（我又不做金融，那些数字看不懂）
	股票信息的部分内容在下方，当然还有更多的数据在其他的标签中，如图表数据等等
<div class="detail-data" style="height:80px">
 <dl>
  <dt>
   最高
  </dt>
  <dd>
   --
  </dd>
  <dt>
   最低
  </dt>
  <dd>
   --
  </dd>
  <dt>
   成交量
  </dt>
  <dd>
   417万
  </dd>
  <dt>
   成交额
  </dt>
  <dd>
   4,054万
  </dd>
 </dl>
 <dl>
  <dt>
   今开
  </dt>
  <dd>
   --
  </dd>
  <dt>
   昨收
  </dt>
  <dd>
   9.58
  </dd>
  <dt>
   日振幅
  </dt>
  <dd>
   3.34%
  </dd>
  <dt>
   换手率
  </dt>
  <dd>
   1.92%
  </dd>
 </dl>
 <dl>
  <dt>
   总市值
  </dt>
  <dd>
   94.08亿
  </dd>
  <dt>
   流通市值
  </dt>
  <dd>
   21.33亿
  </dd>
  <dt>
   总股本
  </dt>
  <dd>
   9.60亿
  </dd>
  <dt>
   流通股本
  </dt>
  <dd>
   2.18亿
  </dd>
 </dl>
 <dl>
  <dt>
   52周最高
  </dt>
  <dd>
   --
  </dd>
  <dt>
   52周最低
  </dt>
  <dd>
   --
  </dd>
  <dt>
   市盈率
  </dt>
  <dd>
   --
  </dd>
  <dt>
   市净率
  </dt>
  <dd>
   2.36
  </dd>
 </dl>
 <dl>
  <dt>
   股息
  </dt>
  <dd>
   --
  </dd>
  <dt>
   股息收益率
  </dt>
  <dd>
   --
  </dd>
  <dt>
   ROA
  </dt>
  <dd>
   --
  </dd>
  <dt>
   ROE
  </dt>
  <dd>
   --
  </dd>
 </dl>
 <dl>
  <dt>
   每股收益
  </dt>
  <dd>
   --
  </dd>
 </dl>
</div>








<div class="detail-data" style="height:80px">
 <dl>
  <dt>
   最高
  </dt>
  <dd>
   --
  </dd>
  <dt>
   最低
  </dt>
  <dd>
   --
  </dd>
  <dt>
   成交量
  </dt>
  <dd>
   417万
  </dd>
  <dt>
   成交额
  </dt>
  <dd>
   4,054万
  </dd>
 </dl>
 <dl>
  <dt>
   今开
  </dt>
  <dd>
   --
  </dd>
  <dt>
   昨收
  </dt>
  <dd>
   9.58
  </dd>
  <dt>
   日振幅
  </dt>
  <dd>
   3.34%
  </dd>
  <dt>
   换手率
  </dt>
  <dd>
   1.92%
  </dd>
 </dl>
 <dl>
  <dt>
   总市值
  </dt>
  <dd>
   94.08亿
  </dd>
  <dt>
   流通市值
  </dt>
  <dd>
   21.33亿
  </dd>
  <dt>
   总股本
  </dt>
  <dd>
   9.60亿
  </dd>
  <dt>
   流通股本
  </dt>
  <dd>
   2.18亿
  </dd>
 </dl>
 <dl>
  <dt>
   52周最高
  </dt>
  <dd>
   --
  </dd>
  <dt>
   52周最低
  </dt>
  <dd>
   --
  </dd>
  <dt>
   市盈率
  </dt>
  <dd>
   --
  </dd>
  <dt>
   市净率
  </dt>
  <dd>
   2.36
  </dd>
 </dl>
 <dl>
  <dt>
   股息
  </dt>
  <dd>
   --
  </dd>
  <dt>
   股息收益率
  </dt>
  <dd>
   --
  </dd>
  <dt>
   ROA
  </dt>
  <dd>
   --
  </dd>
  <dt>
   ROE
  </dt>
  <dd>
   --
  </dd>
 </dl>
 <dl>
  <dt>
   每股收益
  </dt>
  <dd>
   --
  </dd>
 </dl>
</div>