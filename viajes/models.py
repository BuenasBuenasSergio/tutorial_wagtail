from django.db import models
from wagtail.core.models import Page, Orderable
# from wagtailleafletwidget.edit_handlers import GeoPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]


class ViajePage(Page):
    # location = models.CharField(max_length=250, blank=True, null=True)
    latitud = models.CharField("latitud", max_length=250, null=True)
    longitud = models.CharField("longitud", max_length=250, null=True)
    descripcion = models.TextField("descripcion", null=True)
    content_panels = Page.content_panels + [
        # GeoPanel('location'),
        FieldPanel('latitud'),
        FieldPanel('longitud'),
        FieldPanel('descripcion'),
        InlinePanel('gallery_images', 
            label="Galería de imágenes"),
    ]

class NoticiasPageGalleryImage(Orderable):
    page = ParentalKey(ViajePage, 
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