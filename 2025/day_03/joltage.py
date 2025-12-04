
import numpy as np
from PIL import Image

z = np.zeros((1300, 1300, 3), dtype=np.uint8)

SIZE = 1300 // 5

i = 0
for x in range(5):
    for y in range(5):

        a = np.random.randint(1, 16, size=(1, 12))
        b = np.random.randint(1, 16, size=(12, 1))
        M = a * b - 1

        c = np.kron(M, np.ones((20, 20)))
        c = c.astype(np.uint8)
        z[y*SIZE:y*SIZE+c.shape[0], x*SIZE:x*SIZE+c.shape[1], i % 3] = c
        
        i += 1

im = Image.fromarray(z)
im.save("joltage.png")