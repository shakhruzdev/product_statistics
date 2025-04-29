from django.views.generic import ListView, CreateView

from apps.models import Client, Product


class ClientCreateListView(CreateView, ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'

class ProductCreateUpdateListView (CreateView, ListView):
    model = Product
    template_name = 'products.html'



