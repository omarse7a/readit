from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('book-manager/', include('manageBooks.urls')),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),  
    path('add-books/', dashboard_views.addBooks, name='addbooks'),  
    path('books/', include('BooksViewer.urls')),
    path('', include('home.urls')),
    path('borrowed-books/', include('borrowedBooks.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
