from collections import deque
import math


with open("input.txt") as fin:
    data = []
    for x in fin.read().splitlines():
        data.append([int(y) for y in x])


def get_neighbors(i, j):
    res = {(i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j)}
    if i == 0:
        res.discard((i - 1, j))
    if j == 0:
        res.discard((i, j - 1))
    if i == len(data) - 1:
        res.discard((i + 1, j))
    if j == len(data[0]) - 1:
        res.discard((i, j + 1))
    return res

  
def flood_fill(i, j):
    q = deque([(i, j)])
    points = 1
    v = set([(i, j)])
    
    while len(q) != 0:
        i, j = q.popleft()
        for x, y in get_neighbors(i, j):
            if data[x][y] != 9 and (x, y) not in v:
                q.append((x, y))
                v.add((x, y))
                points += 1
    
    return points
  
  
def part1():
    lows = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if all(data[i][j] < data[x][y] for x, y in get_neighbors(i, j)):
                lows.add((i, j))

    return sum(data[i][j] + 1 for i, j in lows)


def part2():
    basins = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if all(data[i][j] < data[x][y] for x, y in get_neighbors(i, j)):
                basins.append(flood_fill(i, j))
    
    basins.sort()
    return math.prod(basins[-3:])
  
