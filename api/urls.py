from django.urls import re_path #re_path is used for regex-based URL patterns

from .views import book_view

app_name = "api"

urlpatterns = [
    re_path(r'books/$', book_view, name='books'),
]