from django.urls import path

from Ecommerce.favorites.views import add_to_favorites, GetProducts

urlpatterns = (
    path('', GetProducts.as_view(), name='get_favourite_products'),
    path('add/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
)