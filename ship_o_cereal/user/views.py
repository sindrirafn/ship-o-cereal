from django.shortcuts import render
from .models import Profile
from .forms import TheProfileForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def item(request):
    return render(request, 'user/edit_profile.html')


def wish(request):
    return render(request, 'user/wishlist.html')


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = TheProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/index.html', {
        'form': TheProfileForm(instanec=profile)
    })
