from collections import defaultdict


with open("input.txt") as f:
    data = []
    for x in f.read().splitlines():
        lines = x.split(" -> ")
        data.append([[int(x) for x in y.split(",")] for y in lines])


def p1():
    d = defaultdict(int)
    for (p, q) in data:
        if p[0] == q[0] or p[1] == q[1]:
            dx = -1 if p[0] > q[0] else 0 if p[0] == q[0] else 1
            dy = -1 if p[1] > q[1] else 0 if p[1] == q[1] else 1
            d[p[0], p[1]] += 1
            while p != q:
                p[0] += dx
                p[1] += dy
                d[p[0], p[1]] += 1
    return sum(x > 1 for x in d.values())


def p2():
    d = defaultdict(int)
    for (p, q) in data:
        dx = -1 if p[0] > q[0] else 0 if p[0] == q[0] else 1
        dy = -1 if p[1] > q[1] else 0 if p[1] == q[1] else 1
        d[p[0], p[1]] += 1
        while p != q:
            p[0] += dx
            p[1] += dy
            d[p[0], p[1]] += 1
    return sum(x > 1 for x in d.values())
