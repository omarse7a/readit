from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from .models import Book

# Create your views here.

@login_required
def book_manager(request):
    try:
        profile = Profile.objects.get(user=request.user)
        role = profile.role
        if role == 'Admin':
            user = request.user
            fname = user.first_name 
            lname = user.last_name
            return render(request, "admin-section/book-manager.html", {"books": Book.objects.all(), 'fname': fname,
                'lname': lname,})
    except Profile.DoesNotExist:
        return redirect('home')

@login_required
def book_details(request, book_id):
    try:
        profile = Profile.objects.get(user=request.user)
        role = profile.role
        if role == 'Admin':
            user = request.user
            fname = user.first_name 
            lname = user.last_name
            book = Book.objects.get(id=book_id)
            categories = Book.CATEGORY_CHOICES
            languages = Book.LANGUAGE_CHOICES   
            context = {"book": book, "categories" : categories, "languages" : languages, 'fname': fname,
                'lname': lname,}
            return render(request, "admin-section/book-update.html", context)
    except Profile.DoesNotExist:
        return redirect('home')


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
            book.reviews = request.POST.get("reviews")
            book.ratings = request.POST.get("ratings")
            book.copies = request.POST.get("copies")
            book.save()
            return redirect('book_update', book_id=book.id)
        
        elif action == "delete":
            book.delete()
            return redirect('book_list')
