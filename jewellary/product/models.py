from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Order(models.Model):
    products_id = models.ForeignKey(Product, on_delete=model.CASCADE)
    is_active = models.BooleanField(default=False)
    order_date=models.DateField(default=timezone.now())
    def __str__(self):
        return f"Order {self.products_id} by {self.user.username}"


class Delivery(models.Model):
    user_name = models.OneToOneField('Order', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    delivery_date=models.DateField(null=True,blank=True)
    phone_number = models.CharField(
        max_length=12,
    )

    def __str__(self):
        return f"Delivery for Order {self.order.id}"

    def set_delivered(self):
        self.status = 'delivered'
        self.delivery_date = timezone.now().date()
        self.save()
