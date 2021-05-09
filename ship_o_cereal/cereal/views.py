from django.shortcuts import render
# Create your views here.

cereals = [
    {'name': 'Cocoa Puffs', 'price': 420},
    {'name': 'Rice Krispies', 'price': 69},
    {'name': 'Cheerios', 'price': 6969},

]

def index(request):
    return render(request, 'cereal/index.html', context={'cereals': cereals})

def item(request):
    return render(request, 'cereal/single_product.html')