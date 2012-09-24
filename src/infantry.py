import helper
from piece import Piece

class Infantry(Piece):
    def __init__(self, x, y, dir):
        Piece.__init__(self, x, y, dir)
        self.attackPower = 1
        self.remainingHealth = 3
        self.maxHealth = 3

    def getValidMoves(self):
        li = [ # Static list is easy
            (self.x, self.y+2),
            (self.x, self.y-2),
            (self.x-1, self.y-1),
            (self.x-1, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y+1)
        ]

        return filterValidSpots(li, Piece.getState().getWidth(), Piece.getState().getHeight())

    def getValidAttacks(self):
        pass