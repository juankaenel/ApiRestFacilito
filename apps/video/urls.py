from django.conf.urls import url
from django.urls import path

from .views import ListVideo,DetailVideo
urlpatterns = [
    url(r'^videos/$', ListVideo.as_view(), name='lista-video'),
    url(r'^videos/(?P<pk>[0-9]+)$', DetailVideo.as_view(), name='detail-video'),
]
