from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
import json
# Create your views here.

"""
def index(request):
    return render(request, 'cart/index.html')
"""


def index(request):
    if request.user.is_authenticated:
        customer = request.user.Profile
        cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
        items = cart.cartitem_set.all()
    else:
        items = []
        cart = {'get_cart_total':0}
    context = {'item': items, 'order':cart}
    return render(request, 'cart/index.html', context)


