from django.db.models import Sum


def cart_products_count(request):
    if request.user.is_authenticated:
        user = request.user

        data = user.cart.products.all()

        count = len(data)

        return {'cart_products_count': count}
    return {'cart_products_count': 0}


def overall_products_price(request):
    if request.user.is_authenticated:
        user = request.user

        data = user.cart.products.values(
            'id', 'name', 'price', 'image', 'brand'
        ).annotate(count=Sum('cartproducts__count'))

        price = sum(int(record['price']) * int(record['count']) for record in data)

        return {'overall_products_price': price}
    return {'overall_products_price': 0}
