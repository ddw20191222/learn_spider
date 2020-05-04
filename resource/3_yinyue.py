#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 3_yinyue.py
# date: 2020.05.04
# website: https://www.51zxw.net/list.aspx?cid=732

__author__="ddw20191222"

import re
import requests
import logging

header={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
}

SongID = []
SongName = []

# 分析网站地址
# 第一页： http://www.htqyy.com/top/hot
# 第二页： http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# 第三页： http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
# 猜测第一页为 http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# format： number i： http://www.htqyy.com/top/musicList/hot?pageIndex=(i-1)&pageSize=20


# 分析音乐url
# <li class="mItem">
#             <input type="checkbox" name="checked" checked="checked" value="46"><span
#                 class="num">40</span><span class="title"><a href="/play/46" target="play" title="琵琶语" sid="46">琵琶语</a></span>
#             <span class="artistName"><a href="/artist/7" title="林海" target="_blank">林海</a></span>
#             <span class="albumName"><a href="/album/7" title="林海精选集" target="_blank">林海精选集</a></span>
#             <span class="playCount">37684人听过</span><a href="/play/46" class="playBtn mr" target="play" title="播放">播放</a><a
#                 class="playlistBtn" href="javascript:void()" onclick="addPlay(this)" title="加入列表">加入列表</a></li>

# </ul>
# 得到title和sid
# 找到url内容 http://f2.htqyy.com/play7/468/mp3/5

# 使用正则表达式 

# MusicName 


def load_html(ID, name):
	print("正在下载: ", name)
	url = music_url = "http://f2.htqyy.com/play7/" + str(ID) + "/mp3/5"
	res = requests.get(url).content
	return res

def write_music(data, name):
	print("正在保存: ", name)
	with open("E:\\learn_spider\\product\\{}.mp3".format(name), "wb") as f:
		f.write(data)


def music_spider():
	start = 1
	end = 3
	url_first = "http://www.htqyy.com/top/musicList/hot?pageIndex="
	for i in range(start - 1, end):
		url_page = url_first + str(i) + "&pageSize=20"
		logging.info(url_page)
		res = requests.get(url_page).text
		pat1 = r'title="(.*?)" sid='
		pat2 = r'sid="(.*?)"'
		titlelist = re.findall(pat1, res)
		idlist = re.findall(pat2, res)
		SongID.extend(idlist)
		SongName.extend(titlelist)
	# print(SongID, SongName)
	# print(len(SongID), len(SongName))
	for i in range(0, len(SongID)):

		data = load_html(SongID[i], SongName[i])
		write_music(data, SongName[i])
if __name__=="__main__":
	music_spider()
