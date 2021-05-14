from django.db import models
from user.models import Profile
from cereal.models import Product
from checkout.models import ContactInfo
# Create your models here.

# model that keeps all carts users make
# both active (complete = False) and old (complete = True)
class Cart(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transactionId = models.CharField(max_length=255, null=True)
    contactinfo = models.ForeignKey(ContactInfo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    #calculates the total price of cart
    @property
    def get_cart_total(self):
        orderItems = self.cartitem_set.all()
        total = sum([item.get_total for item in orderItems])
        return total

# Model that keeps indivitial item in cart
# links with cart via ForeignKey relationship
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    count = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # gets total for indivitual product (product*number of items)
    @property
    def get_total(self):
        total = self.product.price * self.count
        return total


