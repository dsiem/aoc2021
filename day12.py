from collections import defaultdict

edges = defaultdict(list)
with open('day12.txt', encoding='utf8') as file:
    for line in file:
        src, dst = line.rstrip().split('-')
        edges[src].append(dst)
        edges[dst].append(src)

def walk(twice=True, cave='start', small=set()):
    if cave == 'end':
        return 1
    if cave.islower():
        small = small | {cave}
    return sum(walk(twice | seen, dst, small) for dst in edges[cave]
               if not (seen := dst in small) or (not twice and dst != 'start'))

print(walk(), walk(False))
