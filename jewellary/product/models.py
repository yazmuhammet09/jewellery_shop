from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Material(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='products', blank=True, null=True)  # Connect to Material
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)  # Connect to Category
    def __str__(self):
        return f"{self.name} {self.price} {self.gender}"


class Order(models.Model):
    products_id = models.ForeignKey(Product, on_delete=models.CASCADE)
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


class About(models.Model):
    address = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.CharField(max_length=255)
    descriptoin = models.CharField(max_length=255)
    work_time = models.IntegerField()
    social_network = models.CharField(max_length=255)