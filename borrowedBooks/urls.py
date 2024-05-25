from django.urls import path
from . import views

urlpatterns = [
    path('', views.borrowedBooks, name='borrowed-books'),
    path('api/books/', views.book_list, name='book-list'),
    path('api/borrowed-books/', views.borrowed_books_list, name='borrowed-book-list'),
]
