# -*- coding:utf-8 -*-
# @Time : 2020/3/30 下午7:50
# @Author: hang.yu06
# @File : WriteCaseToDBController.py

from diffTools.biz.WriteCaseToDBBiz import *
from diffTools.comman.model.HttpResponseResult import BaseResponse
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(5)


def write_DB_from_file(request):
	"""
	从文件中读取内容写入DB
	@param request: request
	@return: Response
	"""
	# 参数校验
	app_code = request.GET.get("app_code", None)
	service_name = request.GET.get("service_name", None)
	method_name = request.GET.get("method_name", None)
	if not all([app_code, service_name, method_name]):
		return BaseResponse.failure(message="app_code, service_name, method_name不能为空")
	# 执行业务逻辑
	result = To_DB_from_file(app_code, service_name, method_name)
	if type(result) is str:
		return BaseResponse.failure(message=result)
	return BaseResponse.success()


def async_write_DB_from_file(request):
	"""
	异步从线上日志同步数据到数据库
	@param request:
	@return:
	"""
	app_code = request.GET.get("app_code", None)
	service_name = request.GET.get("service_name", None)
	method_name = request.GET.get("method_name", None)
	effectiveTime = request.GET.get("effectiveTime", None)
	if not all([app_code, service_name, method_name, effectiveTime]):
		return BaseResponse.failure(message="app_code, service_name, method_name不能为空")
	executor.submit(async_to_DB_from_file, app_code, service_name, method_name,
					effectiveTime)

	return BaseResponse.success()
