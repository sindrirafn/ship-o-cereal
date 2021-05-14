from django.shortcuts import render, get_object_or_404
from cereal.models import Product
from user.models import Profile
from cart.models import Cart, CartItem
from django.http import JsonResponse
import json

# Create your views here.


# def index(request):
#     if 'orderBy' in request.GET:
#         orderParameter = request.GET['orderBy']
#         context = {'products': Product.objects.all().order_by(orderParameter)}
#     else:
#         context = {'products': Product.objects.all().order_by('name')}
#
#     return render(request, 'cereal/creditcard.html', context)
brandNames = Product.objects.values('brand').distinct()
# def index(request):
#
#     if 'searchStr' not in request.GET and 'filterBy' not in request.GET:
#         return render(request, 'cereal/creditcard.html',
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
#         return render(request, 'cereal/creditcard.html', context)

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
        } for x in Product.objects.filter(brand__icontains=brandFilter).order_by('name')]
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

# search function, used in search
def product_by_name(request, name):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Product, name=name)
    })


# used to update cart when cart button is clicked, see cart.js
def updatecart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.Profile
    product = Product.objects.get(id=productId)
    cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    # add adds one but remove removes all instances of object in cart
    if action == 'add':
        cartItem.count = (cartItem.count +1)
    elif action == 'remove':
        cartItem.count = 0
    cartItem.save()

    if cartItem.count <= 0:
        cartItem.delete()

    return JsonResponse('Item was added', safe=False)

