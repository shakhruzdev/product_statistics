from django.views.generic import ListView, CreateView

from apps.models import Client, Product, Order


class ClientCreateListView(CreateView, ListView):
    model = Client
    template_name = 'clients.html'
    fields = '__all__'
    context_object_name = 'clients'



class ProductCreateUpdateListView(CreateView, ListView):
    model = Product
    template_name = 'products.html'


class OrderCreateListView(CreateView, ListView):
    model = Order
    template_name = 'orders.html'
