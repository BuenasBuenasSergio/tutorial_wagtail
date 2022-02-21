import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import jovian

#En caso de que pida API KEY de jovian:
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NDkxNzc0MSwianRpIjoiY2QxNjBjNTYtN2MxYy00Mzg5LWE4ZDgtN2I5OGQ5MjZhNzA5IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5Ijp7ImlkIjoxNTc3MjUsInVzZXJuYW1lIjoiYnVlbmFzYnVlbmFzc2VyZ2lvIn0sIm5iZiI6MTY0NDkxNzc0MSwiZXhwIjoxNjQ4ODA1NzQxfQ.iu-pnAmmr3IOEN6UNHtXkZh1Vcs4bke1xrHbhEkQBQU

site_url = 'https://myanimelist.net'

response = requests.get(site_url)
response.status_code
len(response.text)
# paginas = [x for x in range(0,1000,50)]
doc = BeautifulSoup(response.text)
type(doc)

jovian.commit(project="my-anime-list-webscraping")

#top_anime_url = site_url + '/topanime.php'
# top_anime_url = site_url + '/topanime.php?limit={x}'
top_anime = []

for x in range(0,1000,50):
    #capturando la url para los datos
    top_anime_url = site_url + '/topanime.php?limit={}'.format(x)
    response = requests.get(top_anime_url)
    response.status_code

    doc = BeautifulSoup(response.text)

    doc.title

    doc.title.text.strip()

    headers = doc.find('tr', class_ = 'table-header')
    headers.find_all('td') 

    row_content = doc.find_all('tr', {'class' : "ranking-list"})
    len(row_content)


    
    #consiguiendo listado de episodios
    def parse_episodes(listt):
        result = []
        for i in listt[:2]:
            r = i.strip()
            result.append(r)
        return result

    #extrayendo datos leyendo por filas donde se encuentran
    for row in row_content:
        episode = parse_episodes(row.find('div', class_ = "information di-ib mt4").text.strip().split('\n'))
        ranking = {
            'Rank' : row.find('td', class_ = "rank ac").find('span').text,
            'Title': row.find('div', class_="di-ib clearfix").find('a').text,
            'Rating': row.find('td', class_="score ac fs14").find('span').text,
            'Image_URL': row.find('td', class_ ='title al va-t word-break').find('img')['data-src'],
            'Episodes': episode[0],
            'Dates': episode[1]
        }
        top_anime.append(ranking)

    def parse_episodes(listt):
        result = []
        for i in listt[:2]:
            r = i.strip()
            result.append(r)
        return result
    #Guardando datos en un CSV
    def write_csv(items, path):
        # Importante abrir archivo con decodificacion UTF-8 si no da fallo en los simblos de los nombres
        with open(path, 'w', encoding='utf-8') as f:
            # Return if there's nothing to write
            if len(items) == 0:
                return
            
            # Escriiendo el encabezado de la tabla
            headers = list(items[0].keys())
            f.write(','.join(headers) + '\n')
            
            # Guardando los registros
            for item in items:
                values = []
                for header in headers:
                    registros = item.get(header, "")
                    values.append(str(registros))
                f.write(','.join(values) + "\n")

write_csv(top_anime, 'top_anime.csv')