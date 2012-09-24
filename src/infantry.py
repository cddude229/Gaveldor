from helper import *
from piece import Piece

class Infantry(Piece):
    def __init__(self, player, x, y, dir):
        Piece.__init__(self, player, x, y, dir)
        self.attackPower = 1
        self.remainingHealth = 3
        self.maxHealth = 3
        if self.player == 1: player_char = 'a'
        else: player_char = 'b'
        self.imageFile = "../res/tiles/infantry_" + player_char + ".png"

    def getValidMoves(self):
        ret = [ # Static list is easy
            (self.x, self.y+2),
            (self.x, self.y-2),
            (self.x-1, self.y-1),
            (self.x-1, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y+1)]

        ret = filterValidSpots(ret, Piece.getState().getWidth(), Piece.getState().getHeight())
        ret = filterBlockedSpots(ret, Piece.getState())
        return ret

    def getValidAttacks(self):
        ret = [ # Static list is easy
            (self.x, self.y+2),
            (self.x, self.y-2),
            (self.x-1, self.y-1),
            (self.x-1, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y+1)]

        # Get current dir + other two adjacent ones
        ret = [ret[self.direction],
            ret[(self.direction+1)%6],
            ret[(self.direction-1)%6]]

        # Filter to only spots on board and that are blocked
        ret = filterValidSpots(ret, Piece.getState().getWidth(), Piece.getState().getHeight())
        ret = filterUnblockedSpots(ret, Piece.getState())

        # NOTE: Currently possible to attack your own troops
        
        return ret

    def attack(self, p):
        p.loseHealth(self.attackPower)
