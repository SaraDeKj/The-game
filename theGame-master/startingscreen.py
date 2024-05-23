import pygame
import sys
pygame.init()

class StartingscreenClass:
    def __init__(self, surface, gameWindowWidth, gameWindowHeight):
        self.theScreen = surface
        self.display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))  # go fullscreen to any resolution
        self.done = True



    def background(self):
        backgroundbillede = pygame.image.load('Images/Background.png')
        display =self.display
        (display.blit(backgroundbillede, (300, 150)))
        pygame.display.update()
    def button (self):
        font = pygame.font.Font(None, 24)
        button_surface = pygame.Surface((150, 50))
        text = font.render("Start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
        button_rect = pygame.Rect(125, 125, 150, 50)

        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if button_rect.collidepoint(event.pos):
                self.done = False

        # Check if the mouse is over the button. This will create the button hover effect
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        button_surface.blit(text, text_rect)

        # Draw the button on the screen
        self.display.blit(button_surface, (button_rect.x, button_rect.y))

        # Update the game state
        pygame.display.update()


surfacedefined = StartingscreenClass((1920, 1080),1920, 1080)
lavbagrund = surfacedefined.background()
lavknap = surfacedefined.button()
while True:
    pass
