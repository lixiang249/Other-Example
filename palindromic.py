# -*- coding:utf-8 -*-
# author:lixiang
# 判断字符串是否是回文

import string

def reverse(text):
	return text[::-1]

def is_palindromic(text):
	text = text.lower() #将大写转换为小写
	text = text.replace(' ','') #删除所有空格
	for ch in string.punctuation: #string.punctuation表示所有的标点符号
		text = text.replace(ch,'')
	return text == reverse(text)

def main():
	str = input("Please input something:")
	if is_palindromic(str):
		print("The string {0} is palindromic!".format(str))
	else:
		print("The string < {0} > isn't palindromic!".format(str))
	
if __name__ == '__main__':
	main()
else:
	print("The python file are imported!")