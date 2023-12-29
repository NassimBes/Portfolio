
from django.db import models

from wagtail.models import Page
from wagtail.fields import  StreamField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel

from streams import blocks as blk
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    # template = "homepage/home_page.html"
    homeHeader = StreamField([
        ("header_block",blk.header_block()),
        ],use_json_field=True,null=False,blank=True,max_num=1)

    bodyHeader = StreamField([
        ("body_block",blk.body_block()),
        ],use_json_field=True,null=False,blank=True,max_num=1)


    max_count = 1
    content_panels = Page.content_panels + [
        FieldPanel("homeHeader"),
        FieldPanel("bodyHeader"),
    ]



