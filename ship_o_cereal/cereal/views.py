from django.shortcuts import render, get_object_or_404
from cereal.models import Cereal
# Create your views here.


def index(request):
    if 'orderBy' in request.GET:
        orderParameter = request.GET['orderBy']
        context = {'cereals': Cereal.objects.all().order_by(orderParameter)}
    else:
        context = {'cereals': Cereal.objects.all().order_by('name')}

    return render(request, 'cereal/index.html', context)

def cereal_by_id(request, id):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Cereal, pk=id)
    })