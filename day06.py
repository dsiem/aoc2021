fish = [0] * 9
with open('day06.txt', encoding='utf8') as file:
    for i in file.readline().split(','):
        fish[int(i)] += 1

def grow(start, end):
    for day in range(start, end):
        fish[(day + 7) % 9] += fish[day % 9]
    return sum(fish)

print(grow(0, 80), grow(80, 256))
