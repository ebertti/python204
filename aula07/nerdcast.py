import requests
from bs4 import BeautifulSoup


response = requests.get('https://jovemnerd.com.br/nerdcast/')
texto = response.text

soup = BeautifulSoup(texto, 'html.parser')
print('bs4',  soup.title.text)

epsodios = []

"""
<article class="item -medium -column">
    <a class="image" href="https://jovemnerd.com.br/nerdcast/o-melhor-de-750-nerdcasts/">
    <img src="https://uploads.jovemnerd.com.br/wp-content/uploads/2020/11/NC_750_melhor-de-50-NC-v4-760x428.png" alt="O Melhor de 750 Nerdcasts">
    </a>
    <div class="info">
        <a class="cat-item product-nerdcast" href="https://jovemnerd.com.br/nerdcast/o-melhor-de-750-nerdcasts/">NerdCast 750</a>
    <h2 class="title">
        <a href="https://jovemnerd.com.br/nerdcast/o-melhor-de-750-nerdcasts/">
        O Melhor de 750 Nerdcasts </a>
    </h2>
        <time class="postedon">
        2 horas e 28 minutos •
        6 de novembro de 2020 </time>
    </div>
</article>
"""

for artigo_el in soup.find_all('article'):
    artigo = {}  # cria um novo dict a cada iteração do for
    categoria_el = artigo_el.find(class_='cat-item product-nerdcast')
    if categoria_el:
        artigo['titulo'] = categoria_el.text.strip()

    titulo_el = artigo_el.find('h2')
    if titulo_el:
        artigo['categoria'] = titulo_el.text.strip()

    imagem_el = artigo_el.find('img')
    if imagem_el:
        artigo['imagem'] = imagem_el['src']

    epsodios.append(artigo)

import csv

titulos = epsodios[0].keys()
with open('saida.csv', 'w', encoding='cp1252') as output_file:
    dict_writer = csv.DictWriter(output_file, titulos)
    dict_writer.writeheader()
    dict_writer.writerows(epsodios)

print('fecha o arquivo')



### formas de abrir um arquivo
# leitura
# r ou rb
# escrita
# w ou wb
# adicionar ao final arquivo
# a ou ab



