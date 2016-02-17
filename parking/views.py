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

	def get(self, request, format=None):
		queryset = sensors.objects.all()
		serializer = SensorSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SensorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
