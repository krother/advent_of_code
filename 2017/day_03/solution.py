"""
Spiral Memory

https://adventofcode.com/2017/day/3
"""


def solve(n):
    """returns the spiral solution for puzzle input n"""
    if n == 1:
        return 0
    circle = 0
    while True:
        edge_length = circle * 2 + 1
        inner = edge_length ** 2
        if n <= inner:
            corners = [(edge_length - 2) ** 2] + [inner - (i * (edge_length-1)) for i in range(4)]
            steps_to_corner = min([abs(c - n) for c in corners])
            steps_to_middle = edge_length // 2 - steps_to_corner
            return circle + steps_to_middle
        circle += 1


def solve2(data):
    return data

if __name__ == '__main__':
    result = solve(265149)
    print(f'Example 1: {result}')

    #result = solve2(input_data)
    #print(f'Example 2: {result}')
