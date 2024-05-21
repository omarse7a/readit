from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
import re


def is_valid_email(email):
    # Regular expression pattern for a valid email address
    email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+$'

    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False
# Create your views here.

def home(request):
    return render(request, "index.html")


def handle_combined(request, *args, **kwargs):
    # Determine the final segment of the URL
    final_segment = request.path.strip('/').split('/')[-1]

    if final_segment == 'login':
        return login(request)
    elif final_segment == 'signup':
        return signup(request)
    else:
        # Default action or 404
        return render(request, '404.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        password2 = request.POST['ConfirmPassword']
        email = request.POST['Email']
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        role = request.POST['user-type']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect("signup")
        if len(username) > 10:
            messages.error(request, "Username must be less than 10 characters")
            return redirect("signup")
        if len(username) < 5:
            messages.error(request, "Username must be more than 5 characters")
            return redirect("signup")
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            return redirect("signup")

        if password != password2:
            messages.error(request, "Passwords must match")
            return redirect("signup")

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect("signup")
        if not is_valid_email(email):
            messages.error(request, "Invalid email address")
            return redirect("signup")

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        profile = Profile(user=myuser, role=role)
        profile.save()

        messages.success(request, "Account created")
        return redirect("login")

    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "You are now logged in")
            return render(request, "index.html", {'FirstName': user.first_name, 'LastName': user.last_name})
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    messages.success(request, "You are now logged out")
    return redirect("home")
