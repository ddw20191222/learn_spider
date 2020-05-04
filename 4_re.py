#!/d:\\learn_spider python3
# -*- coding: utf-8 -*-
# software: sublime
# name: 3_re.py
# date: 2020.05.04
# website: https://www.51zxw.net/list.aspx?cid=732
原子：普通字符，特殊字符，
元字符（原子修饰符:
	[] --同一个级别的字符
		自定义列表
		自定义排除列表
	() 
		--分组，当做一个原子进行修饰
		--改变正则表达式的优先级
	数目相关
	{} --数目
		{m}
		{m, n}
		{m, }
		{, n}
		* 对它前面的正则式匹配0到任意次重复，尽量多的匹配字符串
		？ 0个或1个
		+ 1个或多个
	位置限定符
		^ 
		$
		\A, 限定内容必须在字符串的开头位置 \Ahttp -- 必须以http开头
		\Z， 限定内容必须在字符串的结尾 m\Z
		差别，有换行字符出现的时候， ^可以匹配
		补充内容：具有多行，将每一个行当成一个独立的字符串进行匹配， ^ $ 支持
			主义，多行模式需要“模式修正符”
	词边界，仅为英文， 仅表示一个字符
		\b --能够当做单词分割符号的符号，去除字母和数字， 表示开头
		\B --不能够当做单词分割符号的符号，即字母和数字
		注意，汉字当成字母处理
	选择符号
		| --左右内容二选一
模式修正符
	设定匹配的一些规则
	re.A --ASCII              在ASCII下进行正则匹配操作
	re.U --default re.UNICODE 在Unicode条件下进行正则操作（条件下，汉字也当做字母）
	re.S --Super，			  使得原子 . 可以匹配更多内容
	re.M --Multiline		  支持多行模式，将换行符后面的内容当成一个新的字符串
转义字符的应用
	匹配符号的原来功能
	字符串： \n, \t, \
	\. --去掉特殊字符 . 的其他功能，仅仅保留普通符号的功能
	\[, \] -- 去掉中括号的其他功能，如元字符的语法功能
扩展正则语法
	1. (?Limsux) -- 多种模式修正符的应用，
	2. (?:) --取消单元存储功能，节省存储单元
	3. (?P<name>) -- 自定义模式单元的名称
		索引模式单元应用 <title>baidu</title><body>www.baidu.com</body>
		<(title)>baidu<\1>， 元组模式
		存储内容过多的时候，变成字典模式
		<(?:P<title)>baidu<\1>
	4. (?P=name) -- 获取自定义模式单元的名称
	5. (?#)				--正则注释内容
	正向：有 负向：没有
	先行：向前 后行：向左
	6. (?=)				--正向先行单元 r'lomkey(?=\.com)'
	7. (?!)				--负向先行单元 r'lomkey(?!\.com)' 后面没有
	8. (?<=)			--正向后行单元 r'(?<=xxx)lonkye'
	9. (?<!)			--负向后行单元
	注意事项：
		1.可以同时存在先行和后行
		2.宽度必须制定，不能随意制定
	10. (?(id/name)Y|N) 存在去前面内容，不存在取后面内容
		r'(www)?(?(1).*|\w+\.)', www存在取www， 不存在，取其他内容
例子
1.用户名
	要求：字母数字下划线，至少三个，不能使用特殊字符
	例子：hhh123
	表达式：r"^\w{3, }"
2.ip地址
	要求：四个数字段，0-255，每个数字段使用 . 分割
	书写实例： 92.168.1.103， 192.187.99.0， 127.0.0.1
	书写正则： r"(\d{1, 3}\." ---r"([0-9](?#一位数)|[1-9]\d(?#两位数)|1\d{2}{?#100-199)|2([0-4]\d|5[0-5])(?#200-255))\."
	还可以压缩利用扩展正则语法10
3.电话号码
	要求：11位， 第2， 3位有限制
	书写规则实例
4.身份证
	要求：18位， 前面的为区号， 生日，计算参数， x为最后一位， 符合日期
		地址， 出生日期，顺序码， 校验码


re模块
1. re模块的方法
	compile() 			--编译正则表达式，变成一个对象，可以加入模块修饰符
						--可以多次利用，提高程序效率
						--格式，返回值是正则对象
	escape()			--对字符串进行转义处理，仅处理非数字和字母的字符串
	findall()			--对所有的内容进行匹配，获取所有的内容结果
						--findall(biaodashi, strring, 模式xiuzheng)，返回值为一个列表
	finditer()			--作用非常相似， 返回结果为一个iter， 匹配的结果对象的信息
	match()				--从开始进行匹配
	search()			--匹配到第一个结果，返回匹配对象
	split()				--切割字符串， 第三个参数为最大切割次数 re.split(r'\s', s, 2)
	sub()				--正则替换 re.sub(pattern, replace_s, s), 第四个参数是替换的次数
						>>> s= "蜡笔小新的爸爸是比拉，蜡笔小新的妈妈是丽丽，蜡笔小新的妹妹是哈哈哈哈"
						>>> re.sub(r"蜡笔小新", "小狼", s)
	subn()				--和sub类似，替换结果+替换次数
2. re模块的对象(compile获取)， rx正则表达式对象
	即将正则表达式提取到前面，并且
	匹配操作1: re模块（正则表达式， 字符串） 得到结果
	匹配操作2： 正则表达式对象（字符串）

	findall()
	finditer()
	match()
	search()
	split()
	sub()
	subn()
3. 属性
	flags					--获取模式修正符 rx.flags
	pattern					--获取正则对象的字符串格式
	groups					--表示模式索引单元的个数
	groupindex				--自定义内容

4. 正则对象的扩展用法
	选择字符串的部分内容
	e. g 
	s = "https://www.baidu.com"
	rx = re.compile("baidu")
	rx = rx.compile(s, 0, 10)
	print(rx) 



	flags

__author__="ddw20191222"

import re

def test1():
	str = "张三，李四，王五"
	pat = "李四"
	res = re.findall(pat, str)
	print(res)
def test2():
	with open("E:\\learn_spider\\resource\\4_source.txt", "rb") as f:
		data = f.read().decode()
	pat1 = "时代"
	pat2 = "时候"
	res1 = re.findall(pat1, data)
	res2 = re.findall(pat2, data)
	
	print(res1, res2)
	print(len(res1), len(res2))


def test3():
# 原子，实现匹配的基本单位 pat
# 元字符，正则表达式中具有特殊意义的字符

# 普通字符作为原子，匹配普通字符， 完全一致

# 匹配通用字符
# %w, %W, %d, %D, %s, %S(space)
	c = "%FF%G%FDFDF"
	pat1 = r"\w\w\w"
	print(re.search(pat1, c))
def test4():
	# 匹配数字，英文，中文
	# [0-9], [a-z][A-Z] [\u4e00-\u9fa5]
	d = "(&(#HID(SFJJD09079834983KJS张三K((*(*))))0000PPPPD(S))Dsjidj"
	pat1 = r"[\u4e00-\u9fa5][\u4e00-\u9fa5]"
	pat2 = r"[a-z][a-z]"
	pat3 = r"[0-9]"
	result1 = re.search(pat1, d)
	result2 = re.search(pat2, d)
	result3 = re.search(pat3, d)
	print(result1, result2, result3)
def test5():
	# 原子表， 定义一组平等的原子
	c = ""
def test6():
# ., ^, $, *, ?, +
# 	pass
# match 只匹配开头
# search 只匹配一次，找到第一个ok
# findall 匹配所有，并且返回列表list[]

	a = "pyton123pyton123"
	print(re.match(r"\w", a))
	print(re.search(r"\d+", a))
	print(re.findall(r"\d+", a))
# 编译正则re.compile, 用来代替更长的内容
	pattern = re.compile(r"")
if __name__=="__main__":
	# test1()
	# test2()
	# test3()	test4()
	# test4()
	test6()	