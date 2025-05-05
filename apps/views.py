import json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView
from apps.models import Product, Order
from .models import Client


class ClientCreateListView(CreateView, ListView):
    model = Client
    template_name = 'apps/clients.html'
    fields = '__all__'
    context_object_name = 'clients'
    success_url = reverse_lazy('client_list')

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


class ProductCreateUpdateListView(CreateView, ListView):
    model = Product
    template_name = 'apps/products.html'
    fields = '__all__'


class OrderCreateListView(CreateView, ListView):
    model = Order
    template_name = 'apps/orders.html'
    fields = '__all__'
