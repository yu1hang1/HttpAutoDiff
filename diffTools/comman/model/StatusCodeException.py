# -*- coding:utf-8 -*-
# @Time : 2020/4/17 上午11:35
# @Author: hang.yu06
# @File : StatusCodeException.py

class StatusCodeException(Exception):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message
