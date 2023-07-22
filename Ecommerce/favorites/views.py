from django.core import exceptions
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from Ecommerce.favorites.models import Favorites
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



