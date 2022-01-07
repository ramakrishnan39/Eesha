from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BigAutoField, CharField, IntegerField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from customers.models import Customer
# Create your models here.

class Category(models.Model):
    cat_id = BigAutoField(primary_key="True")
    cat_name = CharField(max_length=250)

class Product(models.Model):
    prod_id = BigAutoField(primary_key="True")
    prod_name = CharField(max_length=250)
    prod_category = ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    ord_id = BigAutoField(primary_key="True")
    cust_id =ForeignKey(Customer, on_delete=models.CASCADE)
    prod_id = ForeignKey(Product, on_delete=models.CASCADE)

class ProdImages(models.Model):
    img_id = BigAutoField(primary_key="True")
    prod_id= ForeignKey(Product, on_delete=models.CASCADE)
    img = ImageField()


    