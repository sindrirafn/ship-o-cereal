from django.shortcuts import render, get_object_or_404
from merch.models import Product
from django.http import HttpResponse
# Create your views here.

merch = [
    {'name': 'Cocoa Puffs Shirt', 'price': 420},
    {'name': 'Kellogs Bowls', 'price': 69},

]

def index(request):
    return render(request, 'merch/index.html', context={'merch': merch})

def merch_by_id(request, id):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Product, pk=id)
    })
