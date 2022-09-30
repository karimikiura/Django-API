from urllib.parse import urlparse
from django.urls import path

from .views import BookListView, delete

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<int:book_id>/delete/', delete, name='book-delete'),
]