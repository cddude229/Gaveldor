import pygame
import pygame.mixer
from board import *
from state import State
from piece import Piece

screenw = 900
screenh = 640

cols=7
rows=11

moveCounter=0;

screen = pygame.display.set_mode([screenw-screenw/4+32,screenh+screenh/rows+100])
pygame.display.set_caption('Gaveldor')

pygame.init()
pygame.mixer.init()

font = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
attack = False

board = pygame.sprite.RenderPlain()
b = Board(screenw,screenh,cols,rows)
board.add(b)

def new_game():
  global gs,spaces,game_begun,done,gameover, \
          turn_stage,selected_piece,hover_piece, \
          attackable_pieces,credits_showing,rules_showing, \
          paused
  gs = State(cols,rows)
  Piece.setState(gs)

  spaces = pygame.sprite.RenderPlain()
  #sets up board
  for i in xrange(cols):
      for j in xrange(rows/2+1):
          if i%2==0:
              s=Space(screenw,screenh,cols,rows,i*screenw/cols-i*screenw/cols/4,2*j*screenh/rows+50,i,j*2)
          else:
              if j < rows/2:
                s=Space(screenw,screenh,cols,rows,i*screenw/cols-i*screenw/cols/4,2*int((j+.5)*screenh/rows)+50,i,j*2+1)
          spaces.add(s)

  game_begun = False
  done = False
  gameover = False
  credits_showing = False
  rules_showing = False
  paused = False

  # stages: piece_select, move, dir_sel, attack
  turn_stage = 'piece_sel'  
  selected_piece = None
  hover_piece = None
  attackable_pieces = []

new_game()
click_sound = pygame.mixer.Sound('../res/sounds/click.wav')
attack_sound = pygame.mixer.Sound('../res/sounds/sword.wav')

while done == False:
    while gameover == False:
        attackable_pieces = []
        if turn_stage == 'attack' and selected_piece != None:
          valid_attacks = selected_piece.getValidAttacks()
          if valid_attacks != []:
            for attack in valid_attacks:
              attackable_pieces.append(attack)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                gameover = True
            turn = gs.currentTurn

            if paused:
              if event.type == pygame.MOUSEBUTTONUP:
                paused = False
              continue

            if game_begun:
              x,y = pygame.mouse.get_pos()
              y -= 50
              hoverx = x/(3*screenw/cols/4)
              if hoverx % 2 == 0: hover = (hoverx, y/(screenh/rows*2)*2)
              else: hover = (hoverx, (y-screenh/rows/2)/(screenh/rows*2)*2+1)
              piece = gs.getPiece(hover[0],hover[1])
              if turn_stage == 'piece_sel':
                if piece != None and gs.currentTurn == piece.player:
                  hover_piece = piece
                else: hover_piece = None
                  
            if event.type == pygame.MOUSEBUTTONUP:
              x,y = pygame.mouse.get_pos()
              y -= 50
              if game_begun == False: 
                if y >= screenh+screenh/rows: 
                  if credits_showing: credits_showing = False
                  elif rules_showing: rules_showing = False
                  else:
                    if x < 236: rules_showing = True
                    elif x > 492: credits_showing = True
                    else:
                      screen.fill(black)
                      game_begun = True
                continue
              if game_status != 0 and y > screenh+screenh/rows+50:
                new_game()
              if y >= screenh+screenh/rows:
                if x < 289:
                  gs.toggleTurn()
                  selected_piece = None
                  turn_stage = 'piece_sel'
                  moveCounter = 0
                  continue
                elif x > 418:
                  # cancel turn
                  pass
                else: 
                  # pause menu
                  paused = True
              clickx = x/(3*screenw/cols/4)
              if clickx % 2 == 0:
                click = (clickx, y/(screenh/rows*2)*2)
              else:
                click = (clickx, (y-screenh/rows/2)/(screenh/rows*2)*2+1)
              
              if turn_stage == 'piece_sel':
                piece = gs.getPiece(click[0],click[1])
                if piece != None and gs.currentTurn == piece.player:
                  click_sound.play()
                  selected_piece = piece
                  turn_stage = 'move'
                else: 
                  selected_piece = None
                  turn_stage = 'piece_sel'
              elif turn_stage == 'move':
                if selected_piece.isValidMove(click[0],click[1]):
                  click_sound.play()
                  selected_piece.moveTo(click[0],click[1])
                  turn_stage = 'dir_sel'
                else:
                  selected_piece = None
                  turn_stage = 'piece_sel'
              elif turn_stage == 'dir_sel':
                dirs = [(selected_piece.x, selected_piece.y-2),
                        (selected_piece.x+1, selected_piece.y-1),
                        (selected_piece.x+1, selected_piece.y+1),
                        (selected_piece.x, selected_piece.y+2),
                        (selected_piece.x-1, selected_piece.y+1),
                        (selected_piece.x-1, selected_piece.y-1)]
                if (click[0],click[1]) in dirs or (click[0],click[1]) == \
                        (selected_piece.x, selected_piece.y): 
                  if (click[0],click[1]) != (selected_piece.x, selected_piece.y):
                    new_dir = dirs.index((click[0],click[1]))
                    selected_piece.direction = new_dir
                  for i in spaces: i.dir_sel = False
                  click_sound.play()
                  valid_attacks = selected_piece.getValidAttacks()
                  if valid_attacks != []:
                    turn_stage = 'attack'
                  else:
                      moveCounter+=1
                      if moveCounter==3:
                          gs.toggleTurn()
                          moveCounter=0
                      selected_piece = None
                      turn_stage = 'piece_sel'
              elif turn_stage == 'attack':
                valid_attacks = selected_piece.getValidAttacks()
                if valid_attacks != []:
                  if selected_piece.isValidAttack(click[0],click[1]): 
                    target = gs.getPiece(click[0],click[1])
                    selected_piece.attack(target)
                    attack_sound.play()
                moveCounter+=1
                if moveCounter==3:
                    gs.toggleTurn()
                    moveCounter=0
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
          i.dir_sel = False
          if selected_piece != None and loc == (selected_piece.x, selected_piece.y):
            if turn_stage == 'dir_sel': i.dir_sel = True
          i.update(gs.getPiece(i.x,i.y))
        spaces.draw(b.image)
        board.draw(screen)

        for i in spaces:
          loc = (i.x, i.y)
          if hover_piece != None and  loc == (hover_piece.x, hover_piece.y):
            hover_overlay = pygame.image.load('../res/tiles/hover.png').convert_alpha()
            hover_overlay = pygame.transform.smoothscale(hover_overlay, (screenw/cols, screenh/rows*2))
            hover_overlay = pygame.transform.rotate(hover_overlay, -60 * hover_piece.direction)
            screen.blit(hover_overlay, i.rect.topleft)
          for attack in attackable_pieces:
            if loc == attack:
              attack_overlay = pygame.image.load('../res/tiles/attackable.png').convert_alpha()
              attack_overlay = pygame.transform.smoothscale(attack_overlay, (screenw/cols, screenh/rows*2))
              screen.blit(attack_overlay, i.rect.topleft)

        for i in spaces:
          if i.dir_sel:
            arrow_img = pygame.image.load('../res/tiles/arrows.png').convert_alpha()
            screen.blit(arrow_img,[i.xpos-80,i.ypos-65])

        # bottom row menu bar
        menu_bar = pygame.image.load('../res/tiles/menu_bar.png').convert_alpha()
        screen.blit(menu_bar, (0, screenh+screenh/rows+50))

        # top row menu bar
        info_bar = pygame.image.load('../res/tiles/info_bar.png').convert_alpha()
        screen.blit(info_bar, (0,0))

        # turn indicator
        player_tile_to_load = '../res/tiles/player_' + str(gs.currentTurn) + '.png'
        player_tile = pygame.image.load(player_tile_to_load).convert_alpha()
        screen.blit(player_tile, (0,0))

        # turn stage indicator
        turn_tile = pygame.image.load('../res/tiles/' + str(turn_stage) + '.png').convert_alpha()
        screen.blit(turn_tile, (150,0))

        # moves left indicator
        moves_left = '../res/tiles/moves_left_' + str(3-moveCounter) + '.png'
        moves_tile = pygame.image.load(moves_left).convert_alpha()
        screen.blit(moves_tile, (357, 0))

        # selected piece info
        if selected_piece != None:
          if selected_piece.type == 'a':
            piece_info = '../res/tiles/archer_info.png'
          elif selected_piece.type == 'c':
            piece_info = '../res/tiles/cavalry_info.png'
          elif selected_piece.type == 'i':
            piece_info = '../res/tiles/infantry_info.png'
          piece_info_tile = pygame.image.load(piece_info).convert_alpha()
          screen.blit(piece_info_tile, (432, 0))

        if game_begun == False:
          if credits_showing: image = '../res/tiles/credits.png'
          elif rules_showing: image = '../res/tiles/rules.png'
          else: image = '../res/tiles/splash.png'
          splash = pygame.image.load(image).convert_alpha()
          screen.blit(splash, (0,0))

        if paused:
          menu = pygame.image.load('../res/tiles/pause.png').convert_alpha()
          screen.blit(menu, (0,0))

        game_status = gs.getStatus()
        if game_begun:
          if game_status == 1:  
            splash = pygame.image.load('../res/tiles/player_1_wins.png').convert_alpha()
            screen.blit(splash, (0,0))
          elif game_status == 2:
            splash = pygame.image.load('../res/tiles/player_2_wins.png').convert_alpha()
            screen.blit(splash, (0,0))
          elif game_status == 3:
            #stalemate
            pass

        pygame.display.flip()

pygame.quit()
