from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class RoomTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_all_rooms(self):
        response = self.client.get('/api/rooms/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testing_book_rooms(self):
        response = self.client.get('/api/book/1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_website(self):
        self.client = APIClient()
        response = self.client.get('hello/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def testing_search_rooms(self):
        response = self.client.get('/api/search/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)