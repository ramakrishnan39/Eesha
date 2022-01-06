from django import forms
from django.contrib.auth.models import User


class FormUser(User):
  class Meta:
    model = User
    fields = [ 'username', 'password1', 'password2' ]
    