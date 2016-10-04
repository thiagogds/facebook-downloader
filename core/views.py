from django.views.generic import View
from django.conf import settings

import requests
from braces.views import JSONResponseMixin


class FacebookDownloader(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        token = settings.FACEBOOK_TOKEN
        facebook_graph = 'https://graph.facebook.com/v2.7/'
        endpoint = facebook_graph + self.request.GET.get('query')
        response = requests.get(endpoint, {'access_token': token})

        return self.render_json_response(response.json())
