from helper import *
from piece import Piece

class Infantry(Piece):
    def __init__(self, player, x, y, dir):
        Piece.__init__(self, player, x, y, dir, 1, 3, "i")
        self.imageFile = "../res/tiles/infantry_p" + str(self.player) + "_h"

    def attack(self, piece):
        power = self.attackPower

        # Back attack
        # first, calculate attack dir.
        # Then, if attack dir is within one of piece's dir, back attack
        ret = [ # Static list is easy.  Keep this sorted in order by direction
            (self.x, self.y-2),   # 0
            (self.x+1, self.y-1), # 1
            (self.x+1, self.y+1), # 2
            (self.x, self.y+2),   # 3
            (self.x-1, self.y+1), # 4
            (self.x-1, self.y-1)  # 5
        ]
        attackDir = ret.index((piece.x, piece.y))
        if attackDir == piece.direction \
        or (attackDir+1)%6 == piece.direction \
        or (attackDir-1)%6 == piece.direction:
            power *= 2

        piece.loseHealth(power)

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

        # Get current dir + other two adjacent ones
        ret = [ret[self.direction],
            ret[(self.direction+1)%6],
            ret[(self.direction-1)%6]]

        # Filter to only spots on board and that are blocked
        ret = filterValidSpots(ret, Piece.getState().getWidth(), Piece.getState().getHeight())
        ret = filterUnblockedSpots(ret, Piece.getState())
        ret = filterMyPieces(ret, Piece.getState(), self.player)

        # NOTE: Currently possible to attack your own troops
        
        return ret
