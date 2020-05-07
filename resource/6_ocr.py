#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 6_ocr.py
# date: 2020.05.05
# website: www.51zxw.com

__author__ = "ddw20191222"

from aip import AipOcr
import re
import requests

APP_ID="19733977"
API_KEY="YtNXpkb6xRpdL7AFtxELU9jw"
SECRET_KEY="MQ7E7GGGuT7qRmO4NWmp4lG1UpsX5cX0"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_image_data(filename):
	with open(filename, "rb") as f:
		return f.read()

filename = 'C:\\Users\\ddw\\Desktop\\图片文字识别\\aa.jpg'
image = get_image_data(filename)
data = client.basicGeneral(image)
print(data)