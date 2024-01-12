from django import template
from designerportfolio.models import CreatorName

register = template.Library()

@register.inclusion_tag("designerportfolio/tags/creatorpage.html",takes_context=True)
def creatorname(context):
    return{
        'creatorname': CreatorName.objects.all(),
        'request' : context['request'],
    }