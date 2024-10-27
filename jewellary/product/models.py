from django.db import models
from django.utils import timezone

class Order(models.Model):
    products_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming there's a user
    is_active = models.BooleanField(default=False)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Order {self.products_id} by {self.user.username}"


class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  # Changed to 'order'
    address = models.CharField(max_length=255)
    email = models.EmailField()
    delivery_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"Delivery for Order {self.order.id}"

    def set_delivered(self):
        self.delivery_date = timezone.now().date()
        self.save()
