from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.NewUser.as_view(), name='NewUser'),
	url(r'^login/', views.TokenView.as_view(), name='TokenView'),
]

