from django.urls import path,include
from django.contrib import admin
from django.urls import re_path
from . import views
from .views import check_password_strength
urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('check_password_strength/', check_password_strength, name='check_password_strength'),]
