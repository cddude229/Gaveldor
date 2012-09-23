import pygame
from board import Board
from board import Space

black = [0,0,0]
white = [255,255,255]

screenw = 900
screenh = 600

x=14
y=10

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

for i in spaces:
    if i.x==3:
        i.update(2)

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