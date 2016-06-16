from .models import *
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models import F
import math, subprocess, datetime
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

def distance(lat1, lon1, lat2, lon2):
	radius = 6371 # km

	dlat = math.radians(lat2-lat1)
	dlon = math.radians(lon2-lon1)
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
		* math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = radius * c

	return d

#Get ordered parking areas based on current latitude and longitude
class OrderedParkingArea(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]
	
	def get(self, request, format=None):
		latitude = request.GET.get('latitude')	
		longitude = request.GET.get('longitude')
		latitude = float(latitude)
		longitude = float(longitude)
		parking_areas = parkingAreas.objects.all()
		parking_areas_list = []
		for area in parking_areas:
			parking_areas_list.append(model_to_dict(area))
		
		for area in parking_areas_list:
			area_latitude  = float(area['latitude'])
			area_longitude = float(area['longitude'])
			area['distance'] = distance(latitude, longitude, area_latitude, area_longitude)
		
		ordered = sorted(parking_areas_list, key=lambda k: k['distance'])
		return Response({"areas": ordered}, status=status.HTTP_200_OK)
	
########################################
################User####################
########################################

#Park and Unpark car from sensor
class ParkCarFromSensor(generics.UpdateAPIView):
	serializer_class = ParkCarFromSensorSerializer
	queryset = sensors.objects.all()	

	def get_object(self):
		return sensors.objects.get(pi = self.kwargs['pi'], pi_port = self.kwargs['pi_port'])

	def perform_update(self, serializer):
		sensor = self.get_object()
		pi = sensor.pi
		previous_occupied = sensor.occupied
		parking_area_obj = parkingRaspberryMapping.objects.get(pi=pi).area
		parking_area = parking_area_obj.id
		parking_charge = parking_area_obj.charge
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
			now = datetime.datetime.now().replace(tzinfo=None)
			parked_at = parkingHistory.objects.get(sensor=sensor, parked_go__isnull=True).parked_at.replace(tzinfo=None)
			parked_time = now - parked_at
			print parked_at, now
			amount = math.ceil(parking_charge*(parked_time.seconds/float(3600)))
			user = parkingHistory.objects.get(sensor=sensor, parked_go__isnull=True).user
			user.wallet = user.wallet - amount
			user.save()			
			parkingHistory.objects.filter(sensor=sensor, parked_go__isnull=True).update(parked_go=now, amount = amount)

#Check if user scanned the QR after parking the car
class CheckQRIfScanned(generics.GenericAPIView):
	def get(self, request, *args, **kwargs):
		pi = int(kwargs['pi'])
		pi_port = int(kwargs['pi_port'])
		sensor = sensors.objects.get(pi=pi, pi_port=pi_port)
		if sensor.occupied == True:
			try:
				parkingHistory.objects.get(sensor=sensor, parked_go__isnull=True)
			except ObjectDoesNotExist:
				return Response(False)
			return Response(True)

#Park Car after user scans QR
class ParkCar(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, format=None):
		user = self.request.user
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

#Navigate a user back to parked location
class NavigateUser(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]	

	def get(self, request, format=None):
		sensor = parkingHistory.objects.get(user=self.request.user, parked_go__isnull=True).sensor
		return Response(model_to_dict(sensor), status=status.HTTP_200_OK)

#Check whether a particular has parked his/her car
class CheckUserParkedStatus(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, format=None):
		try:
			parkingHistory.objects.get(user=self.request.user, parked_go__isnull=True)
		except ObjectDoesNotExist:
			return Response(False)
		return Response(True)	

#Get current balance of user
class CurrentBalance(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, format=None):
		wallet = self.request.user.wallet
		return Response({"wallet": wallet}, status = status.HTTP_200_OK)

#Get Parking History of user
class GetParkingHistory(generics.ListAPIView):
	serializer_class= ParkingHistorySerializer
	queryset = parkingHistory.objects.all()
	permission_classes = [permissions.IsAuthenticated]

	def get_object(self):
		return parkingHistory.objects.get(user=self.request.user)

########################################
##################Pi####################
########################################

#Get all Pis within an area
class ParkingArea(generics.ListAPIView):
	serializer_class = ParkingAreaSerializer
	
	def get_queryset(self):
		area = self.request.GET.get('area')
		return parkingRaspberryMapping.objects.filter(area = area)

#Check whether a pi is online or not
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

#Update IP and MAC of Pi table from Pi
class UpdatePiIP(generics.GenericAPIView):
	
	def put(self, request, format=None):
		mac = request.data['mac']
		ip = request.data['ip']
		id = int(request.data['id'])
		raspberry.objects.filter(raspberry_id=id).update(mac=mac, ip=ip)
		return Response("Updated!", status=status.HTTP_200_OK)

#Delete a Pi
class RaspberryDelete(generics.DestroyAPIView):
	serializer_class = RaspberryDeleteSerializer
	queryset = raspberry.objects.all()

########################################
###############Sensor###################
########################################

#Delete a Sensor
class SensorDelete(generics.DestroyAPIView):
	serializer_class = SensorDeleteSerializer
	queryset = sensors.objects.all()
