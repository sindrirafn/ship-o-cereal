
from django.urls import path
from . import views
urlpatterns = [
    # hhtp://localhost:8000/cereal
    path('', views.index, name="index"),
]