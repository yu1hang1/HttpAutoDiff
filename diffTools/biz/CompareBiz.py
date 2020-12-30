import json_tools
import requests, json
from dao.mapper.CaseMapper import *
from diffTools.comman.constant.globalConstant import *
from diffTools.comman.model.StatusCodeException import *


def StartDiff(old_url, new_url, old_param, new_param, cookie, request_method):
	headers = {'cookie': cookie}
	old_result = __HttpRequestHandler(old_url, request_method, headers, old_param)
	new_result = __HttpRequestHandler(new_url, request_method, headers, new_param)
	if __diffResp(old_result, new_result):
		return __diffResp(old_result, new_result)


def batchDiff(old_url, new_url, cookie, service_name):
	UseCase = OnlineCaseMapper.queryCaseByService(service_name)
	if not UseCase:
		return "到数据库查询用例失败"
	reports = []
	for case in UseCase:
		method_name = list(case.keys())[0]
		param = list(case.values())[0]

		oldUrl = old_url + '/' + method_name
		newUrl = new_url + '/' + method_name

		headers = {'cookie': cookie}
		old_result = __HttpRequestHandler(oldUrl, "POST", headers, param)
		new_result = __HttpRequestHandler(newUrl, "POST", headers, param)
		if not all([old_result, new_result]):
			continue
		diffResult = __diffResp(old_result, new_result)
		report = {
			'Service_name': service_name,
			'method_name': method_name,
			'diff_result': diffResult,
			'diff_num': len(diffResult['diff_result'])

		}
		reports.append(report)
	return reports


def __HttpRequestHandler(url, request_method, headers, param):
	try:
		resp = None
		if request_method == "POST":
			resp = requests.post(url=url, headers=headers, json=param)
		if request_method == "GET":
			resp = requests.get(url=url, headers=headers, params=param)
		if resp.status_code != 200:
			logging.error("请求url报错", '接口请求错误，请求url为%s，请求参数为%s，响应状态码为%s' % (param, url, resp.status_code))
			raise StatusCodeException("请求url报错", '接口请求错误，请求url为%s，响应状态码为%s' % (url, resp.status_code))
		result = json.loads(resp.content.decode())
		return result
	except StatusCodeException as e:
		logging.error(e, "执行请求%s接口异常" % url)
		return 0


def __diffResp(old_result, new_result):
	try:
		diff_result = json_tools.diff(old_result, new_result)
		return {
			"diff_result": diff_result,
		}
	except StatusCodeException as e:
		logging.error(e, "执行diff时异常")
		return 0
