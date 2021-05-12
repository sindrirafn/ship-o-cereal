from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'cart/index.html')

def updateCart(request):
    return JsonResponse('Item added to cart!', safe=False)
