from django.db import models
from cereal.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class SearchHistory(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.CharField(max_length=9999, default="https://img.icons8.com/material-rounded/200/000000/user.png")