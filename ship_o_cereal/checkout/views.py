from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from cart.models import Cart
from checkout.forms import ContactInfoForm, PaymentForm

# Create your views here.


# helper function to get the cart to all views in check-out process
def getcart(request):
    if request.user.is_authenticated:
        customer = request.user.Profile
        cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
        items = cart.cartitem_set.all()
    else:
        items = []
        cart = {'get_cart_total': 0}
    context = {'item': items, 'order': cart}
    return context


def creditcard(request):
    context = getcart(request)
    form = PaymentForm()
    context['form'] = form
    return render(request, 'checkout/creditcard.html', context)


def contact(request):
    if request.method == 'GET':
        context = getcart(request)
        form = ContactInfoForm()
        context['form'] = form
    return render(request, 'checkout/contact.html', context)


def confirmation(request):
    context = getcart(request)
    form = ContactInfoForm()
    context['form'] = form
    return render(request, 'checkout/confirmation.html', context)


def completeCheckout(request):


    return JsonResponse('Payment complate!', safe=False)