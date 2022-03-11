from django.db import models

# Create your models here.
from product.models import Product
from vendor.models import Vendor


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.FloatField(default=0.0)
    vendors = models.ManyToManyField(Vendor, related_name='orders')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order for: {self.first_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        Vendor, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_total_price(self):
        return self.price * self.quantity
