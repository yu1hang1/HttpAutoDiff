from django.urls import path
from provider import CompareController, WriteCaseToDBController

urlpatterns = [
	path('index', CompareController.index_controller),
	path('handler', CompareController.do_excute_diff_controller),
	path('SaveCase', WriteCaseToDBController.write_DB_from_file),
	path('asyncSaveCase', WriteCaseToDBController.async_write_DB_from_file),
	path('batchDiff', CompareController.batch_do_extute_diff_controller)
]
