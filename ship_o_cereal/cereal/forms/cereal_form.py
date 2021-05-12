from django.forms import ModelForm, widgets
from cereal.models import Product
from django import forms

class CandyCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}}))
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'brand': widgets.TextInput(attrs={'class': 'form-control'}),
            'tags': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }
