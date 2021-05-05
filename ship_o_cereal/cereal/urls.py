
from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/cereals
    path('', views.index, name="cereal-index"),
]