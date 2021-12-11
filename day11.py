import numpy as np
from scipy.signal import convolve2d

def step(grid):
    grid += 1
    while (active := grid > 9).any():
        grid[active] = 0
        grid += (grid > 0) * convolve2d(active, kernel, mode='same')
    return grid == 0

octopi = np.genfromtxt('day11.txt', delimiter=1, dtype=np.uint8)
kernel = np.ones((3, 3), dtype= np.uint8)

score = sum(step(octopi).sum() for _ in range(100))
steps = 101
while not step(octopi).all():
    steps += 1

print(score, steps)
