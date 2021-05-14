from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from user.views import change_pw
urlpatterns = [
    # http://localhost:8000/
    path('', views.index, name="frontpage-index"),
    path('register', views.register, name="register-index"),
    path('login', LoginView.as_view(template_name='front_page/login.html'), name='login-index'),
    path('logout', LogoutView.as_view(next_page='login-index'), name='logout-index'),
    path('password/', change_pw)
]