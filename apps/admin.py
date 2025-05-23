from django.contrib import admin

from .models import (
    Client,
    Product,
    Order, OrderItem
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_display_links = ('id', 'full_name', 'phone_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bought_price', 'sold_price', 'quantity')
    list_display_links = ('id', 'name', 'bought_price', 'sold_price', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client',)
    list_display_links = ('client',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')
    list_display_links = ('id', 'product', 'quantity')
