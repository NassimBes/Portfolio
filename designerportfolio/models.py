from django import forms
from django.db import models
from django.contrib.auth.models import User


from phonenumber_field.modelfields import PhoneNumberField

from wagtail.models import Page
from wagtail.fields import  StreamField
from wagtail.admin.panels import (
    FieldPanel,MultiFieldPanel,
    TabbedInterface,ObjectList,FieldRowPanel,InlinePanel
    )

# Create your models here.
from .designerstreams import blocks as blk
from MySnippets.models import RSSFeed,CreatorName,ModalShortcuts


class DesignerPage(Page):
    template = "designerportfolio/index.html"
    #Page Name & Promote
    designertitle=models.CharField(max_length=25,null=True,blank=True)

    #PANELS (SideBar)
    modalshortcuts= models.ForeignKey(
        'MySnippets.ModalShortcuts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    content_panels = Page.content_panels + [
        FieldRowPanel([
            FieldPanel("modalshortcuts"),
        ]
        ,heading="Headers",classname="collapsible  collapsed"),
    ]

    #BODY (RESUME/PORTFOLIO/SERVICES/TESTIMONIALS)
    dscontent_block = StreamField([
        ("dspgaboutblock",blk.AboutBlock()),
        ("dspgresumeblock",blk.ResumeBlock()),
        ("dspgportoflioblock",blk.PortfolioBlock()),
        ("dspgservicesblock",blk.ServicesBlock()),
        ("dspgcontactblock",blk.ContactBlock()),
    ],blank=True,null=True,use_json_field=True,collapsed=True)

    dscontent_panels = [
        MultiFieldPanel([
            FieldPanel("dscontent_block"),
        ],heading="Content"),
        
    ]


    #FOOTER (CreatorName Info/Contact & RssFEED)
    creatorname = models.ForeignKey(
        'MySnippets.CreatorName',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    rss = models.ForeignKey(
        'MySnippets.RSSFeed',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    user_panels = [
        FieldRowPanel([
            FieldPanel("creatorname"),
            FieldPanel("rss"),
        ],heading="Creator Info",classname="collapsible  collapsed"),
    ]


    #BackEnd (Editor/Visualisor)
    edit_handler = TabbedInterface([
        ObjectList(content_panels,heading='Page Title'),
        # ObjectList(dspgnav_panels,heading='NavBar Content'),
        ObjectList(dscontent_panels,heading='Homepage Content'),
        ObjectList(user_panels,heading='RSS FEED'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])