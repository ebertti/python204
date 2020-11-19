import pygame
import psutil
import requests
from bs4 import BeautifulSoup

pygame.init()

fonte = pygame.font.Font(pygame.font.get_default_font(), 36)

FUNDO = (0, 0, 0)
TEXTO = (255, 255, 255)

def montar_tela(contexto):
    cabecalho(contexto)
    corpo(contexto)
    rodape(contexto)

def cabecalho(contexto):
    tela = contexto.tela
    texto_surface = fonte.render('Texto superior', True, TEXTO)
    tela.blit(texto_surface, dest=(0, 0))
    pygame.draw.line(tela, TEXTO, (0, 40), (contexto.largura_tela, 40))

def rodape(contexto):
    tela = contexto.tela
    texto_surface = fonte.render('Texto Inferior', True, TEXTO)
    tela.blit(texto_surface, dest=(0, contexto.altura_tela - 36))
    pygame.draw.line(tela, TEXTO, (0, contexto.altura_tela - 40), (contexto.largura_tela, contexto.altura_tela - 40))

def corpo(contexto):

    ## exibir o titulo do ultimo nerdcast
    tela = contexto.tela
    texto_surface = fonte.render(str(contexto.uso_cpu), True, TEXTO)
    tela.blit(texto_surface, dest=(100, 50))

    titulo_surface = fonte.render(str(contexto.titulo), True, TEXTO)
    tela.blit(titulo_surface, dest=(100, 100))


def carregar_dados(contexto):
    contexto.uso_cpu = psutil.cpu_percent()
    ultimo_epsodio_nerdcast(contexto)


def ultimo_epsodio_nerdcast(contexto):
    if not contexto.titulo:

        if not contexto.HTML:
            response = requests.get('https://jovemnerd.com.br/nerdcast/')
            contexto.HTML = response.text

        soup = BeautifulSoup(contexto.HTML, 'html.parser')
        main_content_el = soup.find('section', class_='main-content')
        artigo_el = main_content_el.find_all('article')
        contexto.titulo = artigo_el[contexto.posicao].find('h2').text.strip()


class Contexto():
    terminou = False
    tela = None
    largura_tela = 800
    altura_tela = 600
    uso_cpu = 0
    titulo = ''
    posicao = 0

    HTML = ''

def main():
    contexto = Contexto()
    tela = pygame.display.set_mode((contexto.largura_tela, contexto.altura_tela))
    clock = pygame.time.Clock()
    contexto.tela = tela

    while not contexto.terminou:

        # Atualiza o desenho na tela
        pygame.display.update()
        tela.fill(FUNDO)

        carregar_dados(contexto)
        montar_tela(contexto)

        # Checar os eventos do mouse aqui:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                press = pygame.key.get_pressed()

                ## magica
                contexto.titulo = ''

                if press[pygame.K_0]:
                    contexto.posicao = 0
                if press[pygame.K_1]:
                    contexto.posicao = 1
                if press[pygame.K_2]:
                    contexto.posicao = 2
                if press[pygame.K_3]:
                    contexto.posicao = 3
                if press[pygame.K_4]:
                    contexto.posicao = 4
                if press[pygame.K_5]:
                    contexto.posicao = 5
                if press[pygame.K_6]:
                    contexto.posicao = 6
                if press[pygame.K_7]:
                    contexto.posicao = 7
                if press[pygame.K_8]:
                    contexto.posicao = 8
                if press[pygame.K_9]:
                    contexto.posicao = 9

            if event.type == pygame.QUIT:
                contexto.terminou = True

        clock.tick(60)

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()


if __name__ == '__main__':
    main()
