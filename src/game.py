import pygame
from board import *
from state import State
from piece import Piece

screenw = 900
screenh = 660

cols=7
rows=11

screen = pygame.display.set_mode([screenw-screenw/4+32,screenh+screenh/rows])
pygame.display.set_caption('Gaveldor')

pygame.init()

font = pygame.font.Font(None, 24)
#font2 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
attack = False

board = pygame.sprite.RenderPlain()
b = Board(screenw,screenh,cols,rows)
board.add(b)

#button = pygame.sprite.RenderPlain()
#but = Button(screenw,screenh,cols,rows)
#button.add(but)

gs = State(cols,rows)
Piece.setState(gs)

spaces = pygame.sprite.RenderPlain()
#sets up board
for i in xrange(cols):
    for j in xrange(rows/2+1):
        if i%2==0:
            s=Space(screenw,screenh,cols,rows,i*screenw/cols-i*screenw/cols/4,2*j*screenh/rows,i,j*2)
        else:
            if j < rows/2:
              s=Space(screenw,screenh,cols,rows,i*screenw/cols-i*screenw/cols/4,2*int((j+.5)*screenh/rows),i,j*2+1)
        spaces.add(s)

done = False
gameover = False

turn_stage = 'piece_sel' # stages: piece_select, move, dir_sel, attack
selected_piece = None

pygame.init()

while done == False:
    while gameover == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                gameover = True
            turn = gs.currentTurn
            if event.type == pygame.MOUSEBUTTONUP:
              x,y = pygame.mouse.get_pos()
              clickx = x/(3*screenw/cols/4)
              if clickx % 2 == 0:
                click = (clickx, y/(screenh/rows*2)*2)
              else:
                click = (clickx, (y-screenh/rows/2)/(screenh/rows*2)*2+1)
              
              if turn_stage == 'piece_sel':
                piece = gs.getPiece(click[0],click[1])
                if piece != None and gs.currentTurn == piece.player:
                  selected_piece = piece
                  turn_stage = 'move'
                else: 
                  selected_piece = None
                  turn_stage = 'piece_sel'
              elif turn_stage == 'move':
                if selected_piece.isValidMove(click[0],click[1]):
                  selected_piece.moveTo(click[0],click[1])
                  turn_stage = 'dir_sel'
              elif turn_stage == 'dir_sel':
                dirs = [(selected_piece.x, selected_piece.y-2),
                        (selected_piece.x+1, selected_piece.y-1),
                        (selected_piece.x+1, selected_piece.y+1),
                        (selected_piece.x, selected_piece.y+2),
                        (selected_piece.x-1, selected_piece.y+1),
                        (selected_piece.x-1, selected_piece.y-1)]
                if (click[0],click[1]) in dirs: 
                  new_dir = dirs.index((click[0],click[1]))
                  selected_piece.direction = new_dir
                  if selected_piece.getValidAttacks() != []:
                      turn_stage = 'attack'
                  else:
                      gs.toggleTurn()
                      selected_piece = None
                      turn_stage = 'piece_sel'
              elif turn_stage == 'attack':
                if selected_piece.getValidAttacks() != []:
                  if selected_piece.isValidAttack(click[0],click[1]):
                    target = gs.getPiece(click[0],click[1])
                    selected_piece.attack(target)
                gs.toggleTurn()
                selected_piece = None
                turn_stage = 'piece_sel'  
                  
            
        if selected_piece != None and turn_stage == 'move': 
          valid_moves = selected_piece.getValidMoves()
        else: valid_moves = []

        gs.player1.clearDeadPieces()
        gs.player2.clearDeadPieces()
        for i in spaces:
          loc = (i.x,i.y)
          if loc in valid_moves: 
            i.highlighted = True
          else: i.highlighted = False
          i.update(gs.getPiece(i.x,i.y))
        #button.draw(b.image)
        spaces.draw(b.image)
        board.draw(screen)

        for i in spaces:
            if i.piece!=None:
                i.health = font.render(str(i.piece.remainingHealth),True,white)
                if i.piece.player==1:
                    screen.blit(i.health,[i.xpos+1.5*i.x3,i.ypos+i.y3])
                else:
                    screen.blit(i.health,[i.xpos+1.5*i.x3,i.ypos+4.5*i.y3])                    
        pygame.display.flip()

pygame.quit()
