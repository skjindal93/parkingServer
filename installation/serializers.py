from .models import *
from rest_framework import serializers
from parking.models import raspberryPhone, raspberry, sensors

class RaspberryPhoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = raspberryPhone
		fields = ('pi', 'phone_mac',)

class LatitudeLongitudeSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('latitude', 'longitude',)
