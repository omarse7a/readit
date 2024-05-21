from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_manager, name="book_list"),
    path("book/<int:book_id>/", views.book_details, name="book_manage"),
]