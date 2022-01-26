from django.contrib import admin
from django.urls import path
from . import views_home

urlpatterns = [
    path('', views_home.v_index, name="Index"),
    path('home/', views_home.v_home, name="Home"),
]
