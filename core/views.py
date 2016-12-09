from django.views.generic import View
from django.conf import settings
from django.shortcuts import redirect

import requests
from braces.views import JSONResponseMixin


class FacebookDownloader(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        token = settings.FACEBOOK_TOKEN
        facebook_graph = 'https://graph.facebook.com/v2.7/'
        endpoint = facebook_graph + self.request.GET.get('query')
        response = requests.get(endpoint, {'access_token': token})
        json_data = response.json()
        if not json_data.get('data'):
            return self.render_json_response(response.json())

        return self.render_json_response(response.json()['data'])


class FacebookCSVDownloader(View):
    def get(self, request, *args, **kwargs):
        token = settings.FACEBOOK_TOKEN
        facebook_graph = 'https://graph.facebook.com/v2.7/'
        endpoint = facebook_graph + self.request.GET.get('query')
        response = requests.get(endpoint, {'access_token': token})
        csv_response = requests.post('https://json-csv.com/conversion/start', {'json': response.text})
        return redirect('https://json-csv.com' + csv_response.json()['href'])
