from django.contrib import admin

from Ecommerce.orders.models import Order
from Ecommerce.utils.admin_mixins import AdminPermissionMixin


@admin.register(Order)
class OrderAdmin(AdminPermissionMixin, admin.ModelAdmin):
    ordering = ('date',)

    list_display = ('order_number', 'payment_method', 'price')
    list_filter = ('date', 'payment_method', 'delivery_method')
    search_fields = ('order_number', 'address')
