
import numpy as np
from PIL import Image

def draw(a, num):
    x = num % 777
    y = num // 777
    if y < 500:
        a[y:y+4, x:x+4, 1] = 255

a = np.zeros((500, 777, 3), dtype=np.uint8)

for i in range(10):
    # single-number repeats
    draw(a, int(str(i) * 2))
    draw(a, int(str(i) * 3))
    draw(a, int(str(i) * 4))
    draw(a, int(str(i) * 5))
    draw(a, int(str(i) * 6))


for i in range(100):
    num = int(str(i) * 2)  # 99 99
    num = int(str(i) * 3)  # 99 99 99
    draw(a, num)

for i in range(1000):
    num = int(str(i) * 2)
    draw(a, num)

im = Image.fromarray(a)
im.save("aoc02_repeats.png")
