from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.core import exceptions
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from Ecommerce.favorites.models import Favorites
from Ecommerce.products.forms import ProductSearchForm
from Ecommerce.products.models import Product


def add_to_favorites(request, product_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            raise exceptions.PermissionDenied
        user = request.user
        product = get_object_or_404(Product, id=product_id)

        Favorites.objects.get_or_create(user=user)

        if product in user.favorites.products.all():
            user.favorites.products.remove(product)
            return JsonResponse({'message': 'removed'}, status=200)
        user.favorites.products.add(product)
        return JsonResponse({'message': 'added'}, status=200)
    else:
        return redirect('index')


class GetProducts(LoginRequiredMixin, views.ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return user.favorites.products.all().values('id', 'name', 'price', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProductSearchForm(self.request.GET)
        return context
