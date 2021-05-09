from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/payment
    path('', views.index, name="checkout-index"),
    path('contactInfo', views.contact, name="checkout-contact"),
]