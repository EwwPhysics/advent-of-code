import math


with open("input.txt") as fin:
    L = fin.read().splitlines()


def p1():
    m = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "#":
                a = visible(i, j)
                if a > m:
                    m = a
    return m - 1

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

print(p1())
