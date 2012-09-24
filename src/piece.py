class Piece:
    state = None
    def __init__(self, x, y, dir):
        self.attackPower = None
        self.remainingHealth = None
        self.maxHealth = None
        self.imageFile = ""
        self.direction = dir
        self.x = x
        self.y = y

    def isValidMove(self, x, y):
        return (x, y) in self.getValidMoves()

    def getValidMoves(self):
        pass # Implemented at next level

    def getValidAttacks(self):
        pass # Implemented at next level

    def loseHealth(self, health):
        self.remainingHealth -= health
        if self.remainingHealth < 0:
            self.remainingHealth = 0

    def isAlive(self):
        return self.remainingHealth > 0

    def moveTo(self, x, y):
        # Does not need to validate the move
        self.x = x
        self.y = y

    def faceDirection(self, dir):
        self.direction = dir % 5

    @staticmethod
    def getState(): # Static
        return Piece.state

    @staticmethod
    def setState(state): # Static
        Piece.state = state