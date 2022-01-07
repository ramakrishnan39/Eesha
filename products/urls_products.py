from django.contrib import admin
from django.urls import path
from . import views_products

urlpatterns = [
    path('', views_products.v_product, name="Product"),
]
