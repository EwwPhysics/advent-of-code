from collections import defaultdict


with open("input.txt") as fin:
    orbits = fin.read().splitlines()

things = {}
for o in orbits:
    a, b = o.split(")")
    things[b] = a


def p1():
    d = defaultdict(int)
    for o in orbits:
        _, b = o.split(")")
        d[b] = n(b)
    return sum(d.values())


def p2():
    g = defaultdict(list)
    for o in orbits:
        a, b = o.split(")")
        g[a].append(b)
        g[b].append(a)
    path = [{*g["SAN"]}]
    i = 0
    while True:
        path.append(set())
        for x in path[-2]:
            path[-1].update(g[x])
        if "YOU" in path[-1]:
            return i
        i += 1

def n(a):
    if things[a] == "COM":
        return 1
    else:
        return n(things[a]) + 1

print(p2())

