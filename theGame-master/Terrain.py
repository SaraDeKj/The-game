import pygame

pygame.init()

class TerrainClass:
    color = (100, 100, 100)

    def __init__(self, screen, _x, _y, _width, _height):
        self.theScreen = screen
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height
        self.terrainLook = pygame.image.load('assets/Background/Blue.png').convert_alpha()

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        terrainLook = pygame.transform.scale(self.terrainLook, (self.width, self.height))
        self.theScreen.blit(terrainLook, (self.x, self.y))