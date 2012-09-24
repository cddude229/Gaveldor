class Piece:
    state = None
    def __init__(self, player, x, y, dir, attackPower, startingHP, type):
        self.player = player
        self.attackPower = attackPower
        self.remainingHealth = startingHP
        self.maxHealth = startingHP
        self.imageFile = ""
        self.direction = dir
        self.x = x
        self.y = y
        self.type = type # "a" "c" "i" for archer, cavalry, infantry (respectively)

    def isValidMove(self, x, y):
        return (x, y) in self.getValidMoves()

    def isValidAttack(self, x, y):
        return (x, y) in self.getValidAttacks()

    def getValidMoves(self):
        pass # Implemented at next level

    def getValidAttacks(self):
        pass # Implemented at next level

    def attack(self, piece):
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
        self.direction = dir % 6

    def getPlayer(self):
        return Piece.getState().getPlayer(self.player)

    @staticmethod
    def getState():
        return Piece.state

    @staticmethod
    def setState(state):
        Piece.state = state
