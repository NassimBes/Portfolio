from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from wagtail.models import Page
from wagtail.fields import  StreamField
from wagtail.admin.panels import (
    FieldPanel,MultiFieldPanel,
    TabbedInterface,ObjectList,
    )

# Create your models here.
from MySnippets.models import RSSFeed


class DesignerPage(Page):
    template = "designerportfolio/index.html"
    designertitle=models.CharField(max_length=25,null=True,blank=True)



    #FOOTER
    emails = User.objects.values_list("email","username")
    email_field= models.CharField(max_length=1000,choices=emails,blank=True)
    phone_field = PhoneNumberField(region="MA",blank=True,help_text="Phone format 0520-686480")
    rss = models.ForeignKey(
        'MySnippets.RSSFeed',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        
    ]

    user_panels = [
        FieldPanel("email_field"),
        FieldPanel("phone_field"),
        FieldPanel("rss"),
    ]


    edit_handler = TabbedInterface([
        ObjectList(content_panels,heading='Page Title'),
        ObjectList(user_panels,heading='RSS FEED'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])