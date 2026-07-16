from rest_framework.test import APITestCase
from django.urls import reverse

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert(response.status_code, 200)
        assert(response.data, {"hello": "Django"})