from django.shortcuts import render, redirect
from django.http import HttpResponse
from manageBooks.models import Book, Borrowed
from authentication.models import Profile
# Create your views here.
def view_books(request):
    return render(request, "user-section/available-books.html", {"books": Book.objects.all()})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "user-section/book-details.html", {"book" : book})

def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    profile = Profile.objects.get(user = request.user) 
    
    if book.current_borrower == None:
        book.current_borrower = profile
        book.isAvailable = False
        book.save()

        borrow = Borrowed(profile=profile, book=book)
        borrow.save()
    return redirect('book', book_id=book.id)