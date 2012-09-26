from player import Player

class State:
    """
    Board squares invariants:
        1) Valid squares always have an even sum for their coordinates
        2) Invalid squares will be "water" terrain (impassable to all)
    """
    terrain = [[]] # 2D map of the terrain at place x, y

    gameStatus = 0 # 0 = playing, 1,2 = who won, 3 = stalemate
    currentTurn = 1 # Whose turn is it?

    player1 = None
    player2 = None

    width = 0
    height = 0

    def __init__(self, width, height):
        # Takes in the board width, height so arrays can be built

        self.terrain = [ [ (None, "water") [ (x+y)%2 ] for y in xrange(height) ] for x in xrange(width) ]

        self.player1 = Player(1)
        self.player2 = Player(2)

        self.width = width
        self.height = height

    def toggleTurn(self):
      if self.currentTurn == 1: self.currentTurn = 2
      else: self.currentTurn = 1

    def getStatus(self):
      if self.player1.hasPiecesLeft() == 0: return 2
      if self.player2.hasPiecesLeft() == 0: return 1
      return 0

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getPiece(self, x, y):
        # Determine which piece (if any) exists at (x, y)
        for piece in self.getAllPieces():
            if piece.x == x and piece.y == y:
                return piece

        return None

    def getAllPieces(self):
        return self.getPlayer(1).getPieces() + self.getPlayer(2).getPieces()

    def getTerrain(self, x, y):
        # Determine which terrain type (if any) exists at (x, y)
        if x < 0 or y < 0:
            return "water"

        if x >= len(self.terrain) or y >= len(self.terrain[0]):
            return "water"

        return self.terrain[x][y]

    def getPlayer(self, id):
        if id == 1:
            return self.player1
        return self.player2
