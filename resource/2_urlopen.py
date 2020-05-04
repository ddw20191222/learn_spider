#!/d:\\awesome-python-webapp/www python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 2_urlopen.py
# date: 2020.05.03

from urllib import request

# 构建处理器对象
http_header=request.HTTPHandler()
# 创建自定opener
opener=request.build_opener(http_header)

# 创建自定义请求对象
req = request.Request("http://www.baidu.com")
# 发送请求，活儿响应

# response=opener.open(req).read().decode()

# 将自定义open设置为全局open，所有的请求都是用自定义的opener
request.install_opener(opener)
response=opener.urlopen(req).read().decode()

print(response)