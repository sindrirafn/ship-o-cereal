from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    #path('update_cart/', views.updatecart, name="checkout")
]