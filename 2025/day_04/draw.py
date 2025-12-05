
from aoc import (
    parse_hash_grid,
)
import numpy as np
from scipy.signal import convolve
from PIL import Image


def parse(data):
    return parse_hash_grid(data.replace("@", "#"))


def get_accessible_rolls(grid):
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    c = convolve(grid, kernel)
    return (c[1:-1, 1:-1] < 4) & grid


def draw(data):
    grid = parse(data)
    a = np.zeros(grid.shape)
    while (removed := get_accessible_rolls(grid)).any():
        a += grid
        grid -= removed

    a = a * 255/ a.max()
    a = a.round().astype(np.uint8)

    z = np.zeros((a.shape[0], a.shape[1], 3), dtype=np.uint8)
    z[:,:,1] = a
    
    z = np.kron(z, np.ones((10, 10, 1), dtype=np.uint8))
    im = Image.fromarray(z)
    im.save("aoc04.png")


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    draw(input_data)
