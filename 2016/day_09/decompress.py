
import re
from functools import reduce


PATTERN = r"\((\d+)x(\d+)\)"

def get_marker(marker):
    size, repeats = re.findall(PATTERN, marker)[0]
    return int(size), int(repeats)


def decompress(code):
    match = re.search(PATTERN, code)
    if match:
        start, end = match.start(), match.end()
        size, repeats = get_marker(code[start:end])
        extra_chars = repeats * size
        return len(code[:start]) + extra_chars + decompress(code[end+size:])
    return len(code)


def get_next_marker(code, i):
    marker = code[i:]
    match = re.search(PATTERN, marker)
    size, repeats = get_marker(marker[match.start(): match.end()])
    steps = match.end()
    marker = size + steps, repeats
    return marker, steps


def product(markers):
    return reduce(lambda a,b: a * b[1], markers, 1)


def update_markers(markers, steps):
    return [(s-steps, r) for s, r in markers if s > steps]


def decompress_v2(code):
    i = 0
    total = 0
    markers = []

    while i < len(code):
        if code[i] == '(':
            m, steps = get_next_marker(code, i)
            markers.append(m)
        else:
            total += product(markers)
            steps = 1

        markers = update_markers(markers, steps)
        i = i + steps

    return total


if __name__ == '__main__':
    code = open('input.txt').read().strip()
    print(decompress(code))
    print(decompress_v2(code))