from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from cereal.models import CerealImage
import json
# Create your views here.

"""
def index(request):
    return render(request, 'cart/creditcard.html')
"""


# GET gets all items in cart for logged in user and images
def index(request):
    if request.user.is_authenticated:
        customer = request.user.Profile
        cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
        items = cart.cartitem_set.all()
        products = [item.product for item in items]
        print(products)
        images = CerealImage.objects.filter(cereal__in=products)
        print(images)
    else:
        items = []
        cart = {'get_cart_total':0}
        images = {'link': ''}
    context = {'item': items, 'order':cart, 'images':images}
    return render(request, 'cart/index.html', context)


