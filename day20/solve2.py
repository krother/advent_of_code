
import re
import numpy as np
from itertools import product

fn = 'input_big.txt'
#fn = 'input.txt'

def parse(fn):
    data = {}
    r = open(fn).read()
    for tile in r.split('Tile')[1:]:
        number, t = tile.split(':')
        number = int(number.strip())
        t = t.strip().replace('#', '1').replace('.','0')
        t = [[int(c) for c in row.strip()] for row in t.split('\n')]
        data[number] = np.array(t, np.uint8)
    return data


def get_borders(p):
    """return borders"""
    bord = {}
    for num, tile in p.items():
        borders = [
            tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1],
            tile[0, :][::-1], tile[-1, :][::-1], tile[:, 0][::-1], tile[:, -1][::-1],
        ]
        bord[num] = borders
    return bord

def match_borders(p, bord):
    """return {num1: [num2, num3,..]}"""
    matches = {k: [] for k in p}
    for (num, borders), (num2, borders2) in product(bord.items(), bord.items()):
        if num == num2: continue # no matches with itself
        for b1, b2 in product(borders, borders2[:4]):
            assert b1.shape == (10,)
            if (b1 - b2).sum() == 0:
                matches[num].append(num2)
    return matches

def find_corners(matches):
    corners = []
    for k, i in matches.items():
        if len(i) == 2:
            corners.append(k)
    assert len(corners) == 4            
    return corners

def get_orientations(tile):
    """return all possible orientations"""
    yield tile
    yield tile[::-1]  # upside-down
    yield tile[:, ::-1]
    yield tile[::-1, ::-1]
    tile = tile.T
    yield tile
    yield tile[::-1]
    yield tile[:, ::-1]
    yield tile[::-1, ::-1]
    
#def solve(fn):
p = parse(fn)
bord = get_borders(p)
matches = match_borders(p, bord)
corners = find_corners(matches)

size = round(len(p) ** 0.5)
puzzle = np.zeros((8*size, 8*size), np.uint8)

def assemble():
    # insert first corner
    remaining = list(p.keys())
    c = corners[0]
    remaining.remove(c)
    
    # LUCKY SHOT, ALSO TRY INVERSE
    cornertile = p[c][::-1]  # test
    if 'big' in fn:
        cornertile = p[c][::-1, ::-1]  # pred
    
    puzzle[:8, :8] = cornertile[1:-1, 1:-1]
    top = cornertile[-1, :]
    left = cornertile[:, -1]
    
    # ASSUME THERE IS EXACTLY ONE MATCH FOR EACH POSITION
    for y, x in product(range(size), range(size)):
        if x == 0 and y == 0:
            continue
        if x > 0:
            # match left side
            found = False
            for r in remaining:
                for ori in get_orientations(p[r]):
                    if (ori[:, 0] - left).sum() == 0:
                        # match found
                        print(f'insert tile {r} at {x}/{y}')
                        tile = ori[1:-1, 1:-1]
                        puzzle[y*8:(y+1)*8, x*8:(x+1)*8] = tile
                        left = ori[:, -1]
                        remaining.remove(r)
                        found = True
                        break
                if found:
                    break
        if y > 0 and x == 0:
            # match top side
            found = False
            for r in remaining:
                for ori in get_orientations(p[r]):
                    if (ori[0, :] - top).sum() == 0:
                        # match found
                        print(f'insert tile {r} at {x}/{y}')
                        tile = ori[1:-1, 1:-1]
                        puzzle[y*8:(y+1)*8, x*8:(x+1)*8] = tile
                        top = ori[-1, :]
                        left = ori[:, -1]
                        remaining.remove(r)
                        found = True
                        break
                if found:
                    break
    
    assert len(remaining) == 0
    return puzzle

puzzle = assemble()

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster = monster.replace('#', '1').replace(' ','0')
monster = np.array([[int(c) for c in row.strip()] for row in monster.split('\n')], dtype=np.uint8)
npix = monster.sum()

if fn == 'input.txt':
    puzzle = puzzle.T
if fn == 'input_big.txt':
    puzzle = puzzle.T
    
MX, MY = 20, 3
for y, x in product(range(puzzle.shape[0]-MY+1), range(puzzle.shape[1]-MX+1)):
    part = puzzle[y:y+MY, x:x+MX]
    if (part & monster).sum() == npix:
        print(f'monster found at {x}/{y}')
        puzzle[y:y+MY, x:x+MX] -= monster

print(puzzle.sum())

#from PIL import Image
#im = Image.fromarray(puzzle*255)
#im.resize((480, 480), resample=Image.BOX)
#im.resize((96*5, 96*5), resample=Image.BOX)

#print(solve('input_big.txt'))
