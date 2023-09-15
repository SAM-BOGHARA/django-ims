from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def dashboard(request):
    return render(request, "basic/dashboard.html")


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username", extra_tags="alert-danger")
            return redirect("/login")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password", extra_tags="alert-danger")
            return redirect("/login")

        else:
            login(request, user)
            return redirect("/")

    return render(request, "basic/login.html")


def logout_page(request):
    logout(request)
    return redirect("/login")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.warning(
                request, "Username already taken.", extra_tags="alert-danger"
            )
            return redirect("/register")

        user = User.objects.create(username=username)

        user.set_password(password)
        user.save()

        messages.success(
            request, "Account Created Successfully.", extra_tags="alert-success"
        )

        return redirect("/login")

    return render(request, "basic/register.html")


def logout_page(request):
    logout(request)
    return redirect("/login")
