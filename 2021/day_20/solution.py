"""Trench Map

https://adventofcode.com/2021/day/20

"""
import numpy as np

BIN = np.array([256, 128, 64, 32, 16, 8, 4, 2, 1], dtype=int)


def line_to_binary(line):
    return [1 if char=='#' else 0 for char in line]


def parse(data):
    algo, img = data.strip().split('\n\n')
    algo = line_to_binary(algo.replace('\n', ''))
    data = [line_to_binary(line) for line in img.strip().split('\n')]
    img = np.array(data, dtype=int)
    return algo, img


def step(img, algo, fill_value):
    """applies a convolution"""
    img = np.pad(img, 2, constant_values=fill_value)
    result = np.zeros((img.shape[0]-2, img.shape[1]-2), dtype=int)
    for y, x in np.ndindex(result.shape):
        bits = img[y:y+3, x:x+3].flatten()
        number = (bits * BIN).sum()
        result[y, x] = algo[number]
    return result


def solve(data, iter=2):
    algo, img = parse(data)
    fill = 0
    for _ in range(iter):
        img = step(img, algo, fill)
        fill = algo[0] - fill  # alternates
    return img.sum()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 5179

    result = solve(input_data, 50)
    print(f'Example 2: {result}')
    # 16112
