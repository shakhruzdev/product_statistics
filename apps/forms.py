from django import forms
from django.db.models import F

from .models import Client, Order, OrderItem, Product

KZ_PREFIXES = {'701', '702', '707', '708', '747', '775', '776', '777', '778'}


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'phone_number']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')

        if not phone.startswith('+7') or len(phone) != 12:
            raise forms.ValidationError("Номер телефона должен быть в формате +7XXXXXXXXXX")

        digits_only = phone[2:]
        if not digits_only.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры после +7")

        prefix = digits_only[:3]
        if prefix not in KZ_PREFIXES:
            raise forms.ValidationError("Номер должен начинаться с допустимого кода Казахстана (например, 707, 778)")

        if Client.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("Клиент с таким номером телефона уже существует.")

        return phone


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client']

    def clean(self):
        data = self.data
        order = Order.objects.create(client_id=data.get('client_id'))
        products = Product.objects.all()
        for i in data:
            if i.startswith('product_id'):
                prod_id = int(data[i])
                quantity = int(data["quantity_" + i[11:]])
                OrderItem.objects.create(order=order, product_id=prod_id, quantity=quantity)
                products.filter(pk=prod_id).update(quantity=F('quantity') - quantity)

        return data
