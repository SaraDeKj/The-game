import pygame
from os.path import join

pygame.init()

class TerrainClass:
    color = (100, 100, 100)


    def __init__(self, screen, _x, _y, _width, _height):
        self.theScreen = screen
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height
        self.terrainLook = pygame.image.load('Images/Background.png').convert_alpha()

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        terrainLook = pygame.transform.scale(self.terrainLook, (self.width, self.height))
        self.theScreen.blit(terrainLook, (self.x, self.y))



pygame.display.set_caption("Platformer")
# Set full screen mode
info = pygame.display.Info()  # Get screen info
WIDTH, HEIGHT = info.current_w, info.current_h
Fps = 60
Player_Vel = 5
Window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

def update(self):
    self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
    self.mask = pygame.mask.from_surface(self.sprite)

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image, objects):
    for tile in background:
        Window.blit(bg_image, tile)
    for obj in objects:
        obj.draw(window)
    pygame.display.update()

def main(Window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    block_size = 96
    num_blocks = WIDTH // 2 // block_size
    start_x = (WIDTH - (num_blocks * block_size)) // 2
    blocks = []
    for i in range(num_blocks):
        block_x = start_x + i * block_size
        block_y = HEIGHT // 1.1 - block_size // 2
        block_y1 = HEIGHT - block_size // 2
        block_y2 = HEIGHT // 1.25 - block_size // 2
        blocks.append(Block(block_x, block_y, block_size))
        blocks.append(Block(block_x, block_y1, block_size))
        blocks.append(Block(block_x, block_y2, block_size))

    run = True
    while run:
        clock.tick(Fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                break

        draw(Window, background, bg_image, blocks)

    pygame.quit()
    quit()

if __name__ == "__main__":
    print("main")
    main(Window)

