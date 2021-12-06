from collections import deque


with open("input.txt") as fin:
    data = [0 for _ in range(9)]
    for x in map(int, fin.read().split(",")):
        data[x] += 1


def solve(L, n):
    d = deque(L)
    for i in range(n):
        d[-2] += d[0]
        d.rotate(-1)
    return sum(d)
