from django.urls import path

from apps.views import ProductCreateUpdateListView, ClientCreateListView, OrderCreateListView

urlpatterns = [
    path('', ClientCreateListView.as_view(), name='client_list'),
    path('products/', ProductCreateUpdateListView.as_view(), name='product_list'),
    path('orders/', OrderCreateListView.as_view(), name='order_list'),
]
