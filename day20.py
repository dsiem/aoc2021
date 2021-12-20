import numpy as np
from scipy.signal import convolve2d

with open('day20.txt', encoding='utf8') as file:
    lut = np.array([c == '#' for c in next(file).rstrip()], dtype=np.int8)
    next(file)
    img = np.array([[c == '#' for c in l.rstrip()] for l in file], dtype=np.int8)

kernel = np.array(2 ** np.arange(9)).reshape(3, 3)
fill = 0

for i in range(50):
    img = lut[convolve2d(img, kernel, fillvalue=fill)]
    fill = lut[511 * fill]
    if i == 1:
        print(img.sum())

print(img.sum())
