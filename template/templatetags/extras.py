from django import template

register = template.Library()

@register.filter(name='inc')
def inc(value, by):
    try:
        res = int(value) + int(by)
    except (ValueError, TypeError):
        return ''
    else:
        return str(res)

@register.simple_tag(name='division')
def division(dividend, divisor, to_int=False):
    try:
        if to_int:
            res = int(float(dividend) // float(divisor))
        else:
            res = float(dividend) / float(divisor)
    except (ValueError, TypeError):
        return ''
    else:
        return str(res)
