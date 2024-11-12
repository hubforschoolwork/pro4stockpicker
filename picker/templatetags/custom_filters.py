from django import template


register = template.Library()

@register.filter
def slice_from_dollar(value):
    if '$' in value:
        return value[value.index('$'):]
    return value


