from django.db import models
from cereal.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SearchedItem(models.Model):
    searchHistory = models.ForeignKey(SearchHistory, on_delete=models.SET_NULL, blank=True, null=True)
    searchItem = models.CharField(max_length=255, null=True, blank=True)


# make_profile creates a entry in the user_profile table connected to user created
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
    profile_img = models.CharField(max_length=9999, default="https://img.icons8.com/material-rounded/200/000000/user.png")

    def make_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = Profile(user=user)
            user_profile.save()
    post_save.connect(make_profile, sender=User)

    def __str__(self):
        return str(self.id)