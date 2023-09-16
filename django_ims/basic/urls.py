from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
   path('', dashboard, name = "dashboard"),
   path('login/', login_page, name = "login_page"),
   path('register/', register_page, name = "register_page"),
   path('logout/', logout_page, name = "logout_page"),
   path('items/', items, name = "items"),
   path('add_item/', additem, name = "add_item"),
   path('delete_item/<int:id>', delete_item, name = "delete_item"),  
   path('categories/',categories,name = "categories"),
   path('locations/',locations,name = "locations"),
]
