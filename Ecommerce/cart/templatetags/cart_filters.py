from django import template

register = template.Library()


@register.filter
def get_full_price(price):
    full_price = str(price).split('.')[0]
    return full_price


@register.filter
def get_cents(price):
    cents = str(price).split('.')[1]
    return cents
