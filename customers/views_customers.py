from django.contrib.auth.forms import UserCreationForm
from django.forms.forms import Form
from django.shortcuts import redirect, render

# Create your views here.
def v_login(request):
  return render(request, 'auth.html', { 'type' : 'log' } )

def v_signup(request):
  frm = UserCreationForm()
  context = { 'type' : 'sign', 'form' : frm }
  return render(request , 'auth.html' , context)