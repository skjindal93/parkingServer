from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^parkCarFromSensor/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.ParkCarFromSensor.as_view(), name='parkCarFromSensor'),
	url(r'^parkCar/$', views.ParkCar.as_view(), name='parkCar'),
	url(r'^areas/$', views.orderedParkingArea, name='areas'),	
	url(r'^areaSensors/$', views.ParkingArea.as_view(), name='areaSensors'),	
	url(r'^checkStatus/$', views.checkStatus, name='checkStatus'),
	url(r'^deleteRaspberry/(?P<pk>[0-9]+)/$', views.RaspberryDelete.as_view(), name='raspberryDelete'),
	url(r'^deleteSensor/(?P<pk>[0-9]+)/$', views.SensorDelete.as_view(), name='sensorDelete'),
	url(r'^navigateUser/(?P<qr>.*)/$', views.NavigateUser.as_view(), name='navigateUser'),
]
