from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login

# Create your views here.
def v_index(request):
    return render(request, 'index.html', context={} )

def v_login(request):
    return render(request, 'registration/login.html' )

def v_signup(request):
    return render(request, 'registration/register.html' )

def v_products(request):
    return render(request)
