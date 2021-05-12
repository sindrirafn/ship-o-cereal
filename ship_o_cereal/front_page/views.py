from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cereal.models import Cereal
from merch.models import Product

# Create your views here.
def index(request):

    if 'searchStr' not in request.GET and 'filterBy' not in request.GET:
        return render(request, 'front_page/index.html')


    else:
        results = Cereal.objects
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
        return render(request, 'products/search_results.html', context)



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-index')
    return render(request, 'front_page/register.html', {
        'form': CustomUserCreationForm()
    })


def product_by_name(request, name):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Cereal, name=name)
    })

# def filter_by_manufacturer(request, manufacturer):
#     manufacturer = request.GET['brand']