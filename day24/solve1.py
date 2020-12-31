
import re

data = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split('\n')

def read_tiles(data):
    tiles = {}
    for line in data:
        line = line.strip()
        directions = re.findall(r'e|se|sw|w|nw|ne', line)
        assert ''.join(directions) == line
        x, y = 0, 0
        for d in directions:
            if d == 'w':
                x -= 1
            elif d == 'e':
                x += 1
            elif d == 'sw':
                x -= 1
                y += 1
            elif d == 'se':
                y += 1
            elif d == 'nw':
                y -= 1
            elif d == 'ne':
                x += 1
                y -= 1
        tiles[(x, y)] = 1 - tiles.get((x, y), 0)
    return tiles

def solve(data):
    tiles = read_tiles(data)    
    total = sum([1 for pos in tiles if tiles[pos] == 1])
    return total


def get_neighbors(x, y):
    yield x-1, y
    yield x+1, y
    yield x-1, y+1
    yield x, y+1
    yield x, y-1
    yield x+1, y-1

def count_neighbors(tiles, x, y):
    count = 0
    for nx, ny in get_neighbors(x, y):
        if tiles.get((nx, ny), 0) == 1:
            count += 1
    return count

def life(tiles):
    """
    Any black tile with zero or more than 2 black tiles immediately adjacent
    to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent 
    to it is flipped to black.
    """
    # clear zero values
    for k in list(tiles):
        if tiles[k] == 0:
            del tiles[k]
    
    # calculate next generation
    new = {}
    for kx, ky in tiles:
        assert tiles[(kx, ky)] == 1
        for x, y in get_neighbors(kx, ky):
            if (x, y) not in new:
                nbcount = count_neighbors(tiles, x, y)
                if nbcount == 2:
                    new[(x, y)] = 1
        # black tiles
        nbcount = count_neighbors(tiles, kx, ky)
        if 0 < nbcount <= 2:
            new[(kx, ky)] = 1
            
    return new
    

assert solve(["e", "eew", "wweee", "senwe", "swene"]) == 1
assert solve(data) == 10

print(solve(open('input_big.txt'))) # 427
print()

tiles = read_tiles(data) # --> 2208
tiles = read_tiles(open('input_big.txt'))
for i in range(1, 101):
    tiles = life(tiles)
    if i <= 10 or i % 10 == 0:
        print(i, sum(tiles.values()))


