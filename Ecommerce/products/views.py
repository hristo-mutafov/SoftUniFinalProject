from datetime import datetime, timedelta

import django.views.generic as views

from Ecommerce.products.models import Product


class GetProducts(views.ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.values('id', 'name', 'price', 'image')


class ProductDetails(views.DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.now().date()

        date_after_two_days = today + timedelta(days=2)
        date_after_four_days = today + timedelta(days=4)

        context['date_after_two_days'] = date_after_two_days
        context['date_after_four_days'] = date_after_four_days

        return context

