"""


https://adventofcode.com/2022/day/21
"""

def parse(data):
    graph = {}
    for line in data.strip().split('\n'):
        name, op = line.split(':')
        op = op.strip().split()
        if len(op) == 1:
            graph[name] = int(op[0])
        else:
            graph[name] = op
    return graph


def resolve(graph, node):
    n = graph[node]
    if type(n) == int:
        return n
    a, operator, b = n
    a = resolve(graph, a)
    b = resolve(graph, b)
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b
    if operator == '=':
        if round(a,1) == round(b, 1):
            return 0
        if a < b:
            return -1
        else:
            return 1


def solve(data):
    graph = parse(data)
    return resolve(graph, 'root')


def binsearch(graph, start, end, mod):
    middle = (end - start) // 2 + start
    graph['humn'] = int(middle)
    result = resolve(graph, 'root')
    print('trying', start, end, result)
    if result == 0:
        return middle
    if result == mod * 1:
        return binsearch(graph, start, max(middle - 1, start), mod)
    if result == mod * -1:
        return binsearch(graph, min(middle + 1, end), end, mod)


def solve2(data, mod=1):
    graph = parse(data)
    graph['root'][1] = '=' 
    return binsearch(graph, 0, 1_000_000_000_000_000, mod)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data, -1)  # humn has opposite influence of test data
    print(f'Example 2: {result}')
