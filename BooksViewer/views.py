from django.shortcuts import render, redirect
from django.http import HttpResponse
from manageBooks.models import Book, Borrowed
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
# Create your views here.
@login_required
def view_books(request):
    try:
        profile = Profile.objects.get(user=request.user)
        role = profile.role
        if role == 'Customer':
            user = request.user
            fname = user.first_name
            lname = user.last_name
            return render(request, "user-section/available-books.html", {"books": Book.objects.all(), 'fname': fname,
                'lname': lname,})
    except Profile.DoesNotExist:
        return redirect('home')

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    if not request.user.is_authenticated:
        return render(request, "user-section/book-details.html", {"book" : book})
    try:
        profile = Profile.objects.get(user=request.user)
        role = profile.role
        if role == 'Customer':  
            book_borrowed = Borrowed.objects.filter(user=request.user, book=book)
            return render(request, "user-section/book-details.html", {"book" : book, "book_borrowed" : book_borrowed})
    except Profile.DoesNotExist:
        return render(request, "user-section/book-details.html", {"book" : book})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    
    if book.copies > book.borrowed_copies:
        book.borrowed_copies += 1
        book.save()
        borrow = Borrowed(user=user, book=book)
        borrow.save()

    return redirect('book', book_id=book.id)

@login_required
def return_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user

    book.borrowed_copies -= 1
    book.save()
    borrowed_book = Borrowed.objects.filter(user=user, book=book)
    borrowed_book.delete()
    return redirect('book', book_id=book.id)