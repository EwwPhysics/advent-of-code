from statistics import mean, median
import math


with open("input.txt") as fin:
    positions = [int(i) for i in fin.read().split(",")]


def p1():
    m = median(positions)
    return sum(abs(m - x) for x in positions)


def p2():
    m = mean(positions)
    res = float("inf")
    for m in range(math.floor(m) - 1, math.floor(m) + 1):
        res = min(res, sum(abs(m - x) / 2 * (abs(m - x) + 1) for x in positions))
    return res


print(p2())
