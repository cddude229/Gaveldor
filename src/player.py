import pygame

class Player:
    def __init__(self, id):
        self.id = id
        self.pieces = []
    def hasPiecesLeft(self):
        return len(pieces) > 0
    def getPieces(self):
        return self.pieces