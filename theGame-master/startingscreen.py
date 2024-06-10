import pygame
import sys
pygame.init()

class StartingscreenClass:
    def __init__(self, surface, gameWindowWidth, gameWindowHeight):
        self.theScreen = surface
        self.display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))  # go fullscreen to any resolution
        self.done = True

    def text_objects(self,text, font):
        textSurface = font.render(text, True,(0,0,0))
        return textSurface, textSurface.get_rect()
    def shadow_text_objects(self,text, font):
        textSurface = font.render(text, True,(255,255,255))
        return textSurface, textSurface.get_rect()




    def background(self, gameWindowWidth, gameWindowHeight):
        while self.done == True:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    self.done==False
                elif event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.done==False
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.done == False
                    pygame.quit()
                    quit()

            backgroundbillede = pygame.image.load('Images/Background.png')
            display =self.display
            (display.blit(backgroundbillede, (300, 150)))
            largeText = pygame.font.Font('fonts\Grand9K Pixel.ttf', 115)
            TextSurf, TextRect = self.text_objects("Rooftop fighters", largeText)
            TextRect.center = ((gameWindowWidth / 2), (gameWindowHeight / 4))
            self.display.blit(TextSurf, TextRect)
            shadow = pygame.font.Font('fonts\Grand9K Pixel.ttf', 115)
            TextSurf, TextRect = self.shadow_text_objects("Rooftop fighters", shadow)
            TextRect.center = ((gameWindowWidth / 2), (gameWindowHeight / 4.2))
            self.display.blit(TextSurf, TextRect)
            smalltext = pygame.font.Font('fonts\Grand9K Pixel.ttf', 70)
            TextSurf, TextRect = self.text_objects("tryk på SPACE for at starte", smalltext )
            TextRect.center = (gameWindowWidth / 2), (gameWindowHeight / 2)
            self.display.blit(TextSurf, TextRect)
            shadow = pygame.font.Font('fonts\Grand9K Pixel.ttf', 72)
            TextSurf, TextRect = self.shadow_text_objects("tryk på SPACE for at starte", shadow)
            TextRect.center = ((gameWindowWidth / 2), (gameWindowHeight / 2.01))
            self.display.blit(TextSurf, TextRect)
            pygame.display.update()
        else:
            quit()

    # def button( self, msg, x, y, w, h, ic, ac, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            print(click)
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(self.display, ac, (x, y, w, h))

                if click[0] == 1 and action != None:
                    self.done = False
            else:
                pygame.draw.rect(self.display, ic, (x, y, w, h))

            smallText = pygame.font.Font('fonts\Grand9K Pixel.ttf', 20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ((x + (w / 2)), (y + (h / 2)))
            self.display.blit(textSurf, textRect)
            pygame.display.update()



surfacedefined = StartingscreenClass((1920, 1080),1920, 1080)
lavbagrund = surfacedefined.background(1920, 1080)
