import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 850
altura = 500

x = largura/2
y = altura/2
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Enigma Quest')
icone = pygame.image.load('img/icone.png')
pygame.display.set_icon(icone)

while True:

    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            exit()

        # Movimentação teclado    
        if pygame.key.get_pressed()[K_a]:
            x = x - 15
        if pygame.key.get_pressed()[K_d]:
            x = x + 15
        if pygame.key.get_pressed()[K_s]:
            y = y + 15
        if pygame.key.get_pressed()[K_w]:
            y = y - 15

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))  
     
    pygame.display.update()