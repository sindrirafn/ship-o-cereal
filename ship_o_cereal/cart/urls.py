from django.urls import path
from . import views
from cereal.views import updatecart
urlpatterns = [
    # http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    path('update_cart/', updatecart, name="update-cart")

]