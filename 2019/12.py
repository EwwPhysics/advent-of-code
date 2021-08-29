import re


with open("input.txt") as fin:
    file = fin.read()
    p = []
    for line in file.splitlines():
        pattern = re.match(r"<.=(-?\d+),\s.=(-?\d+),\s.=(-?\d+)>", line).groups()
        p.append(list(map(int, pattern)))

v = [[0 for _ in range(3)] for _ in range(4)]

def p1():
    for _ in range(1000):
        vel_diffs = [[0 for _ in range(3)] for _ in range(4)]

        for i in range(3):
            locs = [x[i] for x in p]
            for j, planet in enumerate(locs):
                for k, l in enumerate(locs[j + 1:], j + 1):
                    if l < planet:
                        vel_diffs[j][i] -= 1
                        vel_diffs[k][i] += 1
                    elif l > planet:
                        vel_diffs[j][i] += 1
                        vel_diffs[k][i] -= 1

        for i in range(4):
            for j in range(3):
                v[i][j] += vel_diffs[i][j]
                p[i][j] += v[i][j]

    energy = 0
    for a, b in zip(p, v):
        energy += sum(abs(x) for x in a) * sum(abs(x) for x in b)

    return energy


def p2():
    pass

