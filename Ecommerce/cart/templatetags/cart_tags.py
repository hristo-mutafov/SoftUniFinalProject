from datetime import datetime, timedelta

from django import template

register = template.Library()


@register.simple_tag
def get_whole_price(price, quantity):
    return price * quantity


@register.simple_tag
def get_date_two_days_forward():
    today = datetime.now()
    two_days_forward = today + timedelta(days=4)
    return two_days_forward.strftime("%Y-%m-%d")
