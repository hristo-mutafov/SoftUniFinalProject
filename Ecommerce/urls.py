from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ecommerce.accounts.urls')),
    path('', include('Ecommerce.products.urls')),
    path('cart/', include('Ecommerce.cart.urls')),
    path('favorites/', include('Ecommerce.favorites.urls')),
    path('orders/', include('Ecommerce.orders.urls'))
]
