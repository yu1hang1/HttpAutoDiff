from django.shortcuts import render
from biz.CompareBiz import *
from comman.model.HttpResponseResult import BaseResponse


def index_controller(request):
	return render(request, 'templates/index.html')


def do_excute_diff_controller(request):
	old_url = request.POST.get('old_uri', None)
	new_url = request.POST.get('new_uri', None)
	cookie = request.POST.get('cookie', None)
	old_param = request.POST.get('old_param', '{}')
	new_param = request.POST.get('new_param', '{}')
	request_method = request.POST.get('request_method', None)
	if not all([old_url, new_url, cookie, request_method]):
		return BaseResponse.failure(message="old_uri、new_uri、cookie不能为空")

	old_param = json.loads(old_param)
	new_param = json.loads(new_param)

	report = StartDiff(old_url, new_url, old_param, new_param, cookie, request_method)
	if type(report) is str:
		return BaseResponse.failure(message=report)
	return BaseResponse.success(data=report)


def batch_do_extute_diff_controller(request):
	# 1、第一步：收集测试场景：请求url、域名、请求方式、cookie、Service
	parameter_json = request.body
	parameter = json.loads(parameter_json)

	old_url = parameter.get('old_uri', None)
	new_url = parameter.get('new_uri', None)
	cookie = parameter.get('cookie', None)
	service_name = parameter.get('service_name', None)

	# 2、第二步：调用biz执行业务
	report = batchDiff(old_url, new_url, cookie, service_name)
	if type(report) is str:
		return BaseResponse.failure(message=report)
	# 3、第三步：返回给前端
	return BaseResponse.success(data=report)
