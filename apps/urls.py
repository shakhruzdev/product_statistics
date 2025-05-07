from django.urls import path

from apps.views import (
    ProductCreateUpdateListView,
    ClientCreateListView,
    OrderCreateListView,
    ClientDeleteView,
    ClientUpdateView,
)

urlpatterns = [
    path('', ClientCreateListView.as_view(), name='client_list'),
    path('products/', ProductCreateUpdateListView.as_view(), name='product_list'),
    path('orders/', OrderCreateListView.as_view(), name='order_list'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
]
