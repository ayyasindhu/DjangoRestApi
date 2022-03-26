from django.test import TestCase
from rest_framework.test import APIClient

class RestApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_getBookInventorys(self):
        response = self.client.get("/api/bookInventorys")
        assert response.status_code == 200

    def test_postBookInventorys(self):
        response = self.client.post("/api/bookInventorys", {'title':'testbook','author':'author'}, format='json')
        assert response.status_code == 201

    def test_deleteBookInventorys(self):
        response = self.client.delete("/api/bookInventorys")
        assert response.status_code == 204