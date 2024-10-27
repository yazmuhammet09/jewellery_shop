from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def search(request):
    filter_ = Product.objects.filter(field_name='name')
    query = request.GET.get('q')
    if query : 
        product = Product.objects.filter(field_name_icontains=query)
    else:
        product=[]
    context = {'data':product}
    return(request, "template.html", context)