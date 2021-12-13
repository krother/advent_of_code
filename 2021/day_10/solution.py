"""Syntax Scoring

https://adventofcode.com/2021/day/10

"""
MATCHES = {
    '<': '>',
    '(': ')', 
    '{': '}', 
    '[': ']'
}
ERROR_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
AUTOCOMPLETE_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def find_error(line):
    """returns error score and remaining stack"""
    stack = []
    for char in line:
        if char in '[({<':
            stack.append(char)
        else:
            m = stack.pop()
            match = MATCHES[m]
            if char != match:
                return ERROR_SCORE[char], []
    return 0, stack


def autocomplete(stack):
    prod = 0
    for char in stack[::-1]:
        prod *= 5
        prod += AUTOCOMPLETE_SCORE[MATCHES[char]]
    return prod


def solve(data):
    total = 0
    for line in data.strip().split('\n'):
        score, _ = find_error(line)
        total += score
    return total

def solve2(data):
    autos = []
    for line in data.strip().split('\n'):
        score, stack = find_error(line)
        if score == 0:
            autos.append(autocomplete(stack))
    autos.sort()
    middle = len(autos) // 2
    return autos[middle]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 268845

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 4038824534