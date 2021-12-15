from heapq import heappop, heappush

with open('day15.txt', encoding='utf8') as file:
    risks = [list(map(int, line.strip())) for line in file]

def dijkstra(n=1):
    heap = [(0, 0, 0)]
    seen = {(0, 0)}
    while heap:
        total, x, y = heappop(heap)
        if (x, y) == (n*len(risks)-1, n*len(risks)-1):
            return total
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            x_new, y_new = x + dx, y + dy
            if (0 <= x_new < n*len(risks) and 0 <= y_new < n*len(risks) and
                    (x_new, y_new) not in seen):
                x_div, x_mod = divmod(x_new, len(risks))
                y_div, y_mod = divmod(y_new, len(risks))
                risk = (risks[x_mod][y_mod] + x_div + y_div - 1) % 9 + 1
                heappush(heap, (total + risk, x_new, y_new))
                seen.add((x_new, y_new))

print(dijkstra(), dijkstra(5))
