from django.db import models

# Create your models here.


class CerealCategory(models.Model):
    name = models.CharField(max_length=255)


class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank = True)
    price = models.FloatField()
    manufacturer = models.CharField(max_length=200, blank = True)
    category = models.ForeignKey(CerealCategory, on_delete=models.CASCADE)



class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)
