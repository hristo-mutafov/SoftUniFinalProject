from django import template

from Ecommerce.favorites.models import Favorites

register = template.Library()


@register.filter
def is_in_favorites(product, user):
    try:
        favorites = Favorites.objects.get(user=user)
        return any(product['id'] == x.id for x in favorites.products.all())
    except Favorites.DoesNotExist:
        return False
