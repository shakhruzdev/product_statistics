from django.db.models import (
    Model,
    BigIntegerField,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField, DateTimeField, SlugField, JSONField
)
from django.db.models.fields import PositiveIntegerField
from django.utils.text import slugify


class TimeBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Client(Model):
    full_name = CharField(max_length=255)
    phone_number = CharField(max_length=12, unique=True)
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.full_name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.full_name


class Product(TimeBaseModel):
    name = CharField(max_length=255, unique=True)
    bought_price = BigIntegerField()
    sold_price = BigIntegerField()
    quantity = PositiveIntegerField()
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class Order(TimeBaseModel):
    client = ForeignKey('apps.Client', on_delete=CASCADE)

    @property
    def total_price(self):
        t_price = 0
        for order_item in self.order_items.all():
            t_price += order_item.total_price
        return t_price


class OrderItem(Model):
    product = ForeignKey('apps.Product', on_delete=CASCADE)
    order = ForeignKey('apps.Order', on_delete=CASCADE, related_name='order_items')
    quantity = PositiveIntegerField()
    product_price = BigIntegerField(editable=False, auto_created=True)

    class Meta:
        unique_together = (('product', 'order'),)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_price = self.product.sold_price
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        sold_price = self.product_price * self.quantity
        return sold_price
