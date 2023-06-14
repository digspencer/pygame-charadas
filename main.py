import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 500
altura = 850

tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Enigma Quest')
icone = pygame.image.load('img/icone.png')
pygame.display.set_icon(icone)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            exit()
    pygame.display.update()