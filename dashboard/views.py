from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.models import User
from manageBooks.models import Book , Borrowed
from django.contrib.auth import logout
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage

@login_required
def dashboard(request):
    try:
        profile = Profile.objects.get(user=request.user)
        role = profile.role
        if role == 'Admin':
            user = request.user
            fname = user.first_name 
            lname = user.last_name

            published_num = Book.objects.count()
            borrowed_num = Borrowed.objects.count()
            earnings = Borrowed.objects.aggregate(total_earnings=Sum('book__price'))['total_earnings']
            most_borrowed_book = Book.objects.order_by('-borrowed_copies').first()
            if most_borrowed_book:
                most_borrowed_title = most_borrowed_book.title
                most_borrowed_image = most_borrowed_book.cover
            else:
                most_borrowed_title = None
                most_borrowed_image = None

            return render(request, 'admin-section/admin-dashboard.html', {
                'fname': fname,
                'lname': lname,
                'published_num': published_num,
                'borrowed_num': borrowed_num,
                'earnings': earnings,
                'most_borrowed_title': most_borrowed_title,
                'most_borrowed_image': most_borrowed_image,
            })
    except Profile.DoesNotExist:
        return redirect('home')

@login_required
def addBooks(request):
    try:
        profile = Profile.objects.get(user=request.user)
        role = profile.role
        user = request.user
        if role == 'Admin':
            fname = user.first_name 
            lname = user.last_name
            categories = Book.CATEGORY_CHOICES
            languages = Book.LANGUAGE_CHOICES   
            context = {"categories" : categories, "languages" : languages, 'fname': fname,
                'lname': lname,}
            return render(request, 'admin-section/add-books.html' ,context)
    except Profile.DoesNotExist:
        return redirect('home')

def add_book(request):
   if request.method == "POST":
        title = request.POST.get("title")
        cover = request.FILES.get("cover")
        author = request.POST.get("author")
        category = request.POST.get("category")
        no_of_pages = request.POST.get("no_of_pages")
        language = request.POST.get("language")
        description = request.POST.get("description")
        price = request.POST.get("price")
        copies = request.POST.get("copies")

        new_book = Book(
            title=title,
            cover=cover,
            author=author,
            category=category,
            no_of_pages=no_of_pages,
            language=language,
            description=description,
            price=price,
            copies=copies
        )
        new_book.save()
        return redirect('addbooks')

def user_logout(request):
    logout(request)
    return redirect('home')