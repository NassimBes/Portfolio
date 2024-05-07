from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel,FieldRowPanel,MultiFieldPanel
from wagtail.fields import RichTextField

from django.db import models




@register_snippet
class RSSFeed(models.Model):
    title = models.CharField(max_length=25)
    facebook_feed = models.URLField(null=True,blank=True)
    twitter_feed = models.URLField(null=True,blank=True)
    skype_feed = models.URLField(null=True,blank=True)
    github_feed = models.URLField(null=True,blank=True)
    lnkIn_feed = models.URLField(null=True,blank=True)


    panels = [
        MultiFieldPanel([
        FieldPanel("title"),
        FieldPanel("facebook_feed"),
        FieldPanel("twitter_feed"),
        FieldPanel("skype_feed"),
        FieldPanel("github_feed"),
        FieldPanel("lnkIn_feed"),
        ],
        heading="Social Media Footer Page Links",)
    ]

    def __str__(self):
        return self.title


@register_snippet
class CreatorName(models.Model):
    title = models.CharField(max_length=25)
    first_last_name = models.CharField(max_length=25,blank=True,null=True)
    job_title = models.CharField(max_length=250,blank=True,null=True)
    panels = [
        FieldPanel("title"),
        FieldRowPanel([
            FieldPanel("first_last_name"),
        ]),
        FieldPanel("job_title"),
    ]
    

    def __str__(self) -> str:
        return self.title
    

@register_snippet
class ModalShortcuts(models.Model):
    title = models.CharField(max_length=25)
    dspghome = models.CharField(max_length=25,blank=True)
    dspgabout = models.CharField(max_length=25,blank=True)
    dspgresume = models.CharField(max_length=25,blank=True)
    dspgportfolio = models.CharField(max_length=25,blank=True)
    dspgservices = models.CharField(max_length=25,blank=True)
    dspgcontact = models.CharField(max_length=25,blank=True)
    panels = [
        FieldPanel("title"),
        FieldRowPanel([
            FieldPanel("dspghome"),
            FieldPanel("dspgabout"),
            FieldPanel("dspgresume"),
            FieldPanel("dspgportfolio"),
            FieldPanel("dspgservices"),
            FieldPanel("dspgcontact"),
        ]),
    ]
    

    def __str__(self) -> str:
        return self.title