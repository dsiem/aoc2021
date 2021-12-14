from collections import Counter

with open('day14.txt', encoding='utf8') as file:
    template, _, *insertions = file

template = template.strip()
insertions = dict(rule.strip().split(' -> ') for rule in insertions)

def polymerize(steps):
    elements = Counter(template)
    pairs = Counter(template[i:i+2] for i in range(len(template)-1))

    for _ in range(steps):
        new_pairs = Counter()
        for pair, num in pairs.items():
            new_pairs[pair[0] + insertions[pair]] += num
            new_pairs[insertions[pair] + pair[1]] += num
            elements[insertions[pair]] += num
        pairs = new_pairs

    histogram = elements.most_common()
    return histogram[0][1] - histogram[-1][1]

print(polymerize(10), polymerize(40))
