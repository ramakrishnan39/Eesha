from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms_customers import FormCustomer

# Create your views here.
def v_login(request):
  return render(request, 'logsign.html')