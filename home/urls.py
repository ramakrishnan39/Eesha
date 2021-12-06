from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_index, name="Index"),
    path('login/',views.v_login, name="Login" ),
    path('signup/', views.v_signup, name="Signup"),
    
]
