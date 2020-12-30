from django.http import JsonResponse


class BaseResponse():

	@staticmethod
	def success(message='success', data={}, code=200):
		result = {
			'code': code,
			'msg': message,
			'data': data
		}

		return JsonResponse(result)

	@staticmethod
	def failure(message, data={}, code=500):
		result = {
			'code': code,
			'msg': message,
			'data': data
		}

		return JsonResponse(result)
