from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model

from wagtail.models import Page
from wagtail.fields import  StreamField,RichTextField
from wagtail.admin.panels import (
    FieldPanel,MultiFieldPanel,
    TabbedInterface,ObjectList,
    )

from streams import blocks as blk
from phonenumber_field.modelfields import PhoneNumberField

# from wagtail.snippets.models import register_snippet


class HomePage(Page):
    template = "home_page.html"

    #FIELDS
    homeHeader = StreamField([
        ("header_block",blk.header_block()),
        ],use_json_field=True,null=False,blank=True,max_num=1,collapsed=True)

    bodyHeader = StreamField([
        ("body_block",blk.body_block()),
        ],use_json_field=True,null=False,blank=True,max_num=1,collapsed=True)

    navHeader = StreamField([
        ("nav_block",blk.nav_block()),
    ],use_json_field=True,null=False,blank=True,max_num=1,collapsed=True)

    contentBlock = StreamField([
        ("content_block",blk.content_block()),
    ],use_json_field=True,null=False,blank=True,collapsed=True)


    emails = User.objects.values_list("email","username")
    email_field= models.CharField(max_length=1000,choices=emails,blank=1)
    phone_field = PhoneNumberField(region="MA",blank=True)

    max_count = 1
    

    #PANELS
    header_panels=[
         MultiFieldPanel(
            [
                FieldPanel("navHeader"),
                FieldPanel("bodyHeader"),
                FieldPanel("homeHeader"),
            ],
            heading="Headers",classname="collapsible  collapsed"
        ),
    ]
    body_panel=[
        FieldPanel("contentBlock")
        ]

    content_panels = Page.content_panels

    user_panels = [
        FieldPanel("email_field"),
        FieldPanel("phone_field"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels,heading='Page Title'),
        ObjectList(header_panels,heading="Header"),
        ObjectList(body_panel,heading="Body"),
        ObjectList(user_panels,heading="Footer"),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])

    class Meta:
        verbose_name="homepage"





