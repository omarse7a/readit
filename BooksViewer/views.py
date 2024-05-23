from django.shortcuts import render, redirect
from django.http import HttpResponse
from manageBooks.models import Book, Borrowed
from authentication.models import Profile, User
# Create your views here.
def view_books(request):
    return render(request, "user-section/available-books.html", {"books": Book.objects.all()})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    book_borrowed = Borrowed.objects.filter(user=request.user, book=book)
    return render(request, "user-section/book-details.html", {"book" : book, "book_borrowed" : book_borrowed})

def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    
    if book.copies > 0:
        book.copies -= 1
        book.save()
        borrow = Borrowed(user=user, book=book)
        borrow.save()

    return redirect('book', book_id=book.id)

def return_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user

    book.copies += 1
    book.save()
    borrowed_book = Borrowed.objects.filter(user=user, book=book)
    borrowed_book.delete()
    return redirect('book', book_id=book.id)