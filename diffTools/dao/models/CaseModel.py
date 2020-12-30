from django.db import models


class CaseWarehouse(models.Model):
	app_code = models.CharField(max_length=45)
	service_name = models.CharField(max_length=100)
	method_name = models.CharField(max_length=100)
	type = models.IntegerField()
	case_json = models.CharField(max_length=1024)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()
	compress_type = models.PositiveIntegerField()

	class Meta:
		managed = False
		db_table = 'case_warehouse'
		unique_together = ('app_code', 'service_name', 'method_name')

