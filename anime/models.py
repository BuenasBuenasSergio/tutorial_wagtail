from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class Anime(models.Model):
    ranking = models.IntegerField("Ranking", blank=True)
    title = models.CharField('título', max_length=250, blank=True)
    rating = models.DecimalField("Puntuacion",max_digits=6, decimal_places=4, blank=True)
    imagen = models.URLField(max_length=250, blank=True)
    link = models.URLField()
    episodes = models.CharField("Episodios", max_length=250, blank=True)
    emmision = models.CharField("Emision", max_length=250 ,blank=True)
    

    panels = [
        FieldPanel('ranking'),
        FieldPanel('title'),
        FieldPanel('rating'),
        FieldPanel('imagen'),
        FieldPanel('link'),
        FieldPanel('episodes'),
        FieldPanel('emmision')

    ]
    def __str__(self):
        return f'({self.title})'
    
    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'


class AnimeIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        qs = ''
        animes = Anime.objects.all()
        context['animes'] =  animes
        context['qs'] = qs
        
        return context
