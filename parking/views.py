from .models import *
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models import F
import math, subprocess
from django.forms.models import model_to_dict

pi_ports = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

class SensorDetail(generics.ListAPIView):
	serializer_class = SensorDetailSerializer
	def get_queryset(self):
		pi = self.kwargs['pi']
		pi_port = self.kwargs['pi_port']
		queryset = sensors.objects.filter(pi = pi, pi_port = pi_port)
		return queryset

def distance(lat1, lon1, lat2, lon2):
	radius = 6371 # km

	dlat = math.radians(lat2-lat1)
	dlon = math.radians(lon2-lon1)
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
		* math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = radius * c

	return d

def orderedParkingArea(request):
	latitude = request.GET.get('latitude')	
	longitude = request.GET.get('longitude')
	latitude = float(latitude)
	longitude = float(longitude)
	parking_areas = parkingAreas.objects.all()
	parking_areas_list = []
	for area in parking_areas:
		parking_areas_list.append(model_to_dict(area))
	print parking_areas_list
	
	for area in parking_areas_list:
		area_latitude  = float(area['latitude'])
		area_longitude = float(area['longitude'])
		area['distance'] = distance(latitude, longitude, area_latitude, area_longitude)
	
	ordered = sorted(parking_areas_list, key=lambda k: k['distance'])
	print ordered
	return JsonResponse({"areas": ordered})
		
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

class ParkCar(generics.UpdateAPIView):
	serializer_class = ParkCarSerializer
	queryset = sensors.objects.all()
	
	def get_object(self):
		return sensors.objects.get(pi = self.kwargs['pi'], pi_port = self.kwargs['pi_port'])

	def perform_update(self, serializer):
		sensor = self.get_object()
		pi = sensor.pi
		previous_occupied = sensor.occupied
		parking_area = parkingRaspberryMapping.objects.get(pi=pi).area.id
		occupied = self.request.data['occupied']
		occupied = bool(int(occupied))
		print previous_occupied, occupied
		if (previous_occupied != occupied):
			if (occupied):
				parkingAreas.objects.filter(id=parking_area).update(filled = F("filled") + 1)
			else:
				parkingAreas.objects.filter(id=parking_area).update(filled = F("filled") - 1)
		serializer.save()

class ParkingArea(generics.ListAPIView):
	serializer_class = ParkingAreaSerializer
	
	def get_queryset(self):
		area = self.request.GET.get('area')
		return parkingRaspberryMapping.objects.filter(area = area)

class ParkingAreaList(generics.ListAPIView):
	serializer_class = ParkingAreaDetailSerializer
	queryset = parkingAreas.objects.all()

def checkStatus(request):
	import pingparser
	pi = request.GET.get('pi')
	ip = raspberry.objects.get(raspberry_id=pi).ip
	if ip is None:
		return HttpResponse(0)
	ping = subprocess.Popen(["ping", "-c", "1", ip], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	
	out, error = ping.communicate()
	status = pingparser.parse(out)['received']
	return HttpResponse(status)
	
