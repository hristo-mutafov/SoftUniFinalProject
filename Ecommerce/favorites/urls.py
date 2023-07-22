from django.urls import path

from Ecommerce.favorites.views import add_to_favorites

urlpatterns = (
    path('add/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
)