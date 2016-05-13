from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sensors/$', views.SensorList.as_view(), name='sensorList'),
	url(r'^createSensor/$', views.SensorCreate.as_view(), name='sensorCreate'),
	url(r'^sensor/(?P<pi_id>(\d+))/(?P<pi_port>(\d+))/$', views.SensorList.as_view(), name='sensor'),
	url(r'^raspberryPhone/$', views.RaspberryPhone.as_view(), name='raspberryPhone'),
	url(r'^qr/$', views.RaspberryQR.as_view(), name='qr'),
]
