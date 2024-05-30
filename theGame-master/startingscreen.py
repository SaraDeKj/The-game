import pygame
import sys
pygame.init()

class StartingscreenClass:
    def __init__(self, surface, gameWindowWidth, gameWindowHeight):
        self.theScreen = surface
        self.display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))  # go fullscreen to any resolution
        self.done = True

    def text_objects(self,text, font):
        textSurface = font.render(text, True,(192,192,192))
        return textSurface, textSurface.get_rect()



    def background(self, gameWindowWidth, gameWindowHeight):
        while self.done == True:

            backgroundbillede = pygame.image.load('Images/Background.png')
            display =self.display
            (display.blit(backgroundbillede, (300, 150)))
            largeText = pygame.font.Font('fonts\Grand9K Pixel.ttf', 115)
            TextSurf, TextRect = self.text_objects("Rooftop fighters", largeText)
            TextRect.center = ((gameWindowWidth / 2), (gameWindowHeight / 4))
            self.display.blit(TextSurf, TextRect)
            pygame.display.update()
        else:
            quit()

    def button(self,msg, x, y, w, h, ic, ac, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            print(click)
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(self.display, ac, (x, y, w, h))

                if click[0] == 1 and action != None:
                    self.done = False
            else:
                pygame.draw.rect(self.display, ic, (x, y, w, h))

            smallText = pygame.font.SysFont("comicsansms", 20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ((x + (w / 2)), (y + (h / 2)))
            self.display.blit(textSurf, textRect)



surfacedefined = StartingscreenClass((1920, 1080),1920, 1080)
lavknap = surfacedefined.button("Start",150,450,100,50,(0,200,0),(0,255,0))
lavbagrund = surfacedefined.background(1920, 1080)
while self.done == True:
    pass