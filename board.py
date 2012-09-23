import pygame

black = [0,0,0]
white = [255,255,255]

screenw = 900
screenh = 600

x=14
y=10
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
        self.x2=screenw/x/2
        self.y2=screenh/y/2
        self.piece=None
        self.x=xcoord
        self.y=ycoord
        self.image = pygame.Surface([screenw/x,screenh/y])
        self.image.fill(white)
        pygame.draw.line(self.image,black,(self.x2,0),(2*self.x2,0),3)
        pygame.draw.line(self.image,black,(self.x2,2*self.y2),(2*self.x2,2*self.y2),3)
        pygame.draw.line(self.image,black,(0,self.y2),(self.x2,2*self.y2),3)
        pygame.draw.line(self.image,black,(0,self.y2),(self.x2,0),3)
        pygame.draw.line(self.image,black,(2*self.x2,0),(3*self.x2,self.y2),3)
        self.rect = self.image.get_rect()
        self.rect.topleft = [xpos,ypos]
    def update(self,piece):
        self.piece=piece
        if not self.piece==None:
            pygame.draw.rect(self.image,black,[self.x2/2,self.y2/2,3*self.x2/2,3*self.y2/2])
        

        

