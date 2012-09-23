import pygame
from state import State

black = [0,0,0]
white = [255,255,255]

screenw = 900
screenh = 600

x=14
y=10

tile = '../res/tiles/blank.png'
class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([screenw, screenh+screenh/y])
        self.image.fill(white)
        pygame.draw.line(self.image,black,(0,0),(50,50),3)
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]

class Space(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,xcoord,ycoord):
        pygame.sprite.Sprite.__init__(self)
        self.x3=screenw/x/3
        self.y3=screenh/y/3
        self.piece=None
        self.x=xcoord
        self.y=ycoord
        self.image = pygame.image.load(tile).convert_alpha()
        self.image = pygame.transform.scale(self.image,(screenw/x,screenh/y))
        self.rect = self.image.get_rect()
        self.rect.topleft = [xpos,ypos]
    def update(self,piece):
        self.piece=piece
        if not self.piece==None:
            pygame.draw.rect(self.image,black,[self.x3,self.y3,2*self.x3/3,2*self.y3/3])
        

        

