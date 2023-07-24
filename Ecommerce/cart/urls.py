from django.urls import path

from Ecommerce.cart.views import *

urlpatterns = (
    path('', GetCartProducts.as_view(), name='show_cart'),
    path('add/<int:product_id>/', AddProductToCart.as_view(), name='add_to_cart'),
    path('remove/<int:product_id>/', RemoveProductFromCart.as_view(), name='remove_to_cart'),
    path('edit_quantity/<int:product_id>/', edit_product_quantity_in_cart, name='increase_product_count_in_cart'),
)
