import pygame
import os
surface = pygame.Surface((1920, 1080))

class StartingscreenClass:
    backgroundbillede = pygame.image.load('billeder/Background.png')
    done = False
    while not done:
        for event in pg.event.get():
            surface.fill(0,0,0)

