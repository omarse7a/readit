from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def book_manager(request):
    return render(request, "admin-section/book-manager.html", {"books": Book.objects.all()})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "admin-section/book-update.html", {"book" : book})