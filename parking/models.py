from django.db import models

class raspberry(models.Model):
	raspberry_id = models.AutoField(primary_key=True)
	mac = models.CharField(max_length=255, null=True)
	ip = models.CharField(max_length=255, null=True)

class sensors(models.Model):
	sensor_id = models.AutoField(primary_key=True)
	latitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	pi = models.ForeignKey(raspberry, on_delete=models.CASCADE, related_name='sensors')
	pi_port = models.IntegerField(null=False)
	occupied = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	class Meta:
		unique_together = ('pi', 'pi_port',)

class raspberryPhone(models.Model):
	id = models.AutoField(primary_key=True)
	pi = models.ForeignKey(raspberry, on_delete=models.CASCADE)
	phone_mac = models.CharField(max_length=255, null=False)

class parkingAreas(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(blank=False)
	latitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10, null=False)
	capacity = models.IntegerField(null=False)
	filled = models.IntegerField(null=False)

class parkingRaspberryMapping(models.Model):
	area = models.ForeignKey(parkingAreas, on_delete=models.CASCADE, related_name = 'area_mappings')
	pi = models.ForeignKey(raspberry, on_delete=models.CASCADE, related_name = 'pi_mappings')
	
