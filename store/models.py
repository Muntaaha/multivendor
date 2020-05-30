from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length=200, null= True, blank=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

