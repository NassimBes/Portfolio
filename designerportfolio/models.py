from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from wagtail.models import Page
from wagtail.fields import  StreamField
from wagtail.admin.panels import (
    FieldPanel,MultiFieldPanel,
    TabbedInterface,ObjectList,FieldRowPanel
    )

# Create your models here.
from .designerstreams import blocks as blk
from MySnippets.models import RSSFeed,CreatorName,ModalShortcuts


class DesignerPage(Page):
    template = "designerportfolio/index.html"
    designertitle=models.CharField(max_length=25,null=True,blank=True)


    #NAV
    # dspghome = models.CharField(max_length=25,blank=True)
    # dspgabout = models.CharField(max_length=25,blank=True)
    # dspgresume = models.CharField(max_length=25,blank=True)
    # dspgportfolio = models.CharField(max_length=25,blank=True)
    # dspgservices = models.CharField(max_length=25,blank=True)
    # dspgcontact = models.CharField(max_length=25,blank=True)

    modalshortcuts= models.ForeignKey(
        'MySnippets.ModalShortcuts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )



    #DSContent
    creatorname = models.ForeignKey(
        'MySnippets.CreatorName',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )


    dscontent_block = StreamField([
        ("dspgaboutblock",blk.AboutBlock()),
        ("dspgresumeblock",blk.ResumeBlock()),
        ("dspgportoflioblock",blk.PortfolioBlock()),
        ("dspgservicesblock",blk.ServicesBlock()),
        ("dspgcontactblock",blk.ContactBlock()),
    ],blank=True,null=True,use_json_field=True,collapsed=True)






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




    #PANELS
    content_panels = Page.content_panels + [
        FieldRowPanel([
            FieldPanel("modalshortcuts"),
            # FieldPanel("dspgabout"),
            # FieldPanel("dspgresume"),
            # FieldPanel("dspgportfolio"),
            # FieldPanel("dspgservices"),
            # FieldPanel("dspgcontact"),
        ]
        ,heading="Headers",classname="collapsible  collapsed"),
    ]


    dscontent_panels = [
        FieldRowPanel([
            FieldPanel("creatorname"),
        ]),
        MultiFieldPanel([
            FieldPanel("dscontent_block"),
        ],heading="Content"),
        
    ]


    user_panels = [
        FieldPanel("email_field"),
        FieldPanel("phone_field"),
        FieldPanel("rss"),
    ]


    edit_handler = TabbedInterface([
        ObjectList(content_panels,heading='Page Title'),
        # ObjectList(dspgnav_panels,heading='NavBar Content'),
        ObjectList(dscontent_panels,heading='Homepage Content'),
        ObjectList(user_panels,heading='RSS FEED'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])