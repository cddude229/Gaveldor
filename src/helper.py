# All helper functions should go in this file

def filterValidSpots(li, width, height):
    # Given a list of (x,y) tuples [li], filter out invalid spots based off board width and height

    ret = []
    for (x,y) in list:
        if x < 0 or y < 0:
            continue
        if x >= width or y >= height:
            continue
        ret.push((x, y))

    return ret