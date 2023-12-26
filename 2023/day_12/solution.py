"""
Hot Springs

https://adventofcode.com/2023/day/12
"""


def block_fits(pattern, start, length):
    if start + length > len(pattern):
        return False
    for i in range(start, start + length):
        if pattern[i] == ".":
            return False
    return True


def count_combos(blocks, pattern, i, j, cache):
    combos = 0
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        if (i, j) in cache:
            combos += cache[(i, j)]
            continue

        if i == len(pattern) and j == len(blocks):
            combos += 1
        if i < len(pattern):
            if pattern[i] != "#":
                stack.append((i + 1, j))  # add .
            if pattern[i] != "." and j < len(blocks):
                # add next block
                blk = blocks[j]
                if block_fits(pattern, i, blk):
                    if i + blk < len(pattern):
                        if pattern[i + blk] != "#":
                            stack.append((i + blk + 1, j + 1))  # add extra .
                    else:
                        stack.append((i + blk, j + 1))
    return combos


def parse(line, unfold):
    pattern, blocks = line.split(" ")
    if unfold:
        pattern = "?".join([pattern] * 5)
        blocks = ",".join([blocks] * 5)
    blocks = [int(x) for x in blocks.split(",")]
    return pattern, blocks


def solve_line(line, unfold=False):
    """dynamic programming algorithm"""
    pattern, blocks = parse(line, unfold)
    cache = {}
    for i in reversed(range(len(pattern))):
        for j in reversed(range(len(blocks))):
            cache[(i, j)] = count_combos(blocks, pattern, i, j, cache)
    return cache[(0, 0)]


def solve(data):
    return sum(solve_line(line) for line in data.strip().split("\n"))


def solve2(data):
    return sum(solve_line(line, True) for line in data.strip().split("\n"))


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 6488

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 815364548481
