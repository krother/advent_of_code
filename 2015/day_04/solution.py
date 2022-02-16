"""The Ideal Stocking Stuffer

https://adventofcode.com/2015/day/4

"""
from hashlib import md5


def solve(data, prefix='00000'):
    i = 0
    while True:
        s = data + str(i)
        hash = md5(s.encode()).hexdigest()
        if hash.startswith(prefix):
            return i
        i += 1


if __name__ == '__main__':
    result = solve('bgvyzdsv')
    print(f'Example 1: {result}')

    result = solve('bgvyzdsv', '000000')
    print(f'Example 2: {result}')
