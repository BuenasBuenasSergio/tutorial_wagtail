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
    rating = models.DecimalField("Puntuacion",max_digits=6, decimal_places=2, blank=True)
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
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'


class AnimeIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, animes, *args):
            page = request.GET.get('page')
            
            paginator = Paginator(animes, 16)
            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)
            return pages

    def get_context(self, request):

        context = super().get_context(request)
        qs = ''
        animes = Anime.objects.all().order_by('-rating')[:400]

        context['animes'] = self.paginate(request, animes)
        context['qs'] = qs
        
        return context