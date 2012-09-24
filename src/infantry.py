import helper
from piece import Piece

class Infantry(Piece):
    def __init__(self):
        self.attackPower = None
        self.remainingHealth = None
        self.maxHealth = None
        self.direction = None
        self.x = None
        self.y = None
        pass
    def getValidMoves(self):
        li = [
            (self.x, self.y+2),
            (self.x, self.y-2),
            (self.x-1, self.y-1),
            (self.x-1, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y+1)
        ]

        return filterValidSpots(li, self.getState().getWidth(), self.getState().getHeight())
    def getValidAttacks(self):
        pass