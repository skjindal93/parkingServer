from django.db import models

class spots(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, null=False)
	latitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	table_name = models.CharField(max_length=255, null=False)
	filled = models.IntegerField(null=False)
	capacity = models.IntegerField(null=False)

class sensors(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	pi_id = models.IntegerField(null=False)
	pi_port = models.IntegerField(null=False)
	occupied = models.BooleanField(default=False)
