from django import template

from Ecommerce.favorites.models import Favorites

register = template.Library()


@register.filter
def is_in_favorites(product, user):
    product_id = None
    try:
        product_id = product['id']
    except Exception:
        product_id = product.id

    try:
        favorites = Favorites.objects.get(user=user)
        return any(product_id == x.id for x in favorites.products.all())
    except Favorites.DoesNotExist:
        return False
