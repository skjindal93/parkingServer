from .models import *
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('sensor_id','latitude', 'longitude', 'pi', 'pi_port', 'occupied', 'created', 'modified','qr',)

class RaspberrySerializer(serializers.ModelSerializer):
	class Meta:
		model = raspberry
		fields = ('raspberry_id', 'mac',)

class RaspberryDeleteSerializer(serializers.ModelSerializer):
	class Meta:
		model = raspberry
		fields = ('raspberry_id',)

class SensorDeleteSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('sensor_id',)

class SensorPortSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('pi_port', 'occupied',)

class ParkCarFromSensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = sensors
		fields = ('pi','pi_port','occupied',)

class RaspberrySensorsSerializer(serializers.ModelSerializer):
	sensors = SensorSerializer(read_only=True, many=True)
	class Meta:
		model = raspberry
		fields = ('raspberry_id', 'sensors',)

class ParkingRegionSerializer(serializers.ModelSerializer):
	class Meta:
		model = parkingRegions
		fields = ('id', 'name', 'latitude', 'longitude',)

class ParkingAreaSerializer(serializers.ModelSerializer):
	pi = RaspberrySensorsSerializer(read_only=True)
	class Meta:
		model = parkingRaspberryMapping
		fields = ('area','pi',)

class ParkingAreaDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = parkingAreas
		fields = ('id', 'name','latitude','longitude','capacity','filled',)

class ParkingAreasSerializer(serializers.ModelSerializer):
	area = ParkingAreaDetailSerializer(read_only=True)
	class Meta:
		model = areaRegionMapping
		fields = ('region','area')

class ParkingHistorySerializer(serializers.ModelSerializer):
	def area_name(self, obj):
		object = obj.sensor.pi.pi_mappings.all()[0]
		return object.area.name
	def region_name(self, obj):
		queryset = obj.sensor.pi.pi_mappings.all()[0]
		object = queryset.area.region_mappings.all()[0]
		return object.region.name
	area = serializers.SerializerMethodField('area_name')
	region = serializers.SerializerMethodField('region_name')
	class Meta:
		model = parkingHistory
		fields = ('parked_at', 'parked_go', 'amount', 'area', 'region')
