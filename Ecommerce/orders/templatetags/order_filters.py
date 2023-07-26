from django import template

register = template.Library()

methods = {
    'cash_on_delivery': 'Cash On Delivery',
    'stripe': 'Stripe Payment',
    'dhl_office': 'Delivery To DHL Office',
    'dhl_express_office': 'Express Delivery To DHL Office',
    'to_address': 'To Address'
}


@register.filter
def get_full_price(uuid):
    return str(uuid).split('-')[0]


@register.filter
def display_methods(method):
    return methods[method]
