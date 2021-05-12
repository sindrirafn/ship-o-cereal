from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.profile, name="profile-index"),
    path('edit', views.item, name="user-edit"),
    path('wishlist', views.wish, name="user-wishlist"),

]

