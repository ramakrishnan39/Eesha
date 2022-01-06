from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from .views_customers import *

urlpatterns = [
    path('login/',v_login, name="LogSign" ),
]