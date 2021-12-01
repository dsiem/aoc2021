with open('day01.txt') as file:
    input = list(map(int, file))
    for d in 1,3:
        print(sum(x < y for x, y in zip(input, input[d:])))
