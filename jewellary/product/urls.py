from django.urls import path
from .views import *

urlpatterns = [path('jewellary/', search, name='jewellary'),
               path('products/', product_list, name='product_list'), 
               
               
               ]