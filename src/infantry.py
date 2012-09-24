import helper
from helper import *
from piece import Piece

class Infantry(Piece):
    def __init__(self, x, y, dir):
        Piece.__init__(self, x, y, dir)
        self.attackPower = 1
        self.remainingHealth = 3
        self.maxHealth = 3
        self.imageFile = "infantry.png"

    def getValidMoves(self):
        ret = [ # Static list is easy
            (self.x, self.y+2),
            (self.x, self.y-2),
            (self.x-1, self.y-1),
            (self.x-1, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y+1)
        ]

        ret = filterValidSpots(ret, Piece.getState().getWidth(), Piece.getState().getHeight())
        ret = filterBlockedSpots(ret, Piece.getState())
        return ret

    def getValidAttacks(self):
        pass
