from django.db.models.signals import post_save
from django.dispatch import receiver

from Ecommerce.accounts.models import AppUser, UserProfile
from Ecommerce.cart.models import Cart
from Ecommerce.favorites.models import Favorites


@receiver(post_save, sender=AppUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Favorites.objects.create(user=instance)
        Cart.objects.create(user=instance)
