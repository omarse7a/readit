from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Book

# Create your views here.

def book_manager(request):
    return render(request, "admin-section/book-manager.html", {"books": Book.objects.all()})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    categories = Book.CATEGORY_CHOICES
    languages = Book.LANGUAGE_CHOICES
    context = {"book": book, "categories" : categories, "languages" : languages}
    return render(request, "admin-section/book-update.html", context)

def button_clicked(request, book_id):
    book = Book.objects.get(id = book_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "update":
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.category = request.POST.get("category")
            book.no_of_pages = request.POST.get("no_of_pages")
            book.language = request.POST.get("language")
            book.description = request.POST.get("description")
            book.price = request.POST.get("price")
            book.copies = request.POST.get("copies")
            book.save()
            return redirect('book_update', book_id=book.id)
        
        elif action == "delete":
            book.delete()
            return redirect('book_list')
