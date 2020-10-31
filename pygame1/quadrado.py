import random
import pygame

class Quadradinho():

    def __init__(self, largura_tela, altura_tela, x=None, y=None):
        self.largura = 30
        self.altura = 30
        self.x = x or random.randint(0, largura_tela - self.largura)
        self.y = y or random.randint(0, altura_tela - self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20, 255), random.randint(20, 255),
                    random.randint(20, 255))

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)


