from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/aboutus
    path('', views.index, name="aboutus-index"),
]