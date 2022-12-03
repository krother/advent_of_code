"""
Rock Paper Scissors

https://adventofcode.com/2022/day/2
"""
# A B C : Rock Paper Scissors
# X Y Z : Rock Paper Scissors
SCORE = {
    "A": dict(zip("XYZ", (3 + 1, 6 + 2, 0 + 3))),
    "B": dict(zip("XYZ", (0 + 1, 3 + 2, 6 + 3))),
    "C": dict(zip("XYZ", (6 + 1, 0 + 2, 3 + 3))),
}

# X lose, Y draw, Z win
PLAY = {
    "A": dict(zip("XYZ", "ZXY")),
    "B": dict(zip("XYZ", "XYZ")),
    "C": dict(zip("XYZ", "YZX")),
}


def parse_rounds(data):
    for line in data.strip().split("\n"):
        opponent, symbol = line.strip().split()
        yield opponent, symbol


def solve(data):
    return sum(SCORE[opponent][me] for opponent, me in parse_rounds(data))


def solve2(data):
    return sum(
        SCORE[opponent][PLAY[opponent][should_win]]
        for opponent, should_win in parse_rounds(data)
    )


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    # 15632
    result = solve2(input_data)
    print(f"Example 2: {result}")
    # 14416
