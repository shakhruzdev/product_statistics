from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.models import Product, Order
from .forms import ClientForm
from .models import Client


class ClientCreateListView(CreateView, ListView):
    model = Client
    template_name = 'apps/clients.html'
    context_object_name = 'clients'
    success_url = reverse_lazy('client_list')
    form_class = ClientForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = self.object_list
        return context


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')

    def get(self, request, *args, **kwargs):
        return redirect('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'apps/clients.html'
    fields = 'phone_number', 'full_name'
    success_url = reverse_lazy('client_list')


class ProductCreateListView(CreateView, ListView):
    model = Product
    template_name = 'apps/products.html'
    fields = 'name', 'bought_price', 'sold_price', 'quantity'
    context_object_name = 'products'
    success_url = reverse_lazy('product_list')


class OrderCreateListView(CreateView, ListView):
    model = Order
    template_name = 'apps/orders.html'
    fields = '__all__'
