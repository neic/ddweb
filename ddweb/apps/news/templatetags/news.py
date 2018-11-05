from django import template
import datetime

register = template.Library()


@register.filter
def fromtimestamp(unixtime):
    return datetime.datetime.fromtimestamp(unixtime)
