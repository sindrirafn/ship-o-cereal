from django import forms
from django_countries.fields import CountryField


class ContactInfoForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    apartment_number = forms.CharField(max_length=255, required=False)
    additional_information = forms.CharField(max_length=999, required=False)
    country = CountryField(blank_label='(Select country)').formfield()
    city = forms.CharField(max_length=255)
    zip = forms.CharField(max_length=20)


#class PaymentForm(forms.Form):
