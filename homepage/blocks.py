from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock



class BodyBlock(StructBlock):
    desc = RichTextBlock(features=["bold","italic"])
    images = ImageChooserBlock()
    checkbox = BooleanBlock(
        required=False,
        help_text="To be highlighted"
    )
    class Meta:
        icon = "cogs"
        form_classname = "test-block"


