from django.urls import path
from . import views
urlpatterns = [
    # hhtp://localhost:8000/users
    path('', views.index, name="user-index"),
]