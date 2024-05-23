from django.urls import path
from . import views

urlpatterns = [
    path('', views.borrowedBooks, name='borrowed-books'),
]