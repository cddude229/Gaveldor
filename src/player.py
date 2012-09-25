from infantry import Infantry
from cavalry import Cavalry
from archer import Archer

class Player:
    def __init__(self, id):
        self.id = id
        self.pieces = []
        if id == 1:
            self.pieces.append(Infantry(1, 3, 1, 3))
            self.pieces.append(Infantry(1, 2, 0, 3))
            self.pieces.append(Infantry(1, 4, 0, 3))
            self.pieces.append(Cavalry(1, 5, 1, 3))
            self.pieces.append(Cavalry(1, 1, 1, 3))
            self.pieces.append(Archer(1, 6, 0, 3))
            self.pieces.append(Archer(1, 0, 0, 3))
        if id == 2:
            self.pieces.append(Infantry(2, 3, 9, 0))
            self.pieces.append(Infantry(2, 2, 10, 0))
            self.pieces.append(Infantry(2, 4, 10, 0))
            self.pieces.append(Cavalry(2, 5, 9, 0))
            self.pieces.append(Cavalry(2, 1, 9, 0))
            self.pieces.append(Archer(2, 6, 10, 0))
            self.pieces.append(Archer(2, 0, 10, 0))
        
    def hasPiecesLeft(self):
        return len(self.pieces) > 0

    def getPieces(self):
        return self.pieces

    def clearDeadPieces(self):
        ret = []

        for piece in self.pieces:
            if piece.isAlive() == True:
                ret.append(piece)

        self.pieces = ret
