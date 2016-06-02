from django.shortcuts import render
from parking.models import raspberry, raspberryPhone, sensors
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import pyqrcode, os
from django.conf import settings
from rest_framework import generics
from .serializers import *

def registerPi(request):
	obj = raspberry.objects.create(mac='')
	id = obj.raspberry_id
	QR(id)
	img_name = str(id)+'-qr.svg'
	return JsonResponse({'svg':img_name})

def QR(id):
	data = pyqrcode.create(id)
	data.svg('media/'+str(id)+'-qr.svg', scale=8)

class RaspberryPhoneMap(generics.CreateAPIView):
	queryset = raspberryPhone.objects.all()
	serializer_class = RaspberryPhoneSerializer

def newSensorId(request, mac):
	pis = raspberryPhone.objects.filter(phone_mac = mac).values('pi')
	sensor = sensors.objects.get(latitude__isnull = True, longitude__isnull = True, pi__in = pis)
	return JsonResponse({'sensor': sensor.sensor_id})

class newSensor(generics.CreateAPIView):
	queryset = sensors.objects.all()
	serializer_class = SensorSerializer
