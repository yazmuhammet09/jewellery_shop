from django import template

register = template.Library()

def filter(value):
    return value.upper()