from itertools import starmap

points = []
with open('day13.txt', encoding='utf8') as file:
    while (line := next(file)) != '\n':
        points.append(list(map(int, line.split(','))))

cols = 1310
print(len(set(starmap(lambda x, y: (min(x, cols - x), y), points))))

cols, rows = 40, 6
fold = lambda x, y: (cols - abs(x % (2*cols + 2) - cols), rows - abs(y % (2*rows + 2) - rows))
folded = list(starmap(fold, points))
for i in range(rows):
    print(*[' █'[(j, i) in folded] for j in range(cols)], sep='')
