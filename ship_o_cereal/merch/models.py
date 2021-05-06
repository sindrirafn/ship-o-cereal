from django.db import models
from cereal.models import CerealCategory

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank = True)
    price = models.FloatField()
    CerealCategory = models.ForeignKey(CerealCategory, on_delete=models.CASCADE)

