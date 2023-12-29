from wagtail import blocks
from wagtail.blocks import (BooleanBlock,RichTextBlock,PageChooserBlock)
from wagtail.images.blocks import ImageChooserBlock



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


# class 