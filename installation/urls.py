from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^registerPi/$', views.registerPi, name='registerPi'),
	url(r'^raspberryPhoneMap/$', views.RaspberryPhoneMap.as_view(), name='raspberryPhoneMap'),
	url(r'^sensorId/(?P<mac>.*)$', views.newSensorId, name='newSensorId'),
	url(r'^sensorLatitudeLongitude/(?P<pk>.*)$', views.LatitudeLongitude.as_view(), name='latitudeLongitude'),
]
