from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='vendor')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_balance(self):
        items = self.items.filter(
            vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(
            vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
