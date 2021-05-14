from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/payment
    path('creditcard', views.creditcard, name="checkout-creditcard"),
    path('contact', views.contact, name="checkout-contact"),
    path('confirmation', views.confirmation, name="confirmation-index"),
    path('complete_checkout', views.completeCheckout, name="complete-checkout")
]