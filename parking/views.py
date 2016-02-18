from .models import *
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

class SensorList(APIView):

	def get_object(self, pi_id, pi_port):
		try:
			return sensors.objects.get(pi_id=pi_id, pi_port = pi_port)
		except sensors.DoesNotExist:
			raise Http404

	def get(self, request, format=None):
		queryset = sensors.objects.all()
		serializer = SensorSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		sensor = self.get_object(request.data["pi_id"],request.data["pi_port"])
		print sensor
		serializer = SensorSerializer(sensor,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RaspberryPhone(APIView):
	
	def get_object(self, pi_id):
		try:
			return raspberryPhone.objects.get(pi_id=pi_id)
		except raspberryPhone.DoesNotExist:
			return None

	def create_or_update_object(self, pi_id, phone_mac):
		return raspberryPhone.objects.update_or_create(pi_id=pi_id, phone_mac = phone_mac) 
	
	def post(self, request, format=None):
		queryset = self.get_object(request.data["pi_id"])
		print request.data
		print queryset
		serializer = None
		if (queryset == None):
			serializer = RaspberryPhoneSerializer(data=request.data)
		else:
			serializer = RaspberryPhoneSerializer(queryset, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
