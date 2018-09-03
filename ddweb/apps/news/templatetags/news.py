from django import template
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.filter
def fromtimestamp(unixtime):
    return datetime.datetime.fromtimestamp(unixtime)
