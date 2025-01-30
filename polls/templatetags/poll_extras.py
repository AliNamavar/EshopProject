from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()
@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")

@register.filter
def create_date(value):
    return date2jalali(value)

@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + 'تومان'



@register.simple_tag
def multiply(value, arg):
    total = value * arg
    formatted = '{:,}'.format(total)
    return formatted

@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + 'تومان'
