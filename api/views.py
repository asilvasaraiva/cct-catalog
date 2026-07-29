from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import BookNotFoundError
from .serializers import BookSerializer
from .services import BookService

class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        books = BookService.list_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = BookService.create_book(serializer.validated_data)
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)


class BookRetrieveView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            book = BookService.get_book(id)
        except BookNotFoundError as exc:
            raise Http404(str(exc)) from exc
        return Response(BookSerializer(book).data)


class BookUpdateView(APIView):
    def _update(self, request, id, partial):
        try:
            book = BookService.get_book(id)
        except BookNotFoundError as exc:
            raise Http404(str(exc)) from exc

        serializer = BookSerializer(book, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        updated_book = BookService.update_book(book, serializer.validated_data)
        return Response(BookSerializer(updated_book).data)

    def put(self, request, id, *args, **kwargs):
        return self._update(request, id, partial=False)

    def patch(self, request, id, *args, **kwargs):
        return self._update(request, id, partial=True)


class BookDeleteView(APIView):
    def delete(self, request, id, *args, **kwargs):
        try:
            book = BookService.get_book(id)
        except BookNotFoundError as exc:
            raise Http404(str(exc)) from exc

        BookService.delete_book(book)
        return Response(status=status.HTTP_204_NO_CONTENT)


book_list_view = BookListView.as_view()
book_create_view = BookCreateView.as_view()
book_retrieve_view = BookRetrieveView.as_view()
book_update_view = BookUpdateView.as_view()
book_delete_view = BookDeleteView.as_view()
