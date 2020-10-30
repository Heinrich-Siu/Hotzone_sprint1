from django.db import models


# Create your models here.
class Address(models.Model):
    addressZH = models.CharField(max_length=200)
    nameZH = models.CharField(max_length=200)
    x = models.DecimalField(max_digits=20, decimal_places=0)
    y = models.DecimalField(max_digits=20, decimal_places=0)
    nameEN = models.CharField(max_length=200)
    addressEN = models.CharField(max_length=200)
