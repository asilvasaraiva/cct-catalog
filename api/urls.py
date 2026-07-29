from django.urls import re_path #re_path is used for regex-based URL patterns

from .views import (
    book_create_view,
    book_delete_view,
    book_list_view,
    book_retrieve_view,
    book_update_view,
)

app_name = "api"

urlpatterns = [
    re_path(r'books/$', book_list_view, name='books-list'),
    re_path(r'books/create/$', book_create_view, name='books-create'),
    re_path(r'books/(?P<id>\d+)/$', book_retrieve_view, name='books-retrieve'),
    re_path(r'books/(?P<id>\d+)/update/$', book_update_view, name='books-update'),
    re_path(r'books/(?P<id>\d+)/delete/$', book_delete_view, name='books-delete'),
]