from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel,FieldRowPanel,MultiFieldPanel
from wagtail.fields import RichTextField

from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from django.utils import timezone
from django_countries.fields import CountryField

@register_snippet
class RSSFeed(models.Model):
    title = models.CharField(max_length=25)
    facebook_feed = models.URLField(null=True,blank=True)
    twitter_feed = models.URLField(null=True,blank=True)
    skype_feed = models.URLField(null=True,blank=True)
    github_feed = models.URLField(null=True,blank=True)
    gitea_feed = models.URLField(null=True,blank=True)
    linkedIn_feed = models.URLField(null=True,blank=True)

    panels = [
        MultiFieldPanel([
        FieldPanel("title"),
        FieldPanel("facebook_feed"),
        FieldPanel("twitter_feed"),
        FieldPanel("skype_feed"),
        FieldPanel("github_feed"),
        FieldPanel("gitea_feed"),
        FieldPanel("linkedIn_feed"),
        ],
        heading="Social Media Footer Page Links",)
    ]

    def __str__(self):
        return self.title


@register_snippet
class CreatorName(models.Model):
    DEGREES_CHOICE=(
        ("master", "MASTER"),
        ("license", "LICENSE")
    )

    title = models.CharField(max_length=25)
    #NAME & BIRTHDATE
    profile_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    first_last_name = models.CharField(max_length=25,blank=True,null=True)
    creator_birthday = models.DateField(null=True,blank=True)
    #Contact INFO
    emails = User.objects.values_list("email","username")
    creator_mail = models.CharField(max_length=1000,choices=emails,blank=True)
    phone_field = PhoneNumberField(region="MA",blank=True,verbose_name="Phone Number Format(0520-686480)")
    availability = models.BooleanField(blank=True,null=True)
    study_level = models.CharField(null=True,max_length=10,choices=DEGREES_CHOICE)
    country = CountryField(null=True)
    

    #ABOUT
    job_title = models.CharField(max_length=250,blank=True,null=True)
    about_creator = RichTextField(features=['h2', 'h3', 'bold', 'italic','blockquote'],null=True,blank=True)
    
    @property
    def age(self) -> int:
        if not self.creator_birthday:
            return None
        today = timezone.now().date()
        return today.year - self.creator_birthday.year - (
            (today.month, today.day) < (self.creator_birthday.month, self.creator_birthday.day)
        )
    

    panels = [
        FieldPanel("title"),     
            FieldRowPanel([
                FieldPanel("first_last_name"),
                FieldPanel("creator_birthday"),
            ]),
            FieldRowPanel([
                FieldPanel("profile_picture"),
                FieldPanel("study_level"),
                FieldPanel("availability"),
                FieldPanel("creator_mail"),
            ]),
            
            FieldPanel("about_creator"),
            FieldRowPanel([
                
                FieldPanel("country"),
                FieldPanel("phone_field"),
            ]),
            FieldRowPanel([
                FieldPanel("job_title"),
            ]),


    ]
    
    def __str__(self) -> str:
        return self.title
    

@register_snippet
class ModalShortcuts(models.Model):
    title = models.CharField(max_length=25)
    dspghome = models.CharField(max_length=25,blank=True)
    dspgabout = models.CharField(max_length=25,blank=True)
    dspgresume = models.CharField(max_length=25,blank=True)
    dspgportfolio = models.CharField(max_length=25,blank=True)
    dspgservices = models.CharField(max_length=25,blank=True)
    dspgcontact = models.CharField(max_length=25,blank=True)
    panels = [
        FieldPanel("title"),
        FieldRowPanel([
            FieldPanel("dspghome"),
            FieldPanel("dspgabout"),
            FieldPanel("dspgresume"),
            FieldPanel("dspgportfolio"),
            FieldPanel("dspgservices"),
            FieldPanel("dspgcontact"),
        ]),
    ]
    

    def __str__(self) -> str:
        return self.title