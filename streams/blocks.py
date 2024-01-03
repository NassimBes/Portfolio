from wagtail import blocks
from wagtail.blocks import RichTextBlock,BooleanBlock,ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock

from django import forms
from django.contrib.auth.models import User

#HEADERS
class body_block(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    desc = RichTextBlock(features=["bold","italic"])
    images = ImageChooserBlock()
    class Meta:
        template="streams/body.html"
        icon = "cogs"
        form_classname = "body-block"
        

class header_block(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    desc = RichTextBlock(required=True, help_text="Company Description",features=["bold","italic"])
    images = ImageChooserBlock(required=True)
    
    class Meta:
        template="streams/header.html"
        icon = "cogs"
        form_classname = "header_block"


class nav_block(blocks.StructBlock):
    head_nav = blocks.CharBlock(required=True,max_length=25)
    about_nav = blocks.CharBlock(required=True,max_length=25)
    proj_nav = blocks.CharBlock(required=True,max_length=25)
    contact_nav = blocks.CharBlock(required=True,max_length=25)

    class Meta:
        template="streams/navbar.html"
        icon = "wagtail-icon"
        form_classname = "navblock_block"

#BODY

class content_block(blocks.StructBlock):
    content_title=blocks.CharBlock(required=True,max_length=15,help_text="Project name")
    content_bod=blocks.RichTextBlock(required=True,help_text="Project Description",features=["bold","italic"])
    content_image_block = ImageChooserBlock(required=True)
    content_checkbox_block = BooleanBlock(required=False,help_text="To be highligthed")
    class Meta:
        template="streams/contentblock.html"
        icon="wagtail-icon"
        form_classname ="contentblock_block"


# #FOOTER


    

class user_info_block(blocks.StructBlock):
    user_block = blocks.ChoiceBlock(required=False)
    class Meta:
        template="homepage/home_page.html"
        icon="cup"
        form_classname="userinfo_block"