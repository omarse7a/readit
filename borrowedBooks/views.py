from django.shortcuts import render

# Create your views here.
def borrowedBooks(request):
    return render(request, 'user-section/borrowedBooks.html')