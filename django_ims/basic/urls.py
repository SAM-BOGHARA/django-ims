from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
   path('', dashboard, name = "dashboard"),
   path('login/', login_page, name = "login_page"),
   path('register/', register_page, name = "register_page"),
   path('logout/', logout_page, name = "logout_page")
]
