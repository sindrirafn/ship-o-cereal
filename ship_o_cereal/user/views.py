import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .models import Profile, SearchHistory, SearchedItem
from django.contrib import messages
from .forms import (
    TheProfileForm,
    ImprovedUserChangeForm,
    ChangePicForm)




def index(request):
    return render(request, 'user/index.html')


def item(request):
    return render(request, 'user/edit_profile.html')


def wish(request):
    return render(request, 'user/wishlist.html')


@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = TheProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile-index')
    return render(request, 'user/index.html', {
        'form': TheProfileForm(instance=profile)
    })

# View to edit user profile.
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ImprovedUserChangeForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile-index')
    else:
        form = ImprovedUserChangeForm(instance=request.user)
    return render(request, 'user/edit_profile.html', {'form': form})

# View to change the profile picture for the user
@login_required
def change_pic(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ChangePicForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile picture updated, nice one!')
            return redirect('user-pic')
    return render(request, 'user/change_pic.html', {
        'form': ChangePicForm(instance=profile)
    })


# View to change the password for the user, the user does not log out if the password change is successful
@login_required
def change_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'New password confirmed')
            return redirect('profile-index')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user/change_pw.html', {'form': form})



# inserts search string into users search history (except for empty strings)
def update_search_history(request):
    data = json.loads(request.body)
    search_string = data['search_string']
    if request.user.is_authenticated and search_string != "":
        searchhistory, create = SearchHistory.objects.get_or_create(user=request.user)
        searcheditem = SearchedItem.objects.create(searchHistory=searchhistory, searchItem=search_string)
        searcheditem.searchItem = search_string
        searchhistory.save()
        searcheditem.save()
        return JsonResponse('Item was added', safe=False)
    else:
        return JsonResponse({'data': ""})

# returns users search history (5 most recent searches)
def get_search_history(request):
    if request.user.is_authenticated:
        searchhistory, created = SearchHistory.objects.get_or_create(user=request.user)
        items = searchhistory.searcheditem_set.values('searchItem')
        data = list(items)
        data.reverse()
        return JsonResponse({'data': data[:5]})
    else:
        items = []
        return JsonResponse({'data': items})