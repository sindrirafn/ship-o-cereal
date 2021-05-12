from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=999, blank=True)
    price = models.FloatField()


class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Product, on_delete=models.CASCADE)


