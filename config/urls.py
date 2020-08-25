from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

from apps import video

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.video.urls')),
]
