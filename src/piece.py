import pygame

class Piece:
    def __init__(self):
        self.attackPower = None
        self.remainingHealth = None
        self.maxHealth = None
        self.direction = None
        self.x = None
        self.y = None
        pass
    def isValidMove(self,x,y):
        pass
    def getValidMoves(self):
        pass
    def getValidAttacks(self):
        pass
    def loseHealth(self, health):
        pass
    def isAlive(self):
        pass
    def moveTo(self,x,y):
        pass