from django.contrib import admin
from django.urls import path
from nlt_for_railways import views

urlpatterns = [
   path('',views.login),
   path('r',views.register),
   path('home',views.home),
   path('api',views.API)
]