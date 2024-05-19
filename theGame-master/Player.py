import pygame
import os
import PlayerSpriteSheet


class PlayerClass:

    xSpeed=0
    ySpeed=0
    maxSpeed=5
    maxJumpSpeed=100
    width=100
    height=211
    color=(0, 128, 255)
    points=0
    canJump=1

    sfxPath = os.path.normpath(os.path.join('assets', 'sfx', 'aaw.wav')) #kan også være .ogg eller .mp3
    collisionSFX = pygame.mixer.Sound(sfxPath)

    def __init__(self,screen,xpos,ypos,terrainCollection):
        self.x=xpos
        self.y=ypos
        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]

        self.terrainCollection=terrainCollection

    def update(self):

        self.futureX=self.x+self.xSpeed
        self.futureY=self.y+self.ySpeed

        xWillCollide = False
        yWillCollide = False

        for tile in self.terrainCollection:
            #if the player is within the x coordinates of a wall tile, and future Y coordinate is inside the wall:
            if self.x + self.width > tile.x and self.x < tile.x + tile.width and self.futureY + self.height > tile.y and self.futureY < tile.y + tile.height:
                yWillCollide=True
            # if the player is within the Y coordinates of a wall tile, and future X coordinate is inside the wall:
            if self.y + self.height > tile.y and self.y < tile.y + tile.height and self.futureX + self.width > tile.x and self.futureX < tile.x + tile.width:
                xWillCollide=True

        if not xWillCollide:
            self.x = self.futureX
        if not yWillCollide:
            self.y = self.futureY

        #safety to prevent overshoot:
        if self.x+self.width > self.screenWidth:
            self.x = self.screenWidth-self.width
        if self.y+self.height > self.screenHeight:
            self.y = self.screenHeight-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0


    pygame.display.set_mode()
    Lars = pygame.image.load('Images/Lars_der_er_sur_slet_ikke_leprocaun_.png').convert_alpha()
    sprite_sheets = PlayerSpriteSheet.SpriteSheet(Lars)

    frame_0 = sprite_sheets.get_image(0,211,211, 1)
    frame_1 = sprite_sheets.get_image(1, 211, 211, 1)

    def draw(self):
        pygame.draw.rect(self.theScreen, pygame.SRCALPHA, pygame.Rect(self.x, self.y, self.width, self.height))
        self.theScreen.blit(self.frame_0, (self.x - self.width/2, self.y))

def die(self):
    print("dead")

    