from django.shortcuts import render, get_object_or_404
from cereal.models import Product
# Create your views here.


def index(request):
    if 'orderBy' in request.GET:
        orderParameter = request.GET['orderBy']
        context = {'products': Product.objects.all().order_by(orderParameter)}
    else:
        context = {'products': Product.objects.all().order_by('name')}

    return render(request, 'cereal/index.html', context)

def index(request):

    if 'searchStr' not in request.GET and 'filterBy' not in request.GET:
        return render(request, 'cereal/index.html')


    else:
        results = Product.objects
        if 'searchStr' in request.GET:
            searchParameter = request.GET['searchStr']
            results = results.filter(name__icontains=searchParameter).order_by('name')
        if 'filterBy' in request.GET:
            filterParameter = request.GET['filterBy']
            results = results.filter(manufacturer=filterParameter).order_by('name')
        # context = {'products': Cereal.objects.filter(name__icontains=searchParameter).order_by('name')}
        # brands = results.distinct('manufacturer').order_by('manufacturer')
        # context = {'products': results, 'brands': brands}
        context = {'products': results}
        return render(request, 'cereal/index.html', context)
# def cereal_by_id(request, id):
#     return render(request, 'products/single_product.html', {
#         'product': get_object_or_404(Cereal, pk=id)
#     })

def product_by_name(request, name):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Product, name=name)
    })