import pandas as pd
import requests 
from bs4 import BeautifulSoup





# df = pd.read_csv('top_anime.csv')
# df["generos"] = "Accion"
# df.to_csv(r"top_anime.csv", index=False)
generos = []
file = pd.read_csv('top_anime.csv')

# for serie in file.URL:
#     site_url = serie
#     response = requests.get(site_url)
#     response.status_code
#     doc = BeautifulSoup(response.text)
#     doc.title
#     doc.title.text.strip()
#     headers = doc.find('td', class_ = 'borderClass')
#     row_content = doc.find_all('span', {'itemprop' : "genre"})
#     # row_content = doc.find_all('tr', {'class' : "ranking-list"})
#     len(row_content)

#     for row in row_content:
#         gen = " ".join((gen,row.text))
#         genero = { 
#                     'Genero' : gen
#         }
#         generos.append(genero)

print(file.Title)
        
# df = pd.read_csv('top_anime.csv')
# df["generos"] = "Accion"
# df.to_csv(r"top_anime.csv", index=False)
