from django.conf.urls import url

from core.views import FacebookDownloader, FacebookCSVDownloader

urlpatterns = [
    url(r'^download/$', FacebookDownloader.as_view(), name='download'),
    url(r'^download-csv/$', FacebookCSVDownloader.as_view(), name='download-csv'),
]
