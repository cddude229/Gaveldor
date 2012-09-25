from helper import *
from piece import Piece

class Archer(Piece):
    def __init__(self, player, x, y, dir):
        Piece.__init__(self, player, x, y, dir, 1, 2, "a")
        self.imageFile = "../res/tiles/archer_" + str(self.player) + ".png"

    def attack(self, piece):
        power = self.attackPower

        # If opposing piece is cavalry, we do 2x damage
        if piece.type == "c":
            power *= 2

        # Need to implement back attack

        piece.loseHealth(power)

    def getValidMoves(self):
        ret = [
            # One space away
            (self.x, self.y+2),
            (self.x, self.y-2),
            (self.x-1, self.y-1),
            (self.x-1, self.y+1),
            (self.x+1, self.y-1),
            (self.x+1, self.y+1)
        ]

        ret = filterValidSpots(ret, Piece.getState().getWidth(), Piece.getState().getHeight())
        ret = filterBlockedSpots(ret, Piece.getState())
        ret.append((self.x, self.y))
        return ret

    def getValidAttacks(self):
        ret = [ # Static list is easy.  Keep this sorted in order by direction
            (self.x, self.y-2),   # 0
            (self.x+1, self.y-1), # 1
            (self.x+1, self.y+1), # 2
            (self.x, self.y+2),   # 3
            (self.x-1, self.y+1), # 4
            (self.x-1, self.y-1)  # 5
        ]

        ret2 = [
            # Two spaces away
            (self.x, self.y-4),   # 0
            (self.x+1, self.y+3), # 0.5
            (self.x+2, self.y-2), # 1
            (self.x+2, self.y),   # 1.5
            (self.x+2, self.y+2), # 2
            (self.x+1, self.y-3), # 2.5
            (self.x, self.y+4),   # 3
            (self.x-2, self.y),   # 3.5
            (self.x-2, self.y+2), # 4
            (self.x-1, self.y-3), # 4.5
            (self.x-2, self.y-2), # 5
            (self.x-1, self.y+3)  # 5.5
        ]

        # Get current dir + other two adjacent ones
        ret = [
            # One square away
            ret[self.direction],
            ret[(self.direction+1)%6],
            ret[(self.direction-1)%6],

            # Two squares away
            ret2[self.direction*2],
            ret2[(self.direction*2+1)%12],
            ret2[(self.direction*2+2)%12],
            ret2[(self.direction*2-1)%12],
            ret2[(self.direction*2-2)%12],
        ]

        # Filter to only spots on board and that are blocked
        ret = filterValidSpots(ret, Piece.getState().getWidth(), Piece.getState().getHeight())
        ret = filterUnblockedSpots(ret, Piece.getState())
        ret = filterMyPieces(ret, Piece.getState(), self.player)

        # NOTE: Currently possible to attack your own troops
        
        return ret
