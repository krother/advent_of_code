"""


https://adventofcode.com/2024/day/21
"""
import re
from pprint import pprint


DOOR = [
    "789",
    "456",
    "123",
    "-0A"
]
ROBOT = [
    "-^A",
    "<v>",
]

def get_moves(pos, keypad, seq):
    """do not go back and forth ever"""
    x, y = pos
    if (
        y > 0
        and keypad[y-1][x] != "-"
        and re.fullmatch(r"[\<\>]*\^*", seq)
    ):
        yield (x, y - 1), "^"
    if (
        y < len(keypad) - 1
        and keypad[y+1][x] != "-"
        and re.fullmatch(r"[\<\>]*v*", seq)
    ):
        yield (x, y + 1), "v"
    if (
        x > 0
        and keypad[y][x-1] != "-"
        and re.fullmatch(r"[\^v]*\<*", seq)
    ):
        yield (x - 1, y), "<"
    if (
        x < len(keypad[0]) - 1
        and keypad[y][x+1] != "-"
        and re.fullmatch(r"[\^v]*\>*", seq)
    ):
        yield (x + 1, y), ">"


def get_keys(keypad):
    for y, row in enumerate(keypad):
        for x, cell in enumerate(row):
            if cell != "-":
                yield cell, (x, y)


def get_shortest_paths(keypad):
    """prepare dictionary to look up alternative paths quickly"""
    result = {}
    for start, start_pos in get_keys(keypad):
        for target, target_pos in get_keys(keypad):
            candidates = [(start_pos, "")]
            paths = []
            while candidates:
                pos, seq = candidates.pop(0)
                if pos == target_pos:
                    paths.append(seq + "A")
                if not paths or len(seq) < len(paths[0]):
                    for newpos, move in get_moves(pos, keypad, seq):
                        candidates.append((newpos, seq + move))
            result[(start, target)] = paths

    return result


def calc_complexity(target, path):
    return path * int(re.findall(r"\d+", target)[0])


def find_sequences(target, path_dict, start):
    candidates = [""]
    for t in target:
        new_candidates = []
        for seq in candidates:
            for path in path_dict[(start, t)]:
                new_candidates.append(seq + path)
        candidates = new_candidates
        start = t
    return candidates


def filter_shortest_candidates(paths):
    shortest = min(len(p) for p in paths)
    print("shortest path length", shortest)
    return [p for p in paths if len(p) == shortest]


def find_path_length(target, robots):
    # old
    print("\ntarget:", target)
    door_paths = get_shortest_paths(DOOR)
    robot_paths = get_shortest_paths(ROBOT)

    paths = find_sequences(target, door_paths, "A")
    paths = filter_shortest_candidates(paths)
    print("paths for door", len(paths))

    for i in range(robots):
        new_paths = []
        for p in paths:
            new_paths += find_sequences(p, robot_paths, "A")
        paths = filter_shortest_candidates(new_paths)
        print(f"paths for robot {i+1}", len(paths))

    return len(paths[0])


class PathCalculator:

    def __init__(self, robots):
        self.robots = robots
        self.door_paths = get_shortest_paths(DOOR)
        self.robot_paths = get_shortest_paths(ROBOT)
        self.cache = {}

    # <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A 
    #   v  < <    A  > >   ^  A    <    A  >  A   v   A    <   ^  A A  >  A    <  v   A A A  >   ^  A 
    #             <           A         ^     A       >           ^ ^     A           v v v         A
    #                         0               2                           9                         A
    def calc_moves(self, path, robot):
        key = robot, path
        if key in self.cache:
            return self.cache[key]

        result = 0
        start = "A"
        for p in path:
            if robot == 1:
                # last robot
                result += len(self.robot_paths[(start, p)][0]) # * 2 + 1
            else:
                # recurse
                candidates = []
                for p2 in self.robot_paths[(start, p)]:
                    candidates.append(self.calc_moves(p2, robot - 1))
                result += min(candidates)
            start = p
        
        #print(key, result)
        self.cache[key] = result
        return result

    def find_path_length(self, target):
        result = 0
        start = "A"
        for t in target:
            result += min(
                self.calc_moves(path, self.robots)
                for path in self.door_paths[(start, t)]
            )
            start = t
        return result


def solve(data, robots):
    result = 0
    for target in data.strip().split():
        pc = PathCalculator(robots)
        path = pc.find_path_length(target)
        result += calc_complexity(target, path)
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, robots=2)
    print(f'Example 1: {result}')  # 205160

    result = solve(input_data, robots=25)
    print(f'Example 2: {result}')
