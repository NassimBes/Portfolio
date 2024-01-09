from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

from django.db import models




@register_snippet
class RSSFeed(models.Model):
    title = models.CharField(max_length=25)
    github_feed = models.URLField(null=True,blank=True)
    lnkIn_feed = models.URLField(null=True,blank=True)


    panels = [
        FieldPanel("title"),
        FieldPanel("github_feed"),
        FieldPanel("lnkIn_feed"),
    ]

    def __str__(self):
        return self.title
