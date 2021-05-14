from django import forms
from django_countries.fields import CountryField
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField



class ContactInfoForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    apartment_number = forms.CharField(max_length=255, required=False)
    additional_information = forms.CharField(max_length=999, required=False, widget=forms.Textarea)
    country = CountryField(blank_label='(Select country)').formfield()
    city = forms.CharField(max_length=255)
    zip = forms.CharField(max_length=20)


class PaymentForm(forms.Form):
    name_on_the_card = forms.CharField(max_length=255, label="Name", widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    cc_number = CardNumberField(label='Card Number', widget=forms.TextInput(attrs={'placeholder': 'Credit card number'}))
    cc_expiry = CardExpiryField(label='Expiration Date', widget=forms.TextInput(attrs={'placeholder': 'Expiry date'}))
    cc_code = SecurityCodeField(label='CVV/CVC', widget=forms.TextInput(attrs={'placeholder': 'CVV/CVC'}))
