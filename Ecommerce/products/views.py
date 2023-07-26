from datetime import datetime, timedelta

import django.views.generic as views

from Ecommerce.products.forms import ProductSearchForm
from Ecommerce.products.models import Product


class GetProducts(views.ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProductSearchForm(self.request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            if search_query:
                queryset = queryset.filter(name__icontains=search_query)

        return queryset.values('id', 'name', 'price', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProductSearchForm(self.request.GET)
        return context


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

