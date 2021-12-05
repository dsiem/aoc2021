import numpy as np

with open('day04.txt', encoding='utf8') as file:
    nums, *boards = file
boards = np.loadtxt(boards, dtype=np.uint8).reshape(-1, 5, 5)

for n in map(int, nums.split(',')):
    boards[boards == n] = 255
    cond = boards == 255
    won = (cond.all(1) | cond.all(2)).any(1)
    if won.any():
        if boards.shape[0] in (1, 100):
            print(np.sum(n * ~cond[won] * boards[won]))
        boards = boards[~won]
