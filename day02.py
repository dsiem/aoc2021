with open('day02.txt', encoding='utf8') as file:
    horiz = depth = aim = 0

    for cmd, n in map(lambda l: l.split(), file):
        n = int(n)
        if cmd == 'up':
            aim -= n
        elif cmd == 'down':
            aim += n
        else:
            horiz += n
            depth += aim * n

    print(horiz * aim)
    print(horiz * depth)
