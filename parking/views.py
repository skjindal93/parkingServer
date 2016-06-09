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
import math, subprocess, datetime
from django.forms.models import model_to_dict

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
		
class ParkCarFromSensor(generics.UpdateAPIView):
	serializer_class = ParkCarFromSensorSerializer
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

		if previous_occupied == 1 and occupied == 0:
			now = datetime.datetime.now()
			parkingHistory.objects.filter(sensor=sensor,parked_go__isnull=True).update(parked_go=now)

class ParkCar(generics.GenericAPIView):
		
	def post(self, request, format=None):
		user = int(request.data['user'])
		sensor_qr = request.data['qr']
		sensor = sensors.objects.get(qr=sensor_qr)
		occupied = sensor.occupied
		if occupied == 0:
			return Response("Parking at an empty location?", status = status.HTTP_400_BAD_REQUEST)
		if not (parkingHistory.objects.filter(user=user, parked_go__isnull=True).exists() or parkingHistory.objects.filter(sensor=sensor, parked_go__isnull=True).exists()):
			obj = parkingHistory.objects.create(user=user, sensor=sensor)
			data = model_to_dict(obj)
			return Response(data, status=status.HTTP_201_CREATED)
		else:
			return Response("(You have already parked the car) or (You are scanning the wrong sensor. Someone else's car is already parked there.)", status=status.HTTP_400_BAD_REQUEST)

class NavigateUser(generics.RetrieveAPIView):
	serializer_class = SensorSerializer
	queryset = sensors.objects.all()

	def get_object(self):
		return sensors.objects.get(qr = self.kwargs['qr'])

class ParkingArea(generics.ListAPIView):
	serializer_class = ParkingAreaSerializer
	
	def get_queryset(self):
		area = self.request.GET.get('area')
		return parkingRaspberryMapping.objects.filter(area = area)

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

class RaspberryDelete(generics.DestroyAPIView):
	serializer_class = RaspberryDeleteSerializer
	queryset = raspberry.objects.all()

class SensorDelete(generics.DestroyAPIView):
	serializer_class = SensorDeleteSerializer
	queryset = sensors.objects.all()
