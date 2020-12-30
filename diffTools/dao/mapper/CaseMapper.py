# -*- coding:utf-8 -*-
# @Time : 2020/3/27 下午8:25
# @Author: hang.yu06
# @File : CaseMapper.py
import json
import logging
import time

from diffTools.dao.models.CaseModel import *
import ast


class OnlineCaseMapper(object):
	@staticmethod
	def insertCase(app_code, service_name, case_json, method_name, type=0, compress_type=0,
				   create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
				   update_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())):
		try:
			caseWarehouse = CaseWarehouse.objects. \
				create(type=type, compress_type=compress_type, create_time=create_time, update_time=update_time,
					   app_code=app_code, service_name=service_name, case_json=case_json, method_name=method_name)
			caseWarehouse.save()
		except Exception as e:
			logging.error("插入一条case失败", e)
			return False
		return True

	@staticmethod
	def queryCaseByService(service_name):
		UserCases = []
		try:
			caseWarehouse = CaseWarehouse.objects.filter(service_name=service_name)

			for case in caseWarehouse:
				UserCase = {
					case.method_name: ast.literal_eval(case.case_json)
				}
				UserCases.append(UserCase)
		except Exception as e:
			logging.error("查询用例失败", e)
			return 0
		return UserCases
