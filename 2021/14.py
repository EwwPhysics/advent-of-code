from collections import *


with open("input.txt") as fin:
    start, thing = fin.read().split("\n\n")
    d = {a: b for a, b in [line.strip().split(" -> ") for line in thing.splitlines()]}


def p1(s, n):
    s = deque(s)
    for _ in range(n):
        i = 0
        while i < len(s):
            s.rotate(-1)
            if (c := "".join([s[-1], s[0]])) in d:
                s.append(d[c])
                i += 1
            i += 1
        s.pop()
    c = Counter(s)
    return max(c.values()) - min(c.values())


def p2(s, n):
    c = defaultdict(int)
    last = s[-1]
    for a, b in zip(s, s[1:]):
        c[a + b] += 1

    for _ in range(n):
        new = defaultdict(int)
        for k, v in c.items():
            new[k[0] + d[k]] += v
            new[d[k] + k[1]] += v
            new[k] -= v
        for k, v in new.items():
            c[k] += v

    counts = defaultdict(int)
    counts[last] += 1
    for k, v in c.items():
        counts[k[0]] += v
        counts[k[1]] += v
    return max(counts.values()) // 2 - min(counts.values()) // 2
