pairs = dict(zip(')]}>', '([{<'))
checker_scores = dict(zip(')]}>', [3, 57, 1197, 25137]))
completer_scores = dict(zip('([{<', [1, 2, 3, 4]))
checker = 0
completer = []

with open('day10.txt') as file:
    for line in file:
        stack = []
        for char in line[:-1]:
            if char in pairs.values():
                stack.append(char)
            elif pairs[char] != stack.pop():
                checker += checker_scores[char]
                break
        else:
            completer.append(0)
            while stack:
                completer[-1] *= 5
                completer[-1] += completer_scores[stack.pop()]

print(checker, sorted(completer)[len(completer) // 2])
