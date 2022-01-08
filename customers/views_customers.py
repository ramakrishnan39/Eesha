from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms_customers import FormCustomer


# Create your views here.
def v_login(request):
  frm = FormCustomer()
  return render(request, 'logsign.html', { 'formlog' : frm } )

def v_signup(request):
  frm = FormCustomer()
  context = { 'formsign' : frm }
  return render(request , '' , context)