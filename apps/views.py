from django.views.generic import ListView, CreateView

from apps.models import Client, Product, Order


class ClientCreateListView(CreateView, ListView):
    model = Client
    template_name = 'apps/clients.html'
    fields = '__all__'
    context_object_name = 'clients'



class ProductCreateUpdateListView(CreateView, ListView):
    model = Product
    template_name = 'apps/products.html'
    fields = '__all__'


class OrderCreateListView(CreateView, ListView):
    model = Order
    template_name = 'apps/orders.html'
    fields = '__all__'
