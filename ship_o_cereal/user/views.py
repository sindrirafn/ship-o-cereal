from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def item(request):
    return render(request, 'user/edit_profile.html')