
from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/cereals
    path('', views.index, name="cereal-index"),
    path('<int:id>', views.cereal_by_id, name="cereal-details"),
]