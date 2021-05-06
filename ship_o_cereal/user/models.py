from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)

class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


