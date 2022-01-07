from django.shortcuts import render

# Create your views here.
def v_product(request):
  return render(request, 'product.html')