from .models import *
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('sensor_id', 'latitude', 'longitude', 'pi_id', 'pi_port', 'occupied',)

class RaspberrySerializer(serializers.ModelSerializer):
	class Meta:
		model = raspberry
		fields = ('raspberry_id', 'mac',)

