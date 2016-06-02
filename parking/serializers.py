from .models import *
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('sensor_id','latitude', 'longitude', 'pi', 'pi_port', 'occupied', 'created', 'modified',)

class RaspberrySerializer(serializers.ModelSerializer):
	class Meta:
		model = raspberry
		fields = ('raspberry_id', 'mac',)

class SensorPortSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('pi_port', 'occupied',)

class SensorDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('pi', 'pi_port', 'latitude', 'longitude', 'occupied',)

class ParkCarSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('pi','pi_port','occupied',)

class RaspberrySensorsSerializer(serializers.ModelSerializer):
	sensors = SensorSerializer(read_only=True, many=True)
	class Meta:
		model = raspberry
		fields = ('raspberry_id', 'sensors',)

class ParkingAreaSerializer(serializers.ModelSerializer):
	pi = RaspberrySensorsSerializer(read_only=True)
	class Meta:
		model = parkingRaspberryMapping
		fields = ('area','pi',)

class ParkingAreaDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = parkingAreas
		fields = ('id', 'name','latitude','longitude','capacity','filled',)
