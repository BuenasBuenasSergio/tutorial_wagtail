from django.db import models
from django import forms

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


  
class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')[:5]
        context['blogpages'] = blogpages
        
        return context
    
    parent_page_types = ['home.HomePage']
    subpage_types = ['noticias.NoticiasPage']
    
class NoticiasPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introducción", max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            ],
            heading='Información'
        ),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]

    parent_page_types = ['noticias.NoticiasIndexPage']
    subpage_types = []

class NoticiasPageGalleryImage(Orderable):
    page = ParentalKey(NoticiasPage, 
        on_delete=models.CASCADE, 
        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
