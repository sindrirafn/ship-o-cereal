from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

merch = [
    {'name': 'Cocoa Puffs Shirt', 'price': 420},
    {'name': 'Kellogs Bowls', 'price': 69},

]

def index(request):
    return render(request, 'merch/index.html', context={'merch': merch})
