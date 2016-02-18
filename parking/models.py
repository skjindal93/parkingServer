from django.db import models

class spots(models.Model):
	spot_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, null=False)
	latitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	table_name = models.CharField(max_length=255, null=False)
	filled = models.IntegerField(null=False)
	capacity = models.IntegerField(null=False)

class raspberry(models.Model):
	raspberry_id = models.AutoField(primary_key=True)
	mac = models.CharField(max_length=255, null=False)

class sensors(models.Model):
	sensor_id = models.AutoField(primary_key=True)
	latitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	pi_id = models.ForeignKey(raspberry, on_delete=models.CASCADE)
	pi_port = models.IntegerField(null=False)
	occupied = models.BooleanField(default=False)


class raspberryPhone(models.Model):
	id = models.AutoField(primary_key=True)
	pi_id = models.ForeignKey(raspberry, on_delete=models.CASCADE)
	phone_mac = models.CharField(max_length=255, null=False)
