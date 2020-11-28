import requests
import pygame.image
import io

USUARIO = input('informe o usuario do github:')

r = requests.get('https://avatars2.githubusercontent.com/u/140394?s=460&u=e62780b6e2a57dabe24c8b99eff3023a25493b17&v=4')
img = io.BytesIO(r.content)
perfil_img = pygame.image.load(img)

pygame.init()

largura_tela = 800
altura_tela = 600
x = 400
y = 300

tela = pygame.display.set_mode((largura_tela, altura_tela))
cor = (0, 0, 255)
terminou = False

while not terminou:
    pygame.display.update()
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, cor, (x - 25, y - 25, 50, 50))

    reat = pygame.Rect((100, 100, 50, 50))

    tela.blit(perfil_img, reat)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()
pygame.quit()
