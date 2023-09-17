"""
Space Image Format

https://adventofcode.com/2019/day/8
"""

def split_layers(data, x, y):
    size = x * y
    return [data[start : start + size] for start in range(0, len(data), size)]


def solve(data, x, y):
    layers = split_layers(data, x, y)
    counts = [[lay.count(num) for num in "012"] for lay in layers]
    _, ones, twos = min(counts)
    return ones * twos


def aggregate(pixels):
    for p in pixels:
        if p == "2":
            continue
        return p

def solve2(data, x, y):
    layers = split_layers(data, x, y)
    result = ""
    for row in range(y):
        for col in range(x):
            pixels = [lay[row * x + col] for lay in layers]
            result += aggregate(pixels)
        result += "\n"

    return result.strip()


if __name__ == "__main__":
    input_data = open("input_data.txt").read().strip()
    result = solve(input_data, 25, 6)
    print(f"Example 1: {result}")  # 1920

    result = solve2(input_data, 25, 6)
    result = result.replace("0", ".").replace("1", "#")
    print(f'Example 2:\n{result}')  # PCULA
