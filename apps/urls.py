from django.urls import path

from apps.views import (
    ProductCreateListView,
    ClientCreateListView,
    OrderCreateListView,
    ClientDeleteView,
    ClientUpdateView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    # Clients
    path('', ClientCreateListView.as_view(), name='client_list'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # Products
    path('products/', ProductCreateListView.as_view(), name='product_list'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Orders
    path('orders/', OrderCreateListView.as_view(), name='order_list'),
]
