from operator import mod
from pyexpat import features
from django.db import models


from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel

# Create your models here.


class HomePage(Page):
    banner_title = models.CharField(max_length=100,blank=False,null=True)
    banner_subtitle = RichTextField()
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    
    max_count = 1
    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('banner_image'),
        PageChooserPanel('banner_cta'),
    ]