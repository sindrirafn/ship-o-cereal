from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import Profile


class TheProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_img': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ImprovedUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ['id', 'last_login', 'is_superuser', 'groups', 'is_staff', 'is_active', 'password',
                   'user_permissions', 'date_joined']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ChangePicForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_img': widgets.TextInput(attrs={'class': 'form-control'})
        }