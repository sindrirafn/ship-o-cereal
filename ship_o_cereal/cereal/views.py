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
    if 'orderBy' in request.GET:
        orderParameter = request.GET['orderBy']
        context = {'cereals': Cereal.objects.all().order_by(orderParameter)}

    elif 'searchStr' in request.GET:
        searchParameter = request.GET['searchStr']
        context = {'cereals': Cereal.objects.filter(name__icontains=searchParameter).order_by('name')}
    else:
        context = {'cereals': Cereal.objects.all().order_by('name')}

    return render(request, 'cereal/index.html', context)

def cereal_by_id(request, id):
    return render(request, 'cereal/single_product.html', {
        'product': get_object_or_404(Cereal, pk=id)
    })