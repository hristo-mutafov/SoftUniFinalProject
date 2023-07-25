import enum
import uuid

from django.db import models

from Ecommerce.utils.model_mixins import GetEnumValuesMixin, GetEnumMaxLenValueMixin
from Ecommerce.products.models import Product


class PaymentMethodEnum(GetEnumValuesMixin, GetEnumMaxLenValueMixin, enum.Enum):
    cash_on_delivery = 'Cash On Delivery'
    stripe = 'Stripe'


class DeliveryMethodEnum(GetEnumValuesMixin, GetEnumMaxLenValueMixin, enum.Enum):
    dhl_office = 'Delivery To DHL Office'
    dhl_express_office = 'Express Delivery To DHL Office'
    to_address = 'To Address'


class Order(models.Model):
    order_number = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    address = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    payment_method = models.CharField(
        choices=PaymentMethodEnum.get_values(),
        max_length=PaymentMethodEnum.get_longer_value(),
        default=PaymentMethodEnum.cash_on_delivery.value,
        null=False,
        blank=False
    )

    delivery_method = models.CharField(
        choices=DeliveryMethodEnum.get_values(),
        max_length=DeliveryMethodEnum.get_longer_value(),
        default=DeliveryMethodEnum.to_address.value,
        null=False,
        blank=False
    )

    comment = models.TextField(
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    products = models.ManyToManyField(
        Product,
        through='OrderProducts'
    )


class OrderProducts(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    count = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

