import pygame
import os
pygame.init()

surface = pygame.display.set_mode((1920, 1080))

class StartingscreenClass:
    backgroundbillede = pygame.image.load('Images/Background.png')
    Done = False
    while not Done:
        surface.blit(backgroundbillede, (300, 150))
        pygame.display.update()

