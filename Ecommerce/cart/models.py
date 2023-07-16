from django.contrib.auth import get_user_model
from django.db import models

from Ecommerce.products.models import Product

UserModel = get_user_model()


class Cart(models.Model):

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    products = models.ManyToManyField(
        Product,
        through='CartProducts'
    )


class CartProducts(models.Model):
    count = models.IntegerField(
        default=1,
        null=False,
        blank=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
