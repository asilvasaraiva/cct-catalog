from django.db.models import QuerySet

from .exceptions import BookNotFoundError
from .models import Book
from .repositories import BookRepository


class BookService:

    @staticmethod
    def list_books() -> QuerySet:
        return BookRepository.list_all()

    @staticmethod
    def get_book(id) -> Book:
        book = BookRepository.get_by_id(id)
        if book is None:
            raise BookNotFoundError(f"Book with id={id} was not found.")
        return book

    @staticmethod
    def create_book(validated_data: dict) -> Book:
        book = Book(**validated_data)
        return BookRepository.save(book)

    @staticmethod
    def update_book(book: Book, validated_data: dict) -> Book:
        for field, value in validated_data.items():
            setattr(book, field, value)
        return BookRepository.save(book)

    @staticmethod
    def delete_book(book: Book) -> None:
        BookRepository.delete(book)
