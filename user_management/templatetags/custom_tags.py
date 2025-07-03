from django import template

register = template.Library()
@register.filter(name='get_currentpage_path')
def get_currentpage_path(value):
    ans = value.split('/')
    return ans[-1]

# your_app/templatetags/query_params.py
from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def url_with_query(context, **kwargs):
    """
    Returns the current URL's query parameters updated with the given kwargs.
    Usage: {% url_with_query sort='newest' %}
    """
    request = context['request']
    query = request.GET.copy()

    for key, value in kwargs.items():
        query[key] = value

    return '?' + urlencode(query)
