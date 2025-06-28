from django import template

register = template.Library()
@register.filter(name='get_currentpage_path')
def get_currentpage_path(value):
    ans = value.split('/')
    return ans[-1]