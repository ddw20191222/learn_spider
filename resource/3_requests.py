#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 3_requests.py
# date: 2020.05.03

__author__="ddw20191222"

# sample 1
import requests
import re


header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}
wd = {"wd": "中国"}
url = "http://www.baidu.com"
def test1():
	req = requests.get("http://www.baidu.com").content.decode()
	print(req)



def test2():
	req = requests.get("http://www.baidu.com/s", params=wd, headers=header)

	# req.text 字符串信息
	# req.content 二进制信息
	# req.content.decode() 二进制文件转换成字符串信息
	print(req, req.content.decode())


# def test3():
# 	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# 	key = "狗狗"
# 	formdata = {
# 	"i":key,
# 	"from":"AUTO",
# 	"to":"AUTO",
# 	"smartresult":"dict",
# 	"client":"fanyideskweb",
# 	"salt":"15503049709404",
# 	"sign":"3da914b136a37f75501f7f31b11e75fb",
# 	"ts":"1550304970940",
# 	"bv":"ab57a166e6a56368c9f95952de6192b5",
# 	"doctype":"json",
# 	"version":"2.1",
# 	"keyfrom":"fanyi.web",
# 	"action":"FY_BY_REALTIME",
# 	"typoResult":"false"
# 	}
# 	res = requests.post(url, headers=header, data= formdata)

# 	pat = r'"tgt":"(.*?)"}]]'
# 	result = re.findall(pat, res.text)
# 	print(result)


# sample4
# 设置ip地址
proxy={
	"http":"http://114.239.122.65:4216"
}
def test4():
	res = requests.get("http://www.baidu.com", proxies=proxy)
	print(res)


def test5():
	res = requests.get(url)
	cookiesdict = requests.utils.dict_from_cookiejar(res.cookies)
	print(cookiesdict, res.cookies)

def test6():
	# 使用session实现登陆
	# 创建session对象
	ses = requests.session()
	
	# 构造登陆的参数
	data={
	"submit_type": "user_login",
	"name": "SA19020033",
	"pass": "IFUWXU",
	"user_type": "2",
	"Submit": "LOG+IN"
	}
	# 通过传递用户名传递cookies
	ses.post(url, data= data)
	res = ses.get("http://epc.ustc.edu.cn/m_practice.asp?second_id=2001")
	print(res.text)

if __name__=="__main__":
	# test1()
	# test2()
	# test3()
	# test4()
	# test5()
	test6()