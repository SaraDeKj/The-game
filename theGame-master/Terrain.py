import pygame
pygame.init()
width=800
height=600
screen=pygame.display.set_mode((0,0))

class Terrain:
    def __init__(self,x,y,w,h,image):
        self.rect_width=w
        self.rect_height=h
        self.x=x
        self.y=y
        self.screen=pygame.display.set_mode((0,0))

        self.rect=pygame.Rect(self.x,self.y,self.rect_width,self.rect_height)
        self.color = pygame.image.load(image).convert_alpha()


    def draw(self):
        #color = pygame.transform.scale(self.color, (self.rect_width, self.rect_height))

        #pygame.draw.rect(screen, (255, 255, 255), self.rect)
        n_x = self.rect_width // self.color.get_width()
        n_y = self.rect_height // self.color.get_height()
        #print(f"n_x: {n_x} n_Y:{n_y}")
        for i in range(n_x):
            for j in range(n_y):
                self.screen.blit(self.color, (self.x+i*self.color.get_width(), self.y+j*self.color.get_height()))




Me=Terrain(400,600,800,400,"../billeder/mursten.png")
#hhh=Terrain(200,200,128,128,"assets/Background/Yellow.png")
Me.draw()
#hhh.draw()
run=True
while run:
    #screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    #Me.draw()
    pygame.display.update()


