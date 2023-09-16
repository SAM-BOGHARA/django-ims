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
   path('update_item/<int:id>', update_item, name = "delete_item"),  
   path('categories/',categories,name = "categories"),
   path('locations/',locations,name = "locations"),
   path('request_form/', request_form, name = "request_form"),
   path('review_request/',review_request, name = "review_request"),
   path('review-form/<int:id>', review_form, name = "review_form"),
]
