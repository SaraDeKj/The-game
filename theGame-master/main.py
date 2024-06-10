import pygame
import os

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
# font = pygame.font.Font(os.path.join('assets', 'Roboto-Bold.ttf'), 32)
# highScoreFont = pygame.font.Font(os.path.join('assets', 'Roboto-Bold.ttf'), 64)

musicPath = os.path.normpath(os.path.join('assets', 'music', 'VicePoint.mp3'))
pygame.mixer.music.load(musicPath)  # https://soundcloud.com/synthwave80s/01-vice-point
pygame.mixer.music.play(-1)
from Player import PlayerClass
from Shot import ShotClass
from Terrain import TerrainClass
from startingscreen import StartingscreenClass
import PlayerSpriteSheet

clock = pygame.time.Clock()
gameWindowHeight = 1080
gameWindowWidth = 1920

terrain = []
# Liste der skal indeholde AKTIVE enemy objekter:
enemies = []
shots = []

# highScore=0
# try:
#    with open('highScoreFile') as file:
#        data = file.read()
#        import math
##        highScore=int(float(data.strip()))
#        highScore=math.inf
#        print("Loaded highscore:",highScore)
# except:
#    print("highScoreFile not found, resetting to 0.")

# get resolution info from hardware:
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
# instead of a screen i use a surface, so that i can scale it down to different resolutions from max (1920x1080)
surface = pygame.Surface((1920, 1080))
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))  # go fullscreen to any resolution

# Background image
background = pygame.image.load('Images/Background.png')
background = pygame.transform.scale(background, (1920, 1080))


# startingscreen virker virkelige ikke
def StartingScreen():
    surfacedefined = StartingscreenClass((1920, 1080), 1920, 1080)
    lavbagrund = surfacedefined.background(1920, 1080)


def createTerrain():
    terrain.append(TerrainClass(surface, 600, 700, 800, 600))


createTerrain()
playerObject1 = PlayerClass(surface, xpos=1100, ypos=390, terrainCollection=terrain)
playerObject2 = PlayerClass(surface, xpos=1000, ypos=390, terrainCollection=terrain)


# COLLISION CHECKER tager imod to gameobjekter og returnrer true, hvis de rører hinanden:
def collisionChecker(firstGameObject, secondGameObject):
    if firstGameObject.x + firstGameObject.width > secondGameObject.x and \
            firstGameObject.x < secondGameObject.x + secondGameObject.width and \
            firstGameObject.y + firstGameObject.height > secondGameObject.y and \
            firstGameObject.y < secondGameObject.y + secondGameObject.height:
        return True
    return False


enemyMaxSpeed = 10
number_of_enemies = 10

StartingScreen()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        # -------PLAYER CONTROLS---------

        # KEY PRESSES:
        # Player 1
        if event.type == pygame.KEYDOWN:
            # Player 1
            if event.key == pygame.K_LEFT:
                playerObject1.xSpeed -= playerObject1.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject1.xSpeed += playerObject1.maxSpeed

                # Skud:
            if event.key == pygame.K_m:  # and (playerObject.xSpeed !=0 or playerObject.ySpeed !=0):
                shots.append(ShotClass(surface, spawnPosX=playerObject1.x - playerObject1.width,
                                       spawnPosY=playerObject1.y + playerObject1.height / 2, playerSpeedX=-5,
                                       playerSpeedY=0))

            # Player 2
            if event.key == pygame.K_a:
                playerObject2.xSpeed -= playerObject2.maxSpeed
            if event.key == pygame.K_d:
                playerObject2.xSpeed += playerObject2.maxSpeed

                # Skud:
            if event.key == pygame.K_e:  # and (playerObject.xSpeed !=0 or playerObject.ySpeed !=0):
                shots.append(ShotClass(surface, spawnPosX=playerObject2.x + playerObject2.width,
                                       spawnPosY=playerObject2.y + playerObject2.height / 2, playerSpeedX=5,
                                       playerSpeedY=0))

        # KEY RELEASES:
        if event.type == pygame.KEYUP:
            # Player 1
            if event.key == pygame.K_LEFT:
                playerObject1.xSpeed += playerObject1.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject1.xSpeed -= playerObject1.maxSpeed
            # Jumping
            if event.key == pygame.K_UP and not playerObject1.jumping:
                jumpStartP1 = playerObject1.y - 1
                playerObject1.ySpeed = playerObject1.jumpSpeed
                playerObject1.jumping = True

            # Player 2
            if event.key == pygame.K_a:
                playerObject2.xSpeed += playerObject1.maxSpeed
            if event.key == pygame.K_d:
                playerObject2.xSpeed -= playerObject1.maxSpeed
            # Jumping
            if event.key == pygame.K_w and not playerObject2.jumping:
                jumpStartP2 = playerObject2.y - 1
                playerObject2.ySpeed = playerObject2.jumpSpeed
                playerObject2.jumping = True

    # debug: print out unused pygame events
    # else:
    #        print(event)

    # UPDATE GAME OBJECTS:
    playerObject1.update()
    playerObject2.update()
    for shot in shots:
        shot.update()
        if collisionChecker(shot, playerObject1):
            playerObject1.x += 50
            shots.remove(shot)

        if collisionChecker(shot, playerObject2):
            playerObject2.x += -50
            shots.remove(shot)

    # Jumping player 1
    if playerObject1.jumping:
        if playerObject1.y < 350:
            playerObject1.ySpeed = playerObject1.gravity
        if playerObject1.y > jumpStartP1:
            playerObject1.jumping = False

    # Jumping player 2
    if playerObject2.jumping:
        if playerObject2.y < 350:
            playerObject2.ySpeed = playerObject1.gravity
        if playerObject2.y > jumpStartP2:
            playerObject2.jumping = False

    # Hvis player er faldet af
    if playerObject1.y > 800:
        playerObject1.die()
        StartingScreen()
        playerObject1 = PlayerClass(surface, xpos=1100, ypos=390, terrainCollection=terrain)
        playerObject2 = PlayerClass(surface, xpos=1000, ypos=390, terrainCollection=terrain)

    if playerObject2.y > 800:
        playerObject2.die()
        StartingScreen()
        playerObject1 = PlayerClass(surface, xpos=1100, ypos=390, terrainCollection=terrain)
        playerObject2 = PlayerClass(surface, xpos=1000, ypos=390, terrainCollection=terrain)

    # If player 1 er uden for bygningen kan den ikke hoppe
    if playerObject1.x > 1375:
        jumpStartP1 = playerObject1.y - 1
        playerObject1.jumping = True
    if playerObject1.x < 525:
        jumpStartP1 = playerObject1.y - 1
        playerObject1.jumping = True

    # If player 2 er uden for bygningen kan den ikke hoppe
    if playerObject2.x > 1375:
        jumpStartP2 = playerObject2.y - 1
        playerObject2.jumping = True
    if playerObject2.x < 525:
        jumpStartP2 = playerObject2.y - 1
        playerObject2.jumping = True

    Players = pygame.image.load('Images/Players.png').convert_alpha()
    bg = pygame.image.load("Images/Background.png").convert_alpha()
    sprite_sheets = PlayerSpriteSheet.SpriteSheet(Players)

    Lars_1 = sprite_sheets.get_image(0, 211, 211, 1)
    Lars_2 = sprite_sheets.get_image(1, 211, 211, 1)
    Jørgen_1 = sprite_sheets.get_image(2, 211, 211, 1)
    Jørgen_2 = sprite_sheets.get_image(3, 211, 211, 1)

    # DRAW GAME OBJECTS:
    # Drawing background
    surface.blit(background, (0, 0))

    if playerObject1.jumping:
        playerObject1.draw(Jørgen_2)
    else:
        playerObject1.draw(Jørgen_1)

    if playerObject2.jumping:
        playerObject2.draw(Lars_2)
    else:
        playerObject2.draw(Lars_1)

    for shot in shots:
        shot.draw()
    for enemy in enemies:
        enemy.draw()
    for tile in terrain:
        tile.draw()

    # Score:                                                 antialias?, color
    #    text = font.render('SCORE: ' + str(playerObject.points), True,(0, 255, 0))
    #    surface.blit(text, (0, 0))

    # text = highScoreFont.render('HIGHSCORE: THE HIGHEST POSSIBLE SCORE', True, (255, 0, 0))
    #   surface.blit(text, (gameWindowWidth/2-text.get_width()/2, gameWindowHeight/2))
    clock.tick(60)
    # push the scaled surface to the actual display:
    display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
    pygame.display.flip()
# When done is false the while loop above exits, and this code is run:
# with open('highScoreFile', 'w') as file:
#    print("Saving highscore to file:", highScore)
#    file.write(str(highScore))
