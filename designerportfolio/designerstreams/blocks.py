from django.db import models

from wagtail import blocks
from wagtail.blocks import RichTextBlock,BooleanBlock,CharBlock
from wagtail.images.blocks import ImageChooserBlock

from django.contrib.auth.models import User
from MySnippets.models import CreatorName


class HomeBlock(blocks.StructBlock):
    pass


class AboutBlock(blocks.StructBlock):
    pass


class ResumeBlock(blocks.StructBlock):
    pass


class PortfolioBlock(blocks.StructBlock):
    pass


class ServicesBlock(blocks.StructBlock):
    pass


class ContactBlock(blocks.StructBlock):
    pass