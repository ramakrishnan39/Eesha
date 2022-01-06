from django.shortcuts import redirect, render
from .forms_customers import FormUser

# Create your views here.
def v_login(request):
  page = ""
  if request.method == 'POST':

    return render(request, 'home.html')
  return render(request, 'logsign.html', {'page' : page , })