from django.shortcuts import render
from django.http import HttpResponse
from manageBooks.models import Book
# Create your views here.
def view_books(request):
    return render(request, "user-section/available-books.html", {"books": Book.objects.all()})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "user-section/book-details.html", {"book" : book})
