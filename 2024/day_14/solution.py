"""
Restroom Redoubt

https://adventofcode.com/2024/day/14
"""
import re


def parse(data):
    robots = []
    for line in data.strip().split("\n"):
        robots.append(list(map(int, re.findall(r"-?\d+", line))))
    return robots


def solve(data, xmax, ymax, steps=100):
    quadrants = [[0, 0], [0, 0]]
    robots = parse(data)
    xmid, ymid = xmax // 2, ymax // 2
    for x, y, dx, dy in robots:
        x = (x + dx * steps) % xmax
        y = (y + dy * steps) % ymax
        if x == xmid or y == ymid:
            continue  # ignore middle
        quadrants[x > xmid][y > ymid] += 1

    print(quadrants)
    return quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]


def draw(robots):
    m = [[0] * 101 for _ in range(103)]
    for x, y, _, _ in robots:
        m[y][x] += 1
    print("\n".join("".join(["." if c == 0 else str(c) for c in row]) for row in m))
    print()


def solve2(data, xmax=101, ymax=103):
    robots = parse(data)
    seconds = 0
    while True:
        seconds += 1
        for i, (x, y, dx, dy) in enumerate(robots):
            x = (x + dx) % xmax
            y = (y + dy) % ymax
            robots[i] = (x, y, dx, dy)
        if seconds % 103 == 33 and seconds % 101 == 68:
            print(seconds)
            draw(robots)
            break


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data, 101, 103)
    print(f"Example 1: {result}")

    solve2(input_data)
