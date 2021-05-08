from django.db import models
from cereal.models import Cereal

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)


class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SearchHistory(models.Model):
    item = models.ForeignKey(Cereal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


