from django.db import models


class Category(models.Model):
    NAME_MAX_LEN = 20

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.name} Category'


class Product(models.Model):
    NAME_MAX_LEN = 50
    IMAGE_FIELD_MAX_LEN = 100
    MADE_IN_FIELD_MAX_LEN = 50
    BRAND_MAX_LEN = 30

    image = models.URLField(
        max_length=100,
        null=False,
        blank=False
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    quantity = models.IntegerField(
        null=False,
        blank=False
    )

    brand = models.CharField(
        max_length=BRAND_MAX_LEN,
        null=False,
        blank=False
    )

    made_in = models.CharField(
        max_length=MADE_IN_FIELD_MAX_LEN,
        null=False,
        blank=False
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        null=False,
        blank=False
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    added_on = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.name} Product'
