from django import template

register = template.Library()


@register.filter
def check_completed(dictionary, key):
    return (dictionary.get(key)).completed
