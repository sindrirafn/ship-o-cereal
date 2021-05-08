from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'front_page/index.html')

def register(request):
    return render(request, 'front_page/register.html')

def login(request):
    return render(request, 'front_page/login.html')
