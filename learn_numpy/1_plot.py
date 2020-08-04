#!/d:\\learn_spider\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 1_plot.py
# date: 2020.05.08
# website: https://www.bilibili.com/video/


__author__="ddw20191222"

from matplotlib import pyplot

def test1():
	x = range(2, 26, 2)
	y = range(1, 13, 1)


	pyplot.figure(figsize=(20, 8), dpi=80)
	pyplot.xticks(range(2, 26))
	pyplot.plot(x, y)
	pyplot.show()
	pyplot.savefig("./figsize.png")

if __name__=="__main__":
	test1()