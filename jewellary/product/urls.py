from django.urls import path
from .views import search

urlpatterns = [path('jewellary/', search, name='jewellary')]