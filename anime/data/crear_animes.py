
from anime.models import Anime
from csv import DictReader
import os


# borrar pelis
for a in Anime.objects.all():
    a.delete()

#lista de películas del json
if os.path.exists("top_anime.csv"):
   file = open("top_anime.csv" , encoding="utf-8")
else:
    file = open("top_anime.csv", encoding="utf-8")

animes = DictReader(file)


for a1 in animes:
    a = Anime()
    a.ranking =  a1['Rank']
    a.title = a1['Title']
    a.rating = a1['Rating']
    a.imagen = a1['Image_URL']
    a.episodes = a1['Episodes']
    a.emmision = a1['Dates']
    a.link = a1['URL']
    a.save()
