from django import template

register = template.Library()

@register.filter
def sum_visible(concerts):
    return sum(concert.visible for concert in concerts)