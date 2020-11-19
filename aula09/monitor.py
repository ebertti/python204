import pygame
import psutil

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
    tela = contexto.tela
    texto_surface = fonte.render(str(contexto.uso_cpu), True, TEXTO)
    tela.blit(texto_surface, dest=(100, 50))


def carregar_dados(contexto):
    contexto.uso_cpu = psutil.cpu_percent()



class Contexto():
    terminou = False
    tela = None
    largura_tela = 800
    altura_tela = 600
    uso_cpu = 0

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
            if event.type == pygame.QUIT:
                contexto.terminou = True

        clock.tick(5)

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()


if __name__ == '__main__':
    main()
