from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def search(request):
    query = request.GET.get('q')
    if query:
        product = Product.objects.filter(name__icontains=query)
    else:
        product = []
    context = {'data': product}
    return render(request, "template.html", context)