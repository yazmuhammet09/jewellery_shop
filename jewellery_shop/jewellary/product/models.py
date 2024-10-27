from django.db import models

class About(models.Model):
    address = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.CharField(max_length=255)
    descriptoin = models.CharField(max_length=255)
    work_time = models.IntegerField()
    social_network = models.CharField(max_length=255)


