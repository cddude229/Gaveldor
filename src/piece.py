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
        return (x, y) in self.getValidMoves()
    def getValidMoves(self):
        pass
    def getValidAttacks(self):
        pass
    def loseHealth(self, health):
        self.remainingHealth -= health
        if self.remainingHealth < 0:
            self.remainingHealth = 0
    def isAlive(self):
        return self.remainingHealth > 0
    def moveTo(self,x,y):
        # Does not need to validate the move
        self.x = x
        self.y = y