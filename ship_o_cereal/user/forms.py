from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import UserProfile


class TheProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user']
