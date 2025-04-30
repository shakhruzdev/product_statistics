from django.urls import path

from apps.views import ProductCreateUpdateListView

urlpatterns = [
    path('', ProductCreateUpdateListView.as_view(), name='product_list'),
]
