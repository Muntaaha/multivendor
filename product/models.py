from django.db import models
from store.models import *

class Category(models.Model):
    category_name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='products/', blank = True)
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.PositiveIntegerField()
    product_created = models.DateTimeField(auto_now_add=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    def __str__(self):
        return self.product_name