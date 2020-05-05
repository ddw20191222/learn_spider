#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 1_resquests_bilibili.py
# date: 2020.05.04
# website: https://www.bilibili.com/video/BV1kx411S7Fh?from=search&seid=17694479333795138682

__author__="ddw20191222"

import requests, os

header = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

def get_video(url):
	try:
		res = requests.get(url, headers=header, timeout=10)
		res.encoding = res.apparent_encoding
		# res.raise_for_status()
		return res.content
	except Exception as e:
		print("Error in get_video")

def write_file(filename, file):
	dir = "E:\\"
	path = dir + filename
	try:
		if not os.path.exists(path):
			with open(path, "wb") as f:
				f.write(file)
	except Exception as e:
		raise e
	


def main():
	url = "https://cn-zjnb-cmcc-v-05.bilivideo.com/upgcxcode/82/05/172730582/172730582-1-30032.m4s?expires=1588614600&platform=pc&ssig=WOJuJI_QVSnksw_I7FOrUQ&oi=3748144523&trid=5f6e3b4203414dbf8290c996b0914538u&nfc=1&nfb=maPYqpoel5MI3qOUX6YpRA==&mid=340407524&logo=80000000"
	filename = "qingaibeiyesi"
	file = get_video(url)
	write_file(filename, file)
	print("已经下载完成")
if __name__=="__main__":
	main()
