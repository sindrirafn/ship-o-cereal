from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cereal.models import Cereal
from merch.models import Product

# Create your views here.
def index(request):
    if 'searchStr' in request.GET:
        searchParameter = request.GET['searchStr']
        context = {'cereals': Cereal.objects.filter(name__icontains=searchParameter).order_by('name')}
        return render(request, 'products/search_results.html', context)
    else:
        return render(request, 'front_page/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-index')
    return render(request, 'front_page/register.html', {
        'form': UserCreationForm()
    })

def product_by_name(request, name):
    return render(request, 'products/single_product.html', {
        'product': get_object_or_404(Cereal, name=name)
    })