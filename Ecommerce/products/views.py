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

