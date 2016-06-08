from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^parkCar/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.ParkCar.as_view(), name='parkCar'),
	url(r'^areas/$', views.orderedParkingArea, name='areas'),	
	url(r'^areaSensors/$', views.ParkingArea.as_view(), name='areaSensors'),	
	url(r'^checkStatus/$', views.checkStatus, name='checkStatus'),
	url(r'^deleteRaspberry/(?P<pk>[0-9]+)/$', views.RaspberryDelete.as_view(), name='raspberryDelete'),
]
