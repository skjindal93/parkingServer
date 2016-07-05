from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^parkCarFromSensor/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.ParkCarFromSensor.as_view(), name='parkCarFromSensor'),
	url(r'^parkCar/$', views.ParkCar.as_view(), name='parkCar'),
	url(r'^areas/$', views.OrderedParkingArea.as_view(), name='areas'),
	url(r'^parkingRegions/$', views.ParkingRegionList.as_view(), name='parkingRegions'),
	url(r'^parkingAreasInRegion/$', views.ParkingAreasInRegion.as_view(), name='parkingAreasInRegion'),
	url(r'^areaSensors/$', views.ParkingArea.as_view(), name='areaSensors'),	
	url(r'^checkStatus/$', views.checkStatus, name='checkStatus'),
	url(r'^deleteRaspberry/(?P<pk>[0-9]+)/$', views.RaspberryDelete.as_view(), name='raspberryDelete'),
	url(r'^deleteSensor/(?P<pk>[0-9]+)/$', views.SensorDelete.as_view(), name='sensorDelete'),
	url(r'^navigateUser/$', views.NavigateUser.as_view(), name='navigateUser'),
	url(r'^checkUserParkedStatus/$', views.CheckUserParkedStatus.as_view(), name='checkUserParkedStatus'),
	url(r'^currentBalance/$', views.CurrentBalance.as_view(), name='currentBalance'),
	url(r'^updatePiIP/$', views.UpdatePiIP.as_view(), name='updatePiIP'),	
	url(r'^checkQRIfScanned/(?P<pi>[0-9]+)/(?P<pi_port>[0-9]+)/$', views.CheckQRIfScanned.as_view(), name='checkQRIfScanned'),
	url(r'^parkingHistory/$', views.GetParkingHistory.as_view(), name='parkingHistory'),
]
