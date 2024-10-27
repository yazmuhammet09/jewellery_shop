from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('address', 'number', 'email', 'description', 'work_time', 'social_network')

admin.site.register(About, AboutAdmin)