from django.urls import path,include
from django.contrib import admin
from django.urls import re_path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    re_path(r'^((login|signup)/)*(login|signup)/$', views.handle_combined, name='combined'),
]