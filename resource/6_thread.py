#!/d:\\learn_spider\\mooc python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 6_糗事百科.py
# date: 2020.05.05
# website: www.51zxw.com

__author__ = "ddw20191222"

import requests
import threading
import queue
import time
import re

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

# 定义采集数据线程
class get_html_data(threading.Thread):
    """docstring for get_html_data"""
    def __init__(self, threadName, pageQueue, dataQueue):
        super(get_html_data, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}
        
    def run(self):
        print("启动线程", self.threadName)
        while not flag1:
            try:
                page = self.pageQueue.get()
                url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=" + str((page - 1) * 20)
                res = requests.get(url, headers = self.header, timeout = 10)
                time.sleep(0.5)
                res.raise_for_status()
                res.encoding = res.apparent_encoding
                self.dataQueue.put(res.text)
            except Exception as e:
                raise e
            # except Exception as e:
            #     # return e
            #     print("there are somethin wrong")
            #     pass
            # try:
            #     pass
                
        print("结束线程", self.threadName)

        

# 解析页面和存储
class write_html_data(threading.Thread):
    """docstring for write_html_data"""
    def __init__(self, threadName, dataQueue):
        super(write_html_data, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        # self.filename = filename
    def run(self):
        print("启动线程: ", self.threadName)
        while not flag2:
            try:
                html = self.dataQueue.get()
                pat_rate = re.compile('"rate":"(.*?)","cover_x":.*?,"title":".*?"')
                pat_name = re.compile('"rate":".*?","cover_x":.*?,"title":"(.*?)"')
                rate_list = re.findall(pat_rate, html)
                name_list = re.findall(pat_name, html)
                for i in range(len(rate_list)):
                    print("{:^10}{:^20}{:^10}".format(i+1, name_list[i], rate_list[i]))
            except Exception as e:
                raise e
        print("结束线程", self.threadName)
def threading_spider():

    global flag1, flag2
    flag1, flag2 = False, False
    pageQueue = queue.Queue(300)    # maxsize 一定要大于其内部要输入的量
    dataQueue = queue.Queue(300)    # 多线程不一定比单线程快
    for i in range(1, 200):
        pageQueue.put(i)
    t1 = get_html_data("采集线程", pageQueue, dataQueue)
    t2 = write_html_data("解析线程", dataQueue)
    t1.start()
    t2.start()

    while not pageQueue.empty():
        pass
    flag1 = True

    while not dataQueue.empty():
        pass
    flag2 = True
    t1.join()
    t2.join()



if __name__ == '__main__':
    print("{:^10}{:^20}{:^10}".format('-----', 'Start', '-----'))
    threading_spider()
    print("{:^10}{:^20}{:^10}".format('-----', 'End', '-----'))