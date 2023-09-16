from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import Itemform
from .models import *

# Create your views here.


def dashboard(request):
    return render(request, "basic/dashboard.html")


def categories(request):
    categories = Category.objects.all()
    selected_categories = request.GET.getlist("category")
    items = (
        Item.objects.filter(category__in=selected_categories)
        if selected_categories
        else Item.objects.all()
    )
    return render(
        request,
        "basic/category.html",
        {
            "categories": categories,
            "items": items,
            "selected_categories": selected_categories,
        },
    )


def locations(request):
    locations = Location.objects.all()
    selected_locations = request.GET.getlist("location")
    items = (
        Item.objects.filter(location__in=selected_locations)
        if selected_locations
        else Item.objects.all()
    )
    return render(
        request,
        "basic/location.html",
        {
            "locations": locations,
            "items": items,
            "selected_locations": selected_locations,
        },
    )


def items(request):
    queryset = Item.objects.all()

    context = {"items": queryset}
    return render(request, "basic/items.html", context)


def additem(request):
    form = Itemform()

    if request.method == "POST":
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "basic/dashboard.html")

    context = {
        "form": form,
    }
    return render(request, "basic/additem.html", context)


def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return render(request, "basic/items.html")


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
    if request.method != "POST":
        return render(request, "basic/register.html")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.filter(username=username)

    if user.exists():
        messages.warning(request, "Username already taken.", extra_tags="alert-danger")
        return redirect("/register")

    user = User.objects.create(username=username)

    user.set_password(password)
    user.save()

    messages.success(
        request, "Account Created Successfully.", extra_tags="alert-success"
    )

    return redirect("/login")


def logout_page(request):
    logout(request)
    return redirect("/login")
