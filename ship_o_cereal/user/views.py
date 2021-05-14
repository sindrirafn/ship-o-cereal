from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .models import Profile
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


def edit_profile(request):
    if request.method == 'POST':
        form = ImprovedUserChangeForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile-index')
    else:
        form = ImprovedUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'user/edit_profile.html', args)

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


def change_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'New password confirmed')
            return redirect('profile-index')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'user/change_pw.html', args)
