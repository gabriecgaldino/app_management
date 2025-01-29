from django import template

register = template.Library()

@register.filter
def status_badge_class(value):
    if value == 'Aprovado':
        return 'bg-success'
    elif value == 'Negado':
        return 'bg-danger'
    elif value == 'Em análise':
        return 'bg-warning'