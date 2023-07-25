import os

import stripe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django import views as default_view

from Ecommerce.orders.models import Order
from Ecommerce.settings import STRIPE_SECRET_KEY

from Ecommerce.cart.models import Cart
from Ecommerce.orders.forms import OrderProfileInformationForm, OrderCommentForm, OrderDeliveryMethodForm, \
    OrderPaymentMethodForm


class PaymentProcedure(LoginRequiredMixin, default_view.View):
    template_name = 'order/order.html'

    def get(self, *args, **kwargs):

        context = {
            'publishable_key': os.getenv('STRIPE_PUBLISHABLE_KEY'),
            'profile_information_form': OrderProfileInformationForm(),
            'comment_form': OrderCommentForm(),
            'order_method_form': OrderDeliveryMethodForm(),
            'order_payment_form': OrderPaymentMethodForm()
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        instance = Order.objects.create(
            address=f'{self.request.POST["city"]}, {self.request.POST["address"]}',
            payment_method=self.request.POST['payment_method'],
            delivery_method=self.request.POST['delivery_method'],
            comment=self.request.POST['comment'],
        )

        user_id = self.request.user.id
        cart = Cart.objects.prefetch_related('products').filter(user=user_id).get()
        products = Cart.objects.prefetch_related('products').filter(user=user_id).get().cartproducts_set.all()


        total_price = 0

        for item in products:
            instance.products.add(item.product, through_defaults={'count': item.count})
            total_price += int(item.count) * float(item.product.price)
            cart.products.remove(item.product)
            item.product.quantity -= item.count
            item.product.save()

        instance.price = total_price
        instance.save()

        return redirect('successful_order_page')


class RetrieveClientSecret(default_view.View):
    def post(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return Http404

        user_id = self.request.user.id
        products = Cart.objects.prefetch_related('products').filter(user=user_id).get().cartproducts_set.all()
        amount = sum(int(item.count) * float(item.product.price) for item in products)
        stripe.api_key = STRIPE_SECRET_KEY
        payment = stripe.PaymentIntent.create(
            amount=int(amount * 10),
            currency='bgn',
            payment_method_types=('card',),
        )
        client_secret = payment.client_secret
        return JsonResponse({'client_secret': client_secret}, status=200)

    def get(self, *args, **kwargs):
        return Http404


def show_successful_order_page(request):
    return render(request, 'order/finishedOrderPage.html')



