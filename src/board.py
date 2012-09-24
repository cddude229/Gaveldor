import pygame
from state import State

black = [0,0,0]
white = [255,255,255]

screenw = 900
screenh = 600

x=14
y=20

tile = '../res/tiles/blank.png'
inf = '../res/inf.jpg'
class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([screenw, screenh+screenh/y])
        self.image.fill(white)
        pygame.draw.line(self.image,black,(0,0),(50,50),3)
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]

class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200,50])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.topleft = [(x+2)*screenw/x-(x+2)*screenw/x/4,screenh/2]

class Space(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,xcoord,ycoord):
        pygame.sprite.Sprite.__init__(self)
        self.x3=screenw/x/3
        self.y3=screenh/y/3
        self.piece=None
        self.x=xcoord
        self.y=ycoord
        self.image = pygame.image.load(tile).convert_alpha()
        self.image = pygame.transform.scale(self.image,(screenw/x,screenh/y*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = [xpos,ypos]
    def update(self,piece):
        self.piece=piece
        if not self.piece==None:
            self.image = pygame.image.load(inf).convert_alpha()
        else:
            self.image = pygame.image.load(tile).convert_alpha()
        self.image = pygame.transform.scale(self.image,(screenw/x,screenh/y*2))
        

        

