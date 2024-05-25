from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.models import User
from manageBooks.models import Book , Borrowed
from django.contrib.auth import logout
from django.db.models import Sum

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
        name = user.first_name 
        if role == 'Admin':
            return render(request, 'admin-section/add-books.html' ,{'name': name})
    except Profile.DoesNotExist:
        return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')