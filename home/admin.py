from django.contrib import admin
from .models import Product,Customer, Order,ProdImages
# Register your models here.

admin.site.register(Product)
admin.site.register(ProdImages)
admin.site.register(Customer)
admin.site.register(Order)
