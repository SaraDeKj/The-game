import pygame
import os
pygame.init()

import main

display = pygame.display.set_mode((main.gameWindowWidth, main.gameWindowHeight))
class StartingscreenClass:
    backgroundbillede = pygame.image.load('Images/Background.png')
    Done = False
    while not Done:
        (display.blit(backgroundbillede, (300, 150)))
        pygame.display.update()

