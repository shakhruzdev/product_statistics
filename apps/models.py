from django.db.models import (
    Model,
    BigIntegerField,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField, DateTimeField
)


class TimeBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Client(Model):
    full_name = CharField(max_length=255)
    phone_number = CharField(max_length=12, unique=True)

    def __str__(self):
        return self.full_name


class Product(TimeBaseModel):
    name = CharField(max_length=255)
    bought_price = BigIntegerField()
    sold_price = BigIntegerField()
    quantity = IntegerField()

    def __str__(self):
        return self.name


class Order(TimeBaseModel):
    client = ForeignKey('apps.Client', on_delete=CASCADE)
    product = ForeignKey('apps.Product', on_delete=CASCADE)
    quantity = IntegerField()

    def __str__(self):
        return self.product.name
