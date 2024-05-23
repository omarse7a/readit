from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_books, name='view_books'),
    path("book/<int:book_id>/", views.book_details, name="book"),
    path("book/<int:book_id>/borrow/", views.borrow_book, name="borrow"),
    path("book/<int:book_id>/return/", views.return_book, name="return"),
]

