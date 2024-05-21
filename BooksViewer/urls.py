from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_books, name='view_books'),
    path("book/<int:book_id>/", views.book_details, name="book"),
]

