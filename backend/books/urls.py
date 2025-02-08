from django.urls import path
from .views import book_list, book_create, book_detail, book_update, book_delete

urlpatterns = [
    path("books/", book_list, name="book-list"),
    path("books/new/", book_create, name="book-create"),
    path("books/<int:pk>/", book_detail, name="book-detail"),
    path("books/<int:pk>/edit/", book_update, name="book-update"),
    path("books/<int:pk>/delete/", book_delete, name="book-delete"),
]
