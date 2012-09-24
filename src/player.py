from infantry import Infantry

class Player:
    def __init__(self, id):
        self.id = id
        self.pieces = []
        if id == 1:
            self.pieces.append(Infantry('a', 3, 1, 3))
        if id == 2:
            self.pieces.append(Infantry('b', 3, 9, 0))
        
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
