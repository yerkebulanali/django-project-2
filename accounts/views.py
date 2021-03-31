from django.shortcuts import render
from .models import *

def home(request):
    orders = Orders.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers': customers,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.orders_set.all()
    total_orders = orders.count()
    context = {'customer': customer, 'total_orders': total_orders,
               'orders': orders}
    return render(request, 'accounts/customer.html', context)
