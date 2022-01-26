from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from products.models import Product

# Create your views here.
def v_index(request):
  return render(request, 'index.html')
  
def v_home(request):
    prd = Product.objects.all()
    context = { 'products' : prd }
    return render(request, 'home.html', context)

