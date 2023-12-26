"""
Lavaduct Lagoon

https://adventofcode.com/2023/day/18
"""
import re
from pprint import pprint
from dataclasses import dataclass

HEXCODES = dict(zip(range(4), "RDLU"))

REVERSE = dict(zip("UDLR", "DURL"))
DUPLICATES = {"UU", "DD", "LL", "RR"}
CONVEX = ("URD", "RDL", "DLU", "LUR")  # for clockwise loop


def parse1(data):
    for line in data.strip().split("\n"):
        char, num = re.findall(r"^(\w) (\d+)", line)[0]
        yield char, int(num)


def parse2(data):
    for line in data.strip().split("\n"):
        num = int("0x" + line[-7:-2], 0)
        char = HEXCODES[int(line[-2])]
        yield char, num


def get_points(data, parse_func):
    x, y = 0, 0
    for char, num in parse_func(data):
        if char == "R":
            x += num
        elif char == "L":
            x -= num
        elif char == "U":
            y -= num
        elif char == "D":
            y += num
        yield x, y


def get_last_direction(queue):
    x1, y1 = queue[-2]
    x2, y2 = queue[-1]
    if x1 < x2:
        return "R"
    elif x1 > x2:
        return "L"
    elif y1 < y2:
        return "D"
    return "U"


def points_in_rect(points, top, bottom, left, right):
    for x, y in points:
        if x >= left and x <= right and y >= top and y <= bottom:
            return True
    return False


def remove_bulge(path, queue):
    points = queue[-4:]

    top = min(y for _, y in points)
    bottom = max(y for _, y in points)
    left = min(x for x, _ in points)
    right = max(x for x, _ in points)

    x1, y1 = points[0]
    x2, y2 = points[3]

    # check if the bulge is empty or if other points are in the way
    if (
        (path == "RDL" and points_in_rect(queue[:-4], top, bottom, max(x1, x2), right))
        or (
            path == "LUR" and points_in_rect(queue[:-4], top, bottom, left, min(x1, x2))
        )
        or (
            path == "DLU"
            and points_in_rect(queue[:-4], max(y1, y2), bottom, left, right)
        )
        or (path == "URD" and points_in_rect(queue[:-4], top, min(y1, y2), left, right))
    ):
        return 0

    # remove old points
    for _ in range(3):
        queue.pop()

    # add new points
    if path == "RDL":
        area = (bottom - top + 1) * (right - max(x1, x2))
        if x1 < x2:  # right then down
            queue.append((x2, top))
        if x1 > x2:  # down then left
            queue.append((x1, bottom))
        queue.append((x2, bottom))

    if path == "LUR":
        area = (bottom - top + 1) * (min(x1, x2) - left)
        if x1 > x2:  # right then up
            queue.append((x2, bottom))
        if x1 < x2:  # down then right
            queue.append((x1, top))
        queue.append((x2, top))

    if path == "DLU":
        area = (bottom - max(y1, y2)) * (right - left + 1)
        if y1 < y2:  # down then left
            queue.append((right, y2))
        if y1 > y2:  # left then up
            queue.append((left, y1))
        queue.append((left, y2))

    if path == "URD":
        area = (min(y1, y2) - top) * (right - left + 1)
        if y1 > y2:  # up then right
            queue.append((left, y2))
        if y1 < y2:  # right then down
            queue.append((right, y1))
        queue.append((right, y2))

    assert queue[-1] == points[-1]
    print("remove convex element:", path, "with area", area)
    return area


def remove_back_forth(path, queue):
    print("clean up back-forth move", path)

    x2, y2 = queue.pop()
    x1, y1 = queue.pop()
    x0, y0 = queue[-1]
    queue.append((x2, y2))

    # add area for internal
    if path in ("UD", "DU"):
        metrics = y0, y1, y2
    if path in ("LR", "RL"):
        metrics = x0, x1, x2

    area = max(abs(metrics[1] - metrics[0]), abs(metrics[1] - metrics[2])) - abs(
        metrics[0] - metrics[-1]
    )
    return area


def remove_duplicate(queue, path):
    print("remove duplicate", path)
    one = queue.pop()
    queue.pop()
    queue.append(one)


def calc_area(queue):
    area = 0
    path = ""
    while len(queue) > 2:
        point = queue.pop(0)
        queue.append(point)
        path += get_last_direction(queue)
        if path[-3:] in CONVEX:
            inc = remove_bulge(path[-3:], queue)
            if inc:  # keep path if bulge invalid
                area += inc
                path = ""
        elif path[-2:] in DUPLICATES:
            remove_duplicate(queue, path[-2:])
            path = ""

    dx = abs(queue[0][0] - queue[1][0])
    dy = abs(queue[0][1] - queue[1][1])
    area += max(dx, dy) + 1
    return area


def solve(data):
    points = list(get_points(data, parse1))
    return calc_area(points)


def solve2(data):
    points = list(get_points(data, parse2))
    return calc_area(points)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 34329

    result = solve2(input_data)
    print(f"Example 2: {result}")
    assert result == 42617947302920
