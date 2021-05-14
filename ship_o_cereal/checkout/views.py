from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from cart.models import Cart
from checkout.models import ContactInfo, PaymentInfo
from checkout.forms import ContactInfoForm, PaymentForm
from django_countries import countries

# Create your views here.

# helper function to get the cart to all views in check-out process
def getcart(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(customer=request.user.Profile, complete=False)
            items = cart.cartitem_set.all()
        except ObjectDoesNotExist:
            cart = 'empty'
            items = []
    else:
        items = []
        cart = 'empty'
    context = {'item': items, 'cart': cart}
    return context


def creditcard(request):
    if request.method == 'GET':
        context = getcart(request)
        if context['cart'] != 'empty':
            form = ContactInfoForm()
            context['form'] = form
        else:
            return redirect('/')
        form = PaymentForm()
        context['form'] = form
    if request.method == 'POST':
        form = PaymentForm(request.POST or None)
        if form.is_valid():
            print('Credit Card form is valid')
            nameOnCC = form.cleaned_data.get('name_on_the_card')
            expDate = form.cleaned_data.get('cc_expiry')
            paymentInfo = PaymentInfo(user=request.user.Profile, nameOnCC=nameOnCC, expDate=expDate)
            paymentInfo.save()
            return redirect('checkout-confirmation')
        else:
            context = getcart(request)
            form = PaymentForm()
            context['form'] = form
            context['error'] = 'Input invalid'
    return render(request, 'checkout/creditcard.html', context)


def contact(request):
    if request.method == 'GET':
        context = getcart(request)
        if context['cart'] != 'empty':
            form = ContactInfoForm()
            context['form'] = form
            return render(request, 'checkout/contact.html', context)
        else:
            return redirect('/')
    if request.method == 'POST':
        form = ContactInfoForm(request.POST or None)
        try:
            cart = Cart.objects.get(customer=request.user.Profile, complete=False)
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                address = form.cleaned_data.get('address')
                apartment_number = form.cleaned_data.get('apartment_number')
                additional_information = form.cleaned_data.get('additional_information')
                country = form.cleaned_data.get('country')
                city = form.cleaned_data.get('city')
                zip = form.cleaned_data.get('zip')
                contactinfo = ContactInfo(
                    user=request.user.Profile, first_name=first_name, last_name=last_name, email=email,
                    address=address, apartment_number=apartment_number, additional_information=additional_information,
                    country=country, city=city, zip=zip
                )
                contactinfo.save()
                cart.contactinfo = contactinfo
                cart.save()
                return redirect('checkout-creditcard')
        except ObjectDoesNotExist:
            print('User does not have an active order')
            return redirect('/')



def confirmation(request):
    if request.method == 'GET':
        context = getcart(request)
        if context['cart'] != 'empty':
            contactinfo = ContactInfo.objects.filter(user=request.user.Profile).last()  #saekir nyjasta contact info
            paymentinfo = PaymentInfo.objects.filter(user=request.user.Profile).last()
            country = dict(countries)[contactinfo.country[0]]
            context['contact'] = contactinfo
            context['country'] = country
            context['payment'] = paymentinfo
            return render(request, 'checkout/confirmation.html', context)
        else:
            return redirect('/')
    if request.method == 'POST':
        cart = Cart.objects.get(customer=request.user.Profile, complete=False)
        cart.transactionId = cart.id
        cart.complete = True
        cart.save()
        return redirect('checkout-receipt')

def receipt(request):
    cart = Cart.objects.filter(customer=request.user.Profile).last()
    items = cart.cartitem_set.all()
    paymentinfo = PaymentInfo.objects.filter(user=request.user.Profile).last()
    context = {'item':items, 'payment':paymentinfo}
    return render(request, 'checkout/receipt.html', context)
