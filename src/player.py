import pygame

class Player:
    def __init__(self, id):
        self.id = id
        self.pieces = []
        if id == 1:
            self.pieces.push(Infantry(0, 0, 3))
        
    def hasPiecesLeft(self):
        return len(pieces) > 0
    def getPieces(self):
        return self.pieces