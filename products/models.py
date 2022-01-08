from django.db import models
# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.cat_name

class Product(models.Model):
    prod_name = models.CharField(max_length=250)
    prod_desc = models.CharField(max_length=1000, blank=True, null=True)
    prod_spec = models.CharField(max_length=1000, blank=True, null=True)
    prod_img = models.ImageField(upload_to='products/', null=True)
    prod_price = models.CharField(max_length=200, null=True, blank=True)
    prod_category = models.ForeignKey(Category, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.prod_name
