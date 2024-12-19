"""
Day 19: Linen Layout

https://adventofcode.com/2024/day/19
"""


def parse(data):
    patterns, designs = data.strip().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    return patterns, designs


def build(design, patterns):
    combinations = {0: 1}
    for i in range(1, len(design) + 1):
        # DP: count combinations for length i
        combinations[i] = 0
        for p in patterns:
            if p == design[i - len(p) : i]:
                combinations[i] += combinations[i - len(p)]
    return combinations[len(design)]


def solve(data, count=False):
    result = 0
    patterns, designs = parse(data)
    for d in designs:
        c = build(d, patterns)
        result += c if count else bool(c)
    return result


def solve2(data):
    return solve(data, count=True)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 260

    result = solve2(input_data)
    print(f"Example 2: {result}")
    assert result == 639963796864990
