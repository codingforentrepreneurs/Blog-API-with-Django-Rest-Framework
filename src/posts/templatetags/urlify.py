try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass


from django import template

register = template.Library()

@register.filter
def urlify(value):
    return quote_plus(value)
