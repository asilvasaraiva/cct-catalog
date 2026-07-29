from rest_framework import serializers

from .models import Book
from .repositories import BookRepository


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "isbn", "published_date"]

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title is required.")
        return value.strip()

    def validate_author(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Author is required.")
        return value.strip()

    def validate_isbn(self, value):
        normalized = value.replace("-", "").strip()
        if len(normalized) != 13 or not normalized.isdigit():
            raise serializers.ValidationError("ISBN must be a 13-digit number.")

        exclude_id = self.instance.id if self.instance is not None else None
        if BookRepository.isbn_exists(normalized, exclude_id=exclude_id):
            raise serializers.ValidationError("A book with this ISBN already exists.")

        return normalized
