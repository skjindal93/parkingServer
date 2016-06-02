from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sensorPorts/$', views.sensorPortList, name='sensorPorts'),
	url(r'^sensorDetail/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.SensorDetail.as_view(), name='SensorDetail'),
	url(r'^parkCar/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.ParkCar.as_view(), name='parkCar'),
	url(r'^areas/$', views.orderedParkingArea, name='areas'),	
	url(r'^areaSensors/$', views.ParkingArea.as_view(), name='areaSensors'),	
	url(r'^parkingAreas/$', views.ParkingAreaList.as_view(), name='parkingAreas'),
	url(r'^checkStatus/$', views.checkStatus, name='checkStatus'),
]
