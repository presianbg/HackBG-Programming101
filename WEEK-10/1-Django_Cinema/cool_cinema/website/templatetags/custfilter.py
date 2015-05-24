from django import template

register = template.Library()


@register.simple_tag
def is_taken(taken_seats, row, col):
    row_col = (row, col)
    if row_col in taken_seats:
        return 'red'
    return 'green'


@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg
