from django import template

register = template.Library()


@register.filter
def check_completed(dictionary, key):
    if dictionary.get(key):
        return dictionary.get(key)


@register.filter
def return_user_lesson_relation_by_lesson_id(dictionary, key):
    if dictionary.get(key):
        return dictionary.get(key)
