from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django import views as default_view
from django.urls import reverse
from django.views import generic as views

from Ecommerce.cart.models import Cart, CartProducts
from Ecommerce.products.models import Product


class GetCartProducts(LoginRequiredMixin, views.ListView):
    model = CartProducts
    template_name = 'cart/cart_page.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        queryset = user.cart.products.values(
            'id', 'name', 'price', 'image', 'brand'
        ).annotate(count=Sum('cartproducts__count'))
        return queryset


class AddProductToCart(LoginRequiredMixin, default_view.View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs['product_id']
        user = request.user
        product = get_object_or_404(Product, pk=product_id)

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)

        if product in cart.products.all():
            cart_product = CartProducts.objects.get(cart=cart, product=product)
            cart_product.count += 1
            cart_product.save()
        else:
            CartProducts.objects.create(cart=cart, product=product)

        product.quantity -= 1
        product.save()

        redirect_url = reverse('details_products', args=[product_id])
        return redirect(redirect_url)

    def get(self, *args, **kwargs):
        raise Http404


class RemoveProductFromCart(LoginRequiredMixin, default_view.View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        cart = get_object_or_404(Cart, user=request.user)

        try:
            cart_product = CartProducts.objects.get(cart=cart, product=product)

            cart.products.remove(product)
            product.quantity += cart_product.count

            product.save()

        except CartProducts.DoesNotExist:
            raise Http404

        return redirect('show_cart')

    def get(self, *args, **kwargs):
        raise Http404


def edit_product_quantity_in_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        cart = get_object_or_404(Cart, user=request.user)
        action = request.GET['action']

        try:
            cart_product = CartProducts.objects.get(cart=cart, product=product)

            if action == 'decrease':
                cart_product.count -= 1
                product.quantity += 1

            elif action == 'increase' and product.quantity > 0:
                cart_product.count += 1
                product.quantity -= 1
            else:
                return JsonResponse({'message': 'Run out of stock!'}, status=400)

            product.save()
            cart_product.save()
            return JsonResponse({'price': product.price}, status=200)

        except CartProducts.DoesNotExist:
            raise Http404

    else:
        raise Http404
