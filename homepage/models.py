from django.db import models

from wagtail.models import Page
from wagtail.fields import  StreamField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel,FieldRowPanel

from streams import blocks as blk
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    template = "home_page.html"
    homeHeader = StreamField([
        ("header_block",blk.header_block()),
        ],use_json_field=True,null=False,blank=True,max_num=1)

    bodyHeader = StreamField([
        ("body_block",blk.body_block()),
        ],use_json_field=True,null=False,blank=True,max_num=1)

    navHeader = StreamField([
        ("nav_block",blk.nav_block()),
    ],use_json_field=True,null=False,blank=True,max_num=1)

    contentBlock = StreamField([
        ("content_block",blk.content_block()),
    ],use_json_field=True,null=False,blank=True)

    max_count = 1
    content_panels = Page.content_panels + [
        MultiFieldPanel((
            FieldPanel("navHeader"),
            FieldPanel("bodyHeader"),
            FieldPanel("homeHeader"),
        ),heading="Headers",classname="collapsed"),
        MultiFieldPanel((
            FieldPanel("contentBlock"),
        ),heading="Content",classname="collapsed"),
    ] 

    class Meta:
        verbose_name="homepage"

