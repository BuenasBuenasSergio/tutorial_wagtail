import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import jovian


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

    def write_csv(items, path):
        # Open the file in write mode
        with open(path, 'w', encoding='utf-8') as f:
            # Return if there's nothing to write
            if len(items) == 0:
                return
            
            # Write the headers in the first line
            headers = list(items[0].keys())
            f.write(','.join(headers) + '\n')
            
            # Write one item per line
            for item in items:
                values = []
                for header in headers:
                    registros = item.get(header, "")
                    values.append(str(registros))
                f.write(','.join(values) + "\n")

write_csv(top_anime, 'top_anime.csv')