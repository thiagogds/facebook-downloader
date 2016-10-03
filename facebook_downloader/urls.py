from django.conf.urls import include, url
from django.contrib import admin

from gate_id import urls as gate_id_urls

urlpatterns = [
    url(r'', include(gate_id_urls, namespace='gate_id')),
    url(r'^admin/', include(admin.site.urls)),
]
