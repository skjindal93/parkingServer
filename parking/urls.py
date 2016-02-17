from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sensor/$', \
      views.SensorList.as_view(), \
      name='sensorList'),
]
