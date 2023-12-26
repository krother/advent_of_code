"""
Lens Library

https://adventofcode.com/2023/day/15
"""
from collections import defaultdict


def get_hash(s):
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


def solve(data):
    return sum(get_hash(seq) for seq in data.strip().split(","))


def solve2(data):
    boxes = defaultdict(list)
    for seq in data.strip().split(","):
        if seq[-1] == "-":
            # remove lens
            label = seq[:-1]
            box = boxes[get_hash(label)]
            for i, item in enumerate(box):
                if item[0] == label:
                    box.remove(item)
                    break
        else:
            # add lens
            label, focal = seq.split("=")
            focal = int(focal)
            box = boxes[get_hash(label)]
            found = False
            for item in box:
                if item[0] == label:
                    item[1] = focal
                    found = True
            if not found:
                box.append([label, focal])

    # calc
    total = 0
    for i, box in boxes.items():
        for slot, (_, focal) in enumerate(box, 1):
            total += (i + 1) * slot * focal
    return total


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 512950

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 247153
