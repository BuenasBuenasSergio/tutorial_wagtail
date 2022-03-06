from django.db import models
from wagtail.core.models import Page
from wagtailleafletwidget.edit_handlers import GeoPanel


class ViajePage(Page):
    location = models.CharField(max_length=250, blank=True, null=True)
    
    content_panels = Page.content_panels + [
        GeoPanel('location'),
    ]
