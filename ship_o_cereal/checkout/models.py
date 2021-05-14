from django.db import models
from django_countries.fields import CountryField
from user.models import Profile

# Create your models here.


class ContactInfo(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    apartment_number = models.CharField(max_length=255, blank=True)
    additional_information = models.CharField(max_length=999, blank=True)
    country = CountryField(multiple=True)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class PaymentInfo(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nameOnCC = models.CharField(max_length=255)
    expDate = models.CharField(max_length=10)