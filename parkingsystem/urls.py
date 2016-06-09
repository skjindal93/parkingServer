from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
import users

urlpatterns = (
	url(r'^parking/', include('parking.urls')),
	url(r'^installation/', include('installation.urls')),
	url(r'^users/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/token/', users.views.TokenView.as_view(), name='TokenView'),
)
