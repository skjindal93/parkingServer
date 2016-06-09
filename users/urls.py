from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.NewUser.as_view(), name='NewUser'),
]

