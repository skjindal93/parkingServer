from .models import *
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('id', 'latitude', 'longitude', 'pi_id', 'pi_port', 'occupied')
