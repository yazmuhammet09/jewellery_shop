from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Retrieve all products
    return render(request, 'product_list.html', {'products': products})

def search(request):
    query = request.GET.get('q')
    if query:
        product = Product.objects.filter(name__icontains=query)
    else:
        product = []
    context = {'data': product}
    return render(request, "template.html", context)