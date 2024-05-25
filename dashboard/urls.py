from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('add-books/', views.addBooks, name='addbooks'),  
    path('add-books/add', views.add_book, name='add'),
    path('logout/',views. user_logout, name='logout'),
]
