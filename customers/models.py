from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    cust = models.OneToOneField(User, on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=50, blank=True, null=True)
    cust_phone = models.IntegerField(blank=True, null=True)
    cust_address = models.CharField(max_length=500)
    cust_email = models.CharField(max_length=50)
