import re


def parse(data):
    result = []
    for line in data.strip().split("\n"):
        hail = [int(x) for x in re.findall(r"\-?\d+", line)]
        result.append(hail)
    return result
