from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login

# Create your views here.
def v_index(request):
    return render(request, 'home.html' )

def v_login(request):
    return redirect(request, 'registration/login.html' )

def v_signup(request):
    return redirect(request, 'registration/register.html' )

def v_mobiles(request):
    return render(request, 'mobiles.html')

def v_tvs(request):
    return render(request, 'tvs.html')

def v_order(request):
    return render(request, 'order.html')

