from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^registerPi/$', views.registerPi, name='registerPi'),
	url(r'^raspberryPhoneMap/$', views.RaspberryPhoneMap.as_view(), name='raspberryPhoneMap'),
	url(r'^newSensor/$', views.newSensor.as_view(), name='newSensor'),
	
	url(r'^registerRegion/$', views.ParkingRegionRegister.as_view(), name='parkingRegionRegister'),
	url(r'^registerArea/$', views.ParkingAreaRegister.as_view(), name='parkingAreaRegister'),
	url(r'^regions/$', views.orderedParkingRegion, name='regions'),	
	url(r'^areasInRegion/(?P<region>[0-9]+)/$', views.ParkingAreasInRegion.as_view(), name='parkingAreasInRegion'),	
	
	url(r'^sensorPorts/$', views.sensorPortList, name='sensorPorts'),
	url(r'^sensorDetail/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.SensorDetail.as_view(), name='SensorDetail'),
]
