from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel,FieldRowPanel
from wagtail.fields import RichTextField

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


@register_snippet
class CreatorName(models.Model):
    title = models.CharField(max_length=25)
    first_last_name = models.CharField(max_length=25,blank=True,null=True)
    job_title = RichTextField(features=["bold","italic"],blank=True,null=True)
    panels = [
        FieldPanel("title"),
        FieldRowPanel([
            FieldPanel("first_last_name"),
            FieldPanel("job_title"),
        ])
    ]
    

    def __str__(self) -> str:
        return self.title