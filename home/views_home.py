from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def v_home(request):
    return render(request, 'home.html')

