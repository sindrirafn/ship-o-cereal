from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/merch
    path('', views.index, name="merch-index"),
    path('<int:id>', views.merch_by_id, name="merch-details"),
]