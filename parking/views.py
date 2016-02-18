from .models import *
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

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
	
	def post(self, request, format=None):
		queryset = self.get_object(request.data["pi_id"])
		print request.data
		print queryset
		serializer = None
		if (queryset is None):
			serializer = RaspberryPhoneSerializer(data=request.data)
		else:
			serializer = RaspberryPhoneSerializer(queryset, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RaspberryQR(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'qr.html'

	def get(self, request):
		queryset = raspberry.objects.all()
		serializer = RaspberrySerializer(queryset, many=True)
		return Response({'serializer': serializer})

	def post(self, request, format=None):
		serializer = RaspberrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
