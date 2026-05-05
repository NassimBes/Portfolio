from django import forms
from django.db import models
from django.contrib.auth.models import User


from phonenumber_field.modelfields import PhoneNumberField

from wagtail.models import Page
from wagtail.fields import  StreamField,RichTextField
from wagtail.admin.panels import (
    FieldPanel,MultiFieldPanel,
    TabbedInterface,ObjectList,FieldRowPanel,InlinePanel
    )

# Create your models here.
from .designerstreams import blocks as blk
from wagtail import blocks
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

    creatorname = models.ForeignKey(
        'MySnippets.CreatorName',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    rssfeed = models.ForeignKey(
        'MySnippets.RSSFeed',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    # SNIPPETS
    used_snippet = Page.content_panels + [
            FieldPanel("modalshortcuts"),
            FieldPanel("rssfeed"),
            FieldPanel("creatorname"),
    ]

    #BODY Content

    #ABOUT
    creator_title = models.CharField(max_length=25,blank=True)
    creator_description = RichTextField(max_length=250,blank=True)
    creator_motivation = RichTextField(max_length=250,blank=True)


    about_panels = Page.content_panels + [
        FieldPanel('creator_title'),
        FieldPanel('creator_description'),
        FieldPanel('creator_motivation')
    ]

    # RESUME

    summary = RichTextField(null=True,blank=True)
    resume_education_section = StreamField([
        ("education",blk.ResumeEducationBlock()),
        ("experience", blk.ResumeExperienceBlock()),
    ],use_json_field=True,null=False,blank=True,collapsed=True)


    resume_panels = Page.content_panels + [
        MultiFieldPanel([
            # FieldRowPanel([
                # FieldPanel('resume_education_section'),
                # FieldPanel("summary"),
            # ]),
            
            FieldPanel('resume_education_section'),
            
        ],heading="Resume"),
    ]


    # SKILLS
    skill_section = StreamField([
        ("skills_block",blk.SkillBlock()),
    ],use_json_field=True,null=False,blank=True,collapsed=True)


    skills_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('skill_section'),
        ])
    ]

    #BackEnd (Editor/Visualisor)
    edit_handler = TabbedInterface([
        # ObjectList(dspgnav_panels,heading='NavBar Content'),
        ObjectList(about_panels,heading='About'),
        ObjectList(resume_panels,heading='Resume'),
        ObjectList(skills_panels,heading='Skills'),
        # ObjectList(dscontent_panels,heading='Portfolio'),
        # ObjectList(dscontent_panels,heading='Contact'),
        ObjectList(used_snippet,heading='Used Snippets'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])