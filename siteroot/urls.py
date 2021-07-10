from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .api import urls as api_urls

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
