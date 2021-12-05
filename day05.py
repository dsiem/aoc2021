import numpy as np

vents = np.zeros((1000, 1000, 2), dtype=int)

with open('day05.txt', encoding='utf8') as file:
    for line in file:
        (x1, y1), (x2, y2) = [map(int, point.split(',')) for point in line.rstrip().split(' -> ')]
        dx = np.sign(x2 - x1)
        dy = np.sign(y2 - y1)
        straight = (dx ^ dy) & 1
        while (x1, y1) != (x2+dx, y2+dy):
            vents[x1, y1] += [straight, 1]
            x1 += dx
            y1 += dy

print(*np.sum(vents > 1, axis=(0, 1)))
