from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/
    path('', views.index, name="frontpage-index"),
    path('register', views.register, name="register-index"),
    path('login', views.login, name="login-index"),
]