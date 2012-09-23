class State:
    pieces = [[]]
    terrain = [[]]
    gameStatus = 0 # 0 = playing, 1,2 = who won, 3 = stalemate
    currentTurn = 1 # Whose turn is it?

    def getPiece(x, y):
    	# Determine which piece (if any) exists at (x, y)
        if x < 0 or y < 0: # Make sure in bounds
            return None

        if x >= len(pieces) or y >= len(pieces[0]): # Make sure in bounds, again
            return None

        return pieces[x][y]

    def getTerrain(x, y):
    	# Determine which terrain type (if any) exists at (x, y)
        if x < 0 or y < 0:
            return "water"

        if x >= len(terrain) or y >= len(terrain[0]):
            return "water"

        return terrain[x][y]