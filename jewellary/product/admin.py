from django.contrib import admin
from .models import product, material, category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount', 'weight', 'color')

admin.site.register(product)

# Register your models here.
