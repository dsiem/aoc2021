with open('day06.txt', encoding='utf8') as file:
    fish = list(map(file.read().count, '0123456789'))

def grow(start, stop):
    for day in range(start, stop):
        fish[(day + 7) % 9] += fish[day % 9]
    return sum(fish)

print(grow(0, 80), grow(80, 256))
