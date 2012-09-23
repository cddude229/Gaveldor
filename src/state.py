class State:
    pieces = [[]]
    terrain = [[]]
    gameStatus = 0 # 0 = playing, 1,2 = who won, 3 = stalemate
    currentTurn = 1 # Whose turn is it?

    def __init__(this, width, height):
    	# Takes in the board width, height so arrays can be built

    	this.pieces  = [ [ None for y in xrange(height) ] for x in xrange(width) ]
    	this.terrain = [ [ (None, "water") [ (x+y)%2 ] for y in xrange(height) ] for x in xrange(width) ]

    	"""
    	Board squares invariants:
    		1) Valid squares always have an even sum for their coordinates
			2) Invalid squares will be "water" terrain (impassable to all)
    	"""

    def getPiece(this, x, y):
    	# Determine which piece (if any) exists at (x, y)
        if x < 0 or y < 0: # Make sure in bounds
            return None

        if x >= len(this.pieces) or y >= len(this.pieces[0]): # Make sure in bounds, again
            return None

        return this.pieces[x][y]

    def getTerrain(this, x, y):
    	# Determine which terrain type (if any) exists at (x, y)
        if x < 0 or y < 0:
            return "water"

        if x >= len(this.terrain) or y >= len(this.terrain[0]):
            return "water"

        return this.terrain[x][y]