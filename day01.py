with open('day01.txt', encoding='utf8') as file:
    data = list(map(int, file))
    for d in 1, 3:
        print(sum(x < y for x, y in zip(data, data[d:])))
