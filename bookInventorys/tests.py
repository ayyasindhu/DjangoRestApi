from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.response import Response

class TestAPIRequestFactory(TestCase):

    def getBookInventorys(self):
        factory = APIRequestFactory()
        request = factory.get('/api/bookInventorys')
        assert response.status_code == 200
