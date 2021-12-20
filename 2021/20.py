import numpy as np
from itertools import product


with open("input.txt") as fin:
    algo, start = fin.read().split("\n\n")
    algo = [0 if x == "." else 1 for x in algo]
    start = np.array([['0' if x == "." else '1' for x in line] for line in start.splitlines()], dtype=str)


def solve(image, n):
    image = np.pad(image, n + 1)
    for _ in range(n):
        new = np.empty(image.shape, dtype=str)
        for i in range(len(image)):
            for j in range(len(image[0])):
                s = int("".join([image[x] for x in get_neighbors(i, j, image)]), 2)
                new[i][j] = algo[s]
        image = new
    return len(new[new == '1'])


def get_neighbors(i, j, image):
    res = product([i - 1, i, i + 1], [j - 1, j, j + 1])
    if i == 0:
        res = [x for x in res if x[0] != i - 1]
    if j == 0:
        res = [x for x in res if x[1] != j - 1]
    if i == len(image) - 1:
        res = [x for x in res if x[0] != i + 1]
    if j == len(image[0]) - 1:
        res = [x for x in res if x[1] != j + 1]
    return res

print(solve(start, 2))
print(solve(start, 50))
