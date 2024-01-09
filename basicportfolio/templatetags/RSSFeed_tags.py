from django import template
from basicportfolio.models import RSSFeed

register = template.Library()

@register.inclusion_tag("basicportfolio/RSS.html",takes_context=True)
def rss(context):
    return{
        'rss': RSSFeed.objects.all(),
        'request' : context['request'],
    }