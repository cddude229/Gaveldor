import pygame


black = [0,0,0]
white = [255,255,255]

screenw = 900
screenh = 600

x=15
y=15

class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([screenw, screenh])
        self.image.fill(white)
        pygame.draw.line(self.image,black,(0,0),(50,50),3)
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]

class Space(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,xcoord,ycoord):
        pygame.sprite.Sprite.__init__(self)
        x3=screenw/x/2
        y2=screenh/y/2
        self.x=xcoord
        self.y=ycoord
        self.image = pygame.Surface([screenw/x,screenh/y])
        self.image.fill(white)
        pygame.draw.line(self.image,black,(x3,0),(2*x3,0),3)
        pygame.draw.line(self.image,black,(x3,2*y2),(2*x3,2*y2),3)
        pygame.draw.line(self.image,black,(0,y2),(x3,2*y2),3)
        pygame.draw.line(self.image,black,(0,y2),(x3,0),3)
        pygame.draw.line(self.image,black,(2*x3,0),(3*x3,y2),3)
        self.rect = self.image.get_rect()
        self.rect.topleft = [xpos,ypos]
        

screen = pygame.display.set_mode([screenw,screenh])
pygame.display.set_caption('Gaveldor')

#font = pygame.font.Font(None, 24)
#font2 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

board = pygame.sprite.RenderPlain()
b = Board()
board.add(b)

spaces = pygame.sprite.RenderPlain()
for i in range(x):
    for j in range(y):
        if i%2==0:
            s=Space(i*screenw/x,j*screenh/y,i,j)
        else:
            s=Space(i*screenw/x,int((j+.5)*screenh/y),i,j+1)
        spaces.add(s)

done = False
gameover = False

pygame.init()

while done==False:
    while gameover==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                gameover=True
        spaces.draw(b.image)
        board.draw(screen)
        pygame.display.flip()

pygame.quit()
        

