from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cereal.models import Product

# Create your views here.
def index(request):
    return render(request, 'front_page/index.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-index')

    return render(request, 'front_page/register.html', {
        'form': CustomUserCreationForm
    })

