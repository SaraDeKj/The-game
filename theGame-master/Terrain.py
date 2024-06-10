import pygame
pygame.init()
width=800
height=600
screen=pygame.display.set_mode((0,0))


class TerrainClass:
    def __init__(self,surface,x,y,w,h,image):
        self.width=w
        self.height=h
        self.x=x
        self.y=y
        self.screen=surface

        self.rect= pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = pygame.image.load(image).convert_alpha()


    def draw(self):
        #color = pygame.transform.scale(self.color, (self.rect_width, self.rect_height))

        #pygame.draw.rect(screen, (255, 255, 255), self.rect)
        n_x = self.width // self.color.get_width()
        n_y = self.height // self.color.get_height()
        #print(f"n_x: {n_x} n_Y:{n_y}")
        for i in range(n_x):
            for j in range(n_y):
                self.screen.blit(self.color, (self.x+i*self.color.get_width(), self.y+j*self.color.get_height()))



'''
Me=TerrainClass( 100, 100, 800, 600,"Images/Baby.png")
run=True
while run:
    pass
    #screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    Me.draw()
    pygame.display.update()
'''