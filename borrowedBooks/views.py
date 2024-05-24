from django.shortcuts import render
from manageBooks.models import Book, Borrowed
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def borrowedBooks(request):
    current_user = request.user
    userID = current_user.id
    
    return render(request, 'user-section/borrowedBooks.html', {'userID' : userID})

def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)
    
def borrowed_books_list(request):
    borrowed_books = list(Borrowed.objects.values())
    return JsonResponse(borrowed_books, safe=False)
    