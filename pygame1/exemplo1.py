import random

import pygame

pygame.init()

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCA = (255, 255, 255)
clock = pygame.time.Clock()

terminou = False
i = 0
while not terminou:

    # Atualiza o desenho na tela
    pygame.display.update()
    tela.fill((0,0,0))
    i += 1
    x = i
    y = i

    pygame.draw.rect(tela, BRANCA, (x, y, 50, 50), 1)

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    clock.tick(5)

# Finaliza a janela do jogo
pygame.display.quit()

# Finaliza o pygame
pygame.quit()
