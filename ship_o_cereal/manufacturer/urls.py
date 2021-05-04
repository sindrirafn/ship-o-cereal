from django.urls import path
from . import views
urlpatterns = [
    # hhtp://localhost:8000/manufacturers
    path('', views.index, name="index"),
]