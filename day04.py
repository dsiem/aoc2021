import numpy as np

with open('day04.txt', encoding='utf8') as file:
    nums, *boards = file
boards = np.loadtxt(boards, dtype=np.uint8).reshape(-1, 5, 5)

part = 0
scores = [0, 0]
for n in np.uint8(nums.split(',')):
    boards[boards == n] = 255
    cond = boards == 255

    won = (cond.all(1) | cond.all(2)).any(1)
    if won.any():
        scores[part] = n * np.sum(~cond[won] * boards[won], dtype=int)
        boards = boards[~won]
        part = 1

print(*scores)
