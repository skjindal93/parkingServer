from django.shortcuts import render
from parking.models import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import pyqrcode, os, math
from django.conf import settings
from rest_framework import generics
from .serializers import *

########################################
#################Fxns###################
########################################

def distance(lat1, lon1, lat2, lon2):
	radius = 6371 # km

	dlat = math.radians(lat2-lat1)
	dlon = math.radians(lon2-lon1)
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
		* math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = radius * c

	return d

pi_ports = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

########################################
################Region##################
########################################

#Register a parking region
class ParkingRegionRegister(generics.CreateAPIView):
	serializer_class = ParkingRegionDetailSerializer
	queryset = parkingRegions.objects.all()


#Get ordered regions with a given latitude and longitude
def orderedParkingRegion(request):
	latitude = request.GET.get('latitude')	
	longitude = request.GET.get('longitude')
	latitude = float(latitude)
	longitude = float(longitude)
	parking_regions = parkingRegions.objects.all()
	parking_regions_list = []
	for region in parking_regions:
		parking_regions_list.append(model_to_dict(region))
	print parking_regions_list
	
	for region in parking_regions_list:
		region_latitude  = float(region['latitude'])
		region_longitude = float(region['longitude'])
		region['distance'] = distance(latitude, longitude, region_latitude, region_longitude)
	
	ordered = sorted(parking_regions_list, key=lambda k: k['distance'])
	print ordered
	return JsonResponse({"regions": ordered})

########################################
##################Area##################
########################################

#Register an area within a parking region
class ParkingAreaRegister(generics.CreateAPIView):
	serializer_class = ParkingAreaDetailSerializer
	queryset = parkingAreas.objects.all()
	
	def perform_create(self, serializer):
		region_id = int(self.request.data['region'])
		region = parkingRegions.objects.get(id=region_id)
		area = serializer.save()
		areaRegionMapping.objects.create(area=area, region=region)


class ParkingAreasInRegion(generics.ListAPIView):
	serializer_class = ParkingAreaRegionSerializer

	def get_queryset(self):
		return areaRegionMapping.objects.filter(region=self.kwargs['region'])

########################################
##################Pi####################
########################################

#Register Pi by generating QR
def registerPi(request):
	obj = raspberry.objects.create(mac='')
	id = obj.raspberry_id
	QR(id)
	img_name = str(id)+'-qr.svg'
	return JsonResponse({'svg':img_name})

#Generate QR with given id
def QR(id):
	data = pyqrcode.create(id)
	data.svg('media/'+str(id)+'-qr.svg', scale=8)

#Map a phone with a given raspberry
class RaspberryPhoneMap(generics.CreateAPIView):
	queryset = raspberryPhone.objects.all()
	serializer_class = RaspberryPhoneSerializer

	def perform_create(self, serializer):
		phone_mac = self.request.data['phone_mac']
		pi_id = int(self.request.data['pi'])
		pi = raspberry.objects.get(raspberry_id=pi_id)
		if not raspberryPhone.objects.filter(pi=pi, phone_mac=phone_mac).exists():
			serializer.save()
			area_id = self.request.data['area']
			area = parkingAreas.objects.get(id=area_id)
			parkingRaspberryMapping.objects.create(area=area, pi=pi)

########################################
#################Sensor#################
########################################

#Register a new sensor
class newSensor(generics.CreateAPIView):
	queryset = sensors.objects.all()
	serializer_class = SensorDetailSerializer

#Get a sensor with a given pi and pi_port
class SensorDetail(generics.ListAPIView):
	serializer_class = SensorDetailSerializer
	def get_queryset(self):
		pi = self.kwargs['pi']
		pi_port = self.kwargs['pi_port']
		queryset = sensors.objects.filter(pi = pi, pi_port = pi_port)
		return queryset

#Get sensor list for a given pi
def sensorPortList(request):
	ids = sensors.objects.filter(pi = request.GET.get('pi')).values('pi_port')
	used = []
	for id in ids:
		used.append(id['pi_port'])

	ports = []
	for id in pi_ports:
		if id in used:
			j = {'pi_port': id, 'used': True}
			ports.append(j)
		else:
			j = {'pi_port': id, 'used': False}
			ports.append(j)
	return JsonResponse({"ports":ports})

