import requests
from bs4 import BeautifulSoup

response = requests.get('https://jovemnerd.com.br/nerdcast/')
texto = response.text

soup = BeautifulSoup(texto, 'html.parser')
print('bs4',  soup.title.text)

epsodios = []

main_content_el = soup.find('section', class_='main-content')

for artigo_el in main_content_el.find_all('article'):
    artigo = {}  # cria um novo dict a cada iteração do for
    categoria_el = artigo_el.find(class_='cat-item product-nerdcast')
    if categoria_el:
        artigo['categoria'] = categoria_el.text.strip()

    titulo_el = artigo_el.find('h2')
    if titulo_el:
        artigo['titulo'] = titulo_el.text.strip()

    imagem_el = artigo_el.find('img')
    if imagem_el:
        artigo['imagem'] = imagem_el['src']

    link_el = artigo_el.find('a')
    if link_el:
        artigo['link'] = link_el['href']

        pagina = requests.get(artigo['link'])
        soup2 = BeautifulSoup(pagina.text, 'html.parser')

        conteudo_el = soup2.find(class_='content')
        if conteudo_el:
            artigo['conteudo'] = conteudo_el.text.strip().replace('\n', ' ')

    epsodios.append(artigo)



import csv
titulos = epsodios[0].keys()
with open('saida.csv', 'w', encoding='cp1252') as output_file:
    dict_writer = csv.DictWriter(output_file, titulos)
    dict_writer.writeheader()
    dict_writer.writerows(epsodios)

print('fecha o arquivo')



# ETL
