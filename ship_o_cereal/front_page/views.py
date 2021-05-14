from .forms import ImprovedUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cereal.models import Product
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'front_page/index.html')

# Post view for registration to the site
def register(request):
    if request.method == 'POST':
        form = ImprovedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created, please log in.')
            return redirect('login-index')
    else:
        form = ImprovedUserCreationForm()
    return render(request, 'front_page/register.html', {'form': form})


