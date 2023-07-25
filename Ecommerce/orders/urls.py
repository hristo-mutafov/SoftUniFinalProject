from django.urls import path

from Ecommerce.orders.views import PaymentProcedure, RetrieveClientSecret, show_successful_order_page

urlpatterns = (
    path('', PaymentProcedure.as_view(), name='show_order'),
    path('retrieve_client_secret/', RetrieveClientSecret.as_view()),
    path('successful_order_page/', show_successful_order_page, name='successful_order_page')
)