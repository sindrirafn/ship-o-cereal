from django.shortcuts import render, get_object_or_404
from cereal.models import Cereal
# Create your views here.

# cereals = [
#     {'name': 'Cocoa Puffs', 'price': 420},
#     {'name': 'Rice Krispies', 'price': 69},
#     {'name': 'Cheerios', 'price': 6969},
#
# ]

def index(request):
    return render(request, 'cereal/index.html', context={'cereals': Cereal.objects.all().order_by('name')})

def cereal_by_id(request, id):
    return render(request, 'cereal/single_product.html', {
        'product': get_object_or_404(Cereal, pk=id)
    })