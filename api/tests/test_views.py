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

    def test_retrieve_book_returns_book_details(self):
        response = self.client.get(self.retrieve_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["isbn"], self.book.isbn)

    def test_create_book_with_valid_data_persists_record(self):
        payload = {
            "title": "Clean Architecture",
            "author": "Robert C. Martin",
            "isbn": "9780134494166",
            "published_date": "2017-09-10",
        }

        response = self.client.post(self.create_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data["title"], payload["title"])

    def test_create_book_with_invalid_data_returns_validation_errors(self):
        payload = {
            "title": "",
            "author": "Robert C. Martin",
            "isbn": "9780134494166",
            "published_date": "2017-09-10",
        }

        response = self.client.post(self.create_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertEqual(Book.objects.count(), 1)

    def test_update_book_modifies_existing_record(self):
        payload = {
            "title": "Django for Professionals",
            "author": self.book.author,
            "isbn": self.book.isbn,
            "published_date": "2020-01-01",
        }

        response = self.client.put(self.update_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, payload["title"])

    def test_delete_book_removes_existing_record(self):
        response = self.client.delete(self.delete_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_retrieve_update_delete_missing_book_returns_404(self):
        missing_id = self.book.id + 999
        retrieve_url = reverse("api:books-retrieve", kwargs={"id": missing_id})
        update_url = reverse("api:books-update", kwargs={"id": missing_id})
        delete_url = reverse("api:books-delete", kwargs={"id": missing_id})

        retrieve_response = self.client.get(retrieve_url, format="json")
        update_response = self.client.put(
            update_url,
            {
                "title": "Doesn't matter",
                "author": "Doesn't matter",
                "isbn": "9780000000000",
                "published_date": "2020-01-01",
            },
            format="json",
        )
        delete_response = self.client.delete(delete_url, format="json")

        self.assertEqual(retrieve_response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(update_response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(delete_response.status_code, status.HTTP_404_NOT_FOUND)