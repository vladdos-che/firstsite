from django.utils.html import escape

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeText

register = template.Library()


@register.filter(name='cur')
# @stringfilter
def currency(value, name='тнг.'):
    return f'{value:.2f} {name}'


# register.filter('currency', currency)


# @register.filter(needs_autoescape=True)
# def somefilter(value, autoescape=True):
#     if not isinstance(value, SafeText):
#         value = escape(value)
#     if autoescape:
#         value = escape(value)
#     return mark_safe(value)


# @register.filter(expects_localtime=True)
# def datetime_filter(value):
#     pass


@register.simple_tag
# def lst(context, sep, *args):
def lst(sep, *args):
    return f'{sep.join(args)} (итого: {len(args)})'


@register.inclusion_tag('tags/ulist.html')
def ulist(*args):
    return {'items': args}


@register.filter
def tng_to_dollars(value):  # lesson_36_hw
    try:
        int(value)
        return f'{value / 475: .4f} $'
    except ValueError:
        return f'{value} не число'


@register.filter
def dollars_to_tng(value):  # lesson_36_hw
    try:
        int(value)
        return f'{value * 475}'
    except ValueError:
        return f'{value} не число'


@register.simple_tag
def str_to_list(string, sep):
    return list(string.split(sep))


@register.inclusion_tag('tags/content_to_words.html', name='content_to_words')
def content_to_words_red_lower_capfirst(string):
    return {'items': string.split()}
