import markdown

from django import template
from django.template.defaultfilters import stringfilters

register = template.Library()

@register.filter
def covert_markdown(value):
    return markdown.markdown(value)

