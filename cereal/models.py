from django.db import models

# Create your models here.


class CerealCategory(models.Model):
    name = models.CharField(max_length=255)


class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank = True)
    price = models.FloatField()
    category = models.ForeignKey(CerealCategory, on_delete=models.CASCADE)
    #manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)
