from django.db import models
from django.conf import settings

class raspberry(models.Model):
	raspberry_id = models.AutoField(primary_key=True)
	mac = models.CharField(max_length=255, null=True)
	ip = models.CharField(max_length=255, null=True)

class raspberryPhone(models.Model):
	id = models.AutoField(primary_key=True)
	pi = models.ForeignKey(raspberry, on_delete=models.CASCADE)
	phone_mac = models.CharField(max_length=255, null=False)

class sensors(models.Model):
	sensor_id = models.AutoField(primary_key=True)
	latitude = models.FloatField(null=False)
	longitude = models.FloatField(null=False)
	pi = models.ForeignKey(raspberry, on_delete=models.CASCADE, related_name='sensors')
	pi_port = models.IntegerField(null=False)
	occupied = models.BooleanField(default=False)
	qr = models.CharField(max_length=255, blank=False, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	class Meta:
		unique_together = ('pi', 'pi_port',)

class sensorPortGPIOMappings(models.Model):
	trig = models.IntegerField(null=False)
	echo = models.IntegerField(null=False)
	class Meta:
		unique_together = ('trig', 'echo')

class parkingAreas(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(blank=False)
	latitude = models.FloatField(null=False)
	longitude = models.FloatField(null=False)
	capacity = models.IntegerField(null=False, default=20)
	filled = models.IntegerField(null=False, default=0)
	charge = models.IntegerField(default=20)

class parkingRaspberryMapping(models.Model):
	area = models.ForeignKey(parkingAreas, on_delete=models.CASCADE, related_name = 'area_mappings')
	pi = models.ForeignKey(raspberry, on_delete=models.CASCADE, related_name = 'pi_mappings', unique=True)
	class Meta:
		unique_together = ('area', 'pi',)

class parkingRegions(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, blank=False, unique=True)
	latitude = models.FloatField(null=False)
	longitude = models.FloatField(null=False)
	
class areaRegionMapping(models.Model):
	region = models.ForeignKey(parkingRegions, on_delete=models.CASCADE, related_name = 'region_mappings')
	area = models.ForeignKey(parkingAreas, on_delete=models.CASCADE, related_name = 'region_mappings')
	class Meta:
		unique_together = ('region', 'area',)

class parkingHistory(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='histories')
	sensor = models.ForeignKey(sensors, on_delete=models.CASCADE, related_name = 'histories')
	parked_at = models.DateTimeField(auto_now_add=True)
	parked_go = models.DateTimeField(null=True)
	amount = models.FloatField(null=True)
