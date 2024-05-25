from django.shortcuts import render, redirect

from authentication.models import Profile
from manageBooks.models import Book 
# Create your views here.
def home(request):
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
        role = profile.role
        if role == "Admin":
            return redirect('dashboard')
    except:
        return render(request,'home.html')
    query = request.GET.get('q')
    results = []
    if query:
       results = Book.objects.filter(
            title__icontains=query
        ) | Book.objects.filter(
            author__icontains=query
        ) | Book.objects.filter(
            category__icontains=query
        )
    return render(request, 'home.html', {'results': results, 'query': query})