from django import forms
from django.contrib.auth.models import User
from .models import Customer


class FormCustomer(forms.Form):
  class Meta:
    model = Customer
    fields = [ 'username', 'password1', 'password2' ]
    