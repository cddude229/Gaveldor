import pygame
from board import *
from state import State
from piece import Piece

black = [0,0,0]
white = [255,255,255]

screenw = 900
screenh = 600

x=14
y=20

screen = pygame.display.set_mode([screenw,screenh+screenh/y])
pygame.display.set_caption('Gaveldor')

#font = pygame.font.Font(None, 24)
#font2 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
attack=False

board = pygame.sprite.RenderPlain()
b = Board()
board.add(b)

button = pygame.sprite.RenderPlain()
but = Button()
button.add(but)

gs = State(x,y)
Piece.setState(gs)

spaces = pygame.sprite.RenderPlain()
for i in range(x):
    for j in range(y/2+1):
        if i%2==0:
            s=Space(i*screenw/x-i*screenw/x/4,2*j*screenh/y,i,j*2)
        else:
            s=Space(i*screenw/x-i*screenw/x/4,2*int((j+.5)*screenh/y),i,j*2+1)
        spaces.add(s)

#sets up board


#finds which spaces are occupied
for i in spaces:
    if not gs.getPiece(i.x,i.y)==None:
        i.update(gs.getPiece(i.x,i.y))

done = False
gameover = False

pygame.init()

while done==False:
    while gameover==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                gameover=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1,y1=pygame.mouse.get_pos()
                if x1>(x+2)*screenw/x-(x+2)*screenw/x/4 and y1>screenh/2 and y1<screenh/2+50:
                    attack=True
                startx = x1/(3*screenw/x/4)
                if startx%2==0:
                    start=(startx,y1/(screenh/y*2)*2)
                else:
                    start=(startx,(y1-screenh/y/2)/(screenh/y*2)*2+1)
            if event.type == pygame.MOUSEBUTTONUP:
                x2,y2=pygame.mouse.get_pos()
                endx = x2/(3*screenw/x/4)
                if endx%2==0:
                    end=(endx,y2/(screenh/y*2)*2)
                else:
                    end=(endx,(y2-screenh/y/2)/(screenh/y*2)*2+1)
                if not gs.getPiece(start[0],start[1])==None:
                    p = gs.getPiece(start[0],start[1])
                    if p.isValidMove(end[0],end[1]):
                        p.moveTo(end[0],end[1])
                        for i in spaces:
                            if i.x==start[0] and i.y==start[1]:
                                i.update(None)
        while attack==True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    done=True
                    gameover=True
                    attack=False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1=pygame.mouse.get_pos()
                    if x1>(x+2)*screenw/x-(x+2)*screenw/x/4 and y1>screenh/2 and y1<screenh/2+50:
                        attack=False
                    startx = x1/(3*screenw/x/4)
                    if startx%2==0:
                        start=(startx,y1/(screenh/y*2)*2)
                    else:
                        start=(startx,(y1-screenh/y/2)/(screenh/y*2)*2+1)
                if e.type == pygame.MOUSEBUTTONUP:
                    x2,y2=pygame.mouse.get_pos()
                    endx = x2/(3*screenw/x/4)
                    if endx%2==0:
                        end=(endx,y2/(screenh/y*2)*2)
                    else:
                        end=(endx,(y2-screenh/y/2)/(screenh/y*2)*2+1)
                    if not gs.getPiece(start[0],start[1])==None:
                        p = gs.getPiece(start[0],start[1])
                        if p.isValidAttack(end[0],end[1]):
                            p.attack(gs.getPiece(end[0],end[1]))
                            print "hi"
                            attack = False
                                     
            
        for i in spaces:
            if not gs.getPiece(i.x,i.y)==None:
                i.update(gs.getPiece(i.x,i.y))
        gs.player1.clearDeadPieces()
        gs.player2.clearDeadPieces()
        button.draw(b.image)
        spaces.draw(b.image)
        board.draw(screen)
        pygame.display.flip()

pygame.quit()
