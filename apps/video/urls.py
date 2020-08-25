from django.conf.urls import url
from django.urls import path

from .views import ListVideo
urlpatterns = [
    url(r'^videos/$', ListVideo.as_view(), name='lista-video'),
]
