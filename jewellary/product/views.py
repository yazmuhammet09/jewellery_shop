from django.shortcuts import render, get_object_or_404
from .models import Order, Delivery

def order_list(request):
    orders = Order.objects.filter(is_active=True)
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    delivery = Delivery.objects.filter(order=order).first()  # Get delivery info if exists
    return render(request, 'orders/order_detail.html', {'order': order, 'delivery': delivery})
