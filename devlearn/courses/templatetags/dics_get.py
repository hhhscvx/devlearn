from django import template

register = template.Library()


@register.filter
def check_completed(dictionary, key):
    if dictionary.get(key):
        return (dictionary.get(key)).completed
