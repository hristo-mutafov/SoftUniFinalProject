from django.urls import path

from Ecommerce.products.views import GetProducts, ProductDetails

urlpatterns = (
    path('', GetProducts.as_view(), name='index'),
    path('product/details/<int:pk>', ProductDetails.as_view(), name='details_products')
)
