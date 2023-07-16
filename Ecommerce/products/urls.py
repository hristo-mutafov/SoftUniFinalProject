from django.urls import path

from Ecommerce.products.views import GetProducts, ProductDetails

urlpatterns = (
    path('', GetProducts.as_view(), name='GetProducts'),
    path('product/details/<int:pk>', ProductDetails.as_view(), name='ProductDetails')
)
