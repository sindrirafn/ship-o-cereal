from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from cereal.models import Product
# Create your views here.


# def index(request):
#     if 'orderBy' in request.GET:
#         orderParameter = request.GET['orderBy']
#         context = {'products': Product.objects.all().order_by(orderParameter)}
#     else:
#         context = {'products': Product.objects.all().order_by('name')}
#
#     return render(request, 'cereal/index.html', context)
brandNames = Product.objects.values('brand').distinct()
# def index(request):
#
#     if 'searchStr' not in request.GET and 'filterBy' not in request.GET:
#         return render(request, 'cereal/index.html',
#                       context = {'products': Product.objects.all().order_by('name'), 'brandNames': brandNames })
#
#     else:
#         results = Product.objects
#         if 'searchStr' in request.GET:
#             searchParameter = request.GET['searchStr']
#             results = results.filter(name__icontains=searchParameter).order_by('name')
#         if 'filterBy' in request.GET:
#             filterParameter = request.GET['filterBy']
#             results = results.filter(brand=filterParameter).order_by('name')
#         # context = {'products': Cereal.objects.filter(name__icontains=searchParameter).order_by('name')}
#         # brands = results.distinct('manufacturer').order_by('manufacturer')
#         # context = {'products': results, 'brands': brands}
#         context = {'products': results, 'brandNames': brandNames}
#         return render(request, 'cereal/index.html', context)

def index(request):
    if 'searchStr' in request.GET:
        searchParameter = request.GET['searchStr']
        results = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.cerealimage_set.first().image
        } for x in Product.objects.filter(name__icontains=searchParameter)]
        return JsonResponse({'data': results})
    if 'orderBy' in request.GET:
        orderBy = request.GET['orderBy']
        results = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.cerealimage_set.first().image
        } for x in Product.objects.all().order_by(orderBy) ]
        return JsonResponse({'data': results})
    if 'brand-filter' in request.GET:
        brandFilter = request.GET['brand-filter']
        results = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.cerealimage_set.first().image
        } for x in Product.objects.filter(brand=brandFilter).order_by('name')]
        return JsonResponse({'data': results})
    if 'category-filter' in request.GET:
        categoryFilter = request.GET['category-filter']
        results = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.cerealimage_set.first().image
        } for x in Product.objects.filter(tags__icontains=categoryFilter).order_by('name')]
        return JsonResponse({'data': results})
    context = {'products': Product.objects.all().order_by('name'), 'brandNames': brandNames}
    return render(request, 'cereal/index.html', context)


def product_by_name(request, name):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Product, name=name)
    })

def create_candy(request):
    if request.method =='POST':
        return 1
    else:
        print(2)
    return render(request, 'cereal/create_cereal.html')