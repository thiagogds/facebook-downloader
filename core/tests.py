from django.test import TestCase
from django.urls import reverse

import responses

class DownloadJsonViewTest(TestCase):
    @responses.activate
    def test_correct_response(self):
        facebook_response = {
            "name": "Thiago Garcia Da Silva",
            "id": "438224431"
        }
        responses.add(responses.GET,
                      'https://graph.facebook.com/v2.7/me',
                      json=facebook_response, status=200,
                      content_type='application/json')

        url = reverse('core:download')
        response = self.client.get(url, {'query': 'me'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
