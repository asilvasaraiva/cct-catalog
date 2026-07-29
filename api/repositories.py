from typing import Optional

from django.db.models import QuerySet

from .models import Book


class BookRepository:

    @staticmethod
    def list_all() -> QuerySet:
        return Book.objects.all().order_by("id")

    @staticmethod
    def get_by_id(id) -> Optional[Book]:
        return Book.objects.filter(pk=id).first()

    @staticmethod
    def isbn_exists(isbn: str, exclude_id=None) -> bool:
        queryset = Book.objects.filter(isbn=isbn)
        if exclude_id is not None:
            queryset = queryset.exclude(pk=exclude_id)
        return queryset.exists()

    @staticmethod
    def save(book: Book) -> Book:
        book.save()
        return book

    @staticmethod
    def delete(book: Book) -> None:
        book.delete()
