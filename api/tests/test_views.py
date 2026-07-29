from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from api.models import Book


class BookViewTest(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            isbn="9781503271620",
            published_date="2020-01-01",
        )
        self.list_url = reverse("api:books-list")
        self.create_url = reverse("api:books-create")
        self.retrieve_url = reverse("api:books-retrieve", kwargs={"id": self.book.id})
        self.update_url = reverse("api:books-update", kwargs={"id": self.book.id})
        self.delete_url = reverse("api:books-delete", kwargs={"id": self.book.id})

    def test_list_books_returns_existing_books(self):
        response = self.client.get(self.list_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book.title)

    