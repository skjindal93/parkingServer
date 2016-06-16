from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
import users

urlpatterns = [
	url(r'^parking/', include('parking.urls')),
	url(r'^installation/', include('installation.urls')),
	url(r'^users/', include('users.urls')),
	url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
