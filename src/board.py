import pygame
from state import State

black = [20,20,20]
white = [255,255,255]


class Board(pygame.sprite.Sprite):
    def __init__(self,screenw,screenh,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([screenw, screenh+screenh/y])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
'''
class Button(pygame.sprite.Sprite):
    def __init__(self,screenw,screenh,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200,50])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.topleft = [(x+2)*screenw/x-(x+2)*screenw/x/4,screenh/2]
'''
class Space(pygame.sprite.Sprite):
    def __init__(self,screenw,screenh,boardx,boardy,xpos,ypos,xcoord,ycoord):
        self.screenw = screenw
        self.screenh = screenh
        self.boardx = boardx
        self.boardy = boardy
        pygame.sprite.Sprite.__init__(self)
        self.x3=screenw/boardx/3
        self.y3=screenh/boardy/3
        self.piece=None
        self.x=xcoord
        self.y=ycoord
        self.xpos = xpos
        self.ypos = ypos
        self.image = pygame.image.load('../res/tiles/blank.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(screenw/boardx,screenh/boardy*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = [xpos,ypos]
        self.highlighted = False
        self.dir_sel = False

    def update(self,piece):
        self.piece = piece
        if self.piece != None: 
          self.image = pygame.image.load(self.piece.imageFile).convert_alpha()
          self.image = pygame.transform.smoothscale(self.image, (self.screenw/self.boardx, self.screenh/self.boardy*2))
          self.image = pygame.transform.rotate(self.image, -60 * self.piece.direction)
          self.rect = self.image.get_rect(center = self.rect.center)
        else:
          if self.highlighted: self.image = pygame.image.load('../res/tiles/highlighted.png').convert_alpha()
          else: self.image = pygame.image.load('../res/tiles/blank.png').convert_alpha()
          self.image = pygame.transform.smoothscale(self.image, (self.screenw/self.boardx, self.screenh/self.boardy*2))
          self.rect = self.image.get_rect(center = self.rect.center)
