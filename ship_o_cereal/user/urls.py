from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.profile, name="profile-index"),
    path('edit', views.edit_profile, name="user-edit"),
    path('wishlist', views.wish, name="user-wishlist"),
    path('change_pic', views.change_pic, name="user-pic"),
    path('change_pw', views.change_pw, name="change-pw"),
    path('add_hist', views.update_search_history, name="add-hist"),
    path('get_hist', views.get_search_history, name="get-hist"),


]

