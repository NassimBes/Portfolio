from django import template
from designerportfolio.models import ModalShortcuts

register = template.Library()

@register.inclusion_tag("designerportfolio/tags/modalshortcutspage.html",takes_context=True)
def modalshortcuts(context):
    return{
        'modalshortcuts': ModalShortcuts.objects.all(),
        'request' : context['request'],
    }