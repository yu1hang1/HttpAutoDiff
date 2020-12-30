# -*- coding:utf-8 -*-
# @Time : 2020/3/25 下午8:42
# @Author: hang.yu06
# @File : FetchCaseFromOL.py
import logging
import os
from ..constant.globalConstant import *
from ..model.StatusCodeException import *


def fetch_log_handeler(app_code, service_name, method_name, effectiveTime):
	try:
		os.system(
			'sh /Users/bianlifeng/Documents/Bianlifeng/qa/HttpAutoDiff/HttpAutoDiff/diffTools/comman/util/fetch_case.sh -d %s -a %s -s %s -m %s ' % (
				effectiveTime, app_code, service_name, method_name))
		f = open("/Users/bianlifeng/case_root/%s.%s" % (method_name, effectiveTime))
		data = f.read()
		f.close()
		os.system('rm /Users/bianlifeng/case_root/*')
		if not data:
			logging.error("%s线上拉取日志结果为空" % service_name)
			raise StatusCodeException("线上拉取日志结果为空", -500)
		data = eval(data)
		print("拉取线上日志结果为%s" % data)
		logging.info("拉取线上日志结果为%s" % data)
		return data

	except Exception() as e:
		logging.error("获取线上流量是失败", e)
		raise e
