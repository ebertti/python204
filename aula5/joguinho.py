import pygame, sys
from pygame.locals import *

# CONSTANTES
# Constantes que vamos usar para o tamanho da tela
LARGURA_TELA = 400
ALTURA_TELA = 300
# Será utilizado para a velocidade do jogo
FPS = 200
# Valores para o desenho das paletas e do fundo
LARGURA_LINHA = 5
PALETA_TAMANHO = 50
PALETAOFFSET = 50

# cores
PRETO = (204, 231, 232)
BRANCO = (224, 123, 57)

MOVIMENTO = {
    'cima': False,
    'baixo': False,
    'fator': 1
}


# Função para desenhar o fundoplacar
def desenhaArena():
    DISPLAYSURF.fill(PRETO)
    # Desenha a quadra
    pygame.draw.rect(DISPLAYSURF, BRANCO, ((0, 0), (LARGURA_TELA, ALTURA_TELA)), LARGURA_LINHA * 2)
    # Desenha a linha no centro
    pygame.draw.line(DISPLAYSURF, BRANCO, ((LARGURA_TELA // 2), 0), ((LARGURA_TELA // 2), ALTURA_TELA),
                     (LARGURA_LINHA // 4))


# Função para desenhar a paleta
def desenhaPaleta(paleta):
    # Impede da paleta ir  além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    # Impede da paleta ir  além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
        # Desenha a paleta
    pygame.draw.rect(DISPLAYSURF, BRANCO, paleta)


# Função para desenhar a bola
def desenhaBola(bola):
    pygame.draw.rect(DISPLAYSURF, BRANCO, bola)


# altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX

    if bola.x % MOVIMENTO['fator'] == 0:
        bola.y += bolaDirY

    return bola


# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verificaColisao(bola, bolaDirX, bolaDirY):
    if bola.top == (LARGURA_LINHA) or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY


def inteligenciaArtificial(bola, bolaDirX, paleta2):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bola.x > LARGURA_TELA // 2:
        if bola.x % 2 == 0:
            if paleta2.centery < bola.centery:
                paleta2.y += 1
            else:
                paleta2.y -= 1
    elif bola.x > LARGURA_TELA // 4:
        if bola.x % 5 == 0:
            if paleta2.centery < bola.centery:
                paleta2.y += 1
            else:
                paleta2.y -= 1

    return paleta2


# Verifica a colisão da bola com a paleta1 ou paleta2
def verificaColisaoBola(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:

        if paleta1.centery < bola.centery:
            MOVIMENTO['fator'] = 3
        else:
            MOVIMENTO['fator'] = 1

        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        return -1
    else:
        return 1


# Verifica se o jogador fez ponto e retorna o novo valor do placar
def verificaPlacar(paleta1, bola, placar, bolaDirX):
    # zera a contagem se a bola acerta a borda do jogador
    if bola.left == LARGURA_LINHA:
        return 0
    # 1 ponto por acertar a bola
    elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 2
        return placar
    # 10 pontos se vencer a paleta do computador
    elif bola.right == LARGURA_TELA - LARGURA_LINHA:
        placar += 5
        return placar
    # retorna o mesmo placar se nenhum ponto foi adicionado
    else:
        return placar


# Desenha o placar na tela
def desenhaPlacar(placar):
    resultadoSurf = BASICFONT.render('placar = %s' % (placar), True, BRANCO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 150, 25)
    DISPLAYSURF.blit(resultadoSurf, resultadoRect)


# Função principal
def movimentarPaleta(paleta):

    if MOVIMENTO['cima']:
        paleta.y -= 2

    if MOVIMENTO['baixo']:
        paleta.y += 2

def main():
    placar = 0
    pygame.init()
    ##Informações para a fonte da letra
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)


    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('PongNet')

    # Iniciando as variáveis nas posições iniciais
    # Estas variáveis serão alteradas ao longo da execução
    bolaX = LARGURA_TELA // 2 - LARGURA_LINHA // 2
    bolaY = ALTURA_TELA // 2 - LARGURA_LINHA // 2
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2

    # altera a posição da bola
    bolaDirX = -1
    bolaDirY = -1

    # Criando os retangulos para a bola e paletas.
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    # Desenhando as posições iniciais da Arena
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)

    pygame.mouse.set_visible(0)

    while True:  # Loop principal
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type in (KEYDOWN, KEYUP):
                teclado = pygame.key.get_pressed()
                MOVIMENTO['baixo'] = teclado[K_DOWN]
                MOVIMENTO['cima'] = teclado[K_UP]

        movimentarPaleta(paleta1)

        desenhaArena()
        desenhaPaleta(paleta1)
        desenhaPaleta(paleta2)
        desenhaBola(bola)

        bola = moveBola(bola, bolaDirX, bolaDirY)
        bolaDirX, bolaDirY = verificaColisao(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verificaColisaoBola(bola, paleta1, paleta2, bolaDirX)
        paleta2 = inteligenciaArtificial(bola, bolaDirX, paleta2)

        placar = verificaPlacar(paleta1, bola, placar, bolaDirX)
        desenhaPlacar(placar)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()



# todo:

# -- obrigatoria
# mudar a cor jogo
# mudar a grossura das linhas
# mudar a contagem do placar

# -- dificil
# diminuir a velocidade da paleta do computador
# trocar o movimento de mouse, por movimento de teclado
# alterar movimentação da bola quando bate na parede

# -- desafio
# de acordo com a parte que da paleta, ter mais ou menos inclinação
