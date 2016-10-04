from django.conf.urls import url

from core.views import FacebookDownloader

urlpatterns = [
    url(r'^download/$', FacebookDownloader.as_view(), name='download'),
]
