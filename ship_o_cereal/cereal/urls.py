
from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/cereals
    path('', views.index, name="products-index"),
    # path('<int:id>', views.cereal_by_id, name="cereal-details"),
    path('<str:name>', views.product_by_name, name="product-details"),
    path('update_cart/', views.updatecart, name="checkout"),
]