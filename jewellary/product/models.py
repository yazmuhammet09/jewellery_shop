from django.db import models

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.price} {self.gender}"

class material(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"