from django.db import models

from wagtail import blocks
from wagtail.blocks import RichTextBlock,BooleanBlock,CharBlock,ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from django.contrib.auth.models import User
from MySnippets.models import CreatorName


class HomeBlock(blocks.StructBlock):
    pass


class AboutBlock(blocks.StructBlock):
    # creator_info = SnippetChooserBlock(CreatorName)
    creator_title = blocks.CharBlock(max_length=25)
    creator_title_description = RichTextBlock()
    creator_motivation = RichTextBlock()
    class Meta:
        template="designerstreams/about.html"
        icon = "wagtail-icon"
        # form_classname = "navblock_block"


class ResumeBlock(blocks.StructBlock):
    pass


class PortfolioBlock(blocks.StructBlock):
    pass


class ServicesBlock(blocks.StructBlock):
    pass


class ContactBlock(blocks.StructBlock):
    pass