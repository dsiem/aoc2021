from functools import reduce
from itertools import permutations

MAX_DEPTH = 4

def explode(snail_num):
    for i, (left, depth) in enumerate(snail_num):
        if depth == MAX_DEPTH:
            if i > 0:
                snail_num[i-1] = (snail_num[i-1][0] + left, snail_num[i-1][1])
            snail_num[i] = (0, 3)
            right, _ = snail_num.pop(i + 1)
            if i+1 < len(snail_num):
                snail_num[i+1] = (snail_num[i+1][0] + right, snail_num[i+1][1])
            return True
    return False

def split(snail_num):
    for i, (num, depth) in enumerate(snail_num):
        if num >= 10:
            snail_num[i] = (num // 2, depth + 1)
            snail_num.insert(i+1, ((num+1) // 2, depth + 1))
            return True
    return False

def add(left, right):
    snail_num = [(num, depth + 1) for lr in (left, right) for num, depth in lr]
    while explode(snail_num) or split(snail_num):
        pass
    return snail_num

def magnitude(snail_num):
    for _depth in range(MAX_DEPTH-1, -1, -1):
        for i, (left, depth) in enumerate(snail_num):
            if depth == _depth:
                right, _ = snail_num.pop(i + 1)
                snail_num[i] = (3 * left + 2 * right, depth - 1)
    return snail_num[0][0]

def parse(line):
    snail_num = []
    depth = -1
    for char in line:
        if char.isdigit():
            snail_num.append((int(char), depth))
        elif char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
    return snail_num

with open('day18.txt', encoding='utf8') as file:
    snail_nums = list(map(parse, file))

print(magnitude(reduce(add, snail_nums)))
print(max(magnitude(add(left, right)) for left, right in permutations(snail_nums, 2)))
