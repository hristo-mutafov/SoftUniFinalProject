from django.urls import path

from Ecommerce.orders.views import PaymentProcedure, RetrieveClientSecret, show_successful_order_page, \
    ListShortPopulatedOrders, OrderDetail

urlpatterns = (
    path('', PaymentProcedure.as_view(), name='show_order'),
    path('retrieve_client_secret/', RetrieveClientSecret.as_view()),
    path('successful_order_page/', show_successful_order_page, name='successful_order_page'),
    path('list_orders/', ListShortPopulatedOrders.as_view(), name='list_orders'),
    path('order_detail/', OrderDetail.as_view(), name='order_detail'),
)