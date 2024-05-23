from django.shortcuts import render
from manageBooks.models import Book 
# Create your views here.
def home(request):
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