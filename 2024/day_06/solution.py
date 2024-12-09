"""
Day 6: Guard Gallivant

https://adventofcode.com/2024/day/6
"""

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse(data):
    area = data.strip().split("\n")
    for y, row in enumerate(area):
        if "^" in row:
            x = row.find("^")
            area[y] = row.replace("^", ".")
            break
    return area, y, x

def walk(area, y, x):
    cyclecheck = set()
    visited = set()
    direction = 0
    cycle = False
    while True:
        visited.add((y, x))
        cyclecheck.add((y, x, direction))

        dy, dx = DIRECTIONS[direction]
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= len(area) or nx >= len(area[0]):
            break
        if (ny, nx, direction) in cyclecheck:
            cycle = True
            break
        if area[ny][nx] != ".":
            direction = (direction + 1) % 4
        else:
            y, x = ny, nx
    return len(visited), cycle

def solve(data):
    return walk(*parse(data))[0]


def solve2(data):
    result = 0
    area, ystart, xstart = parse(data)
    for y, row in enumerate(area):
        print(y)       
        for x, _ in enumerate(row):
            a = area[:]
            a[y] = a[y][:x] + "#" + a[y][x+1:]  # "..#.." + "#" + "...#"
            r, cycle = walk(a, ystart, xstart)
            if cycle:
                result += 1
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
