from django.http import Http404
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import BookNotFoundError
from .serializers import BookSerializer
from .services import BookService


@extend_schema(tags=["Books"])
class BookListView(APIView):
    @extend_schema(
        summary="List books",
        description="Returns every book currently stored in the catalog.",
        responses={200: BookSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        books = BookService.list_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@extend_schema(tags=["Books"])
class BookCreateView(APIView):
    @extend_schema(
        summary="Create a book",
        description="Creates a new book entry in the catalog.",
        request=BookSerializer,
        responses={201: BookSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = BookService.create_book(serializer.validated_data)
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Books"])
class BookRetrieveView(APIView):
    @extend_schema(
        summary="Retrieve a book",
        description="Returns a single book by its id.",
        responses={
            200: BookSerializer,
            404: OpenApiResponse(description="Book not found."),
        },
    )
    def get(self, request, id, *args, **kwargs):
        try:
            book = BookService.get_book(id)
        except BookNotFoundError as exc:
            raise Http404(str(exc)) from exc
        return Response(BookSerializer(book).data)


@extend_schema(tags=["Books"])
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

    @extend_schema(
        summary="Replace a book",
        description="Fully replaces an existing book's data.",
        request=BookSerializer,
        responses={200: BookSerializer, 404: OpenApiResponse(description="Book not found.")},
    )
    def put(self, request, id, *args, **kwargs):
        return self._update(request, id, partial=False)

    @extend_schema(
        summary="Partially update a book",
        description="Updates one or more fields of an existing book.",
        request=BookSerializer,
        responses={200: BookSerializer, 404: OpenApiResponse(description="Book not found.")},
    )
    def patch(self, request, id, *args, **kwargs):
        return self._update(request, id, partial=True)


@extend_schema(tags=["Books"])
class BookDeleteView(APIView):
    @extend_schema(
        summary="Delete a book",
        description="Removes a book from the catalog.",
        responses={
            204: OpenApiResponse(description="Book deleted successfully."),
            404: OpenApiResponse(description="Book not found."),
        },
    )
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
