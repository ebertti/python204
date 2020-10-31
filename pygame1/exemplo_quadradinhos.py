import pygame

from pygame1.quadrado import Quadradinho

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False

# Cria relógio
clock = pygame.time.Clock()
lista = []

while not terminou:
    tela.fill((0,0,0))
    apagou = False
    for q in lista:
        q.desenha(tela)

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            for q in lista:
                if q.area.collidepoint(pos):
                    apagou = True
                    break

            if apagou:
                lista.remove(q)

            if not apagou:
                # Obtém as coordenadas do mouse na tela
                quadrado = Quadradinho(largura_tela, altura_tela, *pos)
                quadrado.desenha(tela)

                lista.append(quadrado)

        if event.type == pygame.QUIT:
            terminou = True

    # Atualiza o desenho na tela
    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(5)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
