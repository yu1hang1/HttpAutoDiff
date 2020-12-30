# -*- coding:utf-8 -*-
# @Time : 2020/3/30 下午7:58
# @Author: hang.yu06
# @File : WriteCaseToDBBiz.py
import logging

from ..comman.util.FetchCaseFromOL import fetch_log_handeler
from ..dao.mapper.CaseMapper import OnlineCaseMapper
from ..comman.constant.globalConstant import *


def To_DB_from_file(app_code, service_name, method_name):
	f = open("/Users/bianlifeng/data_root/buildDraftSnap.Ao.2020-03-19.display-manage1.idss.w.bj1")
	data = f.read()
	f.close()
	data = eval(data)
	if not OnlineCaseMapper.insertCase(app_code, service_name, case_json=data, method_name=method_name):
		return "写入数据库失败"

	return 0


def async_to_DB_from_file(app_code, service_name, method_name, effectiveTime):
	data = fetch_log_handeler(app_code, service_name, method_name, effectiveTime)
	if type(data[0]) is dict:
		data = data[0]

	if not OnlineCaseMapper.insertCase(app_code, service_name, case_json=data, method_name=method_name):
		logging.error("写入数据库失败app_code=%s,service_name=%s,method_name=%s" % (app_code, service_name, method_name))
	print("用例存储成功app_code=%s,service_name=%s,method_name=%s,data=%s" % (app_code, service_name, method_name, data))
	logging.info("用例存储成功app_code=%s,service_name=%s,method_name=%s" % (app_code, service_name, method_name))
