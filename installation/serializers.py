from .models import *
from rest_framework import serializers
from parking.models import *
class RaspberryPhoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = raspberryPhone
		fields = ('pi', 'phone_mac',)

class SensorDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('pi', 'pi_port', 'latitude', 'longitude', 'occupied',)

class ParkingAreaDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = parkingAreas
		fields = ('id', 'name','latitude','longitude','capacity','filled',)

class ParkingRegionDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = parkingRegions
		fields = ('id', 'name', 'latitude', 'longitude',)

class ParkingAreaRegionSerializer(serializers.ModelSerializer):
	area = ParkingAreaDetailSerializer(read_only=True)
	class Meta:
		model = areaRegionMapping
		fields = ('area',)
