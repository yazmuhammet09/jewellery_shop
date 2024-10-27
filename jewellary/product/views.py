from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import product
from django.db.models import Q

def testing(request):
    mydata = product.objects.filter(Q(name='') | Q(price='')).values()
    template = loader.get_template('template.http')
    context = {
        'product': mydata,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
