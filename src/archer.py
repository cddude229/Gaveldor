from helper import *
from piece import Piece

class Archer(Piece):
    def __init__(self, player, x, y, dir):
        Piece.__init__(self, player, x, y, dir, 1, 2, "a")
        self.imageFile = "../res/tiles/archer_p" + str(self.player) + "_h"

    def attack(self, piece):
        power = self.attackPower

        # If opposing piece is cavalry, we do 2x damage
        if piece.type == "c":
            power *= 2

        if abs(self.x-piece.x) + abs(self.y-piece.y) == 2:
            # Only one spot away, use old algo...
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
        else:
            # attacking two spots away

            # First, determine the angle from among these:
            ret2 = [
                # Two spaces away
                (self.x, self.y-4),   # 0
                (self.x+1, self.y-3), # 0.5
                (self.x+2, self.y-2), # 1
                (self.x+2, self.y),   # 1.5
                (self.x+2, self.y+2), # 2
                (self.x+1, self.y+3), # 2.5
                (self.x, self.y+4),   # 3
                (self.x-1, self.y+3),   # 3.5
                (self.x-2, self.y+2), # 4
                (self.x-2, self.y), # 4.5
                (self.x-2, self.y-2), # 5
                (self.x-1, self.y-3)  # 5.5
            ]

            angle = ret2.index((piece.x, piece.y))

            # Now that we have the angle, if divisble by two, it's 0,1,2,3,4,5 (on the normal clock)
            # so, that means use the old system again
            if angle % 2 == 0:
                # first, calculate attack dir.
                # Then, if attack dir is within one of piece's dir, back attack
                ret = [ # Static list is easy.  Keep this sorted in order by direction
                    (self.x, self.y-4),   # 0
                    (self.x+2, self.y-2), # 1
                    (self.x+2, self.y+2), # 2
                    (self.x, self.y+4),   # 3
                    (self.x-2, self.y+2), # 4
                    (self.x-2, self.y-2)  # 5
                ]
                attackDir = ret.index((piece.x, piece.y))
                if attackDir == piece.direction \
                or (attackDir+1)%6 == piece.direction \
                or (attackDir-1)%6 == piece.direction:
                    power *= 2
            else :
                # On a half angle... get the piece's back spots.
                # If angle-1 or angle+1 is in those spots, do x2

                ret = [
                    (piece.x, piece.y-2),   # 0
                    (piece.x+1, piece.y-1), # 1
                    (piece.x+1, piece.y+1), # 2
                    (piece.x, piece.y+2),   # 3
                    (piece.x-1, piece.y+1), # 4
                    (piece.x-1, piece.y-1)  # 5
                ]

                back = [
                    ret[(piece.direction+3)%6],
                    ret[(piece.direction+4)%6],
                    ret[(piece.direction-2)%6]
                ]

                ret3 = [
                    # Two spaces away
                    (self.x, self.y-2),   # 0
                    (self.x+1, self.y-3), # 0.5
                    (self.x+1, self.y-1), # 1
                    (self.x+2, self.y),   # 1.5
                    (self.x+1, self.y+1), # 2
                    (self.x+1, self.y+3), # 2.5
                    (self.x, self.y+2),   # 3
                    (self.x-1, self.y+3),   # 3.5
                    (self.x-1, self.y+1), # 4
                    (self.x-2, self.y), # 4.5
                    (self.x-1, self.y-1), # 5
                    (self.x-1, self.y-3)  # 5.5
                ]

                if ret3[(angle-1)%12] in back or ret3[(angle+1)%12] in back:
                    power *= 2

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
            (self.x+1, self.y-3), # 0.5
            (self.x+2, self.y-2), # 1
            (self.x+2, self.y),   # 1.5
            (self.x+2, self.y+2), # 2
            (self.x+1, self.y+3), # 2.5
            (self.x, self.y+4),   # 3
            (self.x-1, self.y+3),   # 3.5
            (self.x-2, self.y+2), # 4
            (self.x-2, self.y), # 4.5
            (self.x-2, self.y-2), # 5
            (self.x-1, self.y-3)  # 5.5
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
