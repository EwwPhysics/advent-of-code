import math
from itertools import cycle


with open("input.txt") as fin:
    L = [list(s) for s in fin.read().splitlines()]


def p1():
    m = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "#":
                a = visible(i, j)
                if a == 261:
                    print(j, i)
                if a > m:
                    m = a
    return m - 1


def p2():
    x, y = 14, 17
    points = []
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "#":
                points.append((j, i))

    points.sort(
        key=lambda coords: (
            coords[0] - x < 0 if coords[0] - x != 0 else y < 0,
            (float("inf") if coords[1] > y else float("-inf"), -abs(coords[1] - y))
            if coords[0] - x == 0
            else (
                (coords[1] - y) / (coords[0] - x),
                (abs(coords[1] - y) + abs(coords[0] - x)),
            ),
        )
    )

    gone = [None]
    v = set()
    cur = 0
    testing = []
    for p in cycle(points):
        if (
            gone[-1]
            != (
                prev := (float("inf") if p[1] > y else float("-inf"))
                if p[0] - x == 0
                else (p[1] - y) / (p[0] - x)
            )
            and p not in v
        ):
            gone.append(prev)
            cur += 1
            testing.append((p, round(prev, 2)))
            if cur > 300:
                return testing
            v.add(p)
            if cur == 200:
                print(testing)
                print(p)
                return p[0] * 100 + p[1]


def visible(i, j):
    a = 0
    for ix in range(len(L)):
        for jx in range(len(L[0])):
            if L[ix][jx] == "#":
                d = math.gcd(abs(ix - i), abs(jx - j))
                if not d:
                    a += 1
                    continue
                diff_x = (ix - i) // d
                diff_y = (jx - j) // d
                x, y = ix - i, jx - j
                while (x, y) != (diff_x, diff_y):
                    x -= diff_x
                    y -= diff_y
                    if L[x + i][y + j] == "#":
                        break
                else:
                    a += 1
    return a


print(p2())
