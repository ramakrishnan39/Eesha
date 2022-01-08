from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class FormCustomer(forms.Form):
  class Meta:
    model = UserCreationForm()
    fields = ("username", "email", "password1", "password2")
    